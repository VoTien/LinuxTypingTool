from Tkinter import *
import ttk

import os


#--Main Windows
window = Tk()
window.title("LAZYNESS...")
window.geometry("200x300")

testButton =Label(window,text="")
testButton.grid(column=0, row=5)

#--Functions
def start_operation():
  if box.get() == 'DA':
    textstart ='service dadaemon start'
  if box.get() == 'DC':
    textstart ='service dcmd start'
  testButton.config(text=textstart)
  r = Tk()
  r.withdraw()
  r.clipboard_clear()
  r.clipboard_append(textstart)
  r.update()
  r.destroy()
def stop_operation():
  if box.get() == 'DA':
    textstart ='service dadaemon stop'
  if box.get() == 'DC':
    textstart ='service dcmd stop'
  testButton.config(text=textstart)
def status_operation():
  if box.get() == 'DA':
    textstart ='service dadaemon status'
  if box.get() == 'DC':
    textstart ='service dcmd status'
  testButton.config(text=textstart)

#--Labels
title = Label(window,text="Please select type of Machine")
title.grid(column=0,row=0)

#Combobox
value = StringVar()
box = ttk.Combobox(window, textvariable=value, state='readonly')
box['values'] = ('DA','DC')
box.current(0)
box.grid(column=0, row=1)

#--Buttons
buttonStart = Button(text="Start",command=start_operation)
buttonStart.grid(column=0,row=2)
buttonStatus = Button(text="Status",command=status_operation)
buttonStatus.grid(column=0,row=3)
buttonStop = Button(text="Stop",command=stop_operation)
buttonStop.grid(column=0,row=4)

window.mainloop()