import tkinter as tk
import logic


# New Window
window = tk.Tk()
window.title('Password Generator')

#Objects
logicObj = logic.Logic()

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
baseFrame = tk.LabelFrame(window,
                     padx=100,
                     pady=100,
                     bg='dark grey', text="Base Frame:")
baseFrame.pack(fill=tk.BOTH, padx=30, pady=30)



# Frame: Generate Password
generatorFrame = tk.LabelFrame(baseFrame, text="Generator Frame", padx=15, pady=15)
generatorFrame.pack()

# Button: Copy Password
copyBtn = tk.Button(generatorFrame, text='Copy', command=lambda:logicObj.copyPwd())
copyBtn.pack(side=tk.LEFT, padx=2)

# Label: Display Password
pwdLabel = tk.Label(generatorFrame, anchor=tk.CENTER, bg='dark grey',
                    textvariable=pwdText, width=33)
pwdLabel.pack(side=tk.LEFT)

# Button: Generate New Password
refreshPwd = tk.Button(master=generatorFrame,
                       text="Generate",
                       command=lambda:logicObj.genPassword(pwdText,
                                                           sliderPos.get(),
                                                           cUpper.get(),
                                                           cLower.get(),
                                                           cDigits.get(),
                                                           cPunc.get()))
refreshPwd.pack(side=tk.LEFT, padx=1)



# Frame: Length of Password
lengthFrame = tk.LabelFrame(master=baseFrame, height=100, width=500, text="Length Frame")
lengthFrame.pack(fill=tk.X)

# Label: Length Widget Header
lengthHdrLabel = tk.Label(master=lengthFrame, text='\nLength:')
lengthHdrLabel.pack(side=tk.LEFT)

# Slider: Adjust length of Generated Password
lengthSlider = tk.Scale(master=lengthFrame, from_=1, to=32, orient='horizontal', showvalue=True, length=150, variable=sliderPos)
lengthSlider.pack(side=tk.LEFT)


# Frame: Symbols Included in Password
symbolsFrame = tk.LabelFrame(master=baseFrame, height=100, width=500, text="Symbols Frame")
symbolsFrame.pack(fill=tk.X)

# Label: Symbols header label
symbolsHdrLabel = tk.Label(master=symbolsFrame, text="\nSymbols:")
symbolsHdrLabel.pack(side=tk.LEFT)

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