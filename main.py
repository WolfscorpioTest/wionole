import requests
import smtplib, ssl
import urllib.request
import json
import re
import time

port = 465  # For SSL
#thisdict = {"loud": 40}
smtp_server = "smtp.gmail.com"
sender_email = "alexshen1109@gmail.com"  # Enter your address
receiver_email = "alexshen1109@gmail.com"  # Enter receiver address
password = "ueqx lcmt mzxg hxby"
message = """Subject: just checking in

  hi"""


def postled(num):
  address = 'https://cn.wio.seeed.io/v1/node/GroveLEDBarUART0/bits/' + str(
      num) + '?access_token=aadeca5188bd15c202e08fe57e72c23e'
  y = requests.post(address)
  return y


def get_sensor_data(url):
  with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())
    return data


def threshold(loud):
  if loud > 20:
    message = """\
    Subject: Turn it down

    It is too loud"""
    sendemail(message)
    return message
  else:
    message = """Subject: just checking in

    hi"""
    return message


def sendemail(message):
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


def flow():
  test = 0

  loud = get_sensor_data(
      'https://cn.wio.seeed.io/v1/node/GroveLoudnessA0/loudness?access_token=aadeca5188bd15c202e08fe57e72c23e'
  )
  level = loud["loudness"]

  threshold(level)
  postled(level)


def main():
  test = 0
  while (test < 5):
    flow()
    test = test + 1


if __name__ == "__main__":
  main()
