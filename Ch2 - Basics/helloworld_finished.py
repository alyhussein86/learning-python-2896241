#
# Example file for HelloWorld
# LinkedIn Learning Python course by Joe Marini
#


# def main():
#     print("hello world!")
#     name = input("What is your name? ")
#     print("Nice to meet you,", name)
# if __name__ == "__main__":
#     main()

def testpali(mylist):
    if mylist == mylist[::-1]:
        return True
    return False

program = True

while (program):
    mylist = input("Enter Text for Palindrome Test or 'exit':")

    mylist = mylist.lower()

    if mylist == "exit":
        program = False
        break

    newstr = ""
    for x in mylist:
        if x.isalnum():
            newstr += x

    print("The palindrome test is ",testpali(newstr))