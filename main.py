import tkinter as tk
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

root = tk.Tk()
root.title("이자 계산기")
root.geometry("350x300")


BojunggeumMoney = ""
junsaeIntRate = ""
junsaeAbleMoney = ""
sinyongIntMoney = ""
sinyongIntRate = ""

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('cat.ico'))
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())

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

def totalClick():
    sindaeMoney = sindaeModey2.get("1.0","end")
    sindaeInt = sindaeInt2.get("1.0","end")
    jundae = jundae2.get("1.0","end")
    jundaeInt = jundaeInt2.get("1.0","end")

    sinyongIntMoney = round(float(sindaeMoney) * float(sindaeInt) / 100 / 12, 1)
    jundaeIntMoney = round(float(jundae) * float(jundaeInt) / 100 / 12, 1)
    totalIntMoney = sinyongIntMoney + jundaeIntMoney

    jundaeIntMoney2.delete("1.0", "end")
    jundaeIntMoney2.insert(1.0, jundaeIntMoney)

    sindaeIntMoney2.delete("1.0", "end")
    sindaeIntMoney2.insert(1.0, sinyongIntMoney)

    totalIntMoney2.delete("1.0", "end")
    totalIntMoney2.insert(1.0, totalIntMoney)

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

jundaeInt1 = tk.Label(lb2,
    text="전세대출금리",
    fg="black",
    bg="white",
    width=10,
    height=1)
jundaeInt1.pack(side="left")

jundaeInt2 = tk.Text(lb2,
                  width=10,
                  height=1,
                  fg="black",
                  padx=1,
                  pady=1
                  )
jundaeInt2.pack(side="left", padx="10")



################################################################

lb4 = tk.Label(root, height=1)
lb4.pack(side="top")

needCash1 = tk.Label(lb4,
    text="필요현금",
    fg="black",
    bg="white",
    width=10,
    height=1)
needCash1.pack(side="left")

needCash2 = tk.Text(lb4,
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

lb5 = tk.Label(root, height=1)
lb5.pack(side="top")

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

################################################################

lb99 = tk.Label(root, height=3, text="\n   ============== 한달에 이자 얼마? ==============   \n")
lb99.pack(side="top")

bojung3 = tk.Button(root,
                    width=10,
                    height=1,
                    text="click!",
                    command=totalClick
                    )
bojung3.pack(side="top", padx="10")

################################################################

lb6 = tk.Label(root, height=1)
lb6.pack(side="top")

jundaeIntMoney1 = tk.Label(lb6,
    text="전세대출이자",
    fg="black",
    bg="white",
    width=10,
    height=1)
jundaeIntMoney1.pack(side="left")

jundaeIntMoney2 = tk.Text(lb6,
                  width=10,
                  height=1,
                  fg="black",
                  padx=1,
                  pady=1
                  )
jundaeIntMoney2.pack(side="left", padx="10")

################################################################

sindaeIntMoney1 = tk.Label(lb6,
    text="신용대출이자",
    fg="black",
    bg="white",
    width=10,
    height=1)
sindaeIntMoney1.pack(side="left")

sindaeIntMoney2 = tk.Text(lb6,
                  width=10,
                  height=1,
                  fg="black",
                  padx=1,
                  pady=1
                  )
sindaeIntMoney2.pack(side="left", padx="10")

################################################################

lb7 = tk.Label(root, height=1)
lb7.pack(side="top")

totalIntMoney1 = tk.Label(lb7,
    text="총 이자",
    fg="black",
    bg="white",
    width=10,
    height=1)
totalIntMoney1.pack(side="left")

totalIntMoney2 = tk.Text(lb7,
                  width=10,
                  height=1,
                  fg="black",
                  bg="yellow",
                  padx=1,
                  pady=1
                  )
totalIntMoney2.pack(side="left", padx="10")

root.mainloop()

