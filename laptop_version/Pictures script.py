import requests
import shutil


'''
f = open("C:/Users/nigel/Desktop/fileresults.txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close()
'''
# container is an array that will hold only the id numbers.
container = []
#numbers = ""

#f opens the path to the txt folder and reads ("file.txt", "r")
f = open("D:/jail text files/fileresults.txt","r")

#mode confirms that the file is being read. 
if f.mode == "r":
    contents = f.read()
    
#for loop that is reading the contents of "file.txt" and using the length of file to
#determine how far it should loop.
    
    for x in range(len(contents)):
        file = contents[x]
        if file == 'i':
            if contents[x+1] == 'd':
                numbers = ""
                #print(file+contents[x+1])
                for y in range(3,9):
                    numbers+=str(contents[x+y])
                    #container.append(contents[x+y])
                container.append(int(numbers))
                
        else:
            continue
for y in range(len(container)):
    #print(container[y])
    id_num = str(container[y])
    url = "https://www.linnsheriff.org/wp-content/mugshots/"+id_num+".jpg"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    response = requests.get(url,headers=headers,stream=True)
    #check to see if you should use w+ instead wb in your file writting.
    with open('D:/jail text files/Pictures/'+str(y)+'.jpg', 'wb') as f:  
        f.write(response.content)
