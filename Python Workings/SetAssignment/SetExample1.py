phones = {'Apple','Samsung','Oppo','Blackberry','Nokia'}
print(phones)

print("Length of the Set : ", len(phones))

phones.add('Google')
print(phones)

newPhones = {'Xioami',"Sony","Hauwei"}
phonesList = list(phones) + list(newPhones)
phonesSet = set(phonesList)

print(("New Phones added : "))
print(phonesSet)

print("Index of 5 : ", list(phonesSet)[5])
print()

print("Delete the First from the Set : ")
phonesSet.remove("Apple")
print(phonesSet)
print()

print("Remove a random element of the Set : ")
phonesSet.pop()
print(phonesSet)
print()