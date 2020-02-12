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
'''trainer.train(['What are the skills of rishabh?', 'rishabh skill set are Communication,Analytical and problem-solving skills,Flexibility and adaptability'])
trainer.train(['What are the skills of anurag?', 'anurag skills are Programming languages,Common operating systems,Software proficiency,Technical writing,Project management,Data analysis' ])
trainer.train(['What are technical skills?','A technical skill is the ability to carry out a task associated with technical roles such as IT, engineering, mechanics, science or finance'])
trainer.train(['What are programming skills of abhishek?','C#, SQL, Java, C++, HTML, JavaScript, XML, C, Perl'])
trainer.train(['What are programming skills of pranjul?','Python, PHP, Objective-C, AJAX, ASP.NET'])
trainer.train(['What is the job level of rishabh','he is a senior executive.he works in an executive management'])
trainer.train(['What is the job level of anurag','he is a executive.he works in an executive management'])
trainer.train(['What is the job level of pranjul','he is a senior director.he works in a middle management'])
trainer.train(['What is the job level of abhishek','he is a director.he works in a middle management'])
trainer.train(['What is the job level of rachit','he is a senior manager.he works in a managers and advisors section'])
trainer.train(['What is the job level of sreshta','she is a manager.she works in a managers and advisors section'])'''


'''convo={
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by team Wired ',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in bangalore',
    'In which language you talk ?',
    'I mostly talk in english'
}'''

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
