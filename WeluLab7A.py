#! /usr/bin/env python3

import tkinter
import re
import xml.etree.ElementTree as et
import xml.dom.minidom as xdm



class MKWindow:
    def __init__(self):
        # Create the main window, label, and adjust size.
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("Modify/Edit --- country.xml")
        self.mainWindow.geometry("300x250")

        # Create the entry fields for country, population, and continent, then label them.
        self.label0 = tkinter.Label(self.mainWindow, text="Country Name")
        self.wordEntry0 = tkinter.Entry(self.mainWindow)

        self.label1 = tkinter.Label(self.mainWindow, text="Population")
        self.wordEntry1 = tkinter.Entry(self.mainWindow)

        self.label2 = tkinter.Label(self.mainWindow, text="Continent")
        self.wordEntry2 = tkinter.Entry(self.mainWindow)

        # Create the Modify XML and Reset buttons.
        self.labelValue = tkinter.StringVar()
        self.labelValue.set("-")
        self.outputLabel = tkinter.Label(self.mainWindow, textvariable=self.labelValue)
        self.convertButton0 = tkinter.Button(self.mainWindow, text="Modify XML", command=self.modifyXML)
        self.convertButton1 = tkinter.Button(self.mainWindow, text="Reset", command=self.xReset)


        # Display the fields and buttons
        self.label0.pack()
        self.wordEntry0.pack()

        self.label1.pack()
        self.wordEntry1.pack()

        self.label2.pack()
        self.wordEntry2.pack()

        self.outputLabel.pack()
        self.convertButton0.pack()
        self.convertButton1.pack()


        # Start and display main window.
        tkinter.mainloop()


    # Define the two functions used to parse the string entered.
    def modifyXML(self):
        try:
            # Get the string value entered
            word0 = str(self.wordEntry0.get())
            word1 = float(self.wordEntry1.get())
            word2 = str(self.wordEntry2.get())

            # Trying to prevent an empty entry.
            # Any string entry could be taken though.
            # One could go crazy trying to prevent a bad entry.
            if word0 == "":
                raise TypeError
            if word2 == "":
                raise TypeError

            # Parse the selected XML file
            tree = et.parse('country.xml')
            root = tree.getroot() # get the nations element
            print(root)

            country0 = et.SubElement(root, 'country')

            name0 = et.SubElement(country0, 'name')
            name0.text = word0

            population0 = et.SubElement(country0, 'population')
            population0.text = str(word1)

            continent0 = et.SubElement(country0, 'continent')
            continent0.text = word2


            # Testing in IDLE to see my data
            et.dump(root)

            # Writing to file
            tree.write('country.xml')

            self.labelValue.set("XML sucessfully modified!")

            
        except:
            self.labelValue.set("Invalid Data Entry")



    # A function to clear the fields and parse result.
    def xReset(self):
        self.wordEntry0.delete(0, tkinter.END)
        self.wordEntry1.delete(0, tkinter.END)
        self.wordEntry2.delete(0, tkinter.END)
        self.labelValue.set("-")


        
# Run the program
myWindow = MKWindow()

