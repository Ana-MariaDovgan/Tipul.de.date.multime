a=set(input("Scrieti un sir A: "))
b=set(input("Scrieti un sir B: "))
print("Caractere ce se intilnesc cel putin o singura data:", a.union(b))
print("Caracterele care apar în ambele şiruri:", a.intersection(b))
print("Apar in A si nu in B:", a.difference(b))