import os, sys
folda = "C:/your/folder/here"
for file in os.listdir(folda):
    name = os.path.join(folda,file)
    # print(name)
    if not os.path.isfile(name): continue
    newname = name.replace('.jfif', '.jpg')
    output = os.rename(name, newname)
