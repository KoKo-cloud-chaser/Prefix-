import os

def modify_lab_files(folder_path, prefix):
    # Define a set of labels to exclude from modification
    exclude_labels = {"SP", "AP", "cl", "vf", "q", "exh", "TRS"}
    
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file has a .lab extension
        if filename.endswith(".lab"):
            file_path = os.path.join(folder_path, filename)
            
            # Read the contents of the file
            with open(file_path, "r") as file:
                lines = file.readlines()
            
            # Modify each line according to the pattern
            modified_lines = []
            for line in lines:
                parts = line.strip().split()
                
                # Check if line has three parts and third part is not in exclude list
                if len(parts) == 3 and parts[2] not in exclude_labels:
                    # Reconstruct the line with the user-defined prefix
                    modified_line = f"{parts[0]} {parts[1]} {prefix}{parts[2]}"
                    modified_lines.append(modified_line)
                else:
                    # If the line should not be modified, keep it as it is
                    modified_lines.append(line.strip())
            
            # Write the modified lines back to the file
            with open(file_path, "w") as file:
                file.write("\n".join(modified_lines) + "\n")

    print("All .lab files have been modified, excluding specified labels.")

# Prompt the user for input and folder path
folder_path = input("Enter the path to your folder: ")
prefix = input("Enter the text you would like to add before each label (e.g., [-0-]): ")

# Run the modification function
modify_lab_files(folder_path, prefix)
