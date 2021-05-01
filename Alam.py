import datetime
import winsound
import sys
from win32com.client import Dispatch
import time

hour = input("Enter hour : ")
min1 = input("Enter Minute : ")
sec = input("Enter sec : ")
shift = str(input("Enter AM/PM : "))
date_=0
flag = 0
        

want = input("Want to Set a Date (Y/N) :")
if want == "Y" or want == "y":
    day = input("Enter Day : ")
    month = input("Enter month : ")
    year = input("Enter year : ")
    year = str(int(year)+2000)
    if int(day)<10:
        day = "0"+day
    if int(month)<10:
        month = "0"+month
    date_ = f"{day}/{month}/{year}"

elif want == "N" or want == "n":
    date_=datetime.datetime.now().strftime("%d/%m/%Y")

else:
    print("wrong Input!")
    sys.exit()

if int(hour)>12:
    print("Error! Hour is 12 Format !")
    sys.exit()
if int(min1)>=60:
    if int(min1) == 60:
        min1 = "0"
    else:
        print("Error! Minute Wrong !")
        sys.exit()
if int(sec)>=60:
    if int(sec) == 60:
        sec = "0"
    else:
        print("Error! Second Wrong !")
        sys.exit()
if int(hour) <10:
    hour =  "0"+hour 
if int(min1) < 10:
    min1 =  "0"+min1 
if int(sec) <10:
    sec =  "0"+sec 
if shift == "am" or shift ==  "AM" :
    if int(hour) == 12:
        hour = "00"
# else:
elif shift == "pm" or shift == "PM":
    hour = str(int(hour) + 12)
else:
    print("Wrong Input")
    sys.exit()

data = f"{hour}:{min1}:{sec}"
remind = input("Want to Set Remainder (Y/N): ")
if remind == "Y" or remind == "y":
    input_remainder = input("Enter Reminder : ")
    with open("reminder.txt","w+") as f:
        f.write("Your Remainder is : '"+input_remainder +"'"+"\nand You set the Time : "+data + "\nand Date : "+date_)
        f.close()
        flag = 1
else:
    pass
voice = ""
sound=Dispatch("SAPI.Spvoice")
print(f"Alam Time is : {data}:{shift} \nDate is : {date_}")
if flag == 1:
    print("Remainder Set!!!")
    with open("reminder.txt","r") as f:
        voice = f.read()
        f.close()
        
else:
    print("Remainder Not Set!!!!")
music_dir = "snd\sound.wav"


while True:
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    date = current_time.strftime("%d/%m/%Y")

    if now == data and date == date_:
        print("Wake Up")
        winsound.PlaySound(music_dir, winsound.SND_ALIAS )
        time.sleep(10)
        winsound.PlaySound(None, winsound.SND_ASYNC)
        with open ("reminder.txt","r") as f:
            a = f.read()
            sound.Speak(voice)
            print("Sir I want To Remind You that : ",a)
        break



