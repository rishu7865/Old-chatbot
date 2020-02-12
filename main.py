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
engine.setProperty('voice',voices[1].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()
#pyttsx3
bot1=ChatBot("My Bot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer=ListTrainer(bot1)

#rahul levels
trainer.train(['what is the proficiency level of rahul in business acumen?','2','what is the proficiency of rahul in business acumen?','2','proficiency of rahul in business acumen','2','what is the level of rahul in business acumen?','2','level of rahul in business acumen','2'])
trainer.train(['what is the proficiency level of rahul in data analysis?','2','what is the proficiency of rahul in data analysis?','2','proficiency of rahul in data analysis','2','what is the level of rahul in data analysis?','2','level of rahul in data analysis','2'])
trainer.train(['what is the proficiency level of rahul in advanced data analytics?','3','what is the proficiency of rahul in advanced data analytics?','3','proficiency of rahul in advanced data analytics','3','what is the level of rahul in advanced data analytics?','3','level of rahul in advanced data analytics','3'])
trainer.train(['what is the proficiency level of rahul in data visualization?','2','what is the proficiency of rahul in data visualization?','2','proficiency of rahul in data visualization','2','what is the level of rahul in data visualization?','2','level of rahul in data visualization','2'])
trainer.train(['what is the proficiency level of rahul in data warehousing?','1','what is the proficiency of rahul in data warehousing?','1','proficiency of rahul in data warehousing','1','what is the level of rahul in data warehousing?','1','level of rahul in data warehousing','1'])
trainer.train(['what is the proficiency level of rahul in substantive hr knowledge?','2','what is the proficiency of rahul in substantive hr knowledge?','2','proficiency of rahul in substantive hr knowledge','2','what is the level of rahul in substantive hr knowledge?','2','level of rahul in substantive hr knowledge','2'])


trainer=ChatterBotCorpusTrainer(bot1)
trainer.train("chatterbot.corpus.english")
#now training the bot with the help of trainer

#trainer.train(convo)
#answer=bot.get_response("hello")
#print(answer)
#print('Talk to bot')
'''while True:
    query=input()
    if query=='exit':
        break
    answer=bot.get_response(query)
    print("bot : ",answer)'''

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
        audio=sr.listen(m)
        query=sr.recognize_google(audio,language='eng-in')
        print(query)
        textF.delete(0,END)
        textF.insert(0,query)
        ask_from_bot()
def ask_from_bot():
    query=textF.get()
    answer_from_bot=bot1.get_response(query)
    msgs.insert(END,"you : "+query)
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
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
t=threading.Thread(target=takeQuery)
t.start()
main.mainloop()
#hello anurag whats up?
