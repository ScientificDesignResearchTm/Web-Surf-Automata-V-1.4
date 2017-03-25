from tkinter import *
class GuiApp:
    def __init__(self):
        self.root = Tk()
        self.root.bind("<Key>", self.key)
        self.root.title('Gui Screen')
        self.heightSize = 300
        self.widthSize = 550
        self.buttonHeightSize = 1
        self.buttonWidthSize = 10
        self.textXPosition = 50
        self.textYPosition = 80
        self.textYIncrement = 30
        self.textUpMinWidthSize = 3
        self.textUpSecWidthSize = 2
        self.colonSymbol = ':'
        self.minutesLabel = "min"
        self.secondsLabel = "sec"
        self.screenLabel = "SDR-WB 0130"
        self.statusLabel = "!!! Hurray to start your process..."
        self.linkOne = "This is first link"
        self.linkTwo = "This is second link"
        self.linkThree = "This is third link"
        self.linkFour = "This is forth link"
        self.linkFive = "This is five link"
        self.textHeightSize = int(self.heightSize/201)
        self.textWidthSize = int(self.widthSize/20)
        self.textUpXMinPosition = self.textXPosition+int(self.widthSize/2.2)
        self.textUpXSecPosition = self.textUpXMinPosition+35
        self.root.wm_minsize(width=self.widthSize,height=self.heightSize)
        #mainFirstLabelFrame
        self.mainFirstLabelFrame = LabelFrame(self.root,width=self.widthSize-6,height=self.heightSize-6)
        self.mainFirstLabelFrame.pack()
        self.mainFirstLabelFrame.place(x=3,y=3)
        #mainSecondLabelFrame
        self.mainSecondLabelFrame = LabelFrame(self.root,width=self.widthSize-10,height=self.heightSize-10)
        self.mainSecondLabelFrame.pack()
        self.mainSecondLabelFrame.place(x=5,y=5)
        #first text
        self.textOne = Text(self.root,width=self.textWidthSize,height=self.textHeightSize,bg='#f6f6f6',fg='#444444')
        self.textOne.pack()
        self.textOne.insert(INSERT, self.linkOne)
        self.textOne.configure(state=DISABLED)
        self.textOne.place(x=self.textXPosition, y=self.textYPosition)
        #second text
        self.textTwo = Text(self.root,width=self.textWidthSize,height=self.textHeightSize,bg='#f6f6f6',fg='#444444')
        self.textTwo.pack()
        self.textTwo.insert(INSERT, self.linkTwo)
        self.textTwo.configure(state=DISABLED)
        self.textTwo.place(x=self.textXPosition, y=self.textYPosition+self.textYIncrement)
        #third text
        self.textThree = Text(self.root,width=self.textWidthSize,height=self.textHeightSize,bg='#f6f6f6',fg='#444444')
        self.textThree.pack()
        self.textThree.insert(INSERT, self.linkThree)
        self.textThree.configure(state=DISABLED)
        self.textThree.place(x=self.textXPosition, y=self.textYPosition+self.textYIncrement*2)
        #fourth text
        self.textFour = Text(self.root,width=self.textWidthSize,height=self.textHeightSize,bg='#f6f6f6',fg='#444444')
        self.textFour.pack()
        self.textFour.insert(INSERT, self.linkFour)
        self.textFour.configure(state=DISABLED)
        self.textFour.place(x=self.textXPosition, y=self.textYPosition+self.textYIncrement*3)
        #fifth text
        self.textFive = Text(self.root,width=self.textWidthSize,height=self.textHeightSize,bg='#f6f6f6',fg='#444444')
        self.textFive.pack()
        self.textFive.insert(INSERT, self.linkFive)
        self.textFive.configure(state=DISABLED)
        self.textFive.place(x=self.textXPosition, y=self.textYPosition+self.textYIncrement*4)
        #first up time
        self.textOneUpMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textOneUpMin.pack()
        self.textOneUpMin.place(x=self.textUpXMinPosition, y=self.textYPosition)
        self.textOneUpMin.insert(INSERT,' 00')
        self.textOneUpSec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textOneUpSec.pack()
        self.textOneUpSec.insert(INSERT, '00')
        self.textOneUpSec.place(x=self.textUpXSecPosition, y=self.textYPosition)
        #first down time
        self.textOneDownMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textOneDownMin.pack()
        self.textOneDownMin.insert(INSERT, ' 00')
        self.textOneDownMin.place(x=self.textUpXMinPosition+80, y=self.textYPosition)
        self.textOneDownSec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textOneDownSec.pack()
        self.textOneDownSec.insert(INSERT, '00')
        self.textOneDownSec.place(x=self.textUpXSecPosition+80, y=self.textYPosition)
        #first delay time
        self.textOneDelayMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textOneDelayMin.pack()
        self.textOneDelayMin.insert(INSERT, ' 00')
        self.textOneDelayMin.place(x=self.textUpXMinPosition+160, y=self.textYPosition)
        self.textOneDelaySec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textOneDelaySec.pack()
        self.textOneDelaySec.insert(INSERT, '00')
        self.textOneDelaySec.place(x=self.textUpXSecPosition+160, y=self.textYPosition)
        #second up time
        self.textTwoUpMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textTwoUpMin.pack()
        self.textTwoUpMin.insert(INSERT, ' 00')
        self.textTwoUpMin.place(x=self.textUpXMinPosition, y=self.textYPosition+self.textYIncrement)
        self.textTwoUpSec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textTwoUpSec.pack()
        self.textTwoUpSec.insert(INSERT, '00')
        self.textTwoUpSec.place(x=self.textUpXSecPosition, y=self.textYPosition+self.textYIncrement)
        #second down time
        self.textTwoDownMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textTwoDownMin.pack()
        self.textTwoDownMin.insert(INSERT, ' 00')
        self.textTwoDownMin.place(x=self.textUpXMinPosition+80, y=self.textYPosition+self.textYIncrement)
        self.textTwoDownSec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textTwoDownSec.pack()
        self.textTwoDownSec.insert(INSERT, '00')
        self.textTwoDownSec.place(x=self.textUpXSecPosition+80, y=self.textYPosition+self.textYIncrement)
        #second delay time
        self.textTwoDelayMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textTwoDelayMin.pack()
        self.textTwoDelayMin.insert(INSERT, ' 00')
        self.textTwoDelayMin.place(x=self.textUpXMinPosition+160, y=self.textYPosition+self.textYIncrement)
        self.textTwoDelaySec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textTwoDelaySec.pack()
        self.textTwoDelaySec.insert(INSERT, '00')
        self.textTwoDelaySec.place(x=self.textUpXSecPosition+160, y=self.textYPosition+self.textYIncrement)
        #third up time
        self.textThirdoUpMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textThirdoUpMin.pack()
        self.textThirdoUpMin.insert(INSERT, ' 00')
        self.textThirdoUpMin.place(x=self.textUpXMinPosition, y=self.textYPosition+self.textYIncrement*2)
        self.textThirdUpSec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textThirdUpSec.pack()
        self.textThirdUpSec.insert(INSERT, '00')
        self.textThirdUpSec.place(x=self.textUpXSecPosition, y=self.textYPosition+self.textYIncrement*2)
        #third down time
        self.textThirdDownMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textThirdDownMin.pack()
        self.textThirdDownMin.insert(INSERT, ' 00')
        self.textThirdDownMin.place(x=self.textUpXMinPosition+80, y=self.textYPosition+self.textYIncrement*2)
        self.textThirdDownSec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textThirdDownSec.pack()
        self.textThirdDownSec.insert(INSERT, '00')
        self.textThirdDownSec.place(x=self.textUpXSecPosition+80, y=self.textYPosition+self.textYIncrement*2)
        #third delay time
        self.textThirdDelayMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textThirdDelayMin.pack()
        self.textThirdDelayMin.insert(INSERT, ' 00')
        self.textThirdDelayMin.place(x=self.textUpXMinPosition+160, y=self.textYPosition+self.textYIncrement*2)
        self.textThirdDelaySec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textThirdDelaySec.pack()
        self.textThirdDelaySec.insert(INSERT, '00')
        self.textThirdDelaySec.place(x=self.textUpXSecPosition+160, y=self.textYPosition+self.textYIncrement*2)
        #fourth up time
        self.textFourUpMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textFourUpMin.pack()
        self.textFourUpMin.insert(INSERT, ' 00')
        self.textFourUpMin.place(x=self.textUpXMinPosition, y=self.textYPosition+self.textYIncrement*3)
        self.textFourUpSec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textFourUpSec.pack()
        self.textFourUpSec.insert(INSERT, '00')
        self.textFourUpSec.place(x=self.textUpXSecPosition, y=self.textYPosition+self.textYIncrement*3)
        #fourth down time
        self.textFourDownMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textFourDownMin.pack()
        self.textFourDownMin.insert(INSERT, ' 00')
        self.textFourDownMin.place(x=self.textUpXMinPosition+80, y=self.textYPosition+self.textYIncrement*3)
        self.textFourDownSec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textFourDownSec.pack()
        self.textFourDownSec.insert(INSERT, '00')
        self.textFourDownSec.place(x=self.textUpXSecPosition+80, y=self.textYPosition+self.textYIncrement*3)
        #fourth delay time
        self.textFourthDelayMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textFourthDelayMin.pack()
        self.textFourthDelayMin.insert(INSERT, ' 00')
        self.textFourthDelayMin.place(x=self.textUpXMinPosition+160, y=self.textYPosition+self.textYIncrement*3)
        self.textFourthDelaySec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textFourthDelaySec.pack()
        self.textFourthDelaySec.insert(INSERT, '00')
        self.textFourthDelaySec.place(x=self.textUpXSecPosition+160, y=self.textYPosition+self.textYIncrement*3)
        #fifth up time
        self.textFiveUpMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textFiveUpMin.pack()
        self.textFiveUpMin.insert(INSERT, ' 00')
        self.textFiveUpMin.place(x=self.textUpXMinPosition, y=self.textYPosition+self.textYIncrement*4)
        self.textFiveUpSec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textFiveUpSec.pack()
        self.textFiveUpSec.insert(INSERT, '00')
        self.textFiveUpSec.place(x=self.textUpXSecPosition, y=self.textYPosition+self.textYIncrement*4)
        #fifth down time
        self.textFiveDownMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textFiveDownMin.pack()
        self.textFiveDownMin.insert(INSERT, ' 00')
        self.textFiveDownMin.place(x=self.textUpXMinPosition+80, y=self.textYPosition+self.textYIncrement*4)
        self.textFiveDownSec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textFiveDownSec.pack()
        self.textFiveDownSec.insert(INSERT, '00')
        self.textFiveDownSec.place(x=self.textUpXSecPosition+80, y=self.textYPosition+self.textYIncrement*4)
        #fifth delay time
        self.textFiveDelayMin = Text(self.root,width=self.textUpMinWidthSize,height=self.textHeightSize)
        self.textFiveDelayMin.pack()
        self.textFiveDelayMin.insert(INSERT, ' 00')
        self.textFiveDelayMin.place(x=self.textUpXMinPosition+160, y=self.textYPosition+self.textYIncrement*4)
        self.textFiveDelaySec = Text(self.root,width=self.textUpSecWidthSize,height=self.textHeightSize)
        self.textFiveDelaySec.pack()
        self.textFiveDelaySec.insert(INSERT, '00')
        self.textFiveDelaySec.place(x=self.textUpXSecPosition+160, y=self.textYPosition+self.textYIncrement*4)
        #button track process
        self.buttonTrackProcess = Button(self.root,width=self.buttonWidthSize,height=self.buttonHeightSize,text="Track Process")
        self.buttonTrackProcess.pack()
        self.buttonTrackProcess.place(x=self.textUpXMinPosition, y=self.textYPosition+40+self.textYIncrement*4)
        #button automate
        self.buttonAutomate = Button(self.root,width=self.buttonWidthSize,height=self.buttonHeightSize,text="Automate")
        self.buttonAutomate.pack()
        self.buttonAutomate.place(x=self.textUpXMinPosition+120 , y=self.textYPosition+40+self.textYIncrement*4)
        #mainLabelFrame
        self.mainLabelFrame = LabelFrame(self.root,width=197,height=40,bd=10)
        self.mainLabelFrame.pack()
        self.mainLabelFrame.place(x=self.widthSize-350,y=7)
        #mainLabel
        self.mainLabel = Label(self.root,text="Asimo Multi Tech Pvt Ltd")
        self.mainLabel.pack()
        self.mainLabel.place(x=self.widthSize-320,y=15)
        #linkFirstLabel
        self.linkFirstLabel = Label(self.root,text="Website Surf")
        self.linkFirstLabel.pack()
        self.linkFirstLabel.place(x=128,y=self.textYPosition-38)
        # linkSecondLabel
        self.linkSecondLabel = Label(self.root,text="Automater Tool")
        self.linkSecondLabel.pack()
        self.linkSecondLabel.place(x=118,y=self.textYPosition-21)
        #screenLabel
        self.screenLabel = Label(self.root,text=self.screenLabel)
        self.screenLabel.pack()
        self.screenLabel.place(x=30,y=10)
        #statusLabel
        self.statusLabel = Label(self.root,text=self.statusLabel)
        self.statusLabel.pack()
        self.statusLabel.place(x=70,y=self.textYPosition+40+self.textYIncrement*4)
        #proweredByLabelFrame
        self.proweredByLabelFrame = LabelFrame(self.root,width=100,height=24)
        self.proweredByLabelFrame.pack()
        self.proweredByLabelFrame.place(x=self.textUpXMinPosition+144,y=self.textYPosition+69+self.textYIncrement*4)
        #proweredByLabel
        self.proweredByLabel = Label(self.root,text="Powered by SDR")
        self.proweredByLabel.pack()
        self.proweredByLabel.place(x=self.textUpXMinPosition+148,y=self.textYPosition+70+self.textYIncrement*4)
        #oneLabel
        self.oneLabel = Label(self.root,text="1)")
        self.oneLabel.pack()
        self.oneLabel.place(x=30,y=self.textYPosition-2)
        #twoLabel
        self.twoLabel = Label(self.root,text="2)")
        self.twoLabel.pack()
        self.twoLabel.place(x=30,y=self.textYPosition-2+self.textYIncrement)
        #threeLabel
        self.threeLabel = Label(self.root,text="3)")
        self.threeLabel.pack()
        self.threeLabel.place(x=30,y=self.textYPosition-2+self.textYIncrement*2)
        #fourLabel
        self.fourLabel = Label(self.root,text="4)")
        self.fourLabel.pack()
        self.fourLabel.place(x=30,y=self.textYPosition-2+self.textYIncrement*3)
        #fiveLabel
        self.fiveLabel = Label(self.root,text="5)")
        self.fiveLabel.pack()
        self.fiveLabel.place(x=30,y=self.textYPosition-2+self.textYIncrement*4)
        #minutesUpLabel
        self.minutesUpLabel = Label(self.root,text=self.minutesLabel)
        self.minutesUpLabel.pack()
        self.minutesUpLabel.place(x=self.textUpXMinPosition,y=self.textYPosition-21)
        #secondsUpLabel
        self.secondsUpLabel = Label(self.root,text=self.secondsLabel)
        self.secondsUpLabel.pack()
        self.secondsUpLabel.place(x=self.textUpXMinPosition+33,y=self.textYPosition-21)
        #minutesDownLabel
        self.minutesDownLabel = Label(self.root,text=self.minutesLabel)
        self.minutesDownLabel.pack()
        self.minutesDownLabel.place(x=self.textUpXMinPosition+80,y=self.textYPosition-21)
        #secondsDownLabel
        self.secondsDownLabel = Label(self.root,text=self.secondsLabel)
        self.secondsDownLabel.pack()
        self.secondsDownLabel.place(x=self.textUpXMinPosition+113,y=self.textYPosition-21)
        #minutesDelayLabel
        self.minutesDelayLabel = Label(self.root,text=self.minutesLabel)
        self.minutesDelayLabel.pack()
        self.minutesDelayLabel.place(x=self.textUpXMinPosition+160,y=self.textYPosition-21)
        #secondsDelayLabel
        self.secondsDelayLabel = Label(self.root,text=self.secondsLabel)
        self.secondsDelayLabel.pack()
        self.secondsDelayLabel.place(x=self.textUpXMinPosition+193,y=self.textYPosition-21)
        #scrollUpLabel
        self.scrollUpLabel = Label(self.root,text="Scroll up time")
        self.scrollUpLabel.pack()
        self.scrollUpLabel.place(x=self.textUpXMinPosition-10,y=self.textYPosition-35)
        #scrollUpLabel
        self.scrollUpLabel = Label(self.root,text="Scroll up time")
        self.scrollUpLabel.pack()
        self.scrollUpLabel.place(x=self.textUpXMinPosition-10,y=self.textYPosition-35)
        #scrollDownLabel
        self.scrollDownLabel = Label(self.root,text="Scroll down time")
        self.scrollDownLabel.pack()
        self.scrollDownLabel.place(x=self.textUpXMinPosition+67,y=self.textYPosition-35)
        #delayLabel
        self.delayLabel = Label(self.root,text="Delay time")
        self.delayLabel.pack()
        self.delayLabel.place(x=self.textUpXMinPosition+159,y=self.textYPosition-35)
        #oneUpColonLabel
        self.oneUpColonLabel = Label(self.root,text=self.colonSymbol)
        self.oneUpColonLabel.pack()
        self.oneUpColonLabel.place(x=self.textUpXMinPosition+27,y=self.textYPosition-2)
        #tweUpColonLabel
        self.tweUpColonLabel = Label(self.root,text=self.colonSymbol)
        self.tweUpColonLabel.pack()
        self.tweUpColonLabel.place(x=self.textUpXMinPosition+27,y=self.textYPosition-2+self.textYIncrement)
        #threeUpColonLabel
        self.threeUpColonLabel = Label(self.root,text=self.colonSymbol)
        self.threeUpColonLabel.pack()
        self.threeUpColonLabel.place(x=self.textUpXMinPosition+27,y=self.textYPosition-2+self.textYIncrement*2)
        #fourUpColonLabel
        self.fourUpColonLabel = Label(self.root,text=self.colonSymbol)
        self.fourUpColonLabel.pack()
        self.fourUpColonLabel.place(x=self.textUpXMinPosition+27,y=self.textYPosition-2+self.textYIncrement*3)
        #fiveUpColonLabel
        self.fiveUpColonLabel = Label(self.root,text=self.colonSymbol)
        self.fiveUpColonLabel.pack()
        self.fiveUpColonLabel.place(x=self.textUpXMinPosition+27,y=self.textYPosition-2+self.textYIncrement*4)
        #onedownColonLabel
        self.onedownColonLabel = Label(self.root,text=self.colonSymbol)
        self.onedownColonLabel.pack()
        self.onedownColonLabel.place(x=self.textUpXMinPosition+107,y=self.textYPosition-2)
        #twedownColonLabel
        self.twedownColonLabel = Label(self.root,text=self.colonSymbol)
        self.twedownColonLabel.pack()
        self.twedownColonLabel.place(x=self.textUpXMinPosition+107,y=self.textYPosition-2+self.textYIncrement)
        #threedownColonLabel
        self.threedownColonLabel = Label(self.root,text=self.colonSymbol)
        self.threedownColonLabel.pack()
        self.threedownColonLabel.place(x=self.textUpXMinPosition+107,y=self.textYPosition-2+self.textYIncrement*2)
        #fourdownColonLabel
        self.fourdownColonLabel = Label(self.root,text=self.colonSymbol)
        self.fourdownColonLabel.pack()
        self.fourdownColonLabel.place(x=self.textUpXMinPosition+107,y=self.textYPosition-2+self.textYIncrement*3)
        #fivedownColonLabel
        self.fivedownColonLabel = Label(self.root,text=self.colonSymbol)
        self.fivedownColonLabel.pack()
        self.fivedownColonLabel.place(x=self.textUpXMinPosition+107,y=self.textYPosition-2+self.textYIncrement*4)
        #onedelayColonLabel
        self.onedelayColonLabel = Label(self.root,text=self.colonSymbol)
        self.onedelayColonLabel.pack()
        self.onedelayColonLabel.place(x=self.textUpXMinPosition+187,y=self.textYPosition-2)
        #twedelayColonLabel
        self.twedelayColonLabel = Label(self.root,text=self.colonSymbol)
        self.twedelayColonLabel.pack()
        self.twedelayColonLabel.place(x=self.textUpXMinPosition+187,y=self.textYPosition-2+self.textYIncrement)
        #threedelayColonLabel
        self.threedelayColonLabel = Label(self.root,text=self.colonSymbol)
        self.threedelayColonLabel.pack()
        self.threedelayColonLabel.place(x=self.textUpXMinPosition+187,y=self.textYPosition-2+self.textYIncrement*2)
        #fourdelayColonLabel
        self.fourdelayColonLabel = Label(self.root,text=self.colonSymbol)
        self.fourdelayColonLabel.pack()
        self.fourdelayColonLabel.place(x=self.textUpXMinPosition+187,y=self.textYPosition-2+self.textYIncrement*3)
        #fivedelayColonLabel
        self.fivedelayColonLabel = Label(self.root,text=self.colonSymbol)
        self.fivedelayColonLabel.pack()
        self.fivedelayColonLabel.place(x=self.textUpXMinPosition+187,y=self.textYPosition-2+self.textYIncrement*4)
        self.root.mainloop()
    # def incrementSecond(self,event):
    #     print(event)
    def key(self, event):
        # Make sure the frame is receiving input!
        print("Pressed", event.widget)
GuiApp()