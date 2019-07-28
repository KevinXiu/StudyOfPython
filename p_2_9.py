"""
#list列表
a = [2,3,'github','KevinXiu']
print(type(a))
print(bool(a))
print(a)
print(a[0]+a[1])
print(a[::-1])
print(list(reversed(a)))
a.reverse()
print(a)
"""

#排序
a = [4,5,6,5,1,2,3]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
b = [5,6,4,5,1,2,36,5,5]
print(sorted(b))