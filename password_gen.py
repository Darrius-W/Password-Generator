import tkinter as tk

# Event Handlers

# New Window
window = tk.Tk()
window.title('Password Generator')
window.resizable(False, False)
window.geometry('500x300')
# Frame: Base frame to hold all other frames

# Frame: Generate Password
# Button: Copy Password
# Label: Display Password
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