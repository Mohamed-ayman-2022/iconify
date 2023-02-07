# importing libraries and modules
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

#app geometry
app = Tk()
app.title("Iconify")
app.resizable(False,False)
app.iconbitmap("robo.ico")

def select_img():
    '''This function to select the image from your pc to convert it to icon'''
    try:
        global img
        global org_img
        global imageLabel

        imageFile = filedialog.askopenfilename(initialdir='res', title='Select image', 
                                            filetypes=(('ALL files','*.*'),('PNG files','*.png'),('JPG files','*.jpg'), 
                                                        ('ICON files','*.ico')))
        org_img = Image.open(imageFile)
        resized_img = org_img.resize((300,300), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(resized_img)
        imageLabel = Label(imageFrame, image=img)
        addLabel.destroy()
        imageLabel.pack()
        uploadBtn.configure(state="disable")
        for child in optionsFrame.winfo_children():
            child.configure(state='normal')
    except AttributeError:
        pass
    
def save_icon():
    '''this function to save the created icon'''
    try:
        global icon
        if len(iconNameE.get()) == 0:
            waringMsg= messagebox.showwarning("Warning", "Please, Enter Your Icon Name!")
            
        else:
            filedir= filedialog.asksaveasfilename(initialdir='res', title='Save icon', 
                                                filetypes=(('ICON files','*.ico'),('ALL files', '*.*')) , initialfile=f"{iconNameE.get()}.ico")
            icon = org_img.save(filedir, format='ICO', sizes=[(ico_size.get(), ico_size.get())])

            successMsg = messagebox.showinfo("Success", "Your Icon Is Created Successfully")
    except FileNotFoundError:
        errorMsg = messagebox.showerror("Error", "There is no folder chosen, please choose your directory")
        

def new_icon():
    '''this function for creating new icon'''
    global addLabel
    iconNameE.delete(0, END)
    ico_size.set(32)
    
    for child in optionsFrame.winfo_children():
        child.configure(state='disable')
        
    imageLabel.destroy()
    
    uploadBtn.configure(state='normal')
    addLabel = Label(imageFrame, text='Add Your Image')
    addLabel.pack(pady=140)
  
   
def close_app():
    '''this function to close the app by button'''
    app.destroy()


# App interface
appName = Label(app, text="iconify", font=('Tahoma', 40))
appName.pack()

describeL = Label(app, text="i c o n  c r e a t o r", font=('Tahoma', 15))
describeL.pack(pady=10)



# Main frame for image
mainFrame= Frame(app, width=400, height=400)
mainFrame.pack(side=LEFT)

imageFrame = LabelFrame(mainFrame, width=300, height=300)
imageFrame.pack(padx=20, pady=20)
imageFrame.pack_propagate(False)

addLabel = Label(imageFrame, text='Add Your Image')
addLabel.pack(pady=140)

uploadBtn = Button(mainFrame, text="Upload", width=10, height=1, command=select_img)
uploadBtn.pack(pady=15)

# Options frame

optionsFrame = LabelFrame(app, text="Icon Options")

nameLabel = Label(optionsFrame, text="Enter The Icon Name: ")
nameLabel.grid(row=0, column=0, padx=5, pady=5)
iconNameE = Entry(optionsFrame, width=20)
iconNameE.grid(row=0, column=1, padx=5, pady=5)

sizeL = Label(optionsFrame, text="Select Icon Size: ")
sizeL.grid(row=1, column=0, padx=5, pady=5) 

ico_size = IntVar()
sizesOptions = [16, 24, 32, 48, 64, 128, 255]
ico_size.set(32)
sizeMenu = OptionMenu(optionsFrame, ico_size, *sizesOptions)
sizeMenu.grid(row=1, column=1, padx=5, pady=5)

saveBtn = Button(optionsFrame, text="Get Your Icon", width=7, height=1, command=save_icon, padx=100)
saveBtn.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

newIconBtn = Button(optionsFrame, text="New Icon", width=7, height=1, command=new_icon, padx=100)
newIconBtn.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

endAppBtn = Button(app, text="End The Program", width=7, height=1, command=close_app, padx=100)
endAppBtn.pack(side=BOTTOM, padx=20, pady=20)

optionsFrame.pack(padx=20, pady=20)

for child in optionsFrame.winfo_children():
    child.configure(state='disable')

app.mainloop()