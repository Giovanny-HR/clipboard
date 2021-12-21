import win32clipboard as clip
import time

old = '' # If old == data it doesn't to be copied

def saveClipboardFile():
    fQuestion =  input("Folder Name: ")
    newFileQUestion = fQuestion + ".txt"
    # f = open(newFileQUestion, "a+")
    # f.write("Now the file has more content!")
    # f.close()
# saveClipboardFile()



saveFile = saveClipboardFile()
while True:  # Clipboard Data
    clip.OpenClipboard() #
    data = clip.GetClipboardData() #
    clip.CloseClipboard() #
    if old != data: #
        with open(saveFile, 'a+') as f: #
            f.write(data + '\n') #
        old = data
    time.sleep(0.5) # Save clipboard

'''
Track copy url
if tracking succesful 
    print Copied!
Print Status
'''
