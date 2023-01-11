import tkinter as tk

# Event Handlers

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
                          width=500,
                          bg='green')
generatorFrame.pack(fill=tk.X)

# Button: Copy Password
copyBtn = tk.Button(master=generatorFrame, text='Copy')
copyBtn.pack(side=tk.LEFT)

# Label: Display Password
pwdLabel = tk.Label(master=generatorFrame,
                    width=20,
                    text='.............................',
                    bg='yellow')
pwdLabel.pack(side=tk.LEFT)
# Button: Generate New Password
refreshPwd = tk.Button(master=generatorFrame, text="Refresh")
refreshPwd.pack(side=tk.LEFT)

# Frame: Length of Password
lengthFrame = tk.Frame(master=baseFrame, height=100, width=500)
lengthFrame.pack(fill=tk.X)

# Label: Widget Header
lengthLabel = tk.Label(master=lengthFrame, text='\nLength:\n')
lengthLabel.pack(side=tk.LEFT)
# Slider: Adjust length of Generated Password
lengthSlider = tk.Scale(master=lengthFrame, from_=0, to=50, orient='horizontal')
lengthSlider.pack(side=tk.LEFT)
# Entry: Hold Current Value of the Slider, and manually input length value
manLengthEntry = tk.Entry(master=lengthFrame, width=4)
manLengthEntry.pack(side=tk.LEFT)


# Frame: Symbols Included in Password
# Label: Widget Header
# Checkboxes: Symbols to be Included in Password

# Execute Mainloop
window.mainloop()