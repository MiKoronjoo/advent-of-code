part1 = part2 = 0
for group in open('inp06').read().split('\n\n'):
    questions = set(group.replace('\n', ''))
    part1 += len(questions)
    pn = group.strip().count('\n') + 1
    part2 += sum(group.count(q) == pn for q in questions)

print(part1, part2, sep='\n')
