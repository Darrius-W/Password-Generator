import tkinter as tk
from tkinter import ttk
import logic


# New Window
window = tk.Tk()
window.title('Password Generator')
window.geometry("460x220")

# Styling
style = ttk.Style(window)
style.theme_use("clam")

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
baseFrame = ttk.LabelFrame(window)
baseFrame.pack(pady=10)



# Frame: Generate Password
generatorFrame = ttk.LabelFrame(baseFrame, padding=(15, 15))
generatorFrame.pack(fill="both", padx=10, pady=10)

# Button: Copy Password
copyBtn = ttk.Button(generatorFrame, text='Copy', command=lambda:logicObj.copyPwd())
copyBtn.pack(side=tk.LEFT, padx=2)

# Label: Display Password
pwdLabel = ttk.Label(generatorFrame, anchor=tk.CENTER, background='dark grey',
                    textvariable=pwdText, width=33)
pwdLabel.pack(side=tk.LEFT)

# Button: Generate New Password
refreshPwd = ttk.Button(master=generatorFrame, text="Generate",
                       command=lambda:logicObj.genPassword(pwdText, sliderPos.get(),
                                                           cUpper.get(), cLower.get(),
                                                           cDigits.get(), cPunc.get()))
refreshPwd.pack(side=tk.LEFT, padx=1)



# Frame: Length of Password
lengthFrame = ttk.LabelFrame(baseFrame)
lengthFrame.pack(fill=tk.BOTH, padx=10, pady=10)

# Label: Length Widget Header
lengthHdrLabel = ttk.Label(lengthFrame, text='Length:', padding=(5,))
lengthHdrLabel.pack(side=tk.LEFT, padx=12)

# Slider: Adjust length of Generated Password
lengthSlider = tk.Scale(lengthFrame, from_=1, to=32, orient='horizontal',
                        showvalue=True, length=180, variable=sliderPos)
lengthSlider.pack(side=tk.LEFT)



# Frame: Symbols Included in Password
symbolsFrame = ttk.LabelFrame(master=baseFrame)
symbolsFrame.pack(fill=tk.BOTH, padx=10, pady=10)

# Label: Symbols header label
symbolsHdrLabel = ttk.Label(master=symbolsFrame, text="Symbols:", padding=(1,))
symbolsHdrLabel.pack(side=tk.LEFT, padx=15)

# Checkboxes: Symbols to be Included in Password: Digits, Punctuation, Uppercase, Lowercawse
#Uppercase
upperCBox = ttk.Checkbutton(master=symbolsFrame, text="Uppercase",
                           variable=cUpper, onvalue=1, offvalue=0)
upperCBox.pack(side=tk.LEFT)
#Lowercase
lowerCBox = ttk.Checkbutton(master=symbolsFrame, text="Lowercase",
                           variable=cLower, onvalue=1, offvalue=0)
lowerCBox.pack(side=tk.LEFT)
#Digits
digitsCBox = ttk.Checkbutton(master=symbolsFrame, text="Digits",
                            variable=cDigits, onvalue=1, offvalue=0)
digitsCBox.pack(side=tk.LEFT)
#Punctuation
puncCBox = ttk.Checkbutton(master=symbolsFrame, text="Punctuation",
                          variable=cPunc, onvalue=1, offvalue=0)
puncCBox.pack(side=tk.LEFT)


# Execute Mainloop
window.mainloop()