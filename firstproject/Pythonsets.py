my_set = {"sun","moon","earth"}
print(my_set)
for x in my_set:
    print(x)
print("sun" in my_set)
my_set.add("mars")
print(my_set)
my_set.update(["venus","mercury"])
print(my_set)
print(len(my_set))
my_set.remove("mars")
print(my_set)
my_set.discard("mars")

my_set.pop()
print(my_set)
my_set_1= {"apple","loop",2,3,4}
print(my_set_1)
# UNION | INTERSECTION
A={'D','F',23,44,1,2,}
B={'D','G',1,3,4,55,6}
print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)

print(A.symmetric_difference(B))
