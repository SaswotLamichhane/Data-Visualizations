with open('clean.csv', 'a+') as w:
    with open('owid-covid-data.csv', 'r') as f:
        for i in f.readlines():
            if 'Nepal' in i:
                w.write(i)