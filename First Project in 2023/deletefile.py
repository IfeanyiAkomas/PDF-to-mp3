import os

file_path = 'C:/xampp/htdocs/blog/public/images/testifier2.jpeg'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("file has successfully been deleted!")

else:
    print("This file does not exist!")
