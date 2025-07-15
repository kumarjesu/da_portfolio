intSetA = {19,22,24,20,25,26}
intSetB = {19,22,20,25,26,24,28,27}
print("Set A: ", intSetA)
print("Set B: ", intSetB)
print()

print("Join 2 Sets : ")
intSetC = intSetA | intSetB
print(intSetC)
print()

intSetD = intSetA.intersection(intSetB)
print("Set A Intersect with Set B (Common Values in both set) : ", intSetD)
print()

print("Is Set A SubSet of Set B : ", intSetA.issubset(intSetB))
print("Is Set B SubSet of Set A : ", intSetB.issubset(intSetA))
print()

print("Is Set A Disjoint Set of Set B : ", intSetA.isdisjoint(intSetB))
print("Is Set B Disjoint Set of Set A : ", intSetB.isdisjoint(intSetA))
print()

copySet = intSetA.copy()
copySet.add(29)
print("Copy of a Set : ",copySet)
print()

print("Difference between 2 Sets (Set B & Set A) : ", intSetB.difference(copySet))
print("Difference between 2 Sets (Set B & Set A) : ", copySet.difference(intSetB))
print()

setA = copySet.copy()
setB = intSetB.copy()
print("Returns the common of both sets !!!!!")
intSetA.intersection_update(intSetB)
print(intSetA)
intSetB.intersection_update(copySet)
print(intSetB)
print()

print("Symmetric Difference between Set A and Set B : ")
symmetricDiffAB = setA.symmetric_difference(setB)
print(symmetricDiffAB)
symmetricDiffBA = setB.symmetric_difference(setA)
print(symmetricDiffBA)
print()
