from tkinter import *
class FlipButtonDemo(Frame):
    """window with a text box, a label, and a button.
    Pressing the button puts the reverse of the text in the label
    """
    def __init__(self):
        """Window setup"""
        Frame.__init__(self)
        self.master.title("Word Flip!")
        self.grid()
        # text box
        self.__text1 = Entry(self)
        self.__text1.grid(row=0, column=0)
        # text label
        self.__label1 = Label(self, text="")
        self.__label1.grid(row=1, column=0)
        # button
        self.__button1 = Button(self, text="Flip!",command=self._flip)
        self.__button1.grid(row=2, column=0)
    def _flip(self):
        """reverses the text in the box and puts it in the label"""
        word = self.__text1.get()
        self.__label1 = Label(self, text=word[::-1])
        self.__label1.grid(row=1, column=0)
def main():
    """initialize the window and wait for events"""
    demo = FlipButtonDemo()
    demo.mainloop()