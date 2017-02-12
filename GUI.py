from tkinter import *
import DIYmain as diy
import io
from PIL import ImageTk, Image
import webbrowser


class Gui:


    def __init__(self):

        self.window = Tk()
        self.window.title("DIY")
        self.window.geometry('1035x660')
        self.buttons = []
        self.skillsArray = []
        self.projectsToChooseFrom = [['Make a quick box using box joints','http://www.instructables.com/id/Make-a-quick-box-using-box-joints/?ALLSTEPS'],['Conspeakuous: Concrete Speakers ','http://www.instructables.com/id/Conspeakuous-Concrete-Speakers/?ALLSTEPS'],['Concrete Lamp','http://www.instructables.com/id/DIY-Concrete-Lamp/?ALLSTEPS'],['Making Wooden Knobs on a Drill Press','http://www.instructables.com/id/Making-Wooden-Knobs-on-a-Drill-Press/?ALLSTEPS'],['Cross Stitch Wood Necklace','http://www.instructables.com/id/Cross-Stitch-Wood-Necklace/?ALLSTEPS'],['light-up penguin with LEDs','http://www.instructables.com/id/How-to-sew-a-light-up-plush-Tux-penguin-with-EL-wi/?ALLSTEPS'],['Electric Violin','http://www.instructables.com/id/Electric-Violin-1/?ALLSTEPS'],['Solid wood bench/coffee table','http://www.instructables.com/id/Solid-wood-benchcoffee-table/?ALLSTEPS'],['Wood Industrial Lamp Desk','http://www.instructables.com/id/Wood-Industrial-Lamp-Desk/?ALLSTEPS'],['Desktop Printing Press','http://www.instructables.com/id/Desktop-Printing-Press/?ALLSTEPS']]
        self.startOver = 0
        #self.window.configure(background = '#FFFFFF')
        self.start()
        self.window.mainloop()

    def startButtons(self):
        self.buttons = []
        self.skillsArray = []

        for i in range(len(self.projectsToChooseFrom)):

            photo = PhotoImage(file=str(i)+'.gif')
            self.buttons.append(Button(text=self.projectsToChooseFrom[i][0], command=lambda i=i: self.chooseSkill(i), width=250, height=100, image=photo, compound='left'))
            self.buttons[i].image = photo

            if i <= 3:
                Row=2
            elif (i>3 and i<=7):
                Row=3
            else:
                Row=4

            self.buttons[i].grid(row=Row, column=i%4, sticky=E)


    def showDIYimg(self):
        DIYimg = ImageTk.PhotoImage(Image.open('DIY1.gif'))
        DIYlabel = Label(image=DIYimg)
        DIYlabel.image = DIYimg
        DIYlabel.grid(columnspan=6, row=0, column=0)


    def showLabel(self, photoName, row, col):
        photo = ImageTk.PhotoImage(Image.open(photoName))
        label2 = Label(image=photo)
        label2.image = photo
        label2.grid(row=row, column=col, columnspan=6)


    def start(self):
        if self.startOver:
            for widget in self.window.winfo_children():
                widget.destroy()
        self.showDIYimg()
        self.showLabel('pick.gif',1,0)
        self.startButtons()


    def chooseSkill(self, idx):
        self.skillsArray = diy.getwords(self.projectsToChooseFrom[idx][1])

        for widget in self.window.winfo_children():
            widget.destroy()

        self.showDIYimg()
        self.showLabel('which.gif',1,0)

        self.skillsArray.pop(0)
        for s in self.skillsArray:
            b = Button(self.window, text=s, command=lambda s=s, i=idx: self.run(self.projectsToChooseFrom[idx][1], s))
            b.grid(column=2)



    def run(self, project, skill):

        urlArray = diy.getUserWishPath(project, skill)
        for widget in self.window.winfo_children():
            widget.destroy()
        self.showDIYimg()
        self.showLabel('your.gif',1,0)
        for i in range(len(urlArray)):
            button = Button(text=urlArray[i], command=lambda i=urlArray[i]: webbrowser.open(i))
            button.grid(column=15, row=(2*i), sticky=S)
            if i != (len(urlArray)-1):
                self.showLabel('arrow.gif',(2*i)+1, 15)


        b = Button(text="start over", command=lambda : self.again(1))
        b.grid(sticky=N)
        quitButton = Button(text="quit", command=lambda : self.window.quit())
        quitButton.grid(sticky=N)

    def openBrowser(self, url):
        webbrowser.open_new(url)

    def again(self, toStart):
        if toStart:
            self.startOver = toStart
            self.start()



diy.biuldGraph()
gui = Gui()



