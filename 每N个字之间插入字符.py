import os
str1 = input('你想处理的句子：')
str2 = str1.replace(' ','')
distance = int(input('隔几个字打一个斜杠(数字表示):'))
a = str2
b = []

l = len(a)
for n in range(l):
    if n % distance == 0:
        b.append(a[n:n+ distance])
#print b
print (r'\\'.join(b))
