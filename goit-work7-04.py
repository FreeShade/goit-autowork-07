def is_integer(s):
    digits_only = "".join(char for char in s if char.isdigit())
    if len(s) == 0:
        return False
    elif digits_only:
        return bool(digits_only)
    else:
        return False
