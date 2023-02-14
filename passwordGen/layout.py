import tkinter as ttk
import logic


# New Window
window = ttk.Tk()
window.title('Password Generator')
window.geometry("460x220")

#Objects
logicObj = logic.Logic()

# Set variables with default values
cDigits = ttk.IntVar()
cDigits.set(1)
cUpper = ttk.IntVar()
cUpper.set(1)
cLower = ttk.IntVar()
cLower.set(1)
cPunc = ttk.IntVar()
cPunc.set(1)
sliderPos = ttk.IntVar()
sliderPos.set(15)
pwdText = ttk.StringVar()
pwdText.set(logicObj.getPassword())


# Frame: Base frame to hold all other frames
baseFrame = ttk.LabelFrame(window)
baseFrame.pack(pady=10)



# Frame: Generate Password
generatorFrame = ttk.LabelFrame(baseFrame, padx=15, pady=15)
generatorFrame.pack(fill=ttk.BOTH, padx=10, pady=10)

# Button: Copy Password
copyBtn = ttk.Button(generatorFrame, text='Copy', command=lambda:logicObj.copyPwd())
copyBtn.pack(side=ttk.LEFT, padx=2)

# Label: Display Password
pwdLabel = ttk.Label(generatorFrame, anchor=ttk.CENTER, bg='dark grey',
                    textvariable=pwdText, width=33)
pwdLabel.pack(side=ttk.LEFT)

# Button: Generate New Password
refreshPwd = ttk.Button(master=generatorFrame, text="Generate",
                       command=lambda:logicObj.genPassword(pwdText, sliderPos.get(),
                                                           cUpper.get(), cLower.get(),
                                                           cDigits.get(), cPunc.get()))
refreshPwd.pack(side=ttk.LEFT, padx=1)



# Frame: Length of Password
lengthFrame = ttk.LabelFrame(baseFrame)
lengthFrame.pack(fill=ttk.BOTH, padx=10, pady=10)

# Label: Length Widget Header
lengthHdrLabel = ttk.Label(lengthFrame, text='Length:', padx=5)
lengthHdrLabel.pack(side=ttk.LEFT, padx=12)

# Slider: Adjust length of Generated Password
lengthSlider = ttk.Scale(lengthFrame, from_=1, to=32, orient='horizontal',
                        showvalue=True, length=180, variable=sliderPos)
lengthSlider.pack(side=ttk.LEFT)



# Frame: Symbols Included in Password
symbolsFrame = ttk.LabelFrame(master=baseFrame)
symbolsFrame.pack(fill=ttk.BOTH, padx=10, pady=10)

# Label: Symbols header label
symbolsHdrLabel = ttk.Label(master=symbolsFrame, text="Symbols:", padx=1)
symbolsHdrLabel.pack(side=ttk.LEFT, padx=15)

# Checkboxes: Symbols to be Included in Password: Digits, Punctuation, Uppercase, Lowercawse
#Uppercase
upperCBox = ttk.Checkbutton(master=symbolsFrame, text="Uppercase",
                           variable=cUpper, onvalue=1, offvalue=0)
upperCBox.pack(side=ttk.LEFT)
#Lowercase
lowerCBox = ttk.Checkbutton(master=symbolsFrame, text="Lowercase",
                           variable=cLower, onvalue=1, offvalue=0)
lowerCBox.pack(side=ttk.LEFT)
#Digits
digitsCBox = ttk.Checkbutton(master=symbolsFrame, text="Digits",
                            variable=cDigits, onvalue=1, offvalue=0)
digitsCBox.pack(side=ttk.LEFT)
#Punctuation
puncCBox = ttk.Checkbutton(master=symbolsFrame, text="Punctuation",
                          variable=cPunc, onvalue=1, offvalue=0)
puncCBox.pack(side=ttk.LEFT)


# Execute Mainloop
window.mainloop()