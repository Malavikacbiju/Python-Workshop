#tuple syntax: (element1,element2,element3)
#TUPLE IS IMMUTABLE that means we cannot change,add,remove elements once tuple is created,it can created using () or tuple()
a=()
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    no=int(input())
    a=a+(no,)
print(a)
s=0
for i in range(0,n):
        s+=a[i]
print(f"The sum is {s}")