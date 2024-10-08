# coding=utf-8


#Angus Goody
#PyPassword 2.0
#02/06/17

#Main Init File

#===============================(IMPORTS)===============================
from tkinter import *
from tkinter import messagebox
import random
import os

from PEM import *
from PyUi import *

#===============================(WINDOW SETUP)===============================
window=Tk()
window.title("PyPassword 2")
window.geometry("500x400")
addUIWindow(window)
addPEMWindow(window)


#---Main Menu---
mainMenu=Menu(window)

fileMenu=Menu(mainMenu)
editMenu=Menu(mainMenu)
viewMenu=Menu(mainMenu)

#---Lock Screen Menu---
lockScreenMenu=Menu(window)

lockFileMenu=Menu(lockScreenMenu)

#--Status bar--
statusVar=StringVar()
statusBar=mainFrame(window)
statusBar.pack(fill=X,side=BOTTOM)
statusLabel=mainLabel(statusBar,textvariable=statusVar)
statusLabel.pack(expand=True)
statusBar.colour("#A9F955")



#===============================(VARIABLES/ARRAYS)===============================
currentDirectory=os.getcwd()
lockedScreens=[]
defaultColour=window.cget("bg")

mainGreenColour="#1BF293"
mainRedColour="#E6607A"
#Log
log=logClass("Main")


#===============================(USER INTERFACE)===============================

#-----Log Screen----
#region logscreen
logScreen=mainScreen(window,"Log",statusVar)

logNotebook=advancedNotebook(logScreen,select="#42f4bf")
logNotebook.pack(expand=True,fill=BOTH)

#Generate log views

for logName in logClass.allLogs:
	#Add tab to main notebook
	newFrame=mainFrame(logNotebook)
	logNotebook.addView(newFrame,logName)
	#Add new notebook on new frame
	newNotebook=advancedNotebook(newFrame,select="#3DCCAB")
	newNotebook.pack(expand=True,fill=BOTH)
	#Add the custom pages
	newNormalFrame=mainFrame(newNotebook)
	newSystemFrame=mainFrame(newNotebook)
	newNotebook.addView(newNormalFrame,"Default")
	newNotebook.addView(newSystemFrame,"System")

	#Add default info
	newNormalTree=ttk.Treeview(newNormalFrame)
	newNormalTree.pack(expand=True,fill=BOTH)
	logClass.allLogs[logName].addTree("Default",newNormalTree)
	#Add system info
	newSystemTree=ttk.Treeview(newSystemFrame)
	newSystemTree.pack(expand=True,fill=BOTH)
	logClass.allLogs[logName].addTree("System",newSystemTree)
	#Create headings for trees
	for tree in [newSystemTree,newNormalTree]:
		tree.config(columns=["Message","Time"],show="headings")
		newTreeScroll=Scrollbar(tree)
		newTreeScroll.pack(side=RIGHT,fill=Y)

		newTreeScroll.config(command=tree.yview)
		tree.config(yscrollcommand=newTreeScroll.set)

		tree.column("Message",width=10,minwidth=45)
		tree.column("Time",width=5,minwidth=20)

		tree.heading("Message",text="Message")
		tree.heading("Time",text="Time")



#endregion
#-----Open Screen----
# region open screen
openScreen=mainScreen(window,"PyPassword",statusVar,menu=lockScreenMenu)
lockedScreens.append(openScreen)
openScreen.show()

#--Top--
openTopVar=StringVar()
openTopVar.set("Select Pod Or Create New One")
openTopFrame=topStrip(openScreen,openTopVar)
openTopFrame.pack(side=TOP,fill=X)

#--Main--
openMainFrame=mainFrame(openScreen)
openMainFrame.pack(expand=True,fill=BOTH)

openMainListbox=advancedListbox(openMainFrame,font="Avenir 25")
openMainListbox.pack(expand=True,fill=BOTH)

#--Bottom--
openBottomFrame=mainFrame(openScreen)
openBottomFrame.pack(fill=X,side=BOTTOM)

openBottomButtonFrame=mainFrame(openBottomFrame)
openBottomButtonFrame.pack(expand=True)

openCreateFileButton=mainButton(openBottomButtonFrame,text="Create Master Pod",width=15)
openCreateFileButton.pack(side=LEFT,padx=5)
openSelectFileButton=mainButton(openBottomButtonFrame,text="Open Selected",width=15)
openSelectFileButton.pack(side=RIGHT,padx=5)

#Colour Section
openScreen.colour("#4A4D9C")

#endregion

#----Open Master Password Screen-----
#region master screen
openMasterScreen=mainScreen(window, "Master Password", statusVar,menu=lockScreenMenu)
lockedScreens.append(openMasterScreen)

openMasterDisplay=displayView(openMasterScreen)
openMasterDisplay.pack(expand=True,fill=BOTH)

#--Top Section--
openMasterTopFrame=centerFrame(openMasterDisplay)
openMasterSub=openMasterTopFrame.miniFrame

titleLabel(openMasterSub,text="File: ").pack(side=LEFT)
openMasterTopVar=StringVar()
openMasterTopVar.set("None")
titleLabel(openMasterSub,textvariable=openMasterTopVar).pack(side=RIGHT)

#--Main Section--
openMasterMainFrame=centerFrame(openMasterDisplay)
openMasterSub=openMasterMainFrame.miniFrame

mainLabel(openMasterSub,text="Enter password",font="Avenir 16").pack()
openMasterEntry=Entry(openMasterSub,show="•",justify=CENTER,width=25)
openMasterEntry.pack()

openHintVar=StringVar()
openHintVar.set("No Hint")
openHintLabel=mainLabel(openMasterSub,textvariable=openHintVar)
openHintLabel.pack()


#--Bottom Section--
openMasterBottomFrame=centerFrame(openMasterDisplay)
openMasterBottomSub=openMasterBottomFrame.miniFrame
"""
openMasterUnlockButton=mainButton(openMasterBottomSub,text="Unlock",width=12)
openMasterUnlockButton.pack(pady=5)
"""
openMasterUnlockButton=mainButton(openMasterBottomSub,text="Unlock",width=12)
openMasterUnlockButton.pack(pady=5)

openMasterCancelButton=mainButton(openMasterBottomSub,text="Cancel",width=12)
openMasterCancelButton.pack()

#--Add Views--
openMasterDisplay.addSection(openMasterTopFrame)
openMasterDisplay.addSection(openMasterMainFrame)
openMasterDisplay.addSection(openMasterBottomFrame)



#Colour Section
openMasterMainFrame.colour("#1877E0")
openMasterTopFrame.colour("#1360B4")
openMasterBottomFrame.colour("#1A86FB")
#endregion

#----Home screen-----
#region home screen
homeScreen=mainScreen(window,"Home",statusVar,menu=mainMenu)

#Top view

homeTopFrame=centerFrame(homeScreen)
homeTopFrame.pack(side=TOP,fill=BOTH)
homeTopLabelVar=StringVar()
homeTopLabel=topStrip(homeTopFrame,homeTopLabelVar)
homeTopLabel.pack(side=TOP,fill=X)

#Search Frame
homeSearchFrame=mainFrame(homeTopFrame)
homeSearchFrame.pack(fill=X)

homeSearchEntry=Entry(homeSearchFrame,justify=CENTER)
homeSearchEntry.pack(fill=X)

homeSearchVar=StringVar()
homeSearchVar.set("Results: 0")
homeSearchLabel=mainLabel(homeSearchFrame,textvariable=homeSearchVar,font="Helvetica 11")
homeSearchLabel.pack(padx=2)

#Main view
homeMainFrame=mainFrame(homeScreen)
homeMainFrame.pack(expand=True,fill=BOTH)

#Fake Notebook View
#todo fake notebook

homePodListbox=searchListbox(homeMainFrame)
homePodListbox.addSearchWidget(homeSearchEntry,resultVar=homeSearchVar)
homePodListbox.pack(expand=True,fill=BOTH)

#Bottom View
homeBottomFrame=centerFrame(homeScreen)
homeBottomFrame.pack(side=BOTTOM,fill=X)
homeBottomSub=homeBottomFrame.miniFrame

homeOpenPodButton=mainButton(homeBottomSub,text="Open Pod",width=9)
homeOpenPodButton.pack()

homeNewPodButton=mainButton(homeBottomSub,text="New Pod",width=9)
homeNewPodButton.pack(pady=5)

#Colour Section
homeScreen.colour("#9C2553")
#endregion

#---View Pod Screen---
#region viewPod screen
viewPodScreen=mainScreen(window,"Pod Info",statusVar)

#--Top Bar--
viewPodTopNameVar=StringVar()
viewPodTopFrame=topStrip(viewPodScreen,viewPodTopNameVar)
viewPodTopFrame.pack(side=TOP,fill=X)

#--Main Notebook--
viewPodNotebookFrame=mainFrame(viewPodScreen)
viewPodNotebookFrame.pack(expand=True,fill=BOTH)

#Notebook
viewPodNotebook=privateNotebook(viewPodNotebookFrame, select="#A9F955")
viewPodNotebook.pack(expand=True,fill=BOTH)
viewPodNotebook.loadTemplate("Login")


#--Bottom section--
viewPodBottomFrame=centerFrame(viewPodScreen)
viewPodBottomFrame.pack(side=BOTTOM,fill=X)
viewPodBottomSub=viewPodBottomFrame.miniFrame

#-Controller--
viewPodChangeController=multiView(viewPodBottomSub)
viewPodChangeController.pack(pady=2)
viewPodNotebook.multiViewInstance=viewPodChangeController

#Edit section
viewPodEditFrame=mainFrame(viewPodChangeController)
viewPodChangeController.addView(viewPodEditFrame,"Edit")
viewPodChangeController.showView("Edit")
viewPodEditButton=mainButton(viewPodEditFrame,text="Edit",width=9)
viewPodEditButton.pack(padx=5)

#Cancel Edit section
viewPodCancelEditSection=mainFrame(viewPodChangeController)
viewPodChangeController.addView(viewPodCancelEditSection,"Cancel")

viewPodCancelButton=mainButton(viewPodCancelEditSection,text="Cancel",width=9)
viewPodCancelButton.grid(row=0,column=0)

viewPodSaveButton=mainButton(viewPodCancelEditSection,text="Save",width=9)
viewPodSaveButton.grid(row=0,column=1)

#Delete Section
viewPodDeleteButton=mainButton(viewPodBottomSub,text="Delete",width=9)
viewPodDeleteButton.pack()

#Colour Section
viewPodScreen.colour("#4B5E9C")
#endregion

#--Generate Password Screen---
#region genPassword
genPasswordScreen=mainScreen(window,"Generate Password",statusVar)

genPasswordNotebook=advancedNotebook(genPasswordScreen,select="#CCEE2B")
genPasswordNotebook.pack(expand=True,fill=BOTH)

#--GenPassword Main---
genPasswordFrame=centerFrame(genPasswordNotebook)
genPasswordFrame.pack(expand=True,fill=BOTH)

genPasswordCenter=genPasswordFrame.miniFrame

#Entry
genPasswordEntry=labelEntry(genPasswordCenter,width=30,justify=CENTER,font="Arial 13")
genPasswordEntry.pack()

#Sliders

genPasswordLengthSlider=advancedSlider(genPasswordCenter,"Length",from_=5,to=50,value=random.randint(5,50))
genPasswordLengthSlider.pack(pady=6)

genPasswordSymbolSlider=advancedSlider(genPasswordCenter,"Symbols",from_=0,to=20,value=random.randint(0,20))
genPasswordSymbolSlider.pack(pady=6)

genPasswordDigitSlider=advancedSlider(genPasswordCenter,"Digits",from_=0,to=20,value=random.randint(0,20))
genPasswordDigitSlider.pack(pady=6)

#Buttons
genPasswordButtonFrame=mainFrame(genPasswordCenter)
genPasswordButtonFrame.pack(pady=15)

genPasswordCopyButton=mainButton(genPasswordButtonFrame,text="Copy",width=12)
genPasswordCopyButton.grid(row=0,column=0,padx=3)

genPasswordRegenerateButton=mainButton(genPasswordButtonFrame,text="Regenerate",width=12)
genPasswordRegenerateButton.grid(row=0,column=1,padx=3)


#--GenPassword Review---
genPasswordReviewFrame=mainFrame(genPasswordNotebook)

genPasswordReviewLabel=titleLabel(genPasswordReviewFrame, text="Password Review")
genPasswordReviewLabel.pack(pady=5)

genPasswordReviewEntry=labelEntry(genPasswordReviewFrame, width=30, justify=CENTER)
genPasswordReviewEntry.pack(pady=5)


genPasswordReviewTree=advancedTree(genPasswordReviewFrame, ["Field", "Report"])
genPasswordReviewTree.pack(expand=True, fill=BOTH)

genPasswordReviewTree.addSection("Field")
genPasswordReviewTree.addSection("Report")

genPasswordReviewTree.addTag("Pass", "#66CD84")
genPasswordReviewTree.addTag("Fail", "#CD426C")

genPasswordReviewBottomFrame=centerFrame(genPasswordReviewFrame)
genPasswordReviewBottomFrame.pack(side=BOTTOM, fill=X)
genPasswordReviewBottomSub=genPasswordReviewBottomFrame.miniFrame

genPasswordReviewCopyButton=mainButton(genPasswordReviewBottomSub, text="Copy", width=15)
genPasswordReviewCopyButton.pack()

#Add to notebook
genPasswordNotebook.addView(genPasswordFrame,"Generate")
genPasswordNotebook.addView(genPasswordReviewFrame, "Review")

#Colour Frames

#Closest match is #E7E7E7
genPasswordFrame.colour("#E7E7E7")
genPasswordReviewFrame.colour("#213380")
#endregion


#===============================(FUNCTIONS)===============================

#=========Screen Specific Functions=========

#region Screen Specific Functions

#=====MENU COMMANDS====

def goHome():
	"""
	The go home function returns to the home
	screen depending on what screen is loaded
	"""
	currentScreen=mainScreen.currentScreen
	if currentScreen in lockedScreens:
		openScreen.show()
	else:
		homeScreen.show()

def lockdown():
	"""
	The lockdown function is used
	to lock the master pod and return
	to the open file screen
	"""
	homePodListbox.fullClear()
	openMasterScreen.show()

#=====VIEW POD=========

def loadDataPod(selectedPod):
	"""
	The actual function that
	loads the right screen and displays pod info
	"""
	#Show screen
	viewPodScreen.show()
	#Set label at top of screen to master/data
	viewPodTopNameVar.set(str(masterPod.currentMasterPod.getRootName()) + " / " + str(selectedPod.podName))
	#Set Variable
	masterPod.currentMasterPod.currentPod=selectedPod

	#Add data to screen
	viewPodNotebook.loadDataPod(selectedPod)
	#Report to log
	log.report("Data pod opened")

def deletePod(selectedPod):
	"""
	This function will take a pod object
	as a parameter and then delete it from
	the program
	"""
	if selectedPod:
		#Ask user if they're sure
		confirm=askConfirm("Delete","Are you sure you wish to delete this pod?")
		if confirm:
			#Deletes the pod
			print("Ready to delete")
			currentMaster=masterPod.currentMasterPod
			if selectedPod.podName in currentMaster.podDict:
				#Remove the reference
				del currentMaster.podDict[selectedPod.podName]
				#Remove from listbox
				homePodListbox.removeItem(selectedPod.podName,False)
				#Save the data
				currentMaster.save()
				#Change the screen
				homeScreen.show()
				#Report to log
				log.report("Successfully deleted pod")

#=====OPEN SCREEN=======
def openMasterPod():
	"""
	This function is for when the user
	attempts to open a master pod file
	"""
	current=openMainListbox.getSelectedObject()
	if current != None:
		#Load screen to enter master password
		openMasterScreen.show()
		#Update top label
		openMasterTopVar.set(getBaseOfDirectory(current,"file"))
		masterPod.currentOpenFileName=current

		#Add the hint to the screen
		try:
			content=openPickle(current)
			openHintVar.set(content.masterHint)
		except:
			pass
	else:
		askMessage("Select","No Pod Selected")

def openOtherMasterPod():
	"""
	This function will open a master pod
	using the built in file explorer.
	"""
	directory=askForFile()
	if directory:
		base=os.path.basename(directory)
		if os.path.splitext(base)[0] in openMainListbox.get(0,END):
			askMessage("Already open","This pod is currently open")
			# todo reopen file
		else:
			addNewPod(directory)

def createNewMasterPodPopup():
	"""
	This function will run to launch a new 
	popup window to allow the user to create a new 
	master pod
	:return: 
	"""
	#Initiate a new TK window
	popupInfoVar=StringVar()
	newWindow=popUpWindow(window,"Create Master Pod",infoVar=popupInfoVar)

	#Add the frame view and ui elements
	popUpFrame=centerFrame(newWindow)
	popUpFrame.pack(expand=True)
	popUpSub=popUpFrame.miniFrame

	mainLabel(popUpSub,text="Enter Master Pod Name").pack()
	popUpEntry=Entry(popUpSub,width=20,justify=CENTER)
	popUpEntry.pack()

	mainLabel(popUpSub,text="Choose Password").pack()
	popUpPasswordEntry=Entry(popUpSub,width=20,justify=CENTER)
	popUpPasswordEntry.pack()

	mainLabel(popUpSub,text="Hint").pack()
	popupHintEntry=Entry(popUpSub,width=20,justify=CENTER)
	popupHintEntry.pack()

	mainLabel(popUpSub,textvariable=popupInfoVar,font="Helvetica 10").pack(side=BOTTOM)
	newWindow.addView(popUpSub)

	#Add bindings
	popUpEntry.bind("<KeyRelease>",lambda event,el=[popUpEntry,popUpPasswordEntry],
	                                      ds=masterPod,pi=newWindow: checkMasterPodDataValid(el,ds,newWindow))
	popUpPasswordEntry.bind("<KeyRelease>",lambda event, el=[popUpEntry,popUpPasswordEntry],
	                                      ds=masterPod,pi=newWindow: checkMasterPodDataValid(el,ds,newWindow))

	popupHintEntry.bind("<KeyRelease>",lambda event, el=[popUpEntry,popUpPasswordEntry],
	                                      ds=masterPod,pi=newWindow: checkMasterPodDataValid(el,ds,newWindow))

	#Disable button by default to avoid blank names and disable resizing
	newWindow.toggle("DISABLED")
	newWindow.resizable(width=False, height=False)

	#Add data sources and return values
	newWindow.addDataSource([popUpEntry,popUpPasswordEntry,popupHintEntry])
	newWindow.addRequiredFields([popUpEntry,popUpPasswordEntry])
	newWindow.addCommands([initiateMasterPod],True)

	#Run
	newWindow.run()

	#Add to log
	log.report("New popup launched","(POPUP)",tag="UI")

def initiateMasterPod(popupInstance):
	"""
	This function will create a new master pod
	with the input from the user using the popup instance
	as a parameter.
	"""
	data=popupInstance.gatheredData
	if len(data) >= 1:
		podName=data[0]
		podPassword=data[1]

		try:
			podHint=data[2]
		except:
			podHint="No Hint"

		#Create file name
		fileName=str(podName)
		if ".mp" not in fileName:
			fileName=fileName+".mp"
		newPod=masterPod(fileName)
		newPod.masterKey=podPassword
		if podHint != None and podHint != "":
			newPod.masterHint=podHint
		newPod.save()
		addNewPod(fileName)

#=====MASTER PASSWORD=======

def attemptUnlockMasterPod():
	"""
	This function will attempt
	to open the master pod. If succesfull
	it will load the data on screen.
	"""
	attempt=openMasterEntry.get()
	if len(attempt.split()) > 0:
		content=openPickle(masterPod.currentOpenFileName)
		if type(content) == masterPod:
			log.report("Valid pod loaded")
		else:
			log.report("Attempted to load invalid pod type")
		if content != None:
			#Attempt to open older master
			if unlockMasterPod(content,attempt):
				currentMasterPod=content
				#Update the key
				currentMasterPod.masterKey=attempt
				#Decrypt the pods
				currentMasterPod.decryptPods()
				#Load screen
				homeScreen.show()
				#Show Pods
				homePodListbox.addPodList(currentMasterPod.podDict)
				#Update top label
				homeTopLabelVar.set(currentMasterPod.getRootName()+" accounts")
				#Update variable
				masterPod.currentMasterPod=currentMasterPod

			else:
				askMessage("Incorrect","Incorrect Password")
		else:
			log.report("Error opening file with pickle",tag="Error")
			askMessage("Error","An error occurred opening the file")
	else:
		askMessage("Blank","Please Enter Something")

	#Clear entry
	insertEntry(openMasterEntry,"")

#=====HOME SCREEN=======

def loadSelectedDataPod():
	"""
	This is the function that runs when a data pod
	needs to be displayed onto the screen. It will
	show the screen and then add the pod data to it
	and updates any variables.
	"""

	#Find the pod the user selected
	selectedPod=homePodListbox.getSelectedObject()
	#Checks if a pod has actually been selected
	if selectedPod != None and selectedPod != False:
		loadDataPod(selectedPod)

def initiatePod(popupInstance):
	"""
	This is the function that runs
	when the user clicks the "Save" button
	on the popup screen when choosing a name
	"""
	data=popupInstance.gatheredData

	if len(data) > 0:
		single=data[0]
		template=data[1]
		#Create pod with that name
		pd=masterPod.currentMasterPod.addPod(single)
		if template in privateTemplate.templateList:
			pd.templateType=template
		#Add to listbox
		homePodListbox.addObject(single, pd)
		#Clear search
		insertEntry(homeSearchEntry,"")
		homePodListbox.search()
		#Save data
		masterPod.currentMasterPod.save()
		#Display the screen
		loadDataPod(pd)

def createNewPodPopup():

	"""
	This function creates a popup window
	that allows the user to enter a name
	for the pod
	"""

	#Will only run if a master pod has been loaded
	if masterPod.currentMasterPod != None:

		#Initiate a new TK window
		popupInfoVar=StringVar()
		newWindow=popUpWindow(window,"Create Pod",infoVar=popupInfoVar)

		#Add the frame view and ui elements
		popUpFrame=centerFrame(newWindow)
		popUpFrame.pack(expand=True)
		popUpSub=popUpFrame.miniFrame

		mainLabel(popUpSub,text="Enter Pod Name").pack()
		popUpEntry=Entry(popUpSub,width=20,justify=CENTER)
		popUpEntry.pack()
		popUpEntry.bind("<KeyRelease>", lambda event, ds=masterPod.currentMasterPod,
		                                      en=popUpEntry, ins=newWindow: checkPodNameValid(en, ds, ins))
		mainLabel(popUpSub,textvariable=popupInfoVar,font="Helvetica 10").pack(padx=9)
		newWindow.addView(popUpSub)

		#Area to select template

		mainLabel(popUpSub,text="Select Template").pack()

		selectedTemplate=StringVar()
		selectedTemplate.set("Login")
		selectTemplate=OptionMenu(popUpSub,selectedTemplate,*privateTemplate.templateList)
		selectTemplate.config(width=15)
		selectTemplate.pack()

		#Disable button by default to avoid blank names and disable resizing
		newWindow.toggle("DISABLED")
		newWindow.resizable(width=False, height=False)

		#Add data sources and return values
		newWindow.addDataSource([popUpEntry,selectedTemplate])
		newWindow.addRequiredFields([popUpEntry])
		newWindow.addCommands([initiatePod],True)

		#Run
		newWindow.run()

		#Add to log
		log.report("New popup launched","(POPUP)",tag="UI")

#=====GENERATE PASSWORD=======

def genPassword():
	"""
	This function takes the values of all the sliders
	and generates a password
	"""
	#Collect the data
	length=genPasswordLengthSlider.getValue()
	digits=genPasswordDigitSlider.getValue()
	symbols=genPasswordSymbolSlider.getValue()
	#Generate the password
	password=generatePassword(length,symbols,digits)
	#Calculate password strength
	strength=calculatePasswordStrength(password)
	if strength[0] == strength[2]:
		genPasswordEntry.changeColour("#A3EEA4")
		genPasswordEntry.updateLabel("Strong Password")
	elif (strength[0]/strength[2])*100 > 50:
		genPasswordEntry.changeColour("#ECD06D")
		genPasswordEntry.updateLabel("Medium Password")
	else:
		genPasswordEntry.changeColour("#EC95A7")
		genPasswordEntry.updateLabel("Weak Password")
	#Add the password to entry
	insertEntry(genPasswordEntry,password)
	#Review the password
	insertEntry(genPasswordReviewEntry, password)
	reviewPassword()

def reviewPassword():
	"""
	This function is used to review a password
	using the strength function and give feedback to the user
	"""
	#Collect data
	data=genPasswordReviewEntry.get()
	strength=calculatePasswordStrength(data)
	#Clear tree
	genPasswordReviewTree.delete(*genPasswordReviewTree.get_children())
	resultDict={True:"Incomplete",False:"Complete"}
	#Add data to tree
	for item in strength[3]:
		value=strength[3][item]
		#If good or bad
		tag="Fail"
		if value:
			tag="Fail"
		else:
			tag="Pass"
		genPasswordReviewTree.insertData((item, resultDict[value]), (tag))
	#Update label
	genPasswordReviewEntry.updateLabel(str(strength[0]) + "/" + str(strength[2]) + " complete")


#endregion

#=========Non Screen Specific Functions=========
#region Non Screen Specific

def loadFilesInDirectory():
	"""
	This function will scan the current directory
	of the python program to locate any pod files
	"""
	filesFound={}
	#Traverse current folder
	for root, dirs, files in os.walk(currentDirectory, topdown=False):
		for name in files:
			if name.endswith(".mp"):
				fileDirectory=(os.path.join(root, name))
				filesFound[name]=fileDirectory

	#Create Master Pods and display them
	for item in filesFound:
		rootName=os.path.splitext(item)[0]
		#Adds to listbox and removes extension
		openMainListbox.addObject(rootName,item)
		#Add name to class array
		if rootName not in masterPod.masterPodNames:
			masterPod.masterPodNames.append(rootName)

def checkPodNameValid(entry, dataSource, popupInstance):
	"""
	This function checks that the data
	entered in the "New Pod" entry is valid
	and is not empty or already a pod
	"""
	if type(dataSource) == masterPod:

		#First Check for actual data
		if len(entry.get().split()) < 1:
			popupInstance.changeEntryColour(mainRedColour)
			popupInstance.toggle("DISABLED")
			popupInstance.infoStringVar.set("Invalid Name (No data)")
			return False
		else:

			#Check by comparing upper cases
			for pod in dataSource.podDict:
				if pod.upper() == entry.get().upper():
					popupInstance.changeEntryColour(mainRedColour)
					popupInstance.toggle("DISABLED")
					popupInstance.infoStringVar.set("Invalid Name (Name taken)")
					return False

			else:
				popupInstance.changeEntryColour(mainGreenColour)
				popupInstance.toggle("NORMAL")
				popupInstance.infoStringVar.set("Valid Name")
				return True

def checkMasterPodDataValid(entryList,dataSource,popupInstance):
	"""
	Checks the validity of the user entering
	 a new master pod name.
	 *Note takes the new master pod name entry as index 0 in list*
	"""
	if type(dataSource) != None:
		valid=True

		#Check length of data first
		for entry in entryList:
			if len(entry.get().split()) < 1:
				valid=False
				popupInstance.changeEntryColour(mainRedColour)
				popupInstance.toggle("DISABLED")
				popupInstance.infoStringVar.set("Invalid Name (Empty Entry)")
				return False

		else:
			#Check if name is taken
			for name in masterPod.masterPodNames:
				if name.upper() == entryList[0].get().upper():
					valid=False
					popupInstance.changeEntryColour(mainRedColour)
					popupInstance.toggle("DISABLED")
					popupInstance.infoStringVar.set("Invalid Name (Name taken)")
					return False

			else:
				popupInstance.changeEntryColour(mainGreenColour)
				popupInstance.toggle("NORMAL")
				popupInstance.infoStringVar.set("Valid Name")
				return True

def addNewPod(location):
	openMainListbox.addObject(getBaseOfDirectory(location,"base"),location)

def loadReview():
	genPasswordScreen.show()
	#Show review tab
	genPasswordNotebook.showView("Review")

#endregion


#===============================(BUTTONS)===============================

#=====OPEN SCREEN=====
openSelectFileButton.config(command=openMasterPod)
openCreateFileButton.config(command=createNewMasterPodPopup)
#=====MASTER SCREEN=====
openMasterUnlockButton.config(command=attemptUnlockMasterPod)
openMasterCancelButton.config(command=lambda: openScreen.show())
#=====HOME SCREEN=====
homeOpenPodButton.config(command=loadSelectedDataPod)
homeNewPodButton.config(command=createNewPodPopup)
#=====VIEW POD=====
viewPodEditButton.config(command=lambda: viewPodNotebook.startEdit())
viewPodCancelButton.config(command=lambda: viewPodNotebook.cancelEdit())
viewPodSaveButton.config(command=lambda: viewPodNotebook.saveData())
viewPodDeleteButton.config(command=lambda: deletePod(masterPod.currentMasterPod.currentPod))

#=====GEN PASSWORD SCREEN=====
genPasswordRegenerateButton.config(command=genPassword)
genPasswordCopyButton.config(command=lambda e=genPasswordEntry:copyDataFromEntry(e))
genPasswordReviewCopyButton.config(command=lambda e=genPasswordReviewEntry:copyDataFromEntry(e))

#===============================(SLIDERS)===============================

#=====GEN PASSWORD SCREEN=====
genPasswordLengthSlider.addCommand(genPassword)
genPasswordSymbolSlider.addCommand(genPassword)
genPasswordDigitSlider.addCommand(genPassword)

#===============================(BINDINGS)===============================

#=====STATUS BAR=====
statusBar.addBinding("<Double-Button-1>",lambda event: goHome())

#=====OPEN SCREEN=====
openMainListbox.bind("<Double-Button-1>", lambda event: openMasterPod())
openMainListbox.bind("<Return>", lambda event: openMasterPod())

#=====MASTER SCREEN=====
openMasterEntry.bind("<Return>", lambda event: attemptUnlockMasterPod())

#=====HOME SCREEN=====
homePodListbox.bind("<Double-Button-1>", lambda event: loadSelectedDataPod())

#=====GEN PASSWORD SCREEN=====
genPasswordReviewEntry.entry.bind("<KeyRelease>", lambda event: reviewPassword())
#===============================(MENU CASCADES)===============================
mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_cascade(label="Edit",menu=editMenu)
mainMenu.add_cascade(label="View",menu=viewMenu)

lockScreenMenu.add_cascade(label="File",menu=lockFileMenu)

#==File==
fileMenu.add_command(label="Home",command=homeScreen.show)
fileMenu.add_command(label="Generate Password",command=genPasswordScreen.show)
fileMenu.add_command(label="Review Password",command=loadReview)


fileMenu.add_separator()
fileMenu.add_command(label="Save Data", command=lambda: masterPod.currentMasterPod.save())
fileMenu.add_command(label="Exit Master Pod",command=lockdown)

lockFileMenu.add_command(label="Open Other",command=openOtherMasterPod)

#==View==
viewMenu.add_command(label="Show Log",command=lambda: logScreen.show())


#===============================(INITIALISER)===============================
loadFilesInDirectory()
genPassword()
#===============================(TESTING AREA)===============================

#===============================(END)===============================
window.mainloop()