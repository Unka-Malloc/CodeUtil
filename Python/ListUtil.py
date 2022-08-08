def remove_dup(given_list: list, keep_order=True) -> list:
    if keep_order:
        return list(dict.fromkeys(given_list))
    else:
        return list(set(given_list))
