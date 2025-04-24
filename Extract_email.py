# This code was run on Google Colab so make sure you run this in diffrent cell step by step

# STEP 1: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')


import imaplib,email
from email.header import decode_header
import json,re,os
from google.colab import drive

mail="Your email Id"
pas="your app password" # go to security, and find 2 step verfication, enable it, click on it and add app password, write your desire name "Mail" and file your password without space
# example it is like "uio uio uio uio" the you have to fill  "uiouiouiouio" 
im="imap.gmail.com"
loc="/content/drive/MyDrive/my_emails.json" # your desire path

def d(v):
 try:
  if isinstance(v,bytes):return v.decode()
  return v
 except: return "err"

def get():
 s=imaplib.IMAP4_SSL(im)
 s.login(mail,pas)
 s.select("inbox")
 a,b=s.search(None,"ALL")
 z=[]
 for i in b[0].split():
  _,c=s.fetch(i,"(RFC822)")
  for x in c:
   if isinstance(x,tuple):
    m=email.message_from_bytes(x[1])
    h,enc=decode_header(m["Subject"])[0]
    h=d(h)
    frm=m.get("From","???")
    bd=""
    if m.is_multipart():
     for p in m.walk():
      if p.get_content_type()=="text/plain":
       try:
        bd=p.get_payload(decode=True).decode()
        break
       except: pass
    else:
     try: bd=m.get_payload(decode=True).decode()
     except: pass
    z.append({"email":frm,"subject":h,"body":bd})
 s.logout()
 return z

drive.mount('/content/drive')

e=get()
with open(loc,"w",encoding="utf-8") as f:
 json.dump(e,f,indent=2)

print("saved at:",loc)
