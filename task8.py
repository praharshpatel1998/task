
filename = "output.txt"

# take first input from user and write
print ("enter text to write to the file ")
text1 = input()
file = open("output.txt", "wt")
file.write(text1)
file.close()
print(f"data successfully written to {filename}")

# take second input from the user in append mode
print ("enter additional text to append ")
text2 = input()
file = open("output.txt", "at")
file.write("\n"+ text2)
file.close()
print("data successfully appended")

# read the file

file = open("output.txt", "r")
contents = file.readlines()
print(f"final content of {filename}")
file.close()
for line in contents:
    print(line.strip())


