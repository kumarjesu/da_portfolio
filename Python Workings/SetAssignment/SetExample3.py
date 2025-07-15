setA = {"Apple","Samsung","Oppo","Blackberry","Nokia"}
listA = ["Xioami","Sony","Hauwei"]
print("Set A : ", setA)
print("List A : ", listA)
print(type(setA))
print(type(listA))
print("Add Set and List : ")
setA.update(listA)
print(setA)
print()
print("Loop through Sets : ")
for x in setA:
    print(x)