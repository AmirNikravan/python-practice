import hashmaker
from os import system
system("clear")
print("Welcome to passwrod hacker with Amir :)")
file_path = input("Please enter the file that contains username and passwrds :")
hashmaker.make_hash()
passes = dict()
passes = hashmaker.hashtodict()
status = input("do you want to save result or just show on the konsole ?(save/show)")

result = dict()
with open(file_path , "r") as file:
    for line in file:
        if line.split(',')[1].strip() in passes:
            result[line.split(',')[0]] =passes[line.split(',')[1].strip()]
        else :
            print(f"""Your passwrod 
                  with hash <<<{line.split(',')[1].strip()}>>> is not between 0000 and 9999 chekck it""")    
if status == "save":
    with open("./Passwrods.txt" , "w") as file:
        for line in result : 
            file.write(f"{line} = {result[line]}\n")
else :
    system("clear")
    for line in result:
        print(f"{line} = {result[line]}") 

# passwrods are :
# sara = 0000
# amir = 1234
# abbas = 5678
# ahmad = 9753