rows = ['apple', 'banana', 'cat', 'dog', 'apple',
        'egg', 'fish', 'cat', 'grape', 'banana',
        'honey', 'ice', 'juice', 'cat', 'dog',
        'kiwi', 'lemon', 'mango', 'nut', 'apple']
d = {}
for x in rows:
    d[x] = d.get(x,0)+1
#print(d)

top = sorted(d.items(),key=lambda kv:kv[1],reverse=True)
print(top)