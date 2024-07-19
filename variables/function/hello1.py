def main():
    name = input("What's your name?")
    hello(name)
# print(name)


# define a function hello that takes an optional argument to print a greeting message
# to = "world" means that if you call the hello function without providing any argument, to will automatically be set to "world".
def hello(to = "world"):
    print(f"hello,", to)

main()






























