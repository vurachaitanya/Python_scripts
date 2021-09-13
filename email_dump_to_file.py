import win32com.client
from datetime import datetime
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)

def dumpMailsToFile(f):
  col_sep="~"
  for i in f.Items:
    if ( i.ReceivedTime.month == 2  ) :
      #sev = i.Subject[:1]
      global c
      filehandler.write(str(i.Subject)+col_sep+i.ReceivedTime.strftime("%d%m%Y")+col_sep+i.ReceivedTime.strftime("%H%M%S")+"\n")
      c+=1

startTime = datetime.now()
filename = "C:\\chaitanya\\"+"email_dump"+startTime.strftime("%d%m%Y")
index_dict={}
c=0
filehandler = open(filename,'w')
for i in inbox.Folders:
    #print(i)
    if str(i) == "personal":
        for j in i.Folders:
            if str(j) == "certifications":
                print(j)
                dumpMailsToFile(j)
filehandler.close()
print(datetime.now()-startTime,"sec",c)
