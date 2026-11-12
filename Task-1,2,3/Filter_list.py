n =[]
print(n)

for i in range(50):
    if i > 0:
        n.append(i)

print(n)

even_n = [i for i in range(1,50) if i%2==0]

print(even_n)