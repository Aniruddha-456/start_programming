# accessing elements of a string using [] index operator
#  [start : end : step] == [inclusive : exclusive : step]  == && [::] == everything

num = "1234-5678-9012-3456"

print(num[::])  # print everything
print(num[0:4]) # print 1st 4 digits 0,1,2,3 and 4 is not included
print(num[::3])  # print evry 3rd element
print(num[-1]) # print last number
print(num[::-1]) # print from last
print(num[-4:])