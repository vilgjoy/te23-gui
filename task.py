import datetime
from tkinter import *


def korrekt_personnummer():
    personummer = entry.get().replace("-", "")
    resultatlabel.config(text="")

    
    if len(personummer) == 12:
        århundrade = personummer[:2]
        personummer = personummer[2:]
    else:
        århundrade = "19"

    
    if len(personummer) != 10 or not personummer.isdigit():
        resultatlabel.config(text="Fel personnummer. Måste vara 10 siffror", fg="red")
        return

   
    try:
        år = int(århundrade + personummer[:2])
        månad = int(personummer[2:4])
        dag = int(personummer[4:6])
        datetime.date(år, månad, dag)
    except ValueError:
        resultatlabel.config(text="Ogiltigt personnummer - Ogiltigt datum", fg="red")
        return

    
    siffror = [int(siffra) for siffra in personummer]
    for i in range(9):
        if i % 2 == 0:
            siffror[i] *= 2
            if siffror[i] > 9:
                siffror[i] -= 9
    
    total_summa = sum(siffror)
    if total_summa % 10 == 0:
        resultatlabel.config(text="Personnumret är giltigt", fg="green")
    else:
        resultatlabel.config(text="Personnumret är ogiltigt, försök igen.", fg="red")


root = Tk()
root.title("Personnummer validator")
root.geometry("400x200")

Label(root, text="Ange ditt personnummer (YYYYMMDD-XXXX):").pack(pady=10)

entry = Entry(root, width=30)
entry.pack(pady=5)

Button(root, text="Validera", command=korrekt_personnummer).pack(pady=10)

resultatlabel = Label(root, text="")
resultatlabel.pack(pady=10)

Button(root, text="Avsluta", command=root.destroy).pack(pady=5)

root.mainloop()

