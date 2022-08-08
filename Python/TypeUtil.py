import re


def is_int(data) -> bool:
    if type(data) == int:
        return True

    if type(data) == str:
        data = str(data).strip()
        reg_exp = r'[+-]?[0-9]+$'
        return re.match(reg_exp, data) is not None

    return False


def is_float(data) -> bool:
    if type(data) == float:
        return True

    if type(data) == str:
        data = str(data).strip()
        reg_exp = r'[+-]?[0-9]+\.[0-9]+([E][+-]?[0-9]+)?$'
        return re.match(reg_exp, data) is not None

    return False


def is_varname(data) -> bool:
    if type(data) == str:
        data = str(data).strip()
        reg_exp = r'[A-Za-z0-9_]$'
        return re.match(reg_exp, data) is not None
    return False


def is_date(data) -> bool:
    if type(data) == str:
        data = str(data).strip()
        reg_exp = r'\d{4}-\d{2}-\d{2}$'
        return re.match(reg_exp, data) is not None
    return False


def is_str(data) -> bool:
    if is_int(data):
        return False
    if is_float(data):
        return False
    if is_date(data):
        return False

    if type(data) == str:
        return True

    return False
