# skokie-mailer
send spoofed emails via sendgrid through discord bot

Windows

Temporarily set the environment variable(accessible only during the current cli session):

set SENDGRID_API_KEY=YOUR_API_KEY

Permanently set the environment variable(accessible in all subsequent cli sessions):

setx SENDGRID_API_KEY "YOUR_API_KEY"

Linux/Mac

echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
<br>
echo "sendgrid.env" >> .gitignore
<br>
source ./sendgrid.env

