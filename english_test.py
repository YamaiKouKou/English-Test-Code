import json
import random
import tkinter as tk

class App(tk.Tk):
    count = 0
    correctcount = 0
    answer = []
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("English Vocabulary Book")
        self.geometry("500x500")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.dic = []
        self.problems = []
        #-------------frame(メニュー画面)-----------------
        self.mainframe = tk.Frame()
        self.mainframe.grid(row=0, column=0, sticky="snew")

        self.mainlabel = tk.Label(self.mainframe, text="英単語帳", font=('Helvetica', '30'))
        self.mainlabel.pack(anchor='center', pady=20)

        self.oboerubutton = tk.Button(self.mainframe, text="単語を覚える")
        self.oboerubutton.pack(side='left', padx=50)
        
        self.testbutton = tk.Button(self.mainframe, text="テストを始める", command=self.StartProblem)
        self.testbutton.pack(side='left', padx=50)

        self.rirekibutton = tk.Button(self.mainframe, text="テスト履歴")
        self.rirekibutton.pack(side='left', padx=40)
        #------------frame1(問題画面)---------------
        self.frame1 = tk.Frame()
        self.frame1.grid(row=0, column=0, sticky="snew")
        
        self.label1 = tk.Label(self.frame1, text="")
        self.label1.pack(anchor='center', pady=10)

        self.AnsEntry = tk.Entry(self.frame1)
        self.AnsEntry.pack(anchor='center', pady=20)
        
        self.button1 = tk.Button(self.frame1, text="次の問題へ", command=self.changeproblem)
        self.button1.pack(anchor='center', pady=20)

        self.back_button = tk.Button(self.frame1, text="テストを途中終了する", command=lambda:self.Changepage(self.mainframe))
        self.back_button.pack(anchor='center', pady=100)
        #---------------resultframe(テスト結果照会画面)------------------------
        self.resultframe = tk.Frame()
        self.resultframe.grid(row=0, column=0, sticky="snew")

        self.resultlabel = tk.Label(self.resultframe, text="結果発表!")
        self.resultlabel.pack(anchor='center', pady=20)

        self.seikaisuulabel = tk.Label(self.resultframe, text="")
        self.seikaisuulabel.pack(anchor='center', pady=20)

        self.resulttestbutton = tk.Button(self.resultframe, text="結果分析", command=lambda:self.Changepage(self.testresultframe))
        self.resulttestbutton.pack(anchor='center')

        self.MenuButton = tk.Button(self.resultframe, text="メインメニューへ", command=lambda:self.Changepage(self.mainframe))
        self.MenuButton.pack(anchor='center', pady=100)
        #---------------testresultframe(テスト結果分析画面)----------------------------------------
        self.testresultframe = tk.Frame()
        self.testresultframe.grid(row=0, column=0, sticky="snew")
        #--------------------------------------------------------------------------------------------
        self.mainframe.tkraise()
        self.mainloop()

    def makeproblem(self):
        with open('./EnglishInformation/Information.json', 'r', encoding='utf-8') as f:
            d = json.load(f)
            testdict = d["AboutTest"]
            return testdict

    def changeproblem(self):
        self.count += 1
        self.label1['text']="問" + str(self.count+1) + "：" + self.problems[self.dic[self.count]]["JaSentence"]

        self.answer.append(self.AnsEntry.get())
        if self.answer[self.count-1].lower() == self.problems[self.dic[self.count-1]]["Answer"]:
            self.correctcount += 1
        elif self.answer[self.count-1] == " ":
            self.answer[self.count-1] = "未回答"

        self.AnsEntry.delete(0, tk.END)
        
        if self.count == 9:
            self.button1['text'] = "問題を終了する"
            self.button1['command'] = self.ResultTest
        
    def Changepage(self, page):
        page.tkraise()

    def StartProblem(self):
        self.frame1.tkraise()
        self.dic = self.makerandomdic()
        self.problems = self.makeproblem()
        
        self.label1['text'] = "問1：" + self.problems[self.dic[0]]["JaSentence"]
        
    def ResultTest(self):
        self.resultframe.tkraise()

        self.answer.append(self.AnsEntry.get())
        if self.answer[self.count-1].lower() == self.problems[self.dic[self.count-1]]["Answer"]:
            self.correctcount += 1
        
        self.count += 1
        
        self.seikaisuulabel['text'] = str(self.correctcount) + " / " + str(self.count)
        #問1
        self.anslabel1 = tk.Label(self.testresultframe, text="問1の解答:" + self.problems[self.dic[0]]["Answer"] + "　　　問1のあなたの解答:" + self.answer[0])
        self.anslabel1.pack()
        #問2
        self.anslabel2 = tk.Label(self.testresultframe, text="問2の解答:" + self.problems[self.dic[1]]["Answer"] + "　　　問2のあなたの解答:" + self.answer[1])
        self.anslabel2.pack()
        #問3
        self.anslabel3 = tk.Label(self.testresultframe, text="問3の解答:" + self.problems[self.dic[2]]["Answer"] + "　　　問3のあなたの解答:" + self.answer[2])
        self.anslabel3.pack()
        #問4
        self.anslabel4 = tk.Label(self.testresultframe, text="問4の解答:" + self.problems[self.dic[3]]["Answer"] + "　　　問4のあなたの解答:" + self.answer[3])
        self.anslabel4.pack()
        #問5
        self.anslabel5 = tk.Label(self.testresultframe, text="問5の解答:" + self.problems[self.dic[4]]["Answer"] + "　　　問5のあなたの解答:" + self.answer[4])
        self.anslabel5.pack()
        #問6
        self.anslabel6 = tk.Label(self.testresultframe, text="問6の解答:" + self.problems[self.dic[5]]["Answer"] + "　　　問6のあなたの解答:" + self.answer[5])
        self.anslabel6.pack()
        #問7
        self.anslabel7 = tk.Label(self.testresultframe, text="問7の解答:" + self.problems[self.dic[6]]["Answer"] + "　　　問7のあなたの解答:" + self.answer[6])
        self.anslabel7.pack()
        #問8
        self.anslabel8 = tk.Label(self.testresultframe, text="問8の解答:" + self.problems[self.dic[7]]["Answer"] + "　　　問8のあなたの解答:" + self.answer[7])
        self.anslabel8.pack()
        #問9
        self.anslabel9 = tk.Label(self.testresultframe, text="問9の解答:" + self.problems[self.dic[8]]["Answer"] + "　　　問9のあなたの解答:" + self.answer[8])
        self.anslabel9.pack()
        #問10
        self.anslabel10 = tk.Label(self.testresultframe, text="問10の解答:" + self.problems[self.dic[9]]["Answer"] + "　　　問10のあなたの解答:" + self.answer[9])
        self.anslabel10.pack()

        
        
        self.button1['text'] = "次の問題へ"
        self.button1['command'] = self.changeproblem
        
        self.count = 0
        self.correctcount = 0
        
    def makerandomdic(self):
        for i in range(1, 11):
            self.dic.append(str(i))

        random.shuffle(self.dic)
        return self.dic
            
if __name__ == "__main__":
    app = App()
