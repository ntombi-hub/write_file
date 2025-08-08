def modify_content(content):
    
     return content.upper()

def read_write_file():
    filename = input("Enter the name of the file to read")

    try:
        with open(filename,"r") as file:
            original_content = file.read()
            print("File read successfully.")

            modified_content = modify_content(original_content)

            new_filename = "modified_" + filename
            with open(new_filename, 'w') as outfile:
                outfile.write(modified_content)
                print("Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("Error : The File does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this read this file.")
    except Exception as e:
        print("An exception error occurred: {e}")                         