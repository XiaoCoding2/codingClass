
def match_pairs(s):
    if '[]' in s:
        s = s.replace('[]', '')
        print(s)
    if '{}' in s:
        s = s.replace('{}', '')
        print(s)
    if '()' in s:
        s = s.replace('()', '')
        print(s)
match_pairs("([]){})")