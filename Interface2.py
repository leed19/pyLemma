from Tkinter import Tk, BOTH, Menu
from ttk import Frame, Button, Style


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
        
    def initUI(self):
      
        self.parent.title("pyLemma Interface test")
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_cascade(label="New Window")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)
        editMenu = Menu(menubar)
        editMenu.add_cascade(label="Undo")
        editMenu.add_cascade(label="Redo")
        editMenu.add_separator()
        editMenu.add_cascade(label="Cut")
        editMenu.add_cascade(label="Copy")
        editMenu.add_cascade(label="Paste")
        menubar.add_cascade(label="Edit", underline=0, menu=editMenu)
    
    
    def onExit(self):
        self.quit()


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()