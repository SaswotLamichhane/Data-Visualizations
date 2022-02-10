import random
routine = []
subjects = ['English', 'Science', 'Nepali', 'Social', "Nepse", 'Parisuchak', "Sharemarket"]
# t = ['1','2','3','4','5']
LEN = 6
D = 6
# print('Enter the name of the subjects seperated by space')
# subjects = input('> ').split()
# len_s = len(subjects)+1
# print('\n', 'Enter the number of Periods')
# LEN = int(input('> '))
# D = int(input('> '))
# while LEN >= len_s and D >= len_s:
#     print('Subjects not sufficient for the number of periods')
#     input('Enter a number greater than subjects > ')
# print('\n', 'Enter the number of days')
def make(LEN):
    c = []
    for i in range(LEN):
        subject = random.choice(subjects)
        while subject in c:
            subject = random.choice(subjects)
        c.append(subject)
    return c

for i in range(D):
    sub = make(LEN)
    for i in routine:
        for n in range(LEN):
            s = sub[n]
            o = i[n]
            if sub[n] == i[n]:
                choice = random.choice([d for d in subjects if d != i[n]])
                while choice in sub:
                    choice = random.choice(subjects)
                sub[n] = choice
    routine.append(sub)
# c = 0
# length = int((len('  '.join(routine[0]))-7)/2)
# print('-'*length, 'Periods', '-'*length)
# for i in range()
# for i in routine:
#     print(' | '.join(i))

for i in routine:
    for elements in i:
        print(f' {elements:^16} ', end=' ')
    print()
# row_format ="{:>15}" * (len(subjects) + 1)
# print(row_format.format("", *subjects))
# for team, row in zip(t, routine):
#     print(row_format.format(team, *row))
 