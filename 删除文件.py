# importing the os Library
import os

# checking if file exist or not
if os.path.isfile("ttest.txt"):

    # os.remove() function to remove the file
    os.remove("ttest.txt")  # remove it

    # Printing the confirmation message of deletion
    print("File Deleted successfully")
else:
    print("File does not exist")
# Showing the message instead of throwig an error
