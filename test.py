
print("Hello")
for i in range(10):
    print(f"{i}".format(1,2,3,4,5,6,7,8,9,0),end=",")
print()
D = {1:2,2:1}
print(list(D.keys()))
x=0
y=1
while x!=5:
    x+=True
    y *= 10*(False+1)
    print(x,y)

print(1 and 0)

def qvart(x):
    return x*x

x= range(5)
print(list(map(qvart,x)))