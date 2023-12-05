import tkinter as tk
from voting import VotingFunctions

class VotingAppGUI:
    def __init__(self, root: tk.Tk) -> None:
        """
        Initialize the VotingAppGUI class.

        Args:
            root: Tkinter root window
        """
        self.root = root
        self.voting_functions = VotingFunctions()

        self.setup_gui()

    def setup_gui(self) -> None:
        """
        Sets up the GUI
        """
        self.root.title('Voting Application')
        self.root.geometry('300x250')
        self.root.resizable(False, False)

        self.var = tk.StringVar()
        self.var.set(None)

        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Creates the GUI widgets
        """
        name_label = tk.Label(self.root, text='Enter your name: ')
        name_label.pack(pady=(10, 5), padx=10, anchor='w')

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5, padx=10, ipadx=50)

        vote_label = tk.Label(self.root, text='Select your vote: ')
        vote_label.pack(pady=5, padx=10, anchor='w')

        vote_frame = tk.Frame(self.root)
        vote_frame.pack(pady=5)

        vote_button1 = tk.Radiobutton(self.root, text='John', variable=self.var, value='John')
        vote_button1.place(relx=0.43, rely=0.28)

        vote_button2 = tk.Radiobutton(self.root, text='Jane', variable=self.var, value='Jane')
        vote_button2.place(relx=0.63, rely=0.28)

        record_button = tk.Button(self.root, text='Record vote', command=self.record_vote_gui)
        record_button.pack(pady=10)

        finish_button = tk.Button(self.root, text='Finish', command=self.finish_vote_gui)
        finish_button.pack(pady=10)

        self.error_label = tk.Label(self.root)
        self.error_label.place(relx=0.5, rely=.95, anchor='s')

    def record_vote_gui(self) -> None:
        """
        Retrieves voter name and vote. Validates that the name is a string and that the 
        vote is clicked or else it will tell the voter to select a candidate.
        """
        name = self.name_entry.get()

        if not name.replace(' ', '').isalpha():
            self.error_label.config(text='Please enter a valid name.')
            return
    
        self.error_label.config(text='')

        vote = self.var.get()

        if vote and vote != "None":
            self.voting_functions.record_vote(name, vote)
        elif vote == "None":
            self.error_label.config(text='Please select a candidate.')

    def finish_vote_gui(self):
        """
        Finish voting and close the GUI.
        """
        self.voting_functions.finish_vote(self.root)

def main() -> None:
    """
    Main function to initialize the app.
    """
    root = tk.Tk()
    VotingAppGUI(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()