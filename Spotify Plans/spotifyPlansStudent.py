from tkinter import *
from tkinter.font import Font

def updatePlan():
    plan = planChoiceVar.get()
    infoVar.set(planInformationList[plan])


    
root = Tk()
root.config(bg="#1DB954")
mainframe = Frame(root, bg="#1DB954")

traffoFontSmall = Font(family="Moonbeam", size=30)
traffoFontLarge = Font(family="Moonbeam", size=60)

planInformationList = ['INDIVIDUAL\n$9.99 CAD/mnth\n1 account', \
                       'DUO\n$12.99 CAD/mnth\n2 accounts', \
                       'FAMILY\n$14.99 CAD/mnth\n6 accounts', \
                       'STUDENT\n$4.99 CAD/mnth\n1 account']

planChoiceVar = IntVar()
individualRadio = Radiobutton(mainframe, text="individiual", \
                              variable=planChoiceVar, value=0, \
                              font=traffoFontSmall, command=updatePlan, bg="#1DB954")
duoRadio = Radiobutton(mainframe, text="duo", variable=planChoiceVar, value=1, font=traffoFontSmall, command=updatePlan, bg="#1DB954")
familyRadio = Radiobutton(mainframe, text="family", variable=planChoiceVar, value=2, font=traffoFontSmall, command=updatePlan, bg="#1DB954")
studentRadio = Radiobutton(mainframe, text="student", variable=planChoiceVar, value=3, font=traffoFontSmall, command=updatePlan, bg="#1DB954")

planChoiceVar.set(0)


infoVar = StringVar()
infoVar.set(planInformationList[0])
infoLabel = Label(mainframe, textvariable=infoVar, font=traffoFontLarge, bg="#1DB954")



#GRID WIDGETS
mainframe.grid(padx=50, pady=50)

individualRadio.grid(row=1, column=1, padx=10)
duoRadio.grid(column=2, row=1, padx=10)
familyRadio.grid(column=3, row=1, padx=10)
studentRadio.grid(column=4, row=1, padx=10)

infoLabel.grid(row=2, column=1, columnspan=4)

root.mainloop()
