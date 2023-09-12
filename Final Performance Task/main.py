"""
To install pillow module for tkinter in your computer or virtual environment,
please enter one of the two:
pip install -r requirements.txt
or
pip install Pillow

Additionally, remember to install the Unicosmo Font in the FPT file
"""
from tkinter import *
from tkinter.messagebox import *
from tkinter.font import Font
from datetime import datetime
from PIL import Image, ImageTk
import random

#fname, lname, days staying, age, number of ppl, activities(swim, hike, canoe, arch, drama)
global date
date = datetime.now().strftime('%a, %d %b %Y, %I:%M%p')

pplList = [
    ['Alyssa', 'Dong', 7, 17, 1, True, False, True, True, False],
    ['Tracy', 'Dong', 7, 20, 1, True, False, False, True, False],
    ['Jason', 'Dong', 7, 50, 1, True, True, True, True, False],
    ['Mei', 'Wang', 7, 50, 1, False, True, True, True, True],
    ['Test', 'One', 6, 100, 5, True, False, False, False, True],
    ['Test', 'Two', 5, 59, 2, False, False, False, False, False ],
    ['Test', 'Three', 3, 18, 4, True, True, True, True, True],
    ['Test', 'Four', 4, 46, 2, False, True, True, True, True],
    ['Test', 'Five', 1, 59, 2, True, False, False, False, False ],
    ['Test', 'Six', 2, 18, 4, True, True, False, True, True],
    ['Test', 'Seven', 6, 46, 2, False, True, True, True, True],
    ['Test', 'Eight', 2, 59, 2, True, False, False, False, False ],
    ['Test', 'Nine', 2, 18, 4, True, True, True, True, True],
    ['Test', 'Ten', 1, 46, 2, False, True, True, True, True],
    ['Test', 'Eleven', 2, 59, 2, False, False, False, False, False ],
    ['Test', 'Twelve', 2, 18, 4, True, True, True, True, True],
    ['Test', 'Thirteen', 6, 46, 2, False, True, True, True, True],
    ['Test', 'Fourteen', 1, 59, 2, True, False, False, False, False ],
    ['Test', 'Fifteen', 2, 18, 4, True, True, True, False, True],
    ['Test', 'Sixteen', 7, 46, 2, False, True, True, False, True]
]

intent = [
    [
        ['register','enter','schedule','record','log'],
        ['😎 On the main screen, there is a \'Register Customer\' button.\nBy clicking it, you will open a new screen.\nEnter the customer information there', '🧐 I wish I knew mate... \nJust kidding!\nkeep on refreshing the answer']
    ],
    [
        ['check', 'list', 'information', 'info', 'delete'],
        ['🥰 Open the Customer List screen\nby navigating to the \'Customer List\' button\nYou\'ll be able to check and delete customer information.']
    ],
    [
        ['hi', 'hello', 'sup', 'yo', 'morning', 'good', 'afternoon', 'evening'],
        ['Hello! 👋', 'Welcome! 🤗']
    ],
    [
        ['bye', 'see', 'later'],
        ['😭 Bye...', 'Goodbye... 😞','🥲 N00Oo。...']
    ],
    [
        ['are', 'name'],
        ['🤖 Hi! I\'m Jenne\nI\'m an inquiry bot that will guide you through the window']
    ],
    [
        ['time', 'date', 'day', 'today'],
        ['👀 Today is ' + date]
    ],
    [
        ['contact', 'cell', 'mail', 'email', 'location'],
        ['The camp\'s contact info:\nCell: (647) 648-6752\nEmail:1dongaly@hdsb.ca\nLocation: 2000 Candy Avenue']
    ],
    [
        ['bored', 'sleepy', 'tired'],
        ['I feel you _(:3>L)__','*gives you a sympathizing gaze*']
    ],
    [
        ['joke', 'funny', 'fun', 'happy'],
        ['Did you hear about the mathematician\nwho’s afraid of negative numbers?\nHe’ll stop at nothing to avoid them.',
         'Knock! Knock!\nWho’s there?\nControl Freak.\nCon…\nOK, now you say, “Control Freak who?” ',
         'Did you hear about the claustrophobic astronaut?\nHe just needed a little space.',
         'Why don’t scientists trust atoms?\nBecause they make up everything.',
         'Where are average things manufactured?\nThe satisfactory.',
         'How do you keep a bagel from getting away?\nPut lox on it.',
         'What do you call a parade of rabbits hopping backwards?\nA receding hare-line.'
         ]
    ]#,
    #[
        #['fuck','shit','hell'],
        #['How could you say that to me :(','...\nYou son of a b****!\nI\'m your assistant!\nHow could you say that to me!!!']
    #]
]

def upload():
    """
    uploads data in the register screen into the pplList
    """
    customer = []
    
    if firstVar.get() == "" or lastVar.get() == "" or dayVar.get() == 0 or numberPpl.get() == 0:
        showinfo("Fill out completely","Please ensure you have filled out required boxes")            
    else:
        customer.append(firstVar.get())
        customer.append(lastVar.get())
        customer.append(dayVar.get())
        customer.append(ageVar.get())
        customer.append(numberPpl.get())
        customer.append(swimVar.get())
        customer.append(hikeVar.get())
        customer.append(canoeVar.get())
        customer.append(archVar.get())
        customer.append(dramaVar.get())
        rootTwo.destroy()
        print(customer)
        pplList.append(customer)
    
def destroyTwo():
    """
    This destroys the register screen after
    user clicks on the cancel button
    """
    global rootTwo
    
    #destroy register screen
    rootTwo.destroy()
    
def registerScreen():
    """
    This secondary screen registers customer info
    """
    global rootTwo
    global firstVar
    global lastVar
    global dayVar
    global ageVar
    global numberPpl
    global swimVar
    global hikeVar
    global canoeVar
    global archVar
    global dramaVar
    
    #register customer screen
    rootTwo = Toplevel()
    mainTwo = Frame(rootTwo)

    resize = img.resize((340,100))
    photo = ImageTk.PhotoImage(resize)
    title = Label(mainTwo, text = "Register\nCustomer", image = photo, compound = "center", font= ("Unicosmo Free", 45), fg = "#fff")

    #first name
    firstVar = StringVar()
    firstEntry = Entry(mainTwo, textvariable = firstVar, width = 35)
    firstLabel = Label(mainTwo, text = "First Name:")

    #last name
    lastVar = StringVar()
    lastEntry = Entry(mainTwo, textvariable = lastVar, width = 35)
    lastLabel = Label(mainTwo, text = "Last Name:")

    #days
    dayLabel = Label(mainTwo, text = "Days:")
    daysList = [1,2,3,4,5,6,7]
    dayVar = IntVar()
    daysOption = OptionMenu(mainTwo, dayVar, *daysList)

    #age
    ageLabel = Label(mainTwo, text = "Age:")
    ageVar = IntVar()
    ageVar.set(100)
    ageScale = Scale(mainTwo, from_=0, to = 100, variable = ageVar, width = 15, showvalue = True, resolution = 1, trough = "#d8dbe8")

    #number of people
    numberLabel = Label(mainTwo, text = "Number of\npeople:")
    numberFrame = LabelFrame(mainTwo)
    numberPpl = IntVar()
    numberPpl.set(0)
    pplOne = Radiobutton(numberFrame, text = "1", variable = numberPpl, value = 1)
    pplTwo = Radiobutton(numberFrame, text = "2", variable = numberPpl, value = 2)
    pplThree = Radiobutton(numberFrame, text = "3", variable = numberPpl, value = 3)
    pplFour = Radiobutton(numberFrame, text = "4", variable = numberPpl, value = 4)
    pplFive = Radiobutton(numberFrame, text = "5", variable = numberPpl, value = 5)

    #activities
    activityLabel = Label(mainTwo, text = "Activities:", font = ("Unicosmo Free", 50), fg = "#657abf")
    activityLabelFrame = LabelFrame(mainTwo)

    swimVar = BooleanVar()
    swimCheck = Checkbutton(activityLabelFrame, variable = swimVar, text = "Swimming", onvalue = True, offvalue = False)

    hikeVar = BooleanVar()
    hikeCheck = Checkbutton(activityLabelFrame, variable = hikeVar, text = "Hiking", onvalue = True, offvalue = False)

    canoeVar = BooleanVar()
    canoeCheck = Checkbutton(activityLabelFrame, variable = canoeVar, text = "Canoeing", onvalue = True, offvalue = False)

    archVar = BooleanVar()
    archCheck = Checkbutton(activityLabelFrame, variable = archVar, text = "Archery", onvalue = True, offvalue = False)

    dramaVar = BooleanVar()
    dramaCheck = Checkbutton(activityLabelFrame, variable = dramaVar, text = "Drama", onvalue = True, offvalue = False)

    #disables full programs
    updateProgram()
    
    if swimming == 50:
        swimCheck.config(state = "disabled")
    else:
        swimCheck.config(state = "normal")
        
    if hiking == 50:
        hikeCheck.config(state = "disabled")
    else:
        hikeCheck.config(state = "normal")
        
    if canoeing == 50:
        canoeCheck.config(state = "disabled")
    else:
        canoeCheck.config(state = "normal")
        
    if archery == 50:
        archCheck.config(state = "disabled")
    else:
        archCheck.config(state = "normal")
        
    if drama == 50:
        dramaCheck.config(state = "disabled")
    else:
        dramaCheck.config(state = "normal")

    #ok and cancel buttons
    cancelButton = Button(activityLabelFrame, text = "Cancel", command = destroyTwo)
    okButton = Button(activityLabelFrame, text = "Ok", command = upload)
    
    #gridding
    mainTwo.grid()

    title.grid(row = 1, column = 1, columnspan = 4)

    firstLabel.grid(row = 2, column = 1, columnspan = 2, sticky = W)
    firstEntry.grid(row = 2, column = 3, columnspan = 2, padx = 10)

    lastLabel.grid(row = 3, column = 1, columnspan = 2, sticky = W)
    lastEntry.grid(row = 3, column = 3, columnspan = 2, padx = 10)

    dayLabel.grid(row = 4, column = 1, sticky = W)
    daysOption.grid(row = 4, column = 2, sticky = EW, pady = 5)

    #format scale somehow so that the values are shown on the other side
    ageLabel.grid(row = 5, column = 1, sticky = W)
    ageScale.grid(row = 6, column = 1, sticky = NS, pady = 5)

    numberLabel.grid(row = 5, column = 2)
    numberFrame.grid(row = 6, column = 2, sticky = NS, pady = 5)
    pplOne.grid(row = 1, column = 1)
    pplTwo.grid(row = 2, column = 1)
    pplThree.grid(row = 3, column = 1)
    pplFour.grid(row = 4, column = 1)
    pplFive.grid(row = 5, column = 1)

    activityLabel.grid(row = 4, column = 3, padx = 10, columnspan = 2, rowspan = 2, sticky = W)
    activityLabelFrame.grid(row = 6, column = 3, sticky = EW, padx = 10, pady = 5)
    swimCheck.grid(row = 1, column = 1, sticky = W)
    hikeCheck.grid(row = 2, column = 1, sticky = W)
    canoeCheck.grid(row = 3, column = 1, sticky = W)
    archCheck.grid(row = 4, column = 1, sticky = W)
    dramaCheck.grid(row = 5, column = 1, sticky = W)
    
    cancelButton.grid(row = 5, column = 3, sticky = E, padx = 5, ipadx = 10, pady = 5)
    okButton.grid(row = 5, column = 2, sticky = E, padx = 5, ipadx = 10, pady = 5)
    
    rootTwo.grab_set()
    rootTwo.mainloop()

def customerList():
    """
    This is the secondary customer list screen
    """
    global rootThree
    global customerslist
    global nameList
    
    List = []
    
    rootThree = Toplevel()
    mainThree = Frame(rootThree)

    #code to return a list of names
    for person in pplList:
        List.append(f"{person[0]} {person[1]}")
    
    #title
    resize = img.resize((240,70))
    photo = ImageTk.PhotoImage(resize)
    title = Label(mainThree, text = "Customer List", image = photo, compound = "center", font=("Unicosmo Free", 40), fg = "#fff")

    #customer listbox
    listFrame = LabelFrame(mainThree)
    nameList = StringVar()
    nameList.set(List)
    customerslist = Listbox(listFrame, listvariable = nameList, selectmode = SINGLE)
    vertListScroller = Scrollbar(listFrame,command = customerslist.yview)
    customerslist.config(yscrollcommand = vertListScroller.set)
    
    #check info
    infoButton = Button(mainThree, text = "Check Info", command = checkInfo)
    #delete button
    delButton = Button(mainThree, text = "Delete", command = delete_customer)

    #gridding
    mainThree.grid(row = 1, column = 1)
    title.grid(row = 1, column = 1, columnspan = 2)

    listFrame.grid(row = 2, column = 1, sticky = W, padx = 10, pady = 10, rowspan = 3)
    customerslist.grid(row = 1, column = 1)
    vertListScroller.grid(row = 1, column = 2, sticky = NS)

    infoButton.grid(row = 2, column = 2, sticky = EW, padx = 10)
    delButton.grid(row = 3, column = 2, sticky = EW+N, padx = 10)

    rootThree.grab_set()
    rootThree.mainloop()

def checkInfo():
    """
    This allows the user to check customer info
    in the customer list window
    """
    global customerslist
    if pplList != []:
        pick = customerslist.curselection()[0]
        pplList
        message = f"Name: {pplList[pick][0]} {pplList[pick][1]}\n\nAge: {pplList[pick][3]}\n\nStaying for {pplList[pick][2]} days\n\nNumber of People: {pplList[pick][4]}\n\nActivities:\n"
        if pplList[pick][5]:
            message += "Swimming "
        if pplList[pick][6]:
            message += "Hiking "
        if pplList[pick][7]:
            message += "Canoeing "
        if pplList[pick][8]:
            message += "Archery "
        if pplList[pick][9]:
            message += "Drama "
        showinfo("Info", message)

def delete_customer():
    """
    This deletes a customer from the customer list window
    """
    global nameList
    global customerslist
    global pplList
    if pplList != []:
        pick = customerslist.curselection()[0]
        pplList.pop(pick)
        List = []
        for person in pplList:
            List.append(f"{person[0]} {person[1]}")
        nameList.set(List)

def updateProgram():
    """
    This updates the program label in the main window
    """
    global swimming
    global hiking
    global canoeing
    global archery
    global drama
    
    swimming = 0
    hiking = 0
    canoeing = 0
    archery = 0
    drama = 0
    
    for person in pplList:
        if person[5] is True:
            swimming += 1
        if person[6] is True:
            hiking += 1
        if person[7] is True:
            canoeing += 1
        if person[8] is True:
            archery += 1
        if person[9] is True:
            drama += 1
    programVar.set(f"Swimming: {swimming}/50\nHiking: {hiking}/50\nCanoeing: {canoeing}/50\nArchery: {archery}/50\nDrama: {drama}/50")

def mainWindow():
    """
    This is the main window
    """
    global programVar
    global questionVar
    global answerVar
    global titleFont
    global img
    
    #main window
    rootOne = Tk()
    mainframeOne = Frame(rootOne)

    #font
    titleFont = Font(family = "Unicosmo Free", size = 60)

    #photo and title
    img = Image.open("bg.jpg")
    resize = img.resize((470,140))
    photo = ImageTk.PhotoImage(resize)
    title = Label(mainframeOne, text = "CAMP\nREGISTRATION", image = photo, compound = "center", font=titleFont, fg = "#fff")
    #title = Label(mainframeOne, image = photo)
    
    #service hours
    hoursFrame = LabelFrame(mainframeOne, text = "Service Hours")
    hours = Label(hoursFrame, text = f"Monday to Friday - 5:00am to 11:00pm\nSaturday to Sunday - 5:00am to 5:00pm")

    #contacts
    contactFrame = LabelFrame(mainframeOne, text = "Contact")
    contact = Label(contactFrame, text = f'Cell: (647) 648-6752\nEmail:1dongaly@hdsb.ca\nLocation: 2000 Candy Avenue, Oakville ',justify = LEFT)

    #buttons
    registerButton = Button(mainframeOne, text = "Register Customer", command = registerScreen)
    customerButton = Button(mainframeOne, text = "Customer List", command = customerList)

    #Programs
    programFrame = LabelFrame(mainframeOne, text = "Programs")
    programVar = StringVar()
    programVar.set("Swimming: 0/50\nHiking: 0/50\nCanoeing: 0/50\nArchery: 0/50\nDrama: 0/50")
    programLabel = Label(programFrame,textvariable = programVar, justify = LEFT)
    updateButton = Button(programFrame, text="Update", command = updateProgram)

    #inquiry box
    inquiryFrame = LabelFrame(mainframeOne, text = "Inquiry")
    questionLabel = Label(inquiryFrame, text = "Questions:")
    answerLabel = Label(inquiryFrame, text = "Reply: ")

    questionVar = StringVar()
    questionEntry = Entry(inquiryFrame, width = 50, textvariable = questionVar)

    answerVar = StringVar()
    answer = Label(inquiryFrame, width = 50, textvariable = answerVar)
    generateReply = Button(inquiryFrame, text = "Run", command = generate)

    inquiryFrame.grid(row = 5, column = 1, columnspan = 2, sticky = EW, pady = 5, padx = 10, ipady = 3)
    questionLabel.grid(row = 1, column = 1)
    answerLabel.grid(row = 2, column = 1)
    questionEntry.grid(row = 1, column = 2)
    answer.grid(row = 2, column = 2)
    generateReply.grid(row = 2, column = 3, padx = 5, sticky = E + S)
    
    #gridding
    mainframeOne.grid()
    title.grid(row = 1, column = 1, columnspan = 2, pady = 10)
    
    hoursFrame.grid(row = 2, column = 1, sticky = E + NS, padx= 10, rowspan = 2)
    hours.grid(row = 1, column = 1, sticky = W)

    contactFrame.grid(row = 4, column = 1, sticky = E + NS, padx = 10, pady = 5)
    contact.grid(row = 1, column = 1, ipady = 10)

    registerButton.grid(row = 2, column = 2, sticky = EW, padx = 10)
    customerButton.grid(row = 3, column = 2, sticky = EW, padx = 10)


    programFrame.grid(row = 4, column = 2, padx = 10, pady = 5, sticky = EW)
    programLabel.grid(row = 1, column = 1)
    
    updateButton.grid(row = 1, column = 2, sticky = S+E, ipadx=30, pady = 5)

    rootOne.mainloop()

def process(Input):
    """
    This function processes the input question
    """
    global answerVar
    global occurence
    global accuracy
    ignore = [",",".",";","?","!"]
    summ = 0

    words = Input.split()
    accuracy = []
    intent_num = len(intent)
    for dataNum in range(0, intent_num):
        occurence = 0
        total = 0
        for word in words:
            for symbol in range(0,len(ignore)-1): #ignore specific symbols
                word = word.replace(ignore[symbol], '')
            for SepString in range(0, len(intent[dataNum][0])):
                total += 1
                if word in intent[dataNum][0][SepString].split():
                    occurence += 1
                    summ += 1
        if total == 0:
            accuracy.append(0.0)
        else:
            accuracy.append((occurence/total)*100)
            #calculate percentage instead of number of occurences
    print(accuracy)
    if summ == 0:
        return "Sorry, I don't quite understand you 🧐"
    return accuracy.index(max(accuracy))
    
def generate():
    """
    This function generates the reply
    """
    global answerVar
    global date

    #updates date time
    date = datetime.now().strftime('%a, %d %b %Y, %I:%M%p')
    intent[5][1].pop(0)
    intent[5][1].append('👀 Today is ' + date)
    
    quest = questionVar.get().lower()
    accurate_response_num = process(quest)
    if isinstance(accurate_response_num, int):
        response_list = intent[accurate_response_num][1]
        pick = random.randint(0,len(response_list)-1)
        answerVar.set(response_list[pick])
    else:
        answerVar.set(accurate_response_num)

mainWindow()
