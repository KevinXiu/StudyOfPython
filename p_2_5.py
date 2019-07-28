"""
# 字符串
print("good good study,day day up")
print('what\' your name')
a = 'tandachun'
b = 1998
# str将整数对象转换为字符串对象
print(a + str(b))
print(a + repr(b))
# raw_input函数
name = input("what's your name")
print(name)
print(a,b)
"""

#input
"""
name = input("what's your name")
age = input(" how old are you")
print("您的个人信息为:\n","姓名："+name+"  "+"年龄："+str(age)+"岁")
"""
#取消输出中的转义字符
"""
print(r"hahha/n")
print("jajjaj//n")
"""
#字符串的格式化输出
"""
a = "KevinXiu"
b = 500
print("Chongqing is more than %d years.%s is live in here"%(b,a))

print("Chongqing is more than {} years .{} live in here".format(b,a))

print("I'm %(age)d years old" %{"age": 15})
"""
#字符串的常用方法
#1、isalpha
a = "anjfkvn"
print(a.isalpha())
a = "fvnjkn1"
print(a.isalpha())
#2. split分割
a = " I love you"
h = a.split(" ")
print(h)
#3.去空格
name = "            tandachun                 '"#两边都有空格
print(name.strip()) #去两边空格
print(name.lstrip())#去左边的空格
print(name)
print(name.rstrip())#去右边的空格
#4.字符大小的转换
a = "tandachun,Python"
print(a)
print(a.upper())#小写变大写
print(a.lower())#大写变小写
print(a.capitalize())
print("jnvjkn Ymklmd".istitle())
#5,join拼接字符
b = "www.baidu.com"
c = b.split(".")
d = ".".join(c)
print(b)
print(c)
print(d)
