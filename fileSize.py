import os
import shutil

# Input directory containing files to sort
dir_path = input("Paste the absolute directory path (use / or \\): ").strip().strip('"')
dir_path = os.path.normpath(dir_path)

if os.path.isdir(dir_path):
    print("File exists and path is valid!")
else:
    print("Invalid file path or file does not exist.")

# Define subdirectories for categorized files
sf_p = os.path.join(dir_path, "Small files")
mf_p = os.path.join(dir_path, "Medium files")
lf_p = os.path.join(dir_path, "Large files")

# Create folders if they don't exist
os.makedirs(sf_p, exist_ok=True)
os.makedirs(mf_p, exist_ok=True)
os.makedirs(lf_p, exist_ok=True)

# List all files in the directory
for name in os.listdir(dir_path):
    f_path = os.path.join(dir_path, name)
    if name in ["Small files", "Medium files", "Large files"]:
           continue  # Don't touch output folders

    if os.path.isfile(f_path):
       

        file_size = os.path.getsize(f_path)

        try:
            if file_size <= 100_000:
                shutil.move(f_path, sf_p)
            elif 100_000 < file_size <= 1_000_000:
                shutil.move(f_path, mf_p)
            else:
                shutil.move(f_path, lf_p)
        except shutil.Error as e:
            print(f"Error moving {name}: {e}")
    elif os.path.isfile(f_path)!=True:
        print(f"Skipping {name} as it is a folder")
print("\nFiles successfully segregated")
    
    

