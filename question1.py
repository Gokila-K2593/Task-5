with open('file1.txt', 'r') as source_file, open('file2.txt', 'w') as destination_file:
    content = source_file.read()
    destination_file.write(content)
print("File copied successfully!")
