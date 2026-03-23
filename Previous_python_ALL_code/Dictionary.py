dict ={
    "Name" : "Moein",
    "Age" : 21,
    "DOB" : "14-11-2001"
}
#print(dict)
#print(len(dict))
#print(dict["Name"])

#      print the  datatype of the dictionary

thisdict ={
    "Name" : "Moein",
    "Age" : 21,
    "DOB" : "14-11-2001"
}
#print(type(thisdict))
#print(thisdict.keys())


for key, value in thisdict.items():
    print(key,value)