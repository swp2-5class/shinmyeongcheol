import pickle

dbfilename = 'test3_4.dat'  # test3_4.dat 파일이름저장


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')  # dbfilename 이진모드로 읽기
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()

    for p in scdb:
        p['Age'] = int(p['Age'])  # age score 정수 변경
        p['Score'] = int(p['Score'])
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                scdb += [record]  # scdb에 record를 추가한다.
            except (IndexError, ValueError, TypeError): #잘못된 인덱스 인덱싱, 값이 부적절, 데이터 유형이 잘못될경우
                print('ERROR!!')  # 에러표시

        elif parse[0] == 'del':
            try:
                cp_scdb = scdb[:] #scdb를 그래도 복사한 카피본생성
                for p in cp_scdb:
                    if p['Name'] == parse[1]:  # Name의 값이 같은 것이 존재한다면
                        scdb.remove(p)  # scdb에서 그 사람의 레코드를 제거한다.
                if cp_scdb == scdb:  #del *에서 *값이 리스트에 없는 경우
                    print("There is no %s" % (parse[1]))  # 오류표시
            except (IndexError, ValueError, TypeError):
                print("error")

        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'quit':
            break

        elif parse[0] == 'find':
            try:  # find명령어를 받으면
                compare = False  #없는파일을 찾으면 없다고 출력하기 위해 필요한 변수 생성.
                for p in scdb:
                    if p['Name'] == parse[1]:  # 같은 이름이 존재하면 내용을 출력한다.
                        print('Age=%d Name=%s Score=%d' % (p['Age'], p['Name'], p['Score']))
                        compare = True  # 찾았을 경우 트루로
                if compare == False:  # 그대로 false면 ,
                    print("There is no %s" % (parse[1]))  #엄서용
            except(TypeError, ValueError, IndexError):
                print ("error")


        elif parse[0] == 'inc':
            compare = False;
            try:
                for p in scdb:  # inc명령어를 받으면
                    if p['Name'] == parse[1]:  # 같은이름이 존재하는지 찾은후
                        p['Score'] += int(parse[2])
                        compare = True
                if compare == False:
                    print("There is no %s" % (parse[1]))  #없어용
            except(TypeError, ValueError, IndexError):
                print('error')
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=%s" % (p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)