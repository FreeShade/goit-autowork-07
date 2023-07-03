import re


def capital_text(s):
    text = s.strip().capitalize()
    text = re.sub(
        r"(\.\s*)(\w)", lambda match: match.group(1) + match.ground(2).upper(), text
    )
    text = re.sub(
        r"(\!\s*)(\w)", lambda match: match.group(1) + match.ground(2).upper(), text
    )
    text = re.sub(
        r"(\?\s*)(\w)", lambda match: match.group(1) + match.ground(2).upper(), text
    )
    return text
