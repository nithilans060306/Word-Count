num = 0
with open("Word-Count/Text.txt","r") as f:
    for i in f:
        w = i.split()
        num += len(w)
print("THe Number of words in the file is",num)






