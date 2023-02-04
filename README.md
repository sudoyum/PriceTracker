# PriceTracker
Grabs price of items from websites and sends them in an email to the user

## Fill In Email Parameters
```
email_params = {
    "recipient_email": 'XXXXXXXXXXXXX',
    "sender_email": "XXXXXXXXXXXXX",
    "password": "XXXXXXXXXXXXX"
}
```
* Note: using Outlook because Protonmail requires paid teir and gmail no longer supports "less secure apps" feature - https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp 

* get_price function will probably need modification depending on website


## Run on a schedule using Cron

```
# Open cron in edit mode
crontab -e


# Add a line with the following format
m h  dom mon dow   command

# For example, run at 6am every day:
0 6 * * * <path>/price_checker.py
```




