import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import logic


# New Window
window = tk.Tk()

# Load and set icon 
icon = Image.open('img\lock_icon.ico')
photo = ImageTk.PhotoImage(icon)
window.wm_iconphoto(False, photo)
window.title("Password Generator")

# Window configuration
window.geometry("420x185")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Styling
style = ttk.Style(window)
style.theme_use("clam")
window.configure(background='#dcdcd4')



# Objects
logicObj = logic.Logic()

# Initialize variables
cDigits = tk.IntVar()
cUpper = tk.IntVar()
cLower = tk.IntVar()
cPunc = tk.IntVar()
sliderPos = tk.IntVar()
dispLabel = tk.IntVar()
pwdText = tk.StringVar()

# Set variables with default values
cDigits.set(1)
cUpper.set(1)
cLower.set(1)
cPunc.set(1)
sliderPos.set(15)
dispLabel.set(sliderPos.get())
pwdText.set(logicObj.getPassword())



# Frame: Base frame to hold all other frames
baseFrame = ttk.LabelFrame(window, padding=(10,10,10,14))
baseFrame.place(relx=.5, rely=.5, anchor="center")



# Frame: Header Frame
hdrFrame = ttk.Frame(baseFrame)
hdrFrame.pack(fill=tk.BOTH, padx=75)

# Load Header image
image = Image.open('img/Lock.png')
img=image.resize((33, 33))
lockImg = ImageTk.PhotoImage(img)

# Label: Lock Header image
hdrImgLabel = ttk.Label(hdrFrame, image=lockImg)
hdrImgLabel.pack(side=tk.LEFT)

# Label: Header
headerLabel = ttk.Label(hdrFrame,
                        padding=(0, 4),
                        text='Password Generator',
                        font=("Helvetica", 17, "italic"))
headerLabel.pack(side=tk.LEFT, pady=3)



# Frame: Generate Password
generatorFrame = ttk.Frame(baseFrame, padding=(5, 5))
generatorFrame.pack(padx=10, pady=1, fill=tk.BOTH)

# Button: Copy Password
copyBtn = ttk.Button(generatorFrame,
                     width=8,
                     text='Copy',
                     command=lambda:logicObj.copyPwd())
copyBtn.pack(side=tk.LEFT, padx=2)

# Label: Display Password
pwdLabel = ttk.Label(generatorFrame,
                     width=40,
                     anchor=tk.CENTER,
                     background='white',
                    textvariable=pwdText)
pwdLabel.pack(side=tk.LEFT)

# Button: Generate New Password
refreshPwd = ttk.Button(generatorFrame,
                        width=10,
                        text="Generate",
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

# Scale: Adjust length of Generated Password
lengthSlider = ttk.Scale(lengthFrame,
                        from_=1,
                        to=32,
                        length=180,
                        orient='horizontal',
                        variable=sliderPos,
                        command=lambda x=None:logicObj.matchSlider(dispLabel, sliderPos))
lengthSlider.pack(side=tk.LEFT)

# Label: Display input length
lengthLabel = ttk.Label(lengthFrame, textvariable=dispLabel, font=15)
lengthLabel.pack(side=tk.LEFT, padx=3)



# Frame: Symbols Included in Password
symbolsFrame = ttk.Frame(baseFrame)
symbolsFrame.pack(fill=tk.BOTH, padx=10, pady=13)

# Label: Symbols header label
symbolsHdrLabel = ttk.Label(symbolsFrame, text="Symbols:", padding=(1,))
symbolsHdrLabel.pack(side=tk.LEFT, padx=15)

# Checkboxes: Symbols to be Included in Password: Digits, Punctuation, Uppercase, Lowercawse
#Uppercase
upperCBox = ttk.Checkbutton(symbolsFrame,
                            text="Uppercase",
                            variable=cUpper,
                            onvalue=1,
                            offvalue=0)
upperCBox.pack(side=tk.LEFT)

#Lowercase
lowerCBox = ttk.Checkbutton(symbolsFrame,
                            text="Lowercase",
                            variable=cLower,
                            onvalue=1,
                            offvalue=0)
lowerCBox.pack(side=tk.LEFT)

#Digits
digitsCBox = ttk.Checkbutton(symbolsFrame,
                            text="Digits",
                            variable=cDigits,
                            onvalue=1,
                            offvalue=0)
digitsCBox.pack(side=tk.LEFT)

#Punctuation
puncCBox = ttk.Checkbutton(symbolsFrame,
                           text="Punctuation",
                           variable=cPunc,
                           onvalue=1,
                           offvalue=0)
puncCBox.pack(side=tk.LEFT)


# Execute Mainloop
window.mainloop()