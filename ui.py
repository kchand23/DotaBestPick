import BestPick as bp
import tkinter as tk



#Get list of all heroes and store in a list 
heroes = bp.get_heroes()

window = tk.Tk()




#Dropdown menu for selecting heroes. 
variable = tk.StringVar(window)
variable.set(heroes[0]) # default value
hero_dropdown = tk.OptionMenu(window, variable, *heroes)
hero_dropdown.pack()

window.mainloop()