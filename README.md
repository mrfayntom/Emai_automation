# Email Automation Project Documentation

![Project Banner](https://i.pinimg.com/736x/b5/9c/f5/b59cf5fc60ba1cbc4008830fb309ef3e.jpg)

## Overview
This project automates email monitoring by integrating machine learning and Telegram bot functionality. It classifies incoming emails as **important** or **non-important**. 

- Important emails are forwarded immediately via Telegram.  
- Non-important ones are batched and their count is reported every hour.

### Project Workflow
Extract_email.py ➝ Clean_json.py ➝ label_json.py ➝ train.py ➝ deploy_bot.py


---

## 1. Email Extraction
**Script:** `Extract_email.py`

### Function
- Extracts emails from a mailbox.
- Converts them into a JSON format.
- Stores the file locally or in your drive.

### Output
- A raw JSON file containing email metadata and content.

### Notes
- Ensure correct login credentials for your email account are configured.
- This script should run in a secure environment to avoid data leakage.

---

## 2. JSON Cleaning and Structuring
**Script:** `Clean_json.py`

### Function
- Loads the raw email JSON.
- Cleans irrelevant fields.
- Structures emails into a format suitable for labeling and ML training.

---

## 3. Email Labeling
**Script:** `label_json.py`

### Function
- Auto-labels all emails as `0` (non-important).
- Allows manual labeling by editing selected emails to `1` (important).

### Instructions
1. Review the cleaned JSON.
2. Set `"label": 1` for important emails.
3. Save the updated file.

---

## 4. Model Training
**Script:** `train.py`

### Function
Trains a classification model to distinguish between important and non-important emails.

### Steps
- Reads labeled data.
- Vectorizes text (e.g., using **TF-IDF**).
- Splits dataset into train/test.
- Trains a suitable model 
- Saves the trained model to disk.

---

## 5. Bot Deployment
**Script:** `deploy_bot.py`

### Function
- Uses the trained model to classify incoming emails.
- Forwards important emails instantly via Telegram.
- Sends count of non-important emails every 1 hour.

### Configuration Required
- `bot_token` – Telegram bot token.
- `chat_id` – Your Telegram chat ID.
- `email`, `password` – Email credentials (ideally app-specific password).

### Behavior
- Fetch emails periodically.
- Apply ML model to classify.
- Push alerts to Telegram based on label.

---

## Showcase

### Screenshot 1
![Showcase 1](https://i.ibb.co/8LjvQ6NJ/Untitled-design-1.png)

### Screenshot 2
![Showcase 2](https://i.ibb.co/WvVpKQR7/Untitled-design.png)

---

> 📝 **Notice:**  
> I need to change my Windows version so I have to take backup and handle the installation. Since I don't have unlimited internet or storage devices, I won’t be uploading anything for a week.  
>  
> Yup, I know no one is reading this right now… maybe in the future — who knows?
