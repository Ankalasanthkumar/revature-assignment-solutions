filename = input("Enter file name: ")
n = int(input("Enter number of last lines to read: "))

with open(filename, 'r') as file:
    lines = file.readlines()
    last_lines = lines[-n:]



print("\nLast", n, "lines from the file:")
for line in last_lines:
    print(line, end='')

filename = input("Enter file name: ")

with open(filename, 'r') as file:
    lines_list = [line.strip() for line in file]

print("\nList of lines from file:")
print(lines_list)


filename = input("Enter file name: ")

with open(filename, 'r') as file:
    line_count = sum(1 for _ in file)

print("\nNumber of lines in the file:", line_count)


filename = input("Enter file name: ")

with open(filename, 'r') as file:
    words = file.read().split()
    max_length = len(max(words, key=len))
    longest_words = [word for word in words if len(word) == max_length]

print("\nLongest word(s) in the file:")
print(longest_words)
