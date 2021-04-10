#!/usr/bin/env python3

"""
Recorders module sequence in dynamodb table `tenant_accounts_table` for cmdb. provides following features,
1. load default sequence template for module order arrangement.
2. updates dynamodb table with rearrange data.
3. create backup file before update for existing accounts.
4. 
3. generates report for each account in tabuler formate.
3. generates logger messages.
4. create backup for existing account details.
5. load default sequence template for order arrangement.
"""


import json
from cmdb import cmdb
import logging
from datetime import date
import boto3
import os
from prettytable import PrettyTable


# Enable logging
logging.basicConfig(format='[%(asctime)s - %(levelname)s]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

logger = logging.getLogger(__name__)

#--- load account list from Dynamodb
def get_account_ids(account_id_file):
    
    logger.info("generate account details file")
    try:
        with open(account_id_file,'w') as f:
            dy_client = boto3.resource('dynamodb')
            table = dy_client.Table('tenant_accounts_table')
            response = table.scan(ProjectionExpression='AccountID')
            items = response['Items']
            for itemkey in items:
                accountid = itemkey['AccountID']
                f.write(accountid + "\n")
            
            while 'LastEvaluatedKey' in response:
                response = table.scan(ProjectionExpression='AccountID',
                                    ExclusiveStartKey=response['LastEvaluatedKey']
                                    )
                items = response['Items']
                for itemkey in items:
                    accountid = itemkey['AccountID']
                    f.write(accountid + "\n")
            logger.info("Account-id file generated successfully.")
    except FileNotFoundError as e:
        raise Exception(e)
                 
#--- load default template
def load_template(template_file:str) -> list:
      
    modules = []
    try:
        with open(template_file, 'r') as f:
            data = json.load(f)
            for module in data['modules']:
                modules.append(*module)
            return modules
    except EnvironmentError as e:
        raise Exception(e)


#--- modify modules list of dict
def modified_modules(unord_modules:list, ord_modules: list) -> list:
    
    new_ordered_modules = []
    unlisted_modules = []
    for key in ord_modules:
        for module in unord_modules:
                if key in module and key not in new_ordered_modules:
                    new_ordered_modules.append(module)
                    break
                
    # make sure no module removed from existing module list append them at the end of list
    for module in ord_modules:
        if module not in new_ordered_modules:
            new_ordered_modules.append(module)
            
    return new_ordered_modules

#--- generate report
def print_report(report):
    
    header = ['account-id', 'status']
    t = PrettyTable(header)
    for line in report:
        id, status = line.split(",")
        t.add_row([id, status])
    print(t)
    

#--- backing up account details for validation
def save_details(account_id:str, data):
    
    # keep copy of original account metadata for validation
    if isinstance(data,dict):
        dir = 'account_lists'
        if not os.path.exists(dir):
            os.makedirs(dir)
        f_name = str('account_lists/' + account_id + '_' + str(date.today()) + ".json")
        with open(f_name, "w") as f:
            json.dump(data,f)

#--- rollback for failed modules
def rollback(account_details,result):
    
    for d in result:
        id, status = d.split(",")
        if status == 'Failed':
            pass
                

#-- get data from cmdb
def get_cmdb(cmdb_table, account_id, require_save=False):
    
    account_details = cmdb_table.get_item(account_id)
    if account_details and account_details['MetaData']:
        metadata = json.loads(account_details['MetaData'])
    else:
        logger.error(f"No data found in cmdb for account: {account_id}")
        exit(0)

    if require_save:
        # create copy of details for validation
        save_details(account_id,account_details)
                        
    return metadata


#--- get/update items from cmdb table
def update_cmdb(account_id_file: str, ord_modules: list):
    
    cmdb_table = cmdb.CMDBTable()
    record_status = []
    try:
        with open(account_id_file,'r') as f:
            accounts = f.readlines()
            #accounts = ['449842814174']
            for account_id in accounts:
                account_id = account_id.strip("\n")
                result = account_id + ',' + 'Failed'
                metadata = get_cmdb(cmdb_table, account_id,True)
                if "modules" in metadata:
                    logger.info(f"Rearrange modules for account: {account_id}")
                    ordered_modules = modified_modules(metadata['modules'], ord_modules)
                    metadata['modules'] = ordered_modules
                    ## update metadata in cmdb here
                    #cmdb_table.update_item(account_id, json.dumps(metadata))
                    result = account_id + ',' + 'Updated'
                    logger.info("Modules reordered successfully.")
                else:
                    logger.error(f"modules missing in metadata for account: {account_id}")
                    result = account_id + ',' + 'Modules Not Present'
                record_status.append(result)

    except Exception as e:
        logger.error(f"Exception {e.__class__} occured.")
        record_status.append(result)
    
    return record_status

#--- Main
def main():
    
    # get correct ordered module list
    ordered_modules = load_template('ordered_modules.json')

    # get account id's from cmdb
    account_id_file = "account_id_extract_from_cmdb_" + str(date.today()) + ".txt"
    get_account_ids(account_id_file)
    
    # modify cmdb module list and generate report
    report = update_cmdb(account_id_file, ordered_modules)
    print_report(report)
    
    # clear list files
    os.remove(account_id_file)
    

if __name__ == "__main__":
    main()
    