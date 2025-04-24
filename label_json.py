# here you have to add label in your email to train model which is important mail and which is not
# label = 0 means not important and label = 1 means important
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
 i['label']=0

with open(p,'w',encoding='utf-8') as f:
 json.dump(d,f,indent=2)

print("ok:",p)
