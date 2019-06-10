import speech_recognition as sr
import keyboard_listener as kl
import MySQLdb as mysql
import time

def stt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        #listen for 5 seconds and create the ambient noise energy level 
        r.adjust_for_ambient_noise(source, duration=1) 
        print("Say something!")
        audio=r.listen(source)

    # recognize speech using Google Speech Recognition 
    try:
        print("Google Speech Recognition thinks you said:")
        text = r.recognize_google(audio, language="zh-TW")
        print(text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return False
    except sr.RequestError as e:
        print("No response from Google Speech Recognition service: {0}".format(e))
        return False

def wait2speak():
    kl.Listener()

def sql(text):
    db = mysql.connect(
        host = "175.182.105.203",
        port = 5050,
        user = "titi",
        passwd = "titi861203",
        db = "mydb"
    )
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    cursor = db.cursor()
    sql = "INSERT INTO ros_user_talk (time, activity) VALUES ('"+localtime+"', '"+text+"')"
    try:
        cursor.execute(sql)
        db.commit()
        print("MySQL commit successful!")
    except:
        db.rollback()
    db.close()

def tranform2english(text):
    if text == "轉圈":
        print("turn around")
        return "turn around"
    elif text == "前進":
        print("go ahead")
        return "go ahead"
    elif text == "後退":
        print("go back")
        return "go back"
    elif text == "找人" or text == "過來" or text == "跟著我":
        print("find person")
        return "find person"
    else:
        print("%s is not the command" %text)
        return "False"

if __name__ == "__main__":
    while True:
        wait2speak()
        text = stt()
        if text:    
            eng = tranform2english(text)
            sql(eng)

