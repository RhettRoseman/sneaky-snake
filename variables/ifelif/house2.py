name = input("What is the student's name?")

# keyword match (look at python docs for more information)

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    # case _ in this case = any info that has not yet been defined will turn who
    case _:
        print("Who?")