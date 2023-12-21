#Ask user for their name
#name = input("What's your name? ").strip().title()

#Split user's name into first name into first name and last name
#first, last = name.split(" ")
#Remove whitespace from str and capitalize user's name
#name = name.strip().title()
#Capitalize user's name
#name = name.capitalize()
#name = name.title()

#Say hello to user
"""
print("hello,",name) # with ,
print("Hello, "+name) # with +
print("Hello, ", end="?")
print(name)
print("hello,", name, sep="123456")
"""

"""
is a comment
hello
"""
#print(f"hello, {first}")
#print('hello, "friend"')
#print("hello, \"friend\"")

"""
def hello():
    print("hello")
"""
"""
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to = "world"):
    print("hello,", to)


main()
"""

def main():
    name = input("What's your name? ")
    print(hello(name))
    

def hello(to = "world"):
    return f"Hello, {to}"

if __name__=="__main__":
    main()

infor = {
    "name": "Van Uy Tri",
    "age": "20",
    "address": "Ben Tre city",
    "school": "Ben Tre College",
}