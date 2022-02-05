from os import close


with open("history/1/2020.txt","r",encoding='utf-8') as file_object:
    #for line in file_object:
       #print(line.rstrip()) 



    lines = file_object.readlines()
for line in lines :
    line += " "
    print(len(line.rstrip()))
    
