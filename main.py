x = int(input())
y = str(input()).split()
z="EASY"
for i in range(0,x):
    if y[i]=="1":
        z="HARD"
    
print(z)
