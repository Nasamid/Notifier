from telnetlib import STATUS
import notifypy
import requests

response = requests.get("https://myflixer.to/home")
status = response.status_code

if status == 200:

    notification = notifypy.Notify()
    notification.title = "MyFlixer"
    notification.message = "A new HD movie is out"
    notification.icon = './myflixer_logo.ico'
    notification.application_name = "MyFlixer"
    notification.send()

