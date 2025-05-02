try:
    with open("Sample.txt", "r") as file:
        print("Reading file content:")

        for i,line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'Sample.txt was not found.")