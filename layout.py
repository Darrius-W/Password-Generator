import tkinter as tk
import logic

#Objects
logicObj = logic.Logic()


# New Window
window = tk.Tk()
window.title('Password Generator')
window.resizable(False, False)


# Set variables with default values
cDigits = tk.IntVar()
cDigits.set(1)
cUpper = tk.IntVar()
cUpper.set(1)
cLower = tk.IntVar()
cLower.set(1)
cPunc = tk.IntVar()
cPunc.set(1)
sliderPos = tk.IntVar()
sliderPos.set(15)
pwdText = tk.StringVar()
pwdText.set(logicObj.getPassword())


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

# Label: Header
windowHdr = tk.Label(master=generatorFrame,
                     text='PASSWORD GENERATOR',
                     font='Helvetica 14 bold').pack(pady=5)

# Button: Copy Password
copyBtn = tk.Button(master=generatorFrame, text='Copy', command=lambda:logicObj.copyPwd())
copyBtn.pack(side=tk.LEFT)

# Label: Display Password
pwdLabel = tk.Label(master=generatorFrame,
                    width=32,
                    textvariable=pwdText,
                    bg='dark grey')
pwdLabel.pack(side=tk.LEFT)

# Button: Generate New Password
refreshPwd = tk.Button(master=generatorFrame, text="Generate", command=lambda:logicObj.genPassword(pwdText, sliderPos.get(), cUpper.get(), cLower.get(), cDigits.get(), cPunc.get()))
refreshPwd.pack(side=tk.LEFT)


# Frame: Header for Length of Password
lengthHdrFrame = tk.Frame(master=baseFrame, height=50, width=500)
lengthHdrFrame.pack(fill=tk.X)

# Label: Length Widget Header
lengthHdrLabel = tk.Label(master=lengthHdrFrame, text='\nLength:')
lengthHdrLabel.pack(side=tk.LEFT)


# Frame: Length of Password
lengthFrame = tk.Frame(master=baseFrame, height=100, width=500)
lengthFrame.pack(fill=tk.X)

# Slider: Adjust length of Generated Password
lengthSlider = tk.Scale(master=lengthFrame, from_=1, to=32, orient='horizontal', showvalue=True, length=150, variable=sliderPos)
lengthSlider.pack(side=tk.LEFT)


# Frame: Symbols Frame
symbolsHdrFrame = tk.Frame(master=baseFrame, height=50, width=500)
symbolsHdrFrame.pack(fill=tk.X)

# Label: Symbols header label
symbolsHdrLabel = tk.Label(master=symbolsHdrFrame, text="\nSymbols:")
symbolsHdrLabel.pack(side=tk.LEFT)


# Frame: Symbols Included in Password
symbolsFrame = tk.Frame(master=baseFrame, height=100, width=500)
symbolsFrame.pack(fill=tk.X)


# Checkboxes: Symbols to be Included in Password: Digits, Punctuation, Uppercase, Lowercawse
#Digits
digitsCBox = tk.Checkbutton(master=symbolsFrame, text="Digits", variable=cDigits, onvalue=1, offvalue=0)
digitsCBox.pack(side=tk.LEFT)
#Punctuation
puncCBox = tk.Checkbutton(master=symbolsFrame, text="Punctuation", variable=cPunc, onvalue=1, offvalue=0)
puncCBox.pack(side=tk.LEFT)
#Uppercase
upperCBox = tk.Checkbutton(master=symbolsFrame, text="Uppercase", variable=cUpper, onvalue=1, offvalue=0)
upperCBox.pack(side=tk.LEFT)
#Lowercase
lowerCBox = tk.Checkbutton(master=symbolsFrame, text="Lowercase", variable=cLower, onvalue=1, offvalue=0)
lowerCBox.pack(side=tk.LEFT)


# Execute Mainloop
window.mainloop()