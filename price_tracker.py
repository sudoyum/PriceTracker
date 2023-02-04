#!/usr/bin/env python3

import requests
import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from bs4 import BeautifulSoup


potential_purchases = {
    "Men's Carolina Hurricanes Sebastian Aho adidas Red Reverse Retro 2.0 Authentic Player Jersey" : "https://shop.nhl.com/carolina-hurricanes/mens-carolina-hurricanes-sebastian-aho-adidas-red-reverse-retro-20-authentic-player-jersey/t-47717300+p-82954282107+z-7-1838027983?_ref=p-DLP:m-GRID:i-r9c0:po-27",
}


email_params = {
    "port": 587,
    "smtp_server": 'smtp-mail.outlook.com',
    "recipient_email": 'XXXXXXXXXXXXX',
    "sender_email": "XXXXXXXXXXXXX",
    "password": "XXXXXXXXXXXXX"
}


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


def send_email(subject, body, recipient):
    msg = MIMEMultipart()
    msg['From'] = email_params["sender_email"]
    msg['To'] = recipient

    msg['Subject'] = subject
    body = MIMEText(body)
    msg.attach(body)

    context = ssl.create_default_context()
    with smtplib.SMTP(email_params["smtp_server"], email_params["port"]) as server:
        server.starttls(context=context)
        server.login(email_params["sender_email"], email_params["password"])
        server.sendmail(email_params["sender_email"], recipient, msg.as_string())


def get_response(url):
    response = requests.get(url.strip(), headers=headers)
    return response.content


def get_price(url):

    page_content = get_response(url)

    soup = BeautifulSoup(page_content, 'html.parser')
    all_prices = soup.find_all(class_='sr-only')
    return all_prices[0].get_text().strip()


def main():
    for name, url in potential_purchases.items():
        subject = name
        body = get_price(url)
        send_email(subject, body, email_params["recipient_email"])

if __name__ == "__main__":
    main()
