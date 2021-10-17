import whois, re ##pip install python-whois 
from tkinter import *

def isValidDomain(str):
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
    p = re.compile(regex)

    if (str == None):
        return False
    if (re.search(p, str)):
        return True
    else:
        return False

def availability(domain):
    try:
        w = whois.whois(domain)
        return False
    except:
        return True

def check():
    querysearch = E1.get()
    
    if isValidDomain(querysearch):
        if availability(querysearch):
            var.set(f"{querysearch} is available :)")
        else:
            var.set(f"{querysearch} is not available :(")
    else:
        var.set(f"{querysearch} is not a valid domain!")
    

top = Tk()
top.title("Domain Checker")

L1 = Label(top, text="Domain name: ")
L1.grid(row=0, column=0, padx=10, pady=20)

E1 = Entry(top, width=50)
E1.grid(row=0, column=1, padx=10, pady=20)

B1 = Button(top, text ="Check", command=check)
B1.grid(row=0, column=2, padx=10, pady=20)

var = StringVar()
Label(top, textvariable=var, width=40).grid(row=1, column=1)


top.geometry("500x100")
top.mainloop()