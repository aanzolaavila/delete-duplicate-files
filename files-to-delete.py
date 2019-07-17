from sys import stdin
import re

def main():
    d = dict()
    l = stdin.readline().strip()
    while len(l) != 0:
        # h, name = l.split()
        res = re.match(r'(\w+)\s{2}(.+)', l)
        # print("Procesando '%s'" % (l))
        h, name = res.group(1), res.group(2)
        
        d[h] = d.get(h, []) + [name]
        l = stdin.readline().strip()

    duplicates = []
    for key in d.keys():
        if len(d[key]) > 1:
            duplicates.extend(d[key][1:])

    print("\n".join(duplicates))

main()
