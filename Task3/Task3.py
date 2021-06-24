import http.client
from tkinter import Tk,Button
import json
from tkinter import *
import sys
import os
Conm=[]



tor = Tk()
tor.title("Corona Virus")
connect = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "e36cf147d2msh773e180e52d7742p1f4ad1jsnd148121bd4cf",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }


connect.request("GET", "/api/npm-covid-data/asia", headers=headers)
rs = connect.getresponse()
data = rs.read()
corona = data.decode("utf-8")
json = json.loads(corona)
conZ = "Japan"
conT = "Turkey"
conTT = "Israel"
conF = "India"
conFF = "Bangladesh"
text = Text (width=700, height=700, fg='#f2f3f4', bg='#db7093', font=("PT Sans", 30, "italic"))
label = Label (font=("Times New Roman", 10, "italic"), fg='#f2f3f4', bg='#310062', text="Country please:")
entry = Entry()
label.pack()
entry.pack()
text.pack()

label = Label(font=("PT Sans", 17, "italic"), text="Country: \nJapan, Turkey, Israel, India, Bangladesh").place(x=1010, y=100)

def pos():
  Conm = entry.get()
  if Conm == conZ:
      for i in range(9,10):
          text.insert('1.0', list(json[i].items())[14])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[12])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[10])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[2])
          text.insert('1.0', '\n')
  elif Conm == conT:
      for i in range(1,2):
          text.insert('1.0', list(json[i].items())[14])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[12])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[10])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[2])
          text.insert('1.0', '\n')
  elif Conm == conTT:
      for i in range(8,9):
          text.insert('1.0', list(json[i].items())[14])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[12])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[10])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[2])
          text.insert('1.0', '\n')
  elif Conm == conF:
      for i in range(0,1):
          text.insert('1.0', list(json[i].items())[14])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[12])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[10])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[2])
          text.insert('1.0', '\n')
  elif Conm == conFF:
      for i in range(7,8):
          text.insert('1.0', list(json[i].items())[14])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[12])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[10])
          text.insert('1.0', '\n')
          text.insert('1.0', list(json[i].items())[2])
          text.insert('1.0', '\n')

Button(tor, text="Enter", font=("PT Sans", 20, "italic"), command=pos, fg='#ffffff', bg='#120a8f', width=14, height=1,).place(x = 1600, y = 60)

def rsp():
    python = sys.executable
    os.execl(python, python, * sys.argv)

Button(tor, text="Restart", font=("PT Sans", 20, "italic"), command=rsp, fg='#ffffff', bg='#CD5C5C',width=14, height=1,).place(x = 1600, y = 140)
tor.mainloop()
