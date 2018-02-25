from Tkinter import *
import ttk
import os
import pyautogui

#--Main Windows
window = Tk()
window.title("LAZYNESS...")
window.geometry("200x300")
#Create Tkinter clipboard
r = Tk()
r.withdraw()
r.clipboard_clear()
#TESTGLOBAL
testButton =Label(window,text="")
testButton.grid(column=0, row=5)

#--Functions
def start_operation():
  if box.get() == 'DA':
    txtstart ='service dadaemon start'
    cmp_clipboard(txtstart)
    move_mouse()
  if box.get() == 'DC':
    txtstart ='service dcmd start'
    cmp_clipboard(txtstart)
    move_mouse()
  testButton.config(text=txtstart)
def stop_operation():
  if box.get() == 'DA':
    txtstop ='service dadaemon stop'
    cmp_clipboard(txtstop)
    move_mouse()
  if box.get() == 'DC':
    txtstop ='service dcmd stop'
    cmp_clipboard(txtstop)
    move_mouse()
  testButton.config(text=txtstop)
def status_operation():
  if box.get() == 'DA':
    txtstatus ='service dadaemon status'
    cmp_clipboard(txtstatus)
    move_mouse()
  if box.get() == 'DC':
    txtstatus ='service dcmd status'
    cmp_clipboard(txtstatus)
    move_mouse()
  if box.get() == 'Vertica':
    txtstatus = 'admintools -t db_status -s UP'
    move_mouse()
  testButton.config(text=txtstatus)
def cmp_clipboard(txt):
  r.withdraw()
  r.clipboard_clear()
  r.clipboard_append(txt)
  r.update()
  r.destroy()
def move_mouse():
  pyautogui.moveTo(1000, 500)
  pyautogui.rightClick()
  pyautogui.press('enter')

#--Labels
title = Label(window,text="Please select type of Machine")
title.grid(column=0,row=0)

#Combobox
value = StringVar()
box = ttk.Combobox(window, textvariable=value, state='readonly')
box['values'] = ('DC','DA','Vertica')
box.current(0)
box.grid(column=0, row=1)
testButton.config(text=box.get())

#--Buttons
buttonStart = Button(text="Start",command=start_operation)
buttonStart.grid(column=0,row=2)
buttonStatus = Button(text="Status",command=status_operation)
buttonStatus.grid(column=0,row=3)
buttonStop = Button(text="Stop",command=stop_operation)
buttonStop.grid(column=0,row=4)

window.mainloop()
