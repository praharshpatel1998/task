import os


file_name = "sample.txt" # enter the file name 


if os.path.exists(file_name):
    with open("sample.txt", "rt") as fh:
        contents = fh.readlines()
        for content in contents:
            print(content.strip())
else:
    print("file not exists")
