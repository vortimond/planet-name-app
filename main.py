import tkinter as tk

def on_submit():
    name_label.configure(text=f'Hello, {name_inp.get()}.')

root = tk.Tk()
root.geometry('640x480+300+300')
name_label = tk.Label(root, text='What is your name?')
name_inp = tk.Entry(root)
submit_btn = tk.Button(root, text='Submit Survey', command=on_submit)
name_label.pack()
name_inp.pack()
submit_btn.pack()
root.mainloop()
