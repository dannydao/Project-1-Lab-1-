import tkinter as tk
from voting import record_vote, finish_vote

def record_vote_gui() -> None:
    """
    Retrieves the name and vote from the GUI components and records the vote.
    """
    name = name_entry.get()
    vote = var.get()
    record_vote(name, vote)

# Main Window creation
root = tk.Tk()
root.title("Voting Application")

root.geometry('250x200')

root.resizable(False, False)

# Creating variable to hold the vote choice
var = tk.StringVar()
# Setting the default value to John
var.set('John')

# GUI Elements
name_label = tk.Label(root, text='Enter your name: ')
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

vote_label = tk.Label(root, text='Select your vote: ')
vote_label.pack()

vote_button1 = tk.Radiobutton(root, text='John', variable=var, value='John')
vote_button1.pack()

vote_button2 = tk.Radiobutton(root, text='Jane', variable=var, value='Jane')
vote_button2.pack()

record_button = tk.Button(root, text='Record vote', command= record_vote_gui)
record_button.pack(pady= 10)

finish_button = tk.Button(root, text='Finish', command=finish_vote)
finish_button.pack(pady=10)

# Run main event loop
root.mainloop()

