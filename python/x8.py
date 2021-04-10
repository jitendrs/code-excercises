"""Define a function is_palindrome() that recognizes
palindromes (i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True."""

def is_palindrome(s: str) -> str:
    return s == s[::-1]



print(is_palindrome("raadar"))
