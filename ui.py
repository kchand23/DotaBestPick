import BestPick as bp
import tkinter as tk



#Get list of all heroes and store in a list 
heroes = bp.get_heroes()

window = tk.Tk()


variable = tk.StringVar(window)
variable.set(heroes[0]) # default value

w = tk.OptionMenu(window, variable, *heroes)
w.pack()

window.mainloop()