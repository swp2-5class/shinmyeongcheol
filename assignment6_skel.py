import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt



class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):

        # 1번쨰 줄.
        Name = QLabel("Name : ") #이름, 나이 점수 라벨을 생성한다.
        Age = QLabel("Age : ")
        Score = QLabel("Score : ")

        self.NameEdit = QLineEdit() #이름, 나이, 점수 텍스트 창을 만든다.
        self.AgeEdit = QLineEdit()
        self.ScoreEdit = QLineEdit()

        layout = QGridLayout() #gird 생성
        layout.setSpacing(5)

        layout.addWidget(Name, 0, 0) #행렬 (0,1) 에 name 라벨을 표시
        layout.addWidget(self.NameEdit, 0, 1) #행렬 (0,2) 에 텍스트창 표시.
        layout.addWidget(Age, 0 ,2)
        layout.addWidget(self.AgeEdit,0,3)
        layout.addWidget(Score,0,4)
        layout.addWidget(self.ScoreEdit,0,5)

        # 2번째 줄.
        Amount = QLabel("Amount:")
        self.AmountEdit = QLineEdit()
        layout.addWidget(Amount,1,0)
        layout.addWidget(self.AmountEdit,1,1,1,3)

        Key = QLabel("Key:")
        layout.addWidget(Key,1,4)

        self.key_box = QComboBox() #선택할 수 있는 박스 생성
        self.key_box.addItems(["Score", "Name", "Age"]) #항목 3개 추가 / 단일 항목일 경우는 additem

        layout.addWidget(self.key_box,1,5,1,6)


        # 3번째 줄.
        btn2 = QPushButton("Add",self)
        layout.addWidget(btn2,2,1)
        btn2.clicked.connect(self.add_btn_clicked)

        btn3 = QPushButton("Del",self)
        layout.addWidget(btn3,2,2)
        btn3.clicked.connect(self.del_btn_clicked)

        btn4 = QPushButton("Find",self)
        layout.addWidget(btn4,2,3)
        btn4.clicked.connect(self.find_btn_clicked)

        btn5 = QPushButton("lnc",self)
        layout.addWidget(btn5,2,4)
        btn5.clicked.connect(self.inc_btn_clicked)

        btn6 = QPushButton("show",self)
        layout.addWidget(btn6,2,5)
        btn6.clicked.connect(self.show_btn_clicked)

        # 4번째 줄.
        Result = QLabel("Result :")
        layout.addWidget(Result,3,0)

        # 5번째 줄.
        self.Text_box = QTextEdit(self)
        self.Text_box.setReadOnly(True) #읽기만 가능 입력 불가
        self.Text_box.setAlignment(Qt.AlignLeft)
        layout.addWidget(self.Text_box,4,0,7,6)

        #etc

        self.setLayout(layout)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        list = []
        self.Text_box.setPlainText("")
        for p in sorted(self.scoredb, key=lambda person: person["Name"]):
            for attr in sorted(p):
                list.append(str(attr) + "=" + str(p[attr]))
            self.Text_box.append(list[0]+ " " + list[1]+ " " + list [2])
            list = []

    def show_btn_clicked(self):
        list = []
        self.Text_box.setPlainText("")
        keyname = str(self.key_box.currentText())
        for p in sorted(self.scoredb, key = lambda  person : person[keyname]):
            for attr in sorted(p):
                list.append(str(attr) + "=" + str(p[attr]))
            self.Text_box.append(list[0]+ " " + list[1]+ " " + list [2])
            list = []


    def add_btn_clicked(self):
        list = []
        self.Text_box.setPlainText("")
        Name = self.NameEdit.text() # 입력한 텍스트 받아오기
        Age = self.AgeEdit.text()
        Score = self.ScoreEdit.text()
        record = {'Name': Name, 'Age': Age, 'Score': Score}
        self.scoredb += [record]
        for p in sorted(self.scoredb, key=lambda person: person["Name"]):
            for attr in sorted(p):
                list.append(str(attr) + "=" + str(p[attr]))
            self.Text_box.append(list[0]+ " " + list[1]+ " " + list [2])
            list = []
        self.NameEdit.clear()
        self.AgeEdit.clear()
        self.ScoreEdit.clear()

    def del_btn_clicked(self):
        list = []
        self.Text_box.setPlainText("")
        for p in self.scoredb:
            if p['Name'] == self.NameEdit.text():
                self.scoredb.remove(p)
        for q in sorted(self.scoredb, key=lambda person: person["Name"]):
            for attr in sorted(q):
                list.append(str(attr) + "=" + str(q[attr]))
            self.Text_box.append(list[0] + " " + list[1] + " " + list[2])
            list = []

    def find_btn_clicked(self):
        self.Text_box.setPlainText("")
        Name = self.NameEdit.text()  # 입력한 텍스트 받아오기
        Age = self.AgeEdit.text()
        Score = self.ScoreEdit.text()
        for i in self.scoredb:
            if i['Name'] == Name :
                self.Text_box.append("Age="+ " "+str(i["Age"])+ " "+ "Name="+ " "+ str(i["Name"])+ " "+ "Score="+ " "+str(i["Score"]))
        self.NameEdit.clear()
        self.AgeEdit.clear()
        self.ScoreEdit.clear()

    def inc_btn_clicked(self):
        self.Text_box.setPlainText("")
        for s in self.scoredb:
            if  s['Name'] == self.NameEdit.text():
                s['Score'] = int(s['Score'])
                s['Score'] = s['Score'] + int(self.AmountEdit.text())
                s['Score'] = str(s['Score'])
                break;
        self.showScoreDB()
        self.NameEdit.clear()
        self.AgeEdit.clear()
        self.ScoreEdit.clear()
        self.AmountEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    ex.show()
    sys.exit(app.exec_())

