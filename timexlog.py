from datetime import datetime
import os
import os.path

def rem():
    output = "logs.txt"
    if os.path.exists(output):
        os.remove(output)
        
        
def logs(self):
    output = "logs.txt"
    checkFile = open(output, 'a')
    checkFile.write(str(self))
    checkFile.close()
    
    
timexstart = "Start details: " + str(datetime.today().strftime("%y/%m/%d|%H:%M:%S") + "\n")

timexstop = "Stop details: " + str(datetime.today().strftime("%y/%m/%d|%H:%M:%S") + "\n")