import os

path = "C:/Users/jiaju/OneDrive/Desktop/Software Development Passion Projects/Python Projects/Mini-Projects/images/"
common_filename = input("Enter new file name: ")
i = 0
for filename in os.listdir(path):
    file_extension = os.path.splitext(path + filename)[1]       # Get the file extension of the file
    new_filename = common_filename + str(i) + file_extension    # New filename will be input + i + filextension
    dest = path + new_filename    
    os.rename(path + filename, dest)                        # Rename the files
    print("Renamed " + filename + " to " + new_filename)
    i=i+1