from tkinter import *
from tkinter import ttk

players = []

# 1. open .csv file
# 2. read all lines and extract necessary information (salary and first + last name)
# 3. safe this information in an array
# 4. write a function to search in this array by player name and return salary, value and difference
# 5. make if fAncYY

# - salary: 1
# - last name: 13
# - first name: 14
# - value: 179
# - valuation Difference: 180

# player {
#   lastName
#   fistName
#   salary
#   value
#   valuationDifference
# }
def extractInfo(row):
    columns = row.split(',')

    if(len(columns) <= 1):
        return

    print(len(columns))

    lastName = columns[13].lower()
    firstName = columns[14].lower()
    salary = int(columns[1])
    value = int(float(columns[179]))
    valuationDifference = int(float(columns[180]))
    player = dict(lastName = lastName, firstName = firstName, salary = salary, value = value, valuationDifference = valuationDifference)
    players.append(player)

def findPlayer(firstName, lastName):
    firstName = firstName.lower()
    lastName = lastName.lower()
    for i in range(0, len(players)):
        player = players[i]
        if(player["firstName"] == firstName and player["lastName"] == lastName):
            return player
    return -1

f = open("./nhl_final.csv","r")
frows = f.readlines()

for i in range(1, len(frows)):
    extractInfo(frows[i])

f.close()

salaryLabel = None
valueLabel = None
valueDifferenceLabel = None

# Get rid of old data
def destroyLabel(label):
    if label is not None:
        label.destroy()

def getSalary():
    global salaryLabel
    global valueLabel
    global valueDifferenceLabel

    destroyLabel(salaryLabel)
    destroyLabel(valueLabel)
    destroyLabel(valueDifferenceLabel)

    inputText = entry.get().strip()
    splitName = inputText.split(" ") 
    player = findPlayer(splitName[0], splitName[1])

    salaryLabel = Label(win, text="Salary: " + str(player["salary"]), font= ('Century 15 bold')) 
    salaryLabel.pack(pady=20)

    valueLabel = Label(win, text="Value: " + str(player["value"]), font= ('Century 15 bold')) 
    valueLabel.pack(pady=20)

    valueDifferenceLabel = Label(win, text="Value Difference: " + str(player["valuationDifference"]), font= ('Century 15 bold')) 
    valueDifferenceLabel.pack(pady=20)

win= Tk()

#Create an Entry Widget
entry= ttk.Entry(win,font=('Century 12'),width=40)
entry.pack(pady= 30)

#Set the geometry of tkinter frame
win.geometry("750x350")

#Create a button to display the text of entry widget
button= ttk.Button(win, text="Enter", command= getSalary)
button.pack()

win.mainloop()