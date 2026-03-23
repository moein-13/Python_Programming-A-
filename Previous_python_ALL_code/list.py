"""friends = ["karin","rahim","aman","rahul","ratul","lee john","saddam"]
         ##     0        1     2      3       4        5          6

friends [0] = "karim" ## updated index 0 . karin to karim.

print(friends[0:7])



list  = ["python", "java", " C++", "C#"]
list1 = [21  ,22 , 23]
##list.append()
##list.insert(1 , "Bhai") ## Insert use for adding elements
list.extend(list1)
list1.extend(list)
print(list)
print(list1)


list = [1,2,1,3,4,1,5,3,1,5,6]
friends = ["Moein" , "Rony" , "Molla","Sadman","Zarif", "Pa2"]
print(list.count(5))     ## that will return how many times that perticular nums or element is repeat.
print(list.index(6))     ## that will tell us the index num of the element
friends.sort()           ## it will return in ascending order
print(friends)
list.reverse()
print(list)
list1 = list.copy()
list1.reverse()

print(list1)
"""

drinks = ["coffee", "tea" , "sprite"]
dinner = ["rice", "pizza", "hotdog"]
dessert = ["ice creame" , "sweet","cake"]

food = [drinks , dinner , dessert]

#print( food , end = " ")

print(food[2][0])




