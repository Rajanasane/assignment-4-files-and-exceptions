first = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(first + "\n")
print("Data successfully written to output.txt.\n")

second = input("Enter additionsl text to append: ")
with open("output.txt", "a") as file:
    file.write(second + "\n")

print("Data successfully appended.\n")

print("Final content of output.txt")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
