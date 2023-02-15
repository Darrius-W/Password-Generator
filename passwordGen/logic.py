import string
import secrets
import pyperclip

class Logic:
    pwd = '*********************'
    length = 0
    symbols = None

    # Set Password Length
    def setLength(self, sliderPos):
        self.length = sliderPos
        
    # Set included symbols 
    def setIncludedSymbols(self, upperVal, lowerVal, digitVal, puncVal):
        # All possible symbols
        digits = string.digits
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        punc = string.punctuation
        
        # clear symbols string
        self.symbols = ''
        
        if upperVal == 1: self.symbols += upper#uppercase symbols
        if lowerVal == 1: self.symbols += lower#lowercase symbols
        if digitVal == 1: self.symbols += digits#digit symbols
        if puncVal == 1: self.symbols += punc#punc symbols
    
    # Generate password
    def genPassword(self, pwdText, sliderPos, upperVal, lowerVal, digitVal, puncVal):
        # clear current password
        self.pwd = ''
        
        # secrets object
        secretsObj = secrets.SystemRandom()
        
        # set Length
        self.setLength(sliderPos)
        
        # set Symbols
        self.setIncludedSymbols(upperVal, lowerVal, digitVal, puncVal)
        
        # if no symbols checked
        if self.symbols == '': self.pwd = 'Need to select Symbols!'
        
        # symbols are checked
        else:
            count = 1
            while(count <= self.length):
                count+=1
                self.pwd += secretsObj.choice(self.symbols)    
                
        pwdText.set(self.getPassword())        
    
    # Get password
    def getPassword(self):
        return self.pwd
    
    # Copy password
    def copyPwd(self):
        pyperclip.copy(self.pwd)
        
    # Set sliderPos to val of manEntry when val entered
    def focus(self, manEntry, sliderPos):
        num = int(sliderPos.get())
        manEntry.set(num)