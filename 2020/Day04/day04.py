def byr(f: str):
    return f.isdigit() and 1920 <= int(f) <= 2002


def iyr(f: str):
    return f.isdigit() and 2010 <= int(f) <= 2020


def eyr(f: str):
    return f.isdigit() and 2020 <= int(f) <= 2030


def hgt(s: str):
    u = s[-2:]
    n = s[:-2]
    if u == 'cm' and n.isdigit() and 150 <= int(n) <= 193:
        return True
    elif u == 'in' and n.isdigit() and 59 <= int(n) <= 76:
        return True
    return False


def hcl(s: str):
    return len(s) == 7 and s[0] == '#' and not s[1:].strip('0123456789abcdef')


def ecl(s: str):
    return s in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def pid(s: str):
    return len(s) == 9 and s.isdigit()


d = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid,
    'cid': lambda _: False
}

part1 = part2 = 0
for info in open('inp04').read().split('\n\n'):
    count1 = count2 = 0
    for field in info.split():
        key, value = field.split(':')
        count1 += key != 'cid'
        count2 += d[key](value)
    part1 += count1 == 7
    part2 += count2 == 7

print(part1)
print(part2)
