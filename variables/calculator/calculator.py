#
def main():
    x = int(input("What's x?"))
    print("x squared is", square(x)) 

def square(n):
    # return n * n # returns square root
    return pow(n, 2)

main()


# # define x define y as whole numbers
# # x = int(input("What's x?"))
# # y = int(input("What's y?"))

# x = float(input("What's x?"))
# y = float(input("What's y?"))

# # function above is the same as the below this one is split between 3 lines
# # x = input("What's x?")
# # y = input("What's y?")
# # integer x + integer y the above does the same thing with less lines
# # z = int(x) + int(y)

# # functions below is the sum of the original lines 2 and 3
# # print(x + y )
# # z = round(x + y)

# # divide x and y
# z = x / y

# #f string approach
# # print(f"{z:.2f}")
# # format z with commas separating the thousands
# # print(f"{z:,}")
# # function below is the docs fucntion to make decimals whole numbers
# # round(number[, ndigits])

# print(z)


