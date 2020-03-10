import requests
from bs4 import BeautifulSoup as bs
import shutil
import xlwt



def requesting_jail_id_data():


    url = "https://www.linnsheriff.org/jail/current-inmates/"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    response = requests.get(url, headers=headers)

    soup = bs(response.content,"html.parser")
    soup_html = soup.prettify
    soup_tags = soup.find_all("td")


    #here I am taking the soup_tags var and writing to a txt file on my desktop.
    f = open("D:/jail text files/fileresults.txt","w+")
    #for i in range(len(soup_tags)):
    f.write(str(soup_tags))
    f.close()


    
def picture_jail_roster():
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


def write_to_spreedsheet():


    path = "D:/jail text files/"
    path_excel = path+"writting.xls"
    #below code was extracted from file writting script, needs a function class for
    #future readability.

    # container is an array that will hold only the id numbers.
    container = []
    #numbers = ""

    #f opens the path to the txt folder and reads ("file.txt", "r")
    f = open(path+"fileresults.txt","r")

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

    count=1


    wb = xlwt.Workbook()
    #edit 1/13/2020
    ws = wb.add_sheet("test",cell_overwrite_ok=True)

    for total_list in range(len(container)):
        id_num = str(container[total_list])
        
    ##############################################################################
    #####
        url = "https://www.linnsheriff.org/jail/current-inmates/view-inmate/?id="+id_num
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        response = requests.get(url, headers=headers)
        soup = bs(response.content,"html.parser")

        
        #this loop is for name
        for z in soup.find_all("h2"):
            
            ws.write(count,0,'<img src="http://linncountyjailroster.com/wp-content/uploads/Pictures/'+ str(count) +'.jpg" alt="inmate"></a>')
            ws.write(count,1,str(z.get_text()))
            wb.save(path_excel)
            
            break
        
        #this loop is for age, date lodged, arresting agency, scheduled release date.         
        for y in soup.find_all("ul",{'class':"inmate-details list-unstyled"}):
            colmn = 1
            for x in y.find_all("li"):
                if colmn == 1:
                    age = str(x.get_text())
                    #print(age[6:])
                    ws.write(count,colmn,age[7:])
                    wb.save(path_excel)
                elif colmn == 2:
                    Date_lod = str(x.get_text())
                    #print(Date_lod[13:])
                    ws.write(count,colmn,Date_lod[14:])
                    wb.save(path_excel)
                elif colmn == 3:
                    Arresting_Agency = str(x.get_text())
                    #print(Arresting_Agency[19:])
                    ws.write(count,colmn,Arresting_Agency[19:])
                    wb.save(path_excel)
                elif colmn == 4:
                    Release_Date = str(x.get_text())
                    #print(Release_Date[23:])
                    ws.write(count,colmn,Release_Date[23:])
                    wb.save(path_excel)
                #elif colmn==5:
                    
                else:
                    ws.write(count,colmn,str(x.get_text()))
                    wb.save(path_excel)
                
                colmn+=1
        Charges=""       
        for x in soup.find_all("td"):
            Charges += str(x.get_text()+"@ ")
            #charges.append(str(x.get_text()))
        #print(Charges)
            
        ws.write(count,6,str(Charges))
        wb.save(path_excel)
        count+=1
    
if __name__ == "__main__":

    #gathers all data to text file.
    requesting_jail_id_data()
    #Grabs photos from website using text file.
    picture_jail_roster()
    #writes all the data from text file to excel.
    write_to_spreedsheet()

























