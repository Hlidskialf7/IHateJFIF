import os, sys
folda = "C:/Users/Tsu/Desktop/test"
for file in os.listdir(folda):
    name = os.path.join(folda,file)
    # print(infilename)
    if not os.path.isfile(name): continue
    newname = name.replace('.jfif', '.jpg')
    output = os.rename(name, newname)