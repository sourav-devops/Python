names = ['sourav', 'ram', 'shyam']
print(f"my name is {names[0]}")
print(f"hi {names[1]} , this is the first time u are coming to my home. i welcome you {names[1]}")
print(f"actually  {names[-1]} couldn't make it today")

absent = 'shyam'
names.remove(absent)
names.append('raja')

print(f"as {absent} couldnt make it i have invited {names[-1]} to join us")
