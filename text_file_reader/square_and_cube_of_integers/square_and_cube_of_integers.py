with open("integers.txt", "r") as source:
    file_double = open("double.txt", "w")
    file_triple = open("triple.txt", "w")

    for line in source:
        num = int(line.strip())
        if num % 2 == 0:
           file_double.write(str(num ** 2) + "\n")
        else:
           file_triple.write(str(num ** 3) + "\n")

    file_double.close()
    file_triple.close()
print("Files generated.")
