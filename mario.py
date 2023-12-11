def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row("#"* size)
"""    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #Print brick
            print("#", end="")
        print()

    for _ in range(height):
        print("#")"""
def print_row(width):
    print("#"* width)
main()
    