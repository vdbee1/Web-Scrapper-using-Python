from bs4 import BeautifulSoup
from urllib.request import urlopen
import sqlite3
import xlsxwriter

#Creating a sqlite table in the given database
com=sqlite3.connect('mydb1.db')
#com.execute("CREATE TABLE wordcount(URL TEXT NOT NULL,Words TEXT NOT NULL, Count INT NOT NULL)")


#Reading the contents of url1.txt which contains the given URL's    
f=open("url1.txt","r")
c=f.read()
url=c.split(",")
#print(url)
f.close()



#Reading the contents of ignore.txt which contains the words that one should ignore (and,I,you,me etc)
f1=open("ignore.txt","r")
a=f1.read()
f1.close()


#Using bs4 to parse through the URL's and extract the text content from them
for i in range(0,len(url)):
    page=urlopen(url[i])
    soup=BeautifulSoup(page,"html.parser")
    for script in soup(["script","style"]):
        script.extract()
    text=soup.get_text()
    T=text.lower()
    #lines=[line.strip() for line in text.splitlines()]
    s=T.split()


    ignore=a.split(" ")
    #print(s)
    result=[]


#Applyinng the ignore.txt to the keywords that are extracted from the URL's
    for keyword in s:
        if keyword in ignore:
            continue
        elif keyword=='':
            continue
        else:
            result.append(keyword)
            b=dict()

#Making a frequency count of the words in the file            
    for co in result:
        
        if co in b:
            b[co]+=1
        else:
            b[co]=1
            b[co]=co.count(co)


            con=dict()
            con=dict((key,value) for (key,value) in b.items())
    #print(con)



#Assigning the keys and values of the dictionary into variables and inserting the variables into the sqlite table
    k=con.keys()
    v=con.values()
#    for key,values in con.items():
#        com.execute("INSERT INTO wordcount(URL,Words,Count) VALUES(?,?,?)",(url[i],key,values))
#    com.commit()





#    workbook = xlsxwriter.Workbook('info.xlsx')
#    worksheet = workbook.add_worksheet()
#    row = 0
#    col = 0
#    order=sorted(con.keys())
#    for key in order:
#        row += 1
#        worksheet.write(row,col,key)
#        for item in con[key]:
#            worksheet.write(row, col + 1, item)
#            row += 1
#     workbook.close()





#Printing the Words with their frequencies
print("Possible Keywords when searching Python Related Content:")

cursor=com.execute('SELECT URL,Words,Count FROM wordcount WHERE Count>=3 ORDER BY Count DESC ')
for row in cursor:
    print("URL:",row[0])
    print("Words:",row[1])
    print("Count:",row[2])






