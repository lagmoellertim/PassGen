import hashlib
from tkinter import *
id = 1
num = 25
standart_salt = "timluca16485"
standart_length = "18"
def generate(event=None):
    global e1,e2,main,id,salt,e3,e4
    small_letters = list('abcdefghijklmnopqrstuvwxyz')
    big_letters = list('ABCDEFGHJKLMNPQRTUVWXYZ')
    numbers = list('0123456789')
    special_characters = list('#!"§$%&/()[]{}=-_+*<>;:.')
    password_characters = small_letters + big_letters + numbers + special_characters
    def convert_bytes_to_password(hashed_bytes, length):
        number = int.from_bytes(bytes(hashed_bytes), byteorder='big')
        password = ''
        while number > 0 and len(password) < length:
            password = password + password_characters[number % len(password_characters)]
            number = number // len(password_characters)
        return password
    s = {10:"(",11:")",12:"[",13:"]",14:"{",15:"}",16:"?",17:"!",18:"$",19:"%",20:"&",21:"/",22:"=",23:"*",24:"+",25:"~",26:",",27:".",28:";",29:":",30:"<",31:">",32:"-",33:"_"}
    url = str(e1.get()).lower()
    try:
        url = url.split("//")[1]
    except:
        pass
    url = url.replace("www.","")
    url = url.split("/")[0]
    url = url.split("?")[0].encode("utf-8")
    password = str(e2.get()).encode("utf-8")
    curl = str(hashlib.sha512(password+str(hashlib.sha384(url).hexdigest()).encode("utf-8")).hexdigest())+str(hashlib.sha512(str(hashlib.sha384(url+password).hexdigest()).encode("utf-8")).hexdigest())
    curl2 = hashlib.sha512(url+password+str(curl).encode("utf-8")).hexdigest()
    cb = str(curl2 * num)
    cb1 = cb+str(url)[2:-1]+str(password)[2:-1]
    curl1 = hashlib.sha512(cb1.encode("utf-8")).hexdigest()
    main.clipboard_clear()
    m = curl1
    counter = 1
    st = ""
    for x in m:
        if x.isnumeric():
            st += x
        else:
            if counter % 3 == 0:
                st += x.upper()
            else:
                st += x.lower()
        counter += 1
    for x,y in s.items():
        st = str(st).replace(str(x),y)
    salt = str(id)+":"+str(e3.get().encode("utf-8"))[2:-1]
    f = convert_bytes_to_password(str(str(hashlib.sha512(str(st+":="+str(salt)).encode("utf-8")).hexdigest())*num).encode("utf-8"), int(str(e4.get().encode("utf-8"))[2:-1]))
    main.clipboard_append(f)
def insert(event=None):
    global e1,main
    try:
        e1.delete(0,END)
        inp = str(main.clipboard_get())
        try:
            inp = inp.split("//")[1]
        except:
            pass
        inp = inp.replace("www.","")
        inp = inp.split("/")[0]
        inp = inp.split("?")[0]
        e1.insert(0,inp)
    except:
        pass
def clear(event=None):
    global main
    main.clipboard_append("")
    main.clipboard_clear()
main = Tk()
main.resizable(width=FALSE, height=FALSE)
main.wm_title("PassGen")
l1 = Label(main,text="URL")
e1 = Entry(main, width=36)
l2 = Label(main,text="Master-Passwort")
e2 = Entry(main,show="*", width=36)
l3 = Label(main,text="Salt")
e3 = Entry(main,width=36)
l4 = Label(main,text="Passwort-Länge")
e4 = Entry(main,width=36)
b2 = Button(main,text="In Zwischenablage kopieren",command=generate, width=30)
b1 = Button(main,text="von Zwischenablage einfügen",command=insert, width=30)
b3 = Button(main,text="Zwischenablage leeren",command=clear, width=30)
l1.pack()
e1.pack()
e1.bind("<Return>", generate)
b1.bind("<Return>", insert)
b1.pack()
l2.pack()
e2.pack()
e2.bind("<Return>", generate)
e3.insert(0,standart_salt)
e3.bind("<Return>", generate)
l3.pack()
e3.pack()
l4.pack()
e4.insert(0,standart_length)
e4.bind("<Return>", generate)
e4.pack()
b2.bind("<Return>", generate)
b2.pack()
b3.bind("<Return>", clear)
b3.pack()
main.mainloop()
