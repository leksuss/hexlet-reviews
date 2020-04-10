# BEGIN
def is_valid_ipv6(ipv6):
    groups = []

    if ipv6.find('::') != ipv6.rfind('::'):
        return False

    for group in filter(None, ipv6.lower().split('::')):
        groups.extend(group.split(':'))

    is_short = '::' in ipv6

    length = len(groups) + 2 if is_short else len(groups)

    if length > 8 or (not is_short and length < 8):
        return False

    return all(
        group and
        not set(group) - set('0123456789abcdef') and
        int(group, 16) < 2**16
        for group in groups
    )
# END
