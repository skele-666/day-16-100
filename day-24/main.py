# READING
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Different way to open
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    # Don't need to manually close

# WRITING
with open("new__file.txt", mode="w") as file:
    file.write("\nNew text.")