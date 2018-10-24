numbersTaken =[2,5,8,10,12,15]

print("Numbers available")

for n in range(1, 20):
    if(n in numbersTaken):
        continue
    print(n)