# Open file1.txt in read mode ('r') and file2.txt in write mode ('w')
with open('file1.txt', 'r') as source_file, open('file2.txt', 'w') as destination_file:
    # Read the contents of file1.txt
    content = source_file.read()
    
    # Write the contents to file2.txt
    destination_file.write(content)

print("File copied successfully!")
