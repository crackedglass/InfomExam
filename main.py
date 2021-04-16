from tkinter import * 
import json
file = open("label_list.json", "r")
str1 = file.read()
a = json.loads(str1)
root = Tk()
root.size("500x500")
root.title(a["title"])
but = Button(root, text = a["button_text"], width = 25, height = 5, bg = "black",fg ="red")
but.pack()


root.mainloop()
