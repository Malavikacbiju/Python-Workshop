#list,dict,tuple,set

#list is mutable,python collection of ordered elements and indexed,created using [] or list(),it also allows duplicate elements,and accessed using index
#tuple is immutable
#dict is key value pair
#set is unordered collection of unique elements

#sum of elements in a list
a=[]
n=int(input("Enter the limit:"))
print("Enter the elements:")
for i in range(0,n):
    k=int(input())
    a.append(k)
s=0
for i in range(0,n):
        s=s+i
print(f"The sum is {s}")

#sum of even numbers in a list
#minus indexing left to right

