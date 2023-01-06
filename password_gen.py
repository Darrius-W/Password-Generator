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

# Frame: Length of Password
# Label: Widget Header
# Slider: Adjust length of Generated Password
# Label: Hold Current Value of the Slider

# Frame: Symbols Included in Password
# Label: Widget Header
# Checkboxes: Symbols to be Included in Password

# Execute Mainloop
window.mainloop()