def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


def is_palindrome_2(s):
    return s.lower() == s.lower()[::-1]

