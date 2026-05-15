#fav_num

fav_num = {'sourav':22,
           'sam':21,
           'mohan':29,
           'ram':10,
           'rohit':45,
           'virat':18,
           'anshika':8,
           }
friends = ['anshika','sourav']
for name in sorted(fav_num):
    print(f"This is {name.title()}.")
    if name in friends:
        print(f"Your jersey number is {fav_num[name]}")

