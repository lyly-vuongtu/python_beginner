"""
names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")


#xóa cũ viết mới
#file = open("names.txt", "w")
#viết tiếp
file = open("names.txt", "a")

file.write(f"{name}\n")
file.close()

name = input("What's your name? ")

with open("names.txt","a") as file:
    file.write(f"{name}\n")
    """
# in ra dòng đã viết trong names.txt có chữ hello phía trc
"""with open("names.txt", "r")as file:
    for line in file:
        print("hello,", line.rstrip())
    
    lines =file.readlines()

for line in lines:
    #print("hello,", line)
    print("hello,", line.rstrip())

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())"""

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")

