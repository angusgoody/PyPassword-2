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

from PyUi import *
from PEM import *

#===============================(WINDOW SETUP)===============================
window=Tk()
window.title("PyPassword 2")
window.geometry("400x300")

#---Main Menu---
mainMenu=Menu(window)

fileMenu=Menu(mainMenu)
editMenu=Menu(mainMenu)
viewMenu=Menu(mainMenu)

#---Lock Screen Menu---
lockScreenMenu=Menu(window)

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
#Log
log=logClass("Main")
#===============================(USER INTERFACE)===============================

#-----Log Screen----
#region logscreen
logScreen=mainScreen(window,"Log",statusVar)
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

openMainListbox=advancedListbox(openMainFrame,font="serif 19")
openMainListbox.pack(expand=True,fill=BOTH)

#--Bottom--
openBottomFrame=mainFrame(openScreen)
openBottomFrame.pack(fill=X,side=BOTTOM)

openBottomButtonFrame=mainFrame(openBottomFrame)
openBottomButtonFrame.pack(expand=True)

openCreateFileButton=mainButton(openBottomButtonFrame,text="Create Master Pod",width=12)
openCreateFileButton.pack(side=LEFT,padx=5)
openSelectFileButton=mainButton(openBottomButtonFrame,text="Open Selected",width=12)
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

mainLabel(openMasterSub,text="Enter password").pack()
openMasterEntry=Entry(openMasterSub,show="•",justify=CENTER)
openMasterEntry.pack()

#--Bottom Section--
openMasterBottomFrame=centerFrame(openMasterDisplay)
openMasterBottomSub=openMasterBottomFrame.miniFrame

openMasterUnlockButton=Button(openMasterBottomSub,text="Unlock",width=12)
openMasterUnlockButton.pack(pady=5)
openMasterCancelButton=Button(openMasterBottomSub,text="Cancel",width=12)
openMasterCancelButton.pack()

#--Add Views--
openMasterDisplay.addSection(openMasterTopFrame)
openMasterDisplay.addSection(openMasterMainFrame)
openMasterDisplay.addSection(openMasterBottomFrame)

openMasterDisplay.showSections()


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
homeTopLabel=titleLabel(homeTopFrame,textvariable=homeTopLabelVar)
homeTopLabel.pack(expand=True)
#Main view
homeMainFrame=mainFrame(homeScreen)
homeMainFrame.pack(expand=True,fill=BOTH)

homePodListbox=advancedListbox(homeMainFrame,font="Arial 18")
homePodListbox.pack(expand=True,fill=BOTH)

#Bottom View
homeBottomFrame=centerFrame(homeScreen)
homeBottomFrame.pack(side=BOTTOM,fill=X)
homeBottomSub=homeBottomFrame.miniFrame

homeOpenPodButton=Button(homeBottomSub,text="Open Pod",width=9)
homeOpenPodButton.pack()

homeNewPodButton=Button(homeBottomSub,text="New Pod",width=9)
homeNewPodButton.pack(pady=5)

#Colour Section
homeScreen.colour("#9C2553")
#endregion

#---View Pod Screen---
#region viewPod screen
viewPodScreen=mainScreen(window,"Pod Info",statusVar)

#--Top Bar--
viewPodTopFrame=centerFrame(viewPodScreen)
viewPodTopFrame.pack(side=TOP,fill=X)
viewPodTopSub=viewPodTopFrame.miniFrame
viewPodTopNameVar=StringVar()
titleLabel(viewPodTopSub,textvariable=viewPodTopNameVar).pack()

#--Main Notebook--
viewPodNotebookFrame=mainFrame(viewPodScreen)
viewPodNotebookFrame.pack(expand=True,fill=BOTH)
viewPodNotebook=ttk.Notebook(viewPodNotebookFrame)
viewPodNotebook.pack(expand=True,fill=BOTH)

#Basic info
viewPodBasicSection=passwordDisplayView(viewPodNotebook)
viewPodBasicSection.createSections(["Title","Username","Password"],["#1188D7","#0F74B7","#0D68A4","#2B6198"])
viewPodBasicSection.showSections()
#Advanced info
viewPodAdvancedSection=displayView(viewPodNotebook)

#Add pages
viewPodNotebook.add(viewPodBasicSection,text="Basic")
viewPodNotebook.add(viewPodAdvancedSection,text="Advanced")

#--Bottom section--
viewPodBottomFrame=centerFrame(viewPodScreen)
viewPodBottomFrame.pack(side=BOTTOM,fill=X)
viewPodBottomSub=viewPodBottomFrame.miniFrame

#-Controller--
viewPodChangeController=multiView(viewPodBottomSub)
viewPodChangeController.pack(pady=2)

#Edit section
viewPodEditFrame=mainFrame(viewPodChangeController)
viewPodChangeController.addView(viewPodEditFrame)
viewPodChangeController.showView(viewPodEditFrame)
viewPodEditButton=Button(viewPodEditFrame,text="Edit",width=9)
viewPodEditButton.pack(padx=5)

#Cancel Edit section
viewPodCancelEditSection=mainFrame(viewPodChangeController)
viewPodChangeController.addView(viewPodCancelEditSection)
viewPodCancelButton=Button(viewPodCancelEditSection,text="Cancel",width=9)
viewPodCancelButton.grid(row=0,column=0)

viewPodSaveButton=Button(viewPodCancelEditSection,text="Save",width=9)
viewPodSaveButton.grid(row=0,column=1)

#Delete Section
viewPodDeleteButton=Button(viewPodBottomSub,text="Delete",width=9)
viewPodDeleteButton.pack()

#Colour Section
viewPodScreen.colour("#4B5E9C")
#endregion

#===============================(FUNCTIONS)===============================

#=========Utility Functions=========
"""
Utility Functions are handy little
functions that help reduce the amount
of code needed.
"""
def insertEntry(entry,message):
	entry.delete(0,END)
	entry.insert(END,message)

def askMessage(pre,message):
	try:
		messagebox.showinfo(pre,message)
	except:
		print(message)

def askFirst(pre,message,command):
	try:
		response=messagebox.askokcancel(pre,message)
	except:
		return False
	else:
		if response:
			command()
		return response

#=========Program Functions=========


#=====Screen Loaders====
"""
These functions will load different screens
when they run. They will execute different commands
as well as load screens
"""

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
	masterPod.currentDataPod=selectedPod
	#Add data to screen
	addBasicPodDataToScreen(selectedPod, viewPodBasicSection)

def getSelectedDataPod():
	"""
	This is the function that runs when a data pod
	needs to be displayed onto the screen. It will
	show the screen and then add the pod data to it
	and updates any variables.
	"""

	#Find the pod the user selected
	selectedPod=homePodListbox.getSelected()
	#Checks if a pod has actually been selected
	if selectedPod != None and selectedPod != False:
		loadDataPod(selectedPod)


def openMasterPod():
	"""
	This function is for when the user
	attempts to open a master pod file
	"""
	current=openMainListbox.getSelected()
	if current != None:
		#Load screen to enter master password
		openMasterScreen.show()
		openMasterTopVar.set(current.getRootName())
		#Load master pod
		masterPod.currentMasterPod=current

	else:
		askMessage("Select","No Pod Selected")

#=====Button Commands====
"""
These commands are fucntions 
that are linked to a button pressed
"""
def unlockMasterPod():
	attempt=openMasterEntry.get()
	if len(attempt.split()) > 0:
		currentMasterPod=masterPod.currentMasterPod

		#Attempt to unlock
		response=currentMasterPod.unlock(attempt)
		if response != None and response != False:
			log.report("Unlock success","(Unlock)",tag="Login")
			#Load screen
			homeScreen.show()
			#Show Pods
			homePodListbox.addPodList(response)
			#Update top label
			homeTopLabelVar.set(currentMasterPod.getRootName()+" accounts")
			#Update variable
			masterPod.currentMasterPod=currentMasterPod
		else:
			askMessage("Incorrect","Password Incorrect")
	else:
		askMessage("Blank","Please Enter Something")

	#Clear entry
	insertEntry(openMasterEntry,"")

def addBasicPodDataToScreen(podInstance, basicDisplayInstance):
	"""
	This function will take a pod and display
	the data
	"""
	if type(basicDisplayInstance) == passwordDisplayView:

		#Clear screen first
		basicDisplayInstance.clearScreen()

		#Get basic pod info
		podVault=podInstance.getVault()
		podTitle=podInstance.podName

		#Add all the data in the vault to screen

		#If the vault itself does not contain title it uses the pod title
		if "Title" not in podVault:
			basicDisplayInstance.sectionDict["Title"].addData(podTitle)

		#Iterate through all data in the pod
		for item in podVault:
			if item in basicDisplayInstance.sectionDict:
				#Add to the correct entry
				basicDisplayInstance.sectionDict[item].addData(podVault[item])

#=====Initialiser Commands====

def loadFilesInDirectory():
	"""
	This function will scan the current directory
	of the python program to locate any pod files
	"""
	filesFound=[]
	#Traverse current folder
	for root, dirs, files in os.walk(currentDirectory, topdown=False):
		for name in files:
			if name.endswith(".mp"):
				filesFound.append(name)

	#Create Master Pods and display them
	for item in filesFound:
		pod=masterPod(item)
		#Adds to listbox and removes extension
		openMainListbox.addItem(os.path.splitext(item)[0],pod)

#=====QUICK RUN Loaders====
"""
Quick run commands are commands
that usually run very quickly and are 
binded to keystrokes etc. They include
search functions while the user is typing
"""
def checkNameValid(entry,dataSource,popupInstance):
	"""
	This function takes the name currently in
	the entry and will check the data source to see
	if the name is taken. If it is the entry will turn
	red and toggle the popup instance button. If not it will turn green
	and return True
	"""
	if type(dataSource) == masterPod:

		#First Check for actual data
		if len(entry.get().split()) < 1:
			entry.config(bg="salmon")
			popupInstance.toggle("DISABLED")
			popupInstance.infoStringVar.set("Invalid Name")
			return False
		else:

			#Check by comparing upper cases
			for pod in dataSource.podDict:
				if pod.upper() == entry.get().upper():
					entry.config(bg="salmon")
					popupInstance.toggle("DISABLED")
					popupInstance.infoStringVar.set("Invalid Name")
					return False

			else:
				entry.config(bg="light green")
				popupInstance.toggle("NORMAL")
				popupInstance.infoStringVar.set("Valid Name")
				return True

#=====Other Commands====

def beginEdit(displayViewList):
	"""
	The begin Edit function is called
	when the user selects to Edit the data
	in the data pod
	"""
	#Show correct view
	viewPodChangeController.showView(viewPodCancelEditSection)

	for display in displayViewList:
		#Change states of Entry
		for sectionTitle in display.sectionDict:
			display.sectionDict[sectionTitle].enableEditing()

def cancelEdit(displayViewList):
	"""
	The begin Edit function is called
	if the user decides to cancel ediing
	the pod data
	"""
	#Show correct view
	viewPodChangeController.showView(viewPodEditFrame)

	for display in displayViewList:

		#Change states of Entry
		for sectionTitle in display.sectionDict:
			hiddenSection=display.sectionDict[sectionTitle]
			#Check to see if data has been modified
			if hiddenSection.getData() != hiddenSection.data.get():
				#Change back to original
				hiddenSection.restoreData()
			hiddenSection.disableEditing()

def overwritePodData(displayViewList):
	"""
	This function will take the data from the
	pods on screen and update the old data
	then save the data to file.
	
	It takes parameter of display view to
	get the data from screen
	"""
	updated=False
	for display in displayViewList:
		for section in display.sectionDict:
			hiddenSection=display.sectionDict[section]
			#Compares saved data to data on screen
			if hiddenSection.getData() != hiddenSection.data.get():
				oldData=hiddenSection.data.get()
				newData=hiddenSection.getData()
				sectionTitle=hiddenSection.title
				#Update the stored data for the display
				hiddenSection.updateData()
				#Update the pod data
				masterPod.currentDataPod.updateVault(sectionTitle,newData)
				if sectionTitle == "Title":
					#Update listbox
					homePodListbox.updateItemLabel(oldData,newData)
				#Update Var
				updated=True

	if updated == False:
		askMessage("No changes","No data was changed")
	else:
		log.report("Saved data successfully","(Saved)")
		#Save to file
		masterPod.currentMasterPod.save()
		#Return to original screen
		cancelEdit(displayViewList)

def deletePod(podInstance):
	rsp=askFirst("Sure","Are you sure you wish to delete this pod?",lambda: masterPod.currentMasterPod.deletePod(podInstance.podName,True))
	#Carry out other tasks such as changing screen and removing from listbox
	if rsp:
		viewPodBasicSection.clearScreen()
		homePodListbox.removeItem(podInstance.podName,False)
		homeScreen.show()




#=====POPUP COMMANDS====
"""
Popup commands are all the commands associated
with the popup windows and the functions that are run when the
user clicks "Save" etc
"""
def initiatePod(popupInstance):
	"""
	This is the function that runs
	when the user clicks the "Save" button
	on the popup screen when choosing a name
	"""
	data=popupInstance.gatheredData

	if len(data) > 0:
		single=data[0]
		#Create pod with that name
		pd=masterPod.currentMasterPod.addPod(single)
		#Add to listbox
		homePodListbox.addItem(single,pd)
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
		popUpEntry=Entry(popUpFrame,width=20,justify=CENTER)
		popUpEntry.pack()
		popUpEntry.bind("<KeyRelease>",lambda event, ds=masterPod.currentMasterPod,
		                                      en=popUpEntry, ins=newWindow: checkNameValid(en,ds,ins))
		mainLabel(popUpSub,textvariable=popupInfoVar,font="Helvetica 10").pack(side=BOTTOM)
		newWindow.addView(popUpSub)

		#Disable button by default to avoid blank names and disable resizing
		newWindow.toggle("DISABLED")
		newWindow.resizable(width=False, height=False)

		#Add data sources and return values
		newWindow.addDataSource([popUpEntry])
		newWindow.addCommands([initiatePod],True)

		#Run
		newWindow.run()

		#Add to log
		log.report("New popup launched","(POPUP)",tag="UI")


#===============================(BUTTONS)===============================

#=====OPEN SCREEN=====
openSelectFileButton.config(command=openMasterPod)
#=====MASTER SCREEN=====
openMasterUnlockButton.config(command=unlockMasterPod)
openMasterCancelButton.config(command=lambda: openScreen.show())
#=====HOME SCREEN=====
homeOpenPodButton.config(command=getSelectedDataPod)
homeNewPodButton.config(command=createNewPodPopup)
#=====VIEW POD=====
viewPodEditButton.config(command=lambda:beginEdit([viewPodBasicSection]))
viewPodCancelButton.config(command=lambda:cancelEdit([viewPodBasicSection]))
viewPodSaveButton.config(command=lambda: overwritePodData([viewPodBasicSection]))
viewPodDeleteButton.config(command=lambda: deletePod(masterPod.currentDataPod))
#===============================(BINDINGS)===============================

#=====STATUS BAR=====
statusBar.addBinding("<Double-Button-1>",lambda event: goHome())
#=====OPEN SCREEN=====
openMainListbox.bind("<Double-Button-1>", lambda event: openMasterPod())
openMainListbox.bind("<Return>", lambda event: openMasterPod())
#=====MASTER SCREEN=====
openMasterEntry.bind("<Return>", lambda event: unlockMasterPod())
#=====HOME SCREEN=====
homePodListbox.bind("<Double-Button-1>", lambda event: getSelectedDataPod())
#===============================(MENU CASCADES)===============================
mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_cascade(label="Edit",menu=editMenu)
mainMenu.add_cascade(label="View",menu=viewMenu)

#==File==
fileMenu.add_command(label="Lock Master Pod",command=lockdown)
fileMenu.add_command(label="Save Data", command=lambda: masterPod.currentMasterPod.save())

#==View==
viewMenu.add_command(label="Show Log",command=lambda: logScreen.show())


#===============================(INITIALISER)===============================
loadFilesInDirectory()
#===============================(TESTING AREA)===============================

#===============================(END)===============================
window.mainloop()