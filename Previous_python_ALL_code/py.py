
#n = 0
#while n < 5:
 #   print (n)
  #  n +=1

#for i in range (5):
 #       print(i)
''''
print(int(-3/2))

print(10 % 3)

import math
print(math.fmod( -10 , 3))
print(math.floor(4/2))
print(math.sqrt(2))
print(math.pow(2,3))



arr = [1,2,3]
print(arr)
arr.append(4)
print(arr)
arr.pop()
print(arr)
arr.insert(1,6)
print(arr)


nums = [1,2,3]

for i , n in enumerate(nums):

    print(i,n)
for n in range (len(nums)):
   print(nums[n])

for n in nums:
    print (n)

arr1 = [1,4,2,6,3,8]
arr1.sort()
print(arr1)
arr1.sort(reverse=True)
print(arr1)

arr = ["ahi" , "hello" , "anha"]

arr.sort(key=lambda x : len(x))
print(arr)



fruit = ["apple" , " banana " , " orenge" , " cherry ","mango"]

#fruit.sort(key=lambda c : len(c))
newlist  = [ c for c in fruit if "a" in c]
print(newlist)


s = "abc"

print(s[0:2])
s+="def"
print(s)


# in rare case U may need the ASCII value then

print(ord('A'))
print(ord('m'),ord('o'),ord('e'),ord('i'),ord('n'))
print(ord('M'),ord('O'),ord('E'),ord('I'),ord('N'))


# COMBINE A STRINGS ELEMENTS
# DELIMITOR

c = ["ab","cd", "ef"]

print("" .join(c))


from collections import deque
# QUEUE

queue = deque()

queue.append(1)
queue.append(2)
print(queue)
queue.popleft()
print(queue)
queue.appendleft(1)
queue.append(3)
print(queue)



# HASHSET

myset = set()

myset.add(1)
myset.add(2)
print(myset)
print(len(myset))
print(1 in myset)   # that will return the boolean type // else true or false.
print(3 in myset)
myset.remove(2)
print(myset)
print(2 in myset)

ms = set()

ms = [i for i in range(5) ]
print(ms)

mymap = {}

mymap ["Moein"] = 22
mymap ["Tanha"] = 20

print(mymap)

# Dictionary comprehension

myset = { i : 2*i for i in range(3)}
#OR
myset1 = {0 : 0 , 1: 2 , 2:4}
print(myset)
print(myset1)


mynam = {"Moein" : 22 ,"Tanha" : 20 }
for key in mynam:
        print(key,mynam[key])

for val in mynam.values():
    print(val)
for key , val in mynam.items():
    print(key,val)

'''


# Heaps

import heapq

minheap = []
heapq.heappush(minheap , 3)
heapq.heappush(minheap , 2)
heapq.heappush(minheap, 4)
heapq.heappush(minheap, 1)

print(minheap)  # print the minheap , but it will print the min first.
while len(minheap):
    print(heapq.heappop(minheap))  # it will print the entire heap from small to largest.
    










