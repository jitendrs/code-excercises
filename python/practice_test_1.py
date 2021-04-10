# <-- EXPAND to see the data classes
import fileinput
import json


class PositiveReview(object):
    def __init__(self, user_id, business_id):
        self.user_id = user_id
        self.business_id = business_id


"""
Sample Input
    {
        "business_of_interest_id": 10,
        "positive_reviews": [
            PositiveReview(
                "user_id": 1,
                "business_id": 10
            ),
            PositiveReview(
                "user_id": 2,
                "business_id": 10
            ),
            PositiveReview(
                "user_id": 1,
                "business_id": 11
            ),
            PositiveReview(
                "user_id": 2,
                "business_id": 11
            ),
            PositiveReview(
                "user_id": 1,
                "business_id": 12
            ),
            PositiveReview(
                "user_id": 2,
                "business_id": 12
            ),
            PositiveReview(
                "user_id": 3,
                "business_id": 12
            )
        ]
    }

Sample Output
    11

Business Similarity Score against business 10:
    11: 2 / (2 + 2 - 2) = 1.0
    12: 2 / (2 + 3 - 2) = 0.667
"""

def find_most_similar_business(business_of_interest_id, positive_reviews):
    # TODO: Complete Me
    b_id_list = []
    # get all the users from business of interest id
    int_user_id = set([ element.user_id in element
                        for element in positive_reviews
                        if element.user_id == business_of_interest_id['business_of_interest_id'] ])
    # figure out similarity with rest of the elements.
    for user_id, b_id in enumerate(positive_reviews):
        # get all the users from positiveReview with matching users from business of interest id
        b_in_user_id = set([ element.user_id in element for element in positive_reviews if element.user_id in int_user_id ])
        if set(int_user_id) & set(b_in_user_id) and (len(int_user_id)/(len(int_user_id) + len(b_in_user_id) - len(int_user_id))):
            b_id_list.add(b_id)
    return b_id




