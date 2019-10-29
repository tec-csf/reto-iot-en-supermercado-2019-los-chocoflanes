from gpiozero import LED, Buzzer
from guizero import App, Box, Text, TextBox, warn
import csv

led8 = LED(19)

def clearDisplay():
    print("Clear display")
    rfidStatus.value = "---"
    rfidText.value = ""
    led8.off()
    rfidStatus.repeat(1000, checkRFidTag)

def checkRFidTag():
    tagId = rfidText.value
    if tagId != "":
        RFidRegistered = False
        print(tagId)
        with open("Database.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["RFid"] == tagId:
                    RFidRegistered = True
                    print("Welcome " + row["User"])
                    rfidStatus.value = "Welcome " + row["User"]
                    led8.on()
                    rfidStatus.after(5000, clearDisplay)
        
        if RFidRegistered == False:
            print("RFid tag is not registered")
            rfidStatus.value = "RFid tag is not registered"
            rfidStatus.after(3000, clearDisplay)
        
        rfidStatus.cancel(checkRFidTag)

app = App(title="RFID EM4100 Simple GUI", width=350, height=150, layout="auto")

instructionText = Text(app, text="Click on the text button below\nand scan your RFid tag.")
rfidText = TextBox(app)
rfidStatus = Text(app, text="---")
rfidStatus.repeat(1000, checkRFidTag)

app.display()