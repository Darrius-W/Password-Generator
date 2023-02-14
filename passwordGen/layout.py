import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import logic


# New Window
window = tk.Tk()
window.title("Password Generator")
window.geometry("420x185")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


# Styling
style = ttk.Style(window)
style.theme_use("clam")
window.configure(background='grey')

# Objects
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

# Open Header image
image = Image.open('img/Lock.png')
img=image.resize((33, 33))
lockImg = ImageTk.PhotoImage(img)



# Frame: Base frame to hold all other frames
baseFrame = ttk.Frame(window)
#baseFrame.grid_rowconfigure(0, weight=1)
#baseFrame.grid_columnconfigure(0, weight=1)
baseFrame.place(relx=.5, rely=.5, anchor="center")
#baseFrame.grid()
#baseFrame.pack(expand=True, fill=tk.BOTH)



# Frame: Header Frame
hdrFrame = ttk.Frame(baseFrame)
hdrFrame.pack(fill=tk.BOTH, padx=75)

# Label: Lock image
imgLabel = ttk.Label(hdrFrame, image=lockImg)
imgLabel.pack(side=tk.LEFT)

# Label: Header
headerLabel = ttk.Label(hdrFrame, text='Password Generator',
                        font=("Helvetica", 17, "italic"),
                        padding=(0, 4)).pack(side=tk.LEFT, pady=3)



# Frame: Generate Password
generatorFrame = ttk.Frame(baseFrame, padding=(5, 5))
generatorFrame.pack(padx=10, pady=1, fill=tk.BOTH)

# Button: Copy Password
copyBtn = ttk.Button(generatorFrame, text='Copy', command=lambda:logicObj.copyPwd(), width=8)
copyBtn.pack(side=tk.LEFT, padx=2)

# Label: Display Password
pwdLabel = ttk.Label(generatorFrame, anchor=tk.CENTER, background='dark grey',
                    textvariable=pwdText, width=40)
pwdLabel.pack(side=tk.LEFT)

# Button: Generate New Password
refreshPwd = ttk.Button(master=generatorFrame, text="Generate", width=10,
                       command=lambda:logicObj.genPassword(pwdText, sliderPos.get(),
                                                           cUpper.get(), cLower.get(),
                                                           cDigits.get(), cPunc.get()))
refreshPwd.pack(side=tk.LEFT, padx=1)



# Frame: Length of Password
lengthFrame = ttk.Frame(baseFrame)
lengthFrame.pack(fill=tk.BOTH, padx=10, pady=10)

# Label: Length Widget Header
lengthHdrLabel = ttk.Label(lengthFrame, text='Length:', padding=(5,))
lengthHdrLabel.pack(side=tk.LEFT, padx=12)

# Slider: Adjust length of Generated Password
lengthSlider = ttk.Scale(lengthFrame, from_=1, to=32, orient='horizontal',
                        length=180, variable=sliderPos)
lengthSlider.pack(side=tk.LEFT)

# Entry: Manually input length
lengthEntry = ttk.Entry(lengthFrame, exportselection=0, textvariable=sliderPos, width=4)
lengthEntry.pack(side=tk.LEFT, padx=3)



# Frame: Symbols Included in Password
symbolsFrame = ttk.Frame(master=baseFrame)
symbolsFrame.pack(fill=tk.BOTH, padx=10, pady=13)

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