import BestPick as bp
import tkinter as tk

window = tk.Tk()
window.title("Counter Picker with Dotabuff")

# Add a grid
mainframe = tk.Frame(window)
mainframe.grid(column=0,row=0)
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 20, padx = 20)

#Get list of all heroes and store in a list 
heroes = bp.get_heroes()

#Label and setting position
label = tk.Label(mainframe, text="Select Hero: ", fg="white", bg="black")
label.grid(row = 0, column = 1)

#Dropdown menu for selecting heroes. 
variable = tk.StringVar(window)
variable.set(heroes[0]) # default value
hero_dropdown = tk.OptionMenu(mainframe, variable, *heroes)
hero_dropdown.grid(row = 0, column = 2)


window.mainloop()