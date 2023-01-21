import tkinter as tk
import string
import secrets

# All possible symbols
digits = string.digits
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
punc = string.punctuation


# Event Handlers
# Generate Password
def genPassword():
    # Call symbol function to see which symbol lists to use
    includedSyms = includedSymbols()
    if includedSyms == '': randomPwd = 'Need to select Symbols!'  
    else:
        # Call length function to get length to use
        genLength = getLength()
        # Using requested symbols & length, generate password
        secretsGen = secrets.SystemRandom()
        randomPwd = str()
        for vals in range(genLength): 
            randomPwd += secretsGen.choice(includedSyms)
             
    # Send generated password to display function
    displayPwd(randomPwd)

# Display Password
def displayPwd(pwd):
    pwdLabel['text'] = pwd
# Copy Password
# Get Password Length
def getLength():
    sliderLength = sliderPos.get()
    return sliderLength
# Confirm included symbols 
def includedSymbols():
    syms = str()
    # Check what symbols are marked
    # Create super list based on what symbols are checked
    if cDigits.get() == 1: syms += digits
    if cUpper.get() == 1: syms += uppercase
    if cLower.get() == 1: syms += lowercase
    if cPunc.get() == 1: syms += punc
    # Pass super list to genPassword
    return syms


# New Window
window = tk.Tk()
window.title('Password Generator')
window.resizable(False, False)

# Frame: Base frame to hold all other frames
baseFrame = tk.Frame(master=window,
                     height=300,
                     width=500,
                     bg='dark grey')
baseFrame.pack(fill=tk.BOTH)


# Frame: Generate Password
generatorFrame = tk.Frame(master=baseFrame,
                          height=100,
                          width=500)
generatorFrame.pack(fill=tk.X)

# Button: Copy Password
copyBtn = tk.Button(master=generatorFrame, text='Copy')
copyBtn.pack(side=tk.LEFT)

# Label: Display Password
pwdLabel = tk.Label(master=generatorFrame,
                    width=20,
                    text='.............................',
                    bg='dark grey')
pwdLabel.pack(side=tk.LEFT)

# Button: Generate New Password
refreshPwd = tk.Button(master=generatorFrame, text="Refresh", command=genPassword)
refreshPwd.pack(side=tk.LEFT)


# Frame: Header for Length of Password
lengthHdrFrame = tk.Frame(master=baseFrame, height=50, width=500)
lengthHdrFrame.pack(fill=tk.X)

# Label: Widget Header
lengthHdrLabel = tk.Label(master=lengthHdrFrame, text='\nLength:')
lengthHdrLabel.pack(side=tk.LEFT)


# Frame: Length of Password
lengthFrame = tk.Frame(master=baseFrame, height=100, width=500)
lengthFrame.pack(fill=tk.X)

# Slider: Adjust length of Generated Password
sliderPos = tk.IntVar()
lengthSlider = tk.Scale(master=lengthFrame, from_=0, to=50, orient='horizontal', showvalue=True, variable=sliderPos, length=150)
lengthSlider.pack(side=tk.LEFT)


# Frame: Symbols Header
symbolsHdrFrame = tk.Frame(master=baseFrame, height=50, width=500)
symbolsHdrFrame.pack(fill=tk.X)

# Label: Symbols header label
symbolsHdrLabel = tk.Label(master=symbolsHdrFrame, text="\nSymbols:")
symbolsHdrLabel.pack(side=tk.LEFT)


# Frame: Symbols Included in Password
symbolsFrame = tk.Frame(master=baseFrame, height=100, width=500)
symbolsFrame.pack(fill=tk.X)


# Checked variables
cDigits = tk.IntVar()
cUpper = tk.IntVar()
cLower = tk.IntVar()
cPunc = tk.IntVar()

# Checkboxes: Symbols to be Included in Password: Digits, Punctuation, Uppercase, Lowercawse
#Digits
digitsCBox = tk.Checkbutton(master=symbolsFrame, text="Digits", variable=cDigits)
digitsCBox.pack(side=tk.LEFT)
#Punctuation
puncCBox = tk.Checkbutton(master=symbolsFrame, text="Punctuation", variable=cPunc)
puncCBox.pack(side=tk.LEFT)
#Uppercase
upperCBox = tk.Checkbutton(master=symbolsFrame, text="Uppercase", variable=cUpper)
upperCBox.pack(side=tk.LEFT)
#Lowercase
lowerCBox = tk.Checkbutton(master=symbolsFrame, text="Lowercase", variable=cLower)
lowerCBox.pack(side=tk.LEFT)


# Execute Mainloop
window.mainloop()