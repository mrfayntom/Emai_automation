# here if you run the Extract email file then your file must saved but not in good condition here you have to run the code in seperate cells

# 1st cell
import json,re
from bs4 import BeautifulSoup

p='/content/drive/MyDrive/my_emails.json'

def cl(b):
 b=BeautifulSoup(b,"html.parser").get_text()
 b=re.sub(r'http\S+','',b)
 b=re.sub(r'\u2007|\u00a0',' ',b)
 b=re.sub(r'[^\x00-\x7F]+','',b)
 b=re.sub(r'\r\n|\n|\r',' ',b)
 b=re.sub(r'[^A-Za-z0-9\s]','',b)
 return b.lower().strip()

with open(p,'r',encoding='utf-8') as f:
 d=json.load(f)

for x in d:
 x['body']=cl(x['body'])

with open(p,'w',encoding='utf-8') as f:
 json.dump(d,f,indent=2)

print("done:",p)



# 2nd cell
import json,re
from bs4 import BeautifulSoup

p='/content/drive/MyDrive/my_emails.json'

def cl(b):
 b=BeautifulSoup(b,"html.parser").get_text()
 b=re.sub(r'http\S+','',b)
 b=re.sub(r'\u2007|\u00a0',' ',b)
 b=re.sub(r'[^\x00-\x7F]+','',b)
 b=re.sub(r'\s+',' ',b)
 b=re.sub(r'\s*\n\s*','\n',b)
 return b.strip()

with open(p,'r',encoding='utf-8') as f:
 d=json.load(f)

for i in d:
 i['body']=cl(i['body'])

with open(p,'w',encoding='utf-8') as f:
 json.dump(d,f,indent=2)

print("saved:",p)


