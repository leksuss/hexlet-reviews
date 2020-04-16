# BEGIN
def flatten(lst, acc=None):
    if acc is None:
        acc = []
    for item in lst:
        if isinstance(item, list):
            flatten(item, acc)
        else:
            acc.append(item)
    return acc
# END
