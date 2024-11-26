def modify_file_content(input_file, output_file):
    try:
        # Reading the input file
        with open(input_file, 'r') as infile:
            content = infile.readlines()
        
        # Modifying the content (e.g., making text uppercase)
        modified_content = [line.upper() for line in content]
        
        # Writing to the output file
        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"File '{input_file}' has been successfully modified and saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for file '{input_file}' or '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask for filenames
input_filename = input("Enter the name of the file to read: ")
output_filename = input("Enter the name of the file to write: ")

# Execute the function
modify_file_content(input_filename, output_filename)
