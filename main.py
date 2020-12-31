import datetime
from translate import Translator
import pyjokes

run = True
print(" what do you want to be called")
name_user = (input())


def greetMe():
  currentH = int(datetime.datetime.now().hour)
  if 0 <= currentH < 12:
    print('Good Morning! , sir')

  if 12 <= currentH < 18:
    print('Good Afternoon! , sir')

  if currentH >= 18 and currentH != 0:
    print('Good Evening! , sir')



def jeff():
  print(" ")
  print("hello "+ name_user + " what do you want to know today?")
  question = (input())

  if 'play' in question:
    print("playing song")
    song = question.replace('play', '')
    print (song)
  if 'who is' in question:
    person = question.replace('who the heck is', '')
    info = wikipedia.summary(person, 1)
    print(info)
  elif 'time' in question:
      times = datetime.datetime.now().strftime('%I:%M %p')
      print(times)
      print("take off one hour and change to the oppisote of am and pm")
  elif 'joke' in question:
      print(pyjokes.get_joke())
  elif 'translate' in question:
    translator= Translator(to_lang="zh")
    print("what do you want to translate")
    tran = (input())
    translation = translator.translate(tran)
    print(translation)
  elif 'open' in question:
    exec(open('open.py').read())


  else:
    print("ohhh i dont understand")


greetMe()
while True:
  jeff()
