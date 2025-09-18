#set syntax ,set can create only by set(),it is unordered collection of unique elements,unindeexing ,
a=set()
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    no=int(input())
    a.add(no)#add() method is used to add elements in set
print(a)
s=0
for x in a:
        s+=x
print(f"The sum is {s}")