import re

pp = r'(byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:)'
pattern = r'(byr:(19[2-8][0-9]|199[0-9]|200[0-2])\s|iyr:(201[0-9]|2020)\s|eyr:(202[0-9]|2030)\s|hgt:(1[5-8][0-9]|19[0-3])cm\s|hgt:(59|6[0-9]|7[0-6])in\s|hcl:#[0-9a-f]{6}\s|ecl:(amb|blu|brn|gry|grn|hzl|oth)\s|pid:\d{9}\s)'

part1 = part2 = 0
for info in open('inp04').read().split('\n\n'):
    part1 += len(re.findall(pp, info)) == 7
    part2 += len(re.findall(pattern, info + ' ')) == 7

print(part1, part2, sep='\n')
