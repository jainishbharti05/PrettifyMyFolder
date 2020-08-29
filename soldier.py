import os


def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)

    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        print()
        if file not in filelist:

            os.rename(file, file.capitalize())

        if file.endswith(f"{format}"):
            os.rename(file,f"{i}{format}")
            i+=1

soldier(r"C:\Users\jaini\Desktop\testing", "jb.txt", ".png")
