numerals = [3,5]
associates = ['Fizz', 'Buzz']
for i in range(1,101):
    reply = ''
    for j in numerals:
        if i%j == 0:
            reply += associates[numerals.index(j)]
    print(i if reply == '' else reply)
