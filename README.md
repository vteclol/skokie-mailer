# Skokie-Mailer
Send spoofed e-mails via SendGrid through Discord bot

# Installation / Tested on Ubuntu 18.04

Download provided files above
<br>
<br>
Installation Commands:
<br>
<br>
**YOU MIGHT HAVE PYTHON3 INSTALLED BY DEFAULT SAME WITH PIP IF NOT YOU WILL NEED TO INSTALL IT VIA THESE COMMANDS!**
<br>
<br>
```sudo apt install python3.8```
<br>
```sudo apt install python3-pip```
<br>
<br>
Getting Ready:
<br>
<br>
```pip3 install -r requirements.txt```
<br>
```python3 main.py```
<br>
<br>
I recommend running it behind screen or something so you can close your SSH Client and have it running in the background.


# Windows

Temporarily set the environment variable(accessible only during the current cli session):

```set SENDGRID_API_KEY=YOUR_API_KEY```

Permanently set the environment variable(accessible in all subsequent cli sessions):

```setx SENDGRID_API_KEY "YOUR_API_KEY"```

# Linux/Mac

```echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env```
<br>
```echo "sendgrid.env" >> .gitignore```
<br>
```source ./sendgrid.env```

