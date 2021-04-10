"""Define a function reverse() that computes the reversal
of a string. For example, reverse("I am testing") should
return the string "gnitset ma I"."""


def reverse(s: str) -> str:
    return s[::-1]



print(reverse("I am testing"))