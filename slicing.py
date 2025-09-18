#slicing syntax
#listname[start:stop:step]
list1=[10,20,30,40,50,60,70,80,90]
print(list1[0:9:2])#prints from index 0 to 8 with step 2
print(list1[1:9:3])#prints from index 1 to 8 with step 3
print(list1[:5])#prints from index 0 to 4   
print(list1[4:])#prints from index 4 to end
print(list1[:])#prints whole list       
print(list1[-1])#prints last element
print(list1[-3:])#prints last 3 elements
print(list1[-5:-1])#prints from index -5 to -2
print(list1[::-1])#prints whole list in reverse order
print(list1[-2::-1])#prints from index -2 to 0 in reverse order
print(list1[-1:-6:-1])#prints from index -1 to -5 in reverse order
print(list1[-3:2:-1])#prints from index