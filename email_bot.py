import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('python.mailbot.S4@gmail.com', 'S4.python.mailbot.abx')
    email = EmailMessage()
    email['From'] = 'python.mailbot.S4@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'ankit': 'pal787871@gmail.com',
    'neeraj': 'nirajmohanrana@gmail.com',
    'yash': 'yashshukla233@gmail.com'
}

def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is subject of your email?')
    subject = get_info()
    talk('Tell me the contents of your mail')
    message = get_info()
    send_email(receiver, subject, message)

get_email_info()