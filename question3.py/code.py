# Open all files: file1.txt and file2.txt for reading, merged.txt for writing
with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2, open('merged.txt', 'w') as merged_file:
    
    # Read lines from both files
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()
    
    # Get the maximum length of both files
    max_length = max(len(file1_lines), len(file2_lines))

    # Iterate through the lines of both files
    for i in range(max_length):
        # Write a line from file1 if it exists
        if i < len(file1_lines):
            merged_file.write(file1_lines[i].strip() + "\n")  # .strip() removes extra newline

        # Write a line from file2 if it exists
        if i < len(file2_lines):
            merged_file.write(file2_lines[i].strip() + "\n")

    print("Files merged successfully into 'merged.txt'!")
