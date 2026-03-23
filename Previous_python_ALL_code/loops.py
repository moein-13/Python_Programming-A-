# ++++++ WHILE LOOPS IN PYTHON ++++++
"""
count = 1
while(count <=5 ):
    count = count+1
    print("Moein")


       ## for infinite loops use this code.

count = 0
while(count == 0)
     print("moein")



count1 = 0
while(count1 < 4):
    count1 = count1 + 1
    print('Moein')

else:
    print("In else Block.")


#  ++++++ FOR LOOPS IN PYTHON ++++++

n=4
for i in range(0 , n):
    print(i)


l = ["python", "java", "C++", "php"]

for i in l:
    print(i)

print("\nString things.")
s = "Moein"

for i in s :
    print(i)

print("\nDictionary Iteration")
d = dict()
d['abc '] = 123
d["xyz "] = 963

for i in d:
    print("%s" "%d" % (i, d[i]))

print("\nSet Iteration.")
set = {1,2,3,4,5}
for i in set:
    print(i)
"""
                       # NASTED LOOPS

for i in range(1 , 5):
    for j in range(i):
        print(i , end= ' ')
    print()



for i in 'Mominul':
    if i == 'm' or i =='u':
        continue
    print("Current letter :", i)

for j in 'Mominul':
    if i == 'm' or i == 'u':
        break
    print("\nCurrent letter :" , i)

# pass will return the last letter of the word.

for letter in 'Moein':
    pass
print("\nLast letter : ", letter)

