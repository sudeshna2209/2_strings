'''Anything which lies in between single quotes,double quotes and three single quotes
 and three double quotes that which assigned to a print statement or to any variable is known as Strings '''

print(len("python"))

a="python"
print(a,type(a))
print(a[0])

'''index position starts from 0'''
'''length will be calculated from 1 and space also calculated in length'''


a="python"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

print(a)
print(len(a))
'''from backside the index starts from -1'''

a="python"
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
print(a[-6])

'''This is single line comment'''

"""This is multiline comment"""

'''Strings are immutable because modification cannot be done'''

a="hello"
print(a)
a[0]='H'

'''This error occurs so strings are immutable TypeError: 'str' object does not support item assignment'''
