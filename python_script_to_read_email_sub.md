## Python Script to extract subject line from outlook and read aloud the content 

```
##### READ THE FILE which MAILS DUMP has created

import win32com.client
from datetime import datetime

import PyPDF2
import pyttsx3
from PyPDF2 import PdfFileReader
import time

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)

def dumpMailsToFile(f):
  col_sep="~"
  for i in f.Items:
    if ( i.ReceivedTime.month == 1  ) :
      #sev = i.Subject[:1]
      global c
      filehandler.write(str(i.Subject)+col_sep+i.ReceivedTime.strftime("%d%m%Y")+col_sep+i.ReceivedTime.strftime("%H%M%S")+"\n")
      c+=1

startTime = datetime.now()
filename = "C:\\Users\\vchaita3\\Chaitanya\\"+"email_dump"+startTime.strftime("%d%m%Y")
index_dict={}
c=0
filehandler = open(filename,'w')
for i in inbox.Folders:
    #print(i)
    if str(i) == "Inbox_archive":
        for j in i.Folders:
            #print(j)
            if str(j) == "Personal":
                #print(j)
                dumpMailsToFile(j)
                
                
                
filehandler.close()
fileread = open(filename,'r')
#text = (fileread.read())
for x in fileread:
    y = x.split("~",x.index("~"))
    z = y[0]
    print(z)
    time.sleep(1)
    
    speak = pyttsx3.init()
    speak.say(z)
    speak.runAndWait()
    

#### Text to speach/voice
#speak = pyttsx3.init()
#speak.say(text)
#speak.runAndWait()


print(datetime.now()-startTime,"sec",c)
```
