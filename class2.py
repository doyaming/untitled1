# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# p = Point(1,5)
# print(p.x+p.y)

# class Point:
#     def __init__(self):
#         self.x=3
#         self.y=4
# p1 =Point()
# print(p1.x, p1.y)
# p2 =Point()
# print(p2.x, p2.y)
# class FullName:
#     def __init__(self):
#         self.first = "Du"
#         self.last = "yaming"
# name1=FullName()
# print(name1.first,name1.last)

# class FullName:
#     def __init__(self, first, last):
#         self.first=first
#         self.last=last
# name1=FullName("shu","wang")
# print(name1.first,name1.last)
# name2=FullName("Du","yaming")
# print(name2.first,name2.last)

# class Point:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,srcx,srcy):
#         return (((self.x-srcx)**2)+((self.y-srcy)**2))**0.5
# p=Point(3,4)
# p.show()
# result=p.distance(0,0)
# print(result)


class File:
    def __init__(self,name):
        self.name=name
        self.file=None
    def open(self):
        self.file=open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
f1=File("data.txt")
f1.open()
data2=f1.read()
print(data2)
#ead second mutil data#
f2=File("data2.txt")
f2.open()
data3=f2.read()
print(data3)






