import tkinter as tk

root = tk.Tk()
root.title("이자 계산기")
root.geometry("350x300")



BojunggeumMoney = ""
junsaeIntRate = ""
junsaeAbleMoney = ""
sinyongIntMoney = ""
sinyongIntRate = ""

def calculate():
    print("totla Amount")

def bojung3Click():
    BojunggeumMoney = bojung2.get("1.0","end")
    junsaeAbleMoney = int(float(BojunggeumMoney)*0.8)
    jundae2.configure(state='normal')
    jundae2.delete("1.0", "end")
    jundae2.insert(1.0, junsaeAbleMoney)
    jundae2.configure(state='disabled')
    needCash2.configure(state='normal')
    needCash2.delete("1.0", "end")
    needCash2.insert(1.0, int(BojunggeumMoney)-junsaeAbleMoney)
    needCash2.configure(state='disabled')

###############################################################

widget1 = tk.Label(    root,
    text="애옹이 이자 계산기",
    fg="white",
    bg="#34A2FE",
    width=40,
    height=2)
widget1.pack(side="top")

################################################################

lb1 = tk.Label(root, height=1)
lb1.grid(row=0, column=0)

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
lb2.grid(row=1, column=0)

jundae1 = tk.Label(lb2,
    text="전세대출금",
    fg="black",
    bg="white",
    width=10,
    height=1)
jundae1.pack(side="left")

jundae2 = tk.Text(lb2,
                  width=10,
                  height=1,
                  bg="#D3D3D3",
                  fg="black",
                  padx=1,
                  pady=1
                  )
jundae2.configure(state='disabled')
jundae2.pack(side="left", padx="10")

################################################################


needCash1 = tk.Label(lb2,
    text="필요현금",
    fg="black",
    bg="white",
    width=10,
    height=1)
needCash1.pack(side="left")

needCash2 = tk.Text(lb2,
                  width=10,
                  height=1,
                  fg="black",
                  bg="#D3D3D3",
                  padx=1,
                  pady=1
                  )
needCash2.configure(state='disabled')
needCash2.pack(side="left", padx="10")

################################################################

lb4 = tk.Label(root, height=1)
lb4.grid(row=2, column=0)

jundaeInt1 = tk.Label(lb4,
    text="전세대출금리",
    fg="black",
    bg="white",
    width=10,
    height=1)
jundaeInt1.pack(side="left")

jundaeInt2 = tk.Text(lb4,
                  width=10,
                  height=1,
                  fg="black",
                  padx=1,
                  pady=1
                  )
jundaeInt2.pack(side="left", padx="10")

################################################################

lb5 = tk.Label(root, height=1)
lb5.grid(row=3, column=0)

sindaeModey1 = tk.Label(lb5,
    text="신용대출금",
    fg="black",
    bg="white",
    width=10,
    height=1)
sindaeModey1.pack(side="left")

sindaeModey2 = tk.Text(lb5,
                  width=10,
                  height=1,
                  fg="black",
                  padx=1,
                  pady=1
                  )
sindaeModey2.pack(side="left", padx="10")

################################################################

sindaeInt1 = tk.Label(lb5,
    text="신용대출금리",
    fg="black",
    bg="white",
    width=10,
    height=1)
sindaeInt1.pack(side="left")

sindaeInt2 = tk.Text(lb5,
                  width=10,
                  height=1,
                  fg="black",
                  padx=1,
                  pady=1
                  )
sindaeInt2.pack(side="left", padx="10")

root.mainloop()

