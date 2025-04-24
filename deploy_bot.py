import imaplib
import email
import joblib
import time
import requests

BOT_TOKEN = 'insert token'
CHAT_ID = 'before token your chat id will be mentioned'

# example token is : 1234567890:asdfghjklqwertyuiop, so the chat id is 1234567890

classifier = joblib.load('/content/drive/MyDrive/email_classifier.pkl')
vectorizer = joblib.load('/content/drive/MyDrive/email_vectorizer.pkl')

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

def check_emails():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login('gmail', 'pass key without space') #you can use same when you were extracting the email in 1st code
    mail.select("inbox")
    _, messages = mail.search(None, "UNSEEN")
    return mail, messages[0].split()

def process_emails(unimportant_count):
    mail, mail_ids = check_emails()
    for mail_id in mail_ids:
        _, data = mail.fetch(mail_id, "(RFC822)")
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = msg.get("subject", "")
                sender = msg.get("from", "")
                body = ""

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode(errors="ignore")
                            break
                else:
                    body = msg.get_payload(decode=True).decode(errors="ignore")

                text = f"{subject} {body}"
                vectorized = vectorizer.transform([text])
                result = classifier.predict(vectorized)

                if result[0] == 1:
                    send_telegram_message(f"* Important Email*\n*From:* {sender}\n*Subject:* {subject}\n*Body:* {body}")
                else:
                    unimportant_count += 1

    return unimportant_count

def periodic_monitor():
    send_telegram_message("Mr. Phantom reporting")
    unimportant_count = 0

    while True:
        unimportant_count = process_emails(unimportant_count)

        if unimportant_count > 0:
            send_telegram_message(f"{unimportant_count} unimportant emails received in the past hour.")
            unimportant_count = 0

        time.sleep(1)

periodic_monitor()
