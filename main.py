#--------------------------------------importing the classes and mondule-----------------------#
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#-------------------------Password Generator-----------------------------------#
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)

    pyperclip.copy(password)



#-------------------------------------------save the data in text file-----------#
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="opps" , message="please dont leave the any entry empty")
    else:

        is_ok=messagebox.askokcancel(title=website   ,message=f"These are the details they entered\n {email} \n {password}\n is it okk to save this")

        if is_ok :
            with open("data.text","a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n ")
                website_entry.delete(0,END)
                password_entry.delete(0,END)


window=Tk()

window.title("Password Manager")
window.config(padx=20,pady=20)
#----------------------puttin the image logo in the window-------------------------------------------#
canvas=Canvas(window, width=200,height=200)
my_logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=my_logo)
canvas.grid(row=0, column=1)
#------------------------creating the label-----------------------------------#
website_label=Label(window, text="Website :" )
website_label.grid(row=1,column=0)
email_label=Label(window,text="Email/Username :")
email_label.grid(row=2,column=0)
password_label=Label(window,text="Password :")
password_label.grid(row=3,column=0)
#----------------------------------------creating the entry field-----------------------------------#
website_entry=Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0,"gymboyabhinav1234@gmail.com")
password_entry=Entry(width=30)
password_entry.grid(row=3 ,column=1)
#---------------------------------------------creating the button--------------------------------------#
generatepassword=Button(text="Generate Password", command=generate_password)
generatepassword.grid(row=3, column=2)
add_button=Button(text="Add",width=36 ,command=save)
add_button.grid(row=4,column=1,columnspan=2)

















window.mainloop()







# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #