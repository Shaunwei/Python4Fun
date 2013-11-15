#!usr/bin/env python

import Tkinter

top = Tkinter.Tk()

label = Tkinter.Label(top, text='Hello World!')
label.pack()

quit = Tkinter.Button(top, text='Click to quit!', command=top.quit)
quit.pack()
Tkinter.mainloop()
