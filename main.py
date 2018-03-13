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
testButton.grid(column=0, row=6)

#--Functions
def start_operation():
  if box.get() == 'DA':
    txtstart ='service dadaemon start'
    cmp_clipboard(txtstart)
    testButton.config(text=txtstart)
    move_mouse()
  if box.get() == 'DC':
    txtstart ='service dcmd start'
    cmp_clipboard(txtstart)
    testButton.config(text=txtstart)
    move_mouse()
def stop_operation():
  if box.get() == 'DA':
    txtstop ='service dadaemon stop'
    cmp_clipboard(txtstop)
    testButton.config(text=txtstop)
    move_mouse()
  if box.get() == 'DC':
    txtstop ='service dcmd stop'
    cmp_clipboard(txtstop)
    testButton.config(text=txtstop)
    move_mouse()
def status_operation():
  if box.get() == 'DA':
    txtstatus ='service dadaemon status'
    cmp_clipboard(txtstatus)
    testButton.config(text=txtstatus)
    move_mouse()
  if box.get() == 'DC':
    txtstatus ='service dcmd status'
    cmp_clipboard(txtstatus)
    testButton.config(text=txtstatus)
    move_mouse()
  if box.get() == 'Vertica':
    txtstatus = 'admintools -t db_status -s UP'
    cmp_clipboard(txtstatus)
    testButton.config(text=txtstatus)
    move_mouse()
  if box.get() == 'PC':
    txtstatus = 'service caperfcenter_eventmanager status && service caperfcenter_devicemanager status && service caperfcenter_sso status && service caperfcenter_console status'
    cmp_clipboard(txtstatus)
    testButton.config(text='4 staus PC commands')
    move_mouse()
def cmp_clipboard(txt):
  r.withdraw()
  r.clipboard_clear()
  r.clipboard_append(txt)
  r.update()
def move_mouse():
  width, height = pyautogui.size()
  pyautogui.moveTo(width - 1000, height - 500)
  pyautogui.rightClick()
  pyautogui.press('enter')
def exit_app():
  global window, r
  r.destroy()
  window.destroy()

#--Labels
title = Label(window,text="Please select type of Machine")
title.grid(column=0,row=0)

#Combobox
value = StringVar()
box = ttk.Combobox(window, textvariable=value, state='readonly')
box['values'] = ('DC','DA','Vertica','PC')
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

#Windows
buttonExit = Button(text="EXIT PROGRAM",command=exit_app)
buttonExit.grid(column=0,row=5)
window.mainloop()
