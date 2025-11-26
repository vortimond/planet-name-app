import tkinter as tk

def on_submit():
    name_label.configure(text=f'Hello, {name_inp.get()}.')

root = tk.Tk()
root.title('Name App')
root.geometry('640x480')
name_label = tk.Label(root, text='What is your name?', font='Arial 16')
name_inp = tk.Entry(root, width=40)
submit_btn = tk.Button(root, text='Submit Survey', command=on_submit)
name_label.pack(pady=50)
name_inp.pack(anchor='n')
submit_btn.pack(padx=15, pady=15, anchor='ne')
root.mainloop()
