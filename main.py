from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from tkinter import *
import speech_recognition as s
import threading
import pyttsx3 as pp

engine=pp.init()
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()
#pyttsx3
bot1=ChatBot("My Bot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer=ListTrainer(bot1)


'''Proficiency level
  --------------------------------------------------------------------------------------------------
   0 = No Capability
  --------------------------------------------------------------------------------------------------
   1 = Basic Level
  -------------------------------------------------------------------------------------------------- 
   2 = Intermediate level
  -------------------------------------------------------------------------------------------------- 
   3 = Advanced Level
  --------------------------------------------------------------------------------------------------'''

#rahul levels
trainer.train(['what is the proficiency level of rahul in business acumen?','2','what is the proficiency of rahul in business acumen?','2','proficiency of rahul in business acumen','2','what is the level of rahul in business acumen?','2','level of rahul in business acumen','2'])
trainer.train(['what is the proficiency level of rahul in data analysis?','2','what is the proficiency of rahul in data analysis?','2','proficiency of rahul in data analysis','2','what is the level of rahul in data analysis?','2','level of rahul in data analysis','2'])
trainer.train(['what is the proficiency level of rahul in advanced data analytics?','3','what is the proficiency of rahul in advanced data analytics?','3','proficiency of rahul in advanced data analytics','3','what is the level of rahul in advanced data analytics?','3','level of rahul in advanced data analytics','3'])
trainer.train(['what is the proficiency level of rahul in data visualization?','2','what is the proficiency of rahul in data visualization?','2','proficiency of rahul in data visualization','2','what is the level of rahul in data visualization?','2','level of rahul in data visualization','2'])
trainer.train(['what is the proficiency level of rahul in data warehousing?','1','what is the proficiency of rahul in data warehousing?','1','proficiency of rahul in data warehousing','1','what is the level of rahul in data warehousing?','1','level of rahul in data warehousing','1'])
trainer.train(['what is the proficiency level of rahul in substantive hr knowledge?','2','what is the proficiency of rahul in substantive hr knowledge?','2','proficiency of rahul in substantive hr knowledge','2','what is the level of rahul in substantive hr knowledge?','2','level of rahul in substantive hr knowledge','2'])

#kanjam levels
trainer.train(['what is the proficiency level of kanjam in business acumen?','1','what is the proficiency of kanjam in business acumen?','1','proficiency of kanjam in business acumen','1','what is the level of kanjam in business acumen?','1','level of kanjam in business acumen','1'])
trainer.train(['what is the proficiency level of kanjam in data analysis?','2','what is the proficiency of kanjam in data analysis?','2','proficiency of kanjam in data analysis','2','what is the level of kanjam in data analysis?','2','level of kanjam in data analysis','2'])
trainer.train(['what is the proficiency level of kanjam in advanced data analytics?','2','what is the proficiency of kanjam in advanced data analytics?','2','proficiency of kanjam in advanced data analytics','2','what is the level of kanjam in advanced data analytics?','2','level of kanjam in advanced data analytics','2'])
trainer.train(['what is the proficiency level of kanjam in data visualization?','0','what is the proficiency of kanjam in data visualization?','0','proficiency of kanjam in data visualization','0','what is the level of kanjam in data visualization?','0','level of kanjam in data visualization','0'])
trainer.train(['what is the proficiency level of kanjam in data warehousing?','3','what is the proficiency of kanjam in data warehousing?','3','proficiency of kanjam in data warehousing','3','what is the level of kanjam in data warehousing?','3','level of kanjam in data warehousing','3'])
trainer.train(['what is the proficiency level of kanjam in substantive hr knowledge?','3','what is the proficiency of kanjam in substantive hr knowledge?','3','proficiency of kanjam in substantive hr knowledge','3','what is the level of kanjam in substantive hr knowledge?','3','level of kanjam in substantive hr knowledge','3'])

#rachit levels
trainer.train(['what is the proficiency level of rachit in business acumen?','2','what is the proficiency of rachit in business acumen?','2','proficiency of rachit in business acumen','2','what is the level of rachit in business acumen?','2','level of rachit in business acumen','2'])
trainer.train(['what is the proficiency level of rachit in data analysis?','1','what is the proficiency of rachit in data analysis?','1','proficiency of rachit in data analysis','1','what is the level of rachit in data analysis?','1','level of rachit in data analysis','1'])
trainer.train(['what is the proficiency level of rachit in advanced data analytics?','3','what is the proficiency of rachit in advanced data analytics?','3','proficiency of rachit in advanced data analytics','3','what is the level of rachit in advanced data analytics?','3','level of rachit in advanced data analytics','3'])
trainer.train(['what is the proficiency level of rachit in data visualization?','3','what is the proficiency of rachit in data visualization?','3','proficiency of rachit in data visualization','3','what is the level of rachit in data visualization?','3','level of rachit in data visualization','3'])
trainer.train(['what is the proficiency level of rachit in data warehousing?','2','what is the proficiency of rachit in data warehousing?','2','proficiency of rachit in data warehousing','2','what is the level of rachit in data warehousing?','2','level of rachit in data warehousing','2'])
trainer.train(['what is the proficiency level of rachit in substantive hr knowledge?','2','what is the proficiency of rachit in substantive hr knowledge?','2','proficiency of rachit in substantive hr knowledge','2','what is the level of rachit in substantive hr knowledge?','2','level of rachit in substantive hr knowledge','2'])

#pratik levels
trainer.train(['what is the proficiency level of pratik in business acumen?','2','what is the proficiency of pratik in business acumen?','2','proficiency of pratik in business acumen','2','what is the level of pratik in business acumen?','2','level of pratik in business acumen','2'])
trainer.train(['what is the proficiency level of pratik in data analysis?','3','what is the proficiency of pratik in data analysis?','3','proficiency of pratik in data analysis','3','what is the level of pratik in data analysis?','3','level of pratik in data analysis','3'])
trainer.train(['what is the proficiency level of pratik in advanced data analytics?','2','what is the proficiency of pratik in advanced data analytics?','2','proficiency of pratik in advanced data analytics','2','what is the level of pratik in advanced data analytics?','2','level of pratik in advanced data analytics','2'])
trainer.train(['what is the proficiency level of pratik in data visualization?','2','what is the proficiency of pratik in data visualization?','2','proficiency of pratik in data visualization','2','what is the level of pratik in data visualization?','2','level of pratik in data visualization','2'])
trainer.train(['what is the proficiency level of pratik in data warehousing?','3','what is the proficiency of pratik in data warehousing?','3','proficiency of pratik in data warehousing','3','what is the level of pratik in data warehousing?','3','level of pratik in data warehousing','3'])
trainer.train(['what is the proficiency level of pratik in substantive hr knowledge?','2','what is the proficiency of pratik in substantive hr knowledge?','2','proficiency of pratik in substantive hr knowledge','2','what is the level of pratik in substantive hr knowledge?','2','level of pratik in substantive hr knowledge','2'])

#pranjul skills
trainer.train(['what is the proficiency level of pranjul in business acumen?','3','what is the proficiency of pranjul in business acumen?','3','proficiency of pranjul in business acumen','3','what is the level of pranjul in business acumen?','3','level of pranjul in business acumen','3'])
trainer.train(['what is the proficiency level of pranjul in data analysis?','2','what is the proficiency of pranjul in data analysis?','2','proficiency of pranjul in data analysis','2','what is the level of pranjul in data analysis?','2','level of pranjul in data analysis','2'])
trainer.train(['what is the proficiency level of pranjul in advanced data analytics?','0','what is the proficiency of pranjul in advanced data analytics?','0','proficiency of pranjul in advanced data analytics','0','what is the level of pranjul in advanced data analytics?','0','level of pranjul in advanced data analytics','0'])
trainer.train(['what is the proficiency level of pranjul in data visualization?','2','what is the proficiency of pranjul in data visualization?','2','proficiency of pranjul in data visualization','2','what is the level of pranjul in data visualization?','2','level of pranjul in data visualization','2'])
trainer.train(['what is the proficiency level of pranjul in data warehousing?','2','what is the proficiency of pranjul in data warehousing?','2','proficiency of pranjul in data warehousing','2','what is the level of pranjul in data warehousing?','2','level of pranjul in data warehousing','2'])
trainer.train(['what is the proficiency level of pranjul in substantive hr knowledge?','1','what is the proficiency of pranjul in substantive hr knowledge?','1','proficiency of pranjul in substantive hr knowledge','1','what is the level of pranjul in substantive hr knowledge?','1','level of pranjul in substantive hr knowledge','1'])

#rishabh level
trainer.train(['Level of rishabh in business acumen','2','What is the proficiency level of rishabh in business acumen','2','what is the level of rishabh in business acumen','2','What is the proficiency of rishabh in business acumen','2','proficiency of rishabh in business aaumen','2'])
trainer.train(['Level of rishabh in data analysis','3','What is the proficiency level of rishabh in data analysis','3','what is the level of rishabh in data analysis','3','What is the proficiency of rishabh in data analysis','3','proficiency of rishabh in data analysis','3'])
trainer.train(['Level of rishabh in adavanced data analysis','2','What is the proficiency level of rishabh in adavanced data analysis','2','what is the level of rishabh in adavanced data analysis','2','What is the proficiency of rishabh in advanced data analysis','2','proficiency of rishabh in advanced data analysis','2'])
trainer.train(['Level of rishabh in data visualization','2','What is the proficiency level of rishabh in data visualization','2','what is the level of rishabh in data visualization','2','What is the proficiency of rishabh in data visualization','2','proficiency of rishabh in data visualization','2'])
trainer.train(['Level of rishabh in data and warehousing','2','What is the proficiency level of rishabh in data and warehousing','2','what is the level of rishabh in data and warehousing','2','What is the proficiency of rishabh in data and warehousing','2','proficiency of rishabh in data and warehousing','2'])
trainer.train(['Level of rishabh in substantive hr knowledge','1','What is the proficiency level of rishabh in substantive hr knowledge','1','what is the level of rishabh in substantive hr knowledge','1','What is the proficiency of rishabh in substantive hr knowledge','1','proficiency of rishabh in substantive hr knowledge','1'])

#anurag level
trainer.train(['Level of anurag in business acumen','2','What is the proficiency level of anurag in business acumen','2','what is the level of anurag in business acumen','2','What is the proficiency of anurag in business acumen','2','proficiency of anurag in business acumen','2'])
trainer.train(['Level of anurag in data analysis','1','What is the proficiency level of anurag in data analysis','1','what is the level of anurag in data analysis','1','What is the proficiency of anurag in data analysis','1','proficiency of anurag in data analysis','1'])
trainer.train(['Level of anurag in adavanced data analysis','3','What is the proficiency level of anurag in adavanced data analysis','3','what is the level of anurag in adavanced data analysis','3','What is the proficiency of anurag in advanced data analysis','3','proficiency of anurag in advanced data analysis','3'])
trainer.train(['Level of anurag in data visualization','3','What is the proficiency level of anurag in data visualization','3','what is the level of anurag in data visualization','3','What is the proficiency of anurag in data visualization','3','proficiency of anurag in data visualization','3'])
trainer.train(['Level of anurag in data and warehousing','2','What is the proficiency level of anurag in data and warehousing','2','what is the level of anurag in data and warehousing','2','What is the proficiency of anurag in data and warehousing','2','proficiency of anurag in data and warehousing','2'])
trainer.train(['Level of anurag in substantive hr knowledge','2','What is the proficiency level of anurag in substantive hr knowledge','2','what is the level of anurag in substantive hr knowledge','2','What is the proficiency of anurag in substantive hr knowledge','2','proficiency of anurag in substantive hr knowledge','2'])

#shubham level
trainer.train(['Level of shubham in business acumen','3','What is the proficiency level of shubham in business acumen','3','what is the level of shubham in business acumen','3','What is the proficiency of shubham in business acumen','3','proficiency of shubham in business acumen','3'])
trainer.train(['Level of shubham in data analysis','0','What is the proficiency level of shubham in data analysis','0','what is the level of shubham in data analysis','0','What is the proficiency of shubham in data analysis','0','proficiency of shubham in data analysis','0'])
trainer.train(['Level of shubham in adavanced data analysis','2','What is the proficiency level of shubham in adavanced data analysis','2','what is the level of shubham in adavanced data analysis','2','What is the proficiency of shubham in advanced data analysis','2','proficiency of shubham in advanced data analysis','2'])
trainer.train(['Level of shubham in data visualization','1','What is the proficiency level of shubham in data visualization','1','what is the level of shubham in data visualization','1','What is the proficiency of shubham in data visualization','1','proficiency of shubham in data visualization','1'])
trainer.train(['Level of shubham in data and warehousing','2','What is the proficiency level of shubham in data and warehousing','2','what is the level of shubham in data and warehousing','2','What is the proficiency of shubham in data and warehousing','2','proficiency of shubham in data and warehousing','2'])
trainer.train(['Level of shubham in substantive hr knowledge','2','What is the proficiency level of shubham in substantive hr knowledge','2','what is the level of shubham in substantive hr knowledge','2','What is the proficiency of shubham in substantive hr knowledge','2','proficiency of shubham in substantive hr knowledge','2'])

#abhishek level
trainer.train(['Level of abhishek in business acumen','1','What is the proficiency level of abhishek in business acumen','1','what is the level of abhishek in business acumen','1','What is the proficiency of abhishek in business acumen','1','proficiency of abhishek in business acumen','1'])
trainer.train(['Level of abhishek in data analysis','2','What is the proficiency level of abhishek in data analysis','2','what is the level of abhishek in data analysis','2','What is the proficiency of abhishek in data analysis','2','proficiency of abhishek in data analysis','2'])
trainer.train(['Level of abhishek in adavanced data analysis','3','What is the proficiency level of abhishek in adavanced data analysis','3','what is the level of abhishek in adavanced data analysis','3','What is the proficiency of abhishek in advanced data analysis','3','proficiency of abhishek in advanced data analysis','3'])
trainer.train(['Level of abhishek in data visualization','2','What is the proficiency level of abhishek in data visualization','2','what is the level of abhishek in data visualization','2','What is the proficiency of abhishek in data visualization','2','proficiency of abhishek in data visualization','2'])
trainer.train(['Level of abhishek in data and warehousing','3','What is the proficiency level of abhishek in data and warehousing','3','what is the level of abhishek in data and warehousing','3','What is the proficiency of abhishek in data and warehousing','3','proficiency of abhishek in data and warehousing','3'])
trainer.train(['Level of abhishek in substantive hr knowledge','2','What is the proficiency level of abhishek in substantive hr knowledge','2','what is the level of abhishek in substantive hr knowledge','2','What is the proficiency of abhishek in substantive hr knowledge','2','proficiency of abhishek in substantive hr knowledge','2'])

#kaustubh level
trainer.train(['Level of kaustubh in business acumen','2','What is the proficiency level of kaustubh in business acumen','2','what is the level of kaustubh in business acumen','2','What is the proficiency of kaustubh in business acumen','2','proficiency of kaustubh in business acumen','2'])
trainer.train(['Level of kaustubh in data analysis','3','What is the proficiency level of kaustubh in data analysis','3','what is the level of kaustubh in data analysis','3','What is the proficiency of kaustubh in data analysis','3','proficiency of kaustubh in data analysis','3'])
trainer.train(['Level of kaustubh in adavanced data analysis','2','What is the proficiency level of kaustubh in adavanced data analysis','2','what is the level of kaustubh in adavanced data analysis','2','What is the proficiency of kaustubh in advanced data analysis','2','proficiency of kaustubh in advanced data analysis','2'])
trainer.train(['Level of kaustubh in data visualization','3','What is the proficiency level of kaustubh in data visualization','3','what is the level of kaustubh in data visualization','3','What is the proficiency of kaustubh in data visualization','3','proficiency of kaustubh in data visualization','3'])
trainer.train(['Level of kaustubh in data and warehousing','1','What is the proficiency level of kaustubh in data and warehousing','1','what is the level of kaustubh in data and warehousing','1','What is the proficiency of kaustubh in data and warehousing','1','proficiency of kaustubh in data and warehousing','1'])
trainer.train(['Level of kaustubh in substantive hr knowledge','3','What is the proficiency level of kaustubh in substantive hr knowledge','3','what is the level of kaustubh in substantive hr knowledge','3','What is the proficiency of kaustubh in substantive hr knowledge','3','proficiency of kaustubh in substantive hr knowledge','3'])

#most proficiency
trainer.train(['who is most proficient in business acumen','shubham and pranjul','most proficient in business acumen','shubham and pranjul'])
trainer.train(['who is most proficient in data analysis','rishabh kaustubh and pratik','most proficient in data analysis','rishabh kaustubh and pratik'])
trainer.train(['who is most proficient in advanced data analysis','anurag abhishek and rachit','most proficient in advanced data analysis','anurag abhishek and rachit'])
trainer.train(['who is most proficient in data visualization','anurag kaustubh and pratik','most proficient in data visualization','anurag kaustubh and pratik'])
trainer.train(['who is most proficient in data and warehousing','abhishek pratik and kanjam','most proficient in data and warehousing','abhishek pratik and kanjam'])
trainer.train(['who is most proficient in substantive hr knowledge','kaustubh and kanjam','most proficient in substantive hr knowledge','kaustubh and kanjam'])

trainer=ChatterBotCorpusTrainer(bot1)
trainer.train("chatterbot.corpus.english")
#now training the bot with the help of trainer

main=Tk()
main.geometry("500x650")
main.title("My Chat bot")
img=PhotoImage(file="bot13.png")
photoL=Label(main,image=img)
photoL.pack(pady=5)

#take query: it takes audio as input from user and convert it to string

def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")
        
def ask_from_bot():
    query=textF.get()
    answer_from_bot=bot1.get_response(query)
    msgs.insert(END,"you : "+query)
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    answer_from_bot1=str(answer_from_bot)
    if(answer_from_bot1=='0'):
        msgs.insert(END,"bot : " +"Employee has no capability in this field")
        speak("Employee has no capability in this field")
    elif(answer_from_bot1=='1'):
        msgs.insert(END,"bot : " +"Employee has basic level in this field")
        speak("Employee has basic level in this field")
    elif(answer_from_bot1=='2'):
        msgs.insert(END,"bot : "+"Employee has intermediate level in this field")
        speak("Employee has intermediate level in this field")
    elif(answer_from_bot1=='3'):
        msgs.insert(END,"bot : "+"Employee has advanced level in this field")
        speak("Employee has advanced level in this field")
    textF.delete(0,END)
    msgs.yview(END)

frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
#creating text field
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask from bot",font=("Verdana",20),command=ask_from_bot)
btn.pack()

#creating a function
def enter_function(event):
    btn.invoke()

#going to bind main window with enter key...
main.bind('<Return>',enter_function)

def repeatL():
    while True:
        takeQuery()
        
t=threading.Thread(target=repeatL)
t.start()
main.mainloop()
