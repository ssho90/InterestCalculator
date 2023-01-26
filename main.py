import tkinter as tk

root = tk.Tk()
root.title("이자 계산기")
root.geometry("250x300")



BojunggeumMoney = ""
junsaeIntRate = ""
junsaeAbleMoney = ""
sinyongIntMoney = ""
sinyongIntRate = ""

def calculate():
    print("totla Amount")

def bojung3Click():
    BojunggeumMoney = bojung2.get("1.0","end")
    junsaeAbleMoney = round(float(BojunggeumMoney)*0.8, 1)
    widget5.configure(state='normal')
    widget5.delete(1.0,"end")
    widget5.insert(1.0, junsaeAbleMoney)
    widget5.configure(state='disabled')

widget1 = tk.Label(    root,
    text="애옹이 이자 계산기",
    fg="white",
    bg="#34A2FE",
    width=40,
    height=2)
widget1.pack(side="top")

################################################################

lb1 = tk.Label(root, height=1)
lb1.pack(side="top")

bojung1 = tk.Label(lb1,
    text="보증금",
    fg="black",
    bg="white",
    width=10,
    height=1)
bojung1.pack(side="left")

bojung2 = tk.Text(lb1,
                  width=10,
                  height=1,
                  padx=1,
                  pady=1
                  )
bojung2.pack(side="left", padx="10")

bojung3 = tk.Button(lb1,
                    width=10,
                    height=1,
                    text="입력",
                    command=bojung3Click
                    )
bojung3.pack(side="left", padx="10")

################################################################

lb2 = tk.Label(root, height=1)
lb2.pack(side="top")

widget4 = tk.Label(lb2,
    text="전세대출금",
    fg="black",
    bg="white",
    width=10,
    height=1)
widget4.pack(side="left")

widget5 = tk.Text(lb2,
                  width=10,
                  height=1,
                  bg="white",
                  fg="black",
                  padx=1,
                  pady=1
                  )
widget5.configure(state='disabled')
widget5.pack(side="left", padx="10")


root.mainloop()

