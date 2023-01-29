set1 = set(input("Set1 - Enter the space seperated inputs : ").split())
set2 = set(input("Set2 - Enter the space seperated inputs : ").split())
print("Set1 : ", set1)
print("Set2 : ", set2)
print("\n")
print("Operations : ", "\n", "1) Add || 2) Remove || 3) Difference || 4) Intersection")
math = int(input("Choose one Operation : "))
set = int(input("Choose a set to operate : "))
print("\n")
#Adding elements in the set
if (math == 1 and set == 1):
    ad1 = input("Enter the element that you want to ADD : ")
    set1.add(ad1)
    print("Modified Set : ", set1)
elif (math == 1 and set == 2):
    ad2 = input("Enter the element that you want to ADD : ")
    set2.add(ad2)
    print("Modified Set : ", set2)
    
#Removing elements from the set
if (math == 2 and set == 1):
    delete1 = input("Enter the element that you want to REMOVE : ")
    set1.remove(delete1)
    print("Modified Set : ", set1)
elif (math == 2 and set == 2):
    delete2 = input("Enter the element that you want to REMOVE : ")
    set2.remove(delete2)
    print("Modified Set : ", set2)
    
#Different elements in both the sets
if (math == 3 and set == 1):
    gap1 = set1.difference(set2)
    print("Different elements in the Set1 : ", gap1)
elif (math == 3 and set == 2):
    gap2 = set2.difference(set1)
    print("Different elements in the Set2 : ", gap2)
    
#Intersecting elements in both the sets
if (math == 4 and set == 1):
    same1 = set1.intersection(set2)
    print("Intersecting elements in the Set1 : ", same1)
elif (math == 4 and set == 2):
    same2 = set2.intersection(set1)
    print("Intersecting elements in the Set2 : ", same2)
