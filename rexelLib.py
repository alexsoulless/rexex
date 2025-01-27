import socket
import os
import json


port = 10500
ChunkSize = 4096
FORMAT = "utf-8"


# messages
class MSG:
    Null = b"MSG_Null"
    SendFile = b"MSG_SendFile"
    Execute = b"MSG_Execute"
    GetDirsDif = b"MSG_GetDirsDif"
    Break = b"MSG_Break"
    SendConf = b"MSG_SendConf"
    SendFileBack = b"MSG_GetFiles"
    Run = b"MSG_Run"
    ReturnResult = b"MSG_ReturnResult"


class Config:
    def __init__(self, req="", main="", sendFiles=[], sendDirs=[]):
        self.req = req
        self.main = main
        self.sendFiles = sendFiles
        self.sendDirs = sendDirs

    def mainInDirs(self):
        for dir in self.sendDirs:
            if dir in self.main:
                return True
            return False

    def normalize(self):
        """
        нужно нормализовать путь до исполняемого файла на тот случай
        если он уже находится в отправляемой директории
        """
        self.req = os.path.basename(self.req)

        for dir in self.sendDirs:
            if dir in self.main:
                self.main = self.main.replace(dir, "")
                if self.main[0] == "/":
                    self.main = self.main[1:]
                self.main = os.path.join(os.path.basename(dir), self.main)
                return self

        self.main = os.path.basename(self.main)
        return self

    def __str__(self):
        return f"conf:\n \
req = {self.req}\n \
main = {self.main}\n \
sendFiles = {self.sendFiles}\n \
sendDirs = {self.sendDirs}"

    def __dict__(self):
        return {
            "req": self.req,
            "main": self.main,
            "sendFiles": self.sendFiles,
            "sendDirs": self.sendDirs,
        }


def SendConf(conn: socket.socket, conf: Config) -> int:
    """
    Функция реализует отправку конфига вычислений
    conf = {
        "requirements" : "path or empty"
        "mainFile" : "path"
    }
    """

    if SendMessage(conn, MSG.SendConf) == 0:
        return 0

    data = json.dumps(conf.__dict__())

    conn.sendall(bytes(data, encoding=FORMAT))
    conn.send(MSG.Null)
    conn.recv(ChunkSize)

    return 1


def ReceiveConf(conn: socket.socket) -> Config:
    """
    Принимает конфиг с сокета conn и возвращает его
    """

    data = ""
    while (tempData := conn.recv(ChunkSize)) != MSG.Null:
        data += tempData.decode(FORMAT)

    conn.send(b"1")
    req, main, sendFiles, sendDirs = json.loads(data).values()
    conf = Config(req, main, sendFiles, sendDirs)
    # print(conf)
    return conf


def Run(conf: Config) -> tuple[int, int, list]:

    if len(conf.req) > 0:
        exitCodeReq = os.system(f"pip install -r {conf.req}")
    else:
        exitCodeReq = 0

    dirBefore = DirectoryList()

    if len(conf.main) > 0:
        exitCodeMain = os.system(f"python3 {conf.main}")
        # exitCodeMain = os.system(f"python3 {conf.main} > REXELOUTPUT.txt")
        # print(f"python3 {conf.main}")
    else:
        # print("no main file to run")
        exitCodeMain = 1

    dirAfter = DirectoryList()
    dirDiff = DirectoryDiff(dirBefore, dirAfter)

    # if "./REXELOUTPUT.txt" in dirDiff:
    #     dirDiff.remove("./REXELOUTPUT.txt")

    return exitCodeReq, exitCodeMain, dirDiff


def goExecute(conn: socket.socket, conf: Config) -> tuple[int, int, list[str]]:
    """
    Запуск вычислений на сервере
    """

    for file in conf.sendFiles:
        SendFile(conn, file)

    for dir in conf.sendDirs:
        SendDir(conn, dir)

    if not conf.mainInDirs():
        SendFile(conn, conf.main)

    if len(conf.req) > 0:
        SendFile(conn, conf.req)

    conf.normalize()

    SendConf(conn, conf)

    goRun(conn)

    exitCodeReq, exitCodeMain, dirDiff = ReturnResult(conn)

    return exitCodeReq, exitCodeMain, dirDiff


def goRun(conn: socket.socket):
    return SendMessage(conn, MSG.Run)


def ReceiveFilesBack(conn: socket.socket, files: list[str], saveTo=""):
    for fileName in files:
        SendMessage(conn, MSG.SendFileBack)

        conn.send(bytes(fileName, encoding=FORMAT))
        conn.recv(1)

        targetFile = os.path.join(saveTo, os.path.basename(fileName))

        file = open(targetFile, "wb")

        while (data := conn.recv(ChunkSize)) != MSG.Null:
            file.write(data)
            conn.send(b"1")

        conn.send(b"done")
        file.close()


def SendFileBack(conn: socket.socket):

    fileName = conn.recv(ChunkSize).decode(FORMAT)
    conn.send(b"1")

    try:
        file = open(fileName, "rb")
    except OSError:
        conn.send(MSG.Null)
        conn.recv(ChunkSize)
        return 0

    while data := file.read(ChunkSize):
        conn.send(data)
        conn.recv(1)

    conn.send(MSG.Null)
    conn.recv(ChunkSize)
    file.close()
    return 1


def SendResult(conn: socket.socket, exitCodeReq, exitCodeMain, dirDiff):

    sendStr = str(exitCodeReq) + " " + str(exitCodeMain) + " " + str(len(dirDiff))

    conn.send(bytes(sendStr, encoding=FORMAT))
    conn.recv(1)

    for fileName in dirDiff:
        conn.send(bytes(fileName, encoding=FORMAT))
        conn.recv(ChunkSize)
    
    return 0


def ReturnResult(conn: socket.socket) -> tuple[int, int, list[str]]:
    SendMessage(conn, MSG.ReturnResult)

    recvData = map(int, conn.recv(ChunkSize).decode(FORMAT).split())
    exitCodeReq, exitCodeMain, countOfNewFiles = recvData
    conn.send(b"1")

    dirDiff = []
    for i in range(countOfNewFiles):
        fileName = conn.recv(ChunkSize).decode(FORMAT)
        conn.send(b"1")
        dirDiff.append(fileName)

    return exitCodeReq, exitCodeMain, dirDiff


def SendMessage(conn: socket.socket, message) -> int:
    """
    Отправка сообщения на сокет
    Вернёт 1 если всё прошло успешно

    TODO надо сделать сериализацию и подумать над конфиденциальностью
    """
    if message is str:
        message = message.encode(FORMAT)
    conn.send(message)
    if conn.recv(ChunkSize) == message:
        return 1
    return 0


def BreakServer(conn: socket.socket) -> int:
    return SendMessage(conn, MSG.Break)


def SendFile(conn: socket.socket, fileName: str, fileDest="") -> int:
    """
    Отправка файла
    Возвращает 1 если файл отправлен успешно

    conn - сокет, на который отправляем файл
    fileName - путь до файла на клиенте
    fileDest - место назначения файла на сервере

    TODO тут надо сделать норм обмен сообщениями и
    отправку файла сделать функцией sendfile
    """
    try:
        file = open(fileName, "rb")
    except OSError:
        # print(f"SendFileErr: cant open {fileName}")
        return 0

    fileNameToServ = os.path.join(fileDest, os.path.basename(fileName))
    # print(f"im sending file {fileNameToServ}")

    if SendMessage(conn, MSG.SendFile) == 0:
        file.close()
        return 0

    conn.send((bytes(fileNameToServ, encoding=FORMAT)))
    conn.recv(ChunkSize)

    while data := file.read(ChunkSize):
        conn.send(data)
        conn.recv(1)

    conn.send(MSG.Null)
    conn.recv(ChunkSize)
    file.close()
    return 1


def SendDir(conn: socket.socket, directoryPath: str) -> int:
    """
    Функция отправляет всё содержимое директории
    Возвращает 1 если отправка успешна
    directoryPath - абсолютный путь до папки
    """
    for root, dirs, files in os.walk(directoryPath):
        for file in files:
            fileName = os.path.join(root, file)
            fileDest = os.path.relpath(root, directoryPath)
            if fileDest == ".":
                fileDest = ""
            fileDest = os.path.join(os.path.basename(directoryPath), fileDest)
            if not SendFile(conn, fileName, fileDest):
                return 0
    return 1


def DirectoryList(target=".") -> list:
    dirList = list()
    for root, dirs, files in os.walk(target):
        for file in files:
            dirList.append(os.path.join(root, file))
    return dirList


def DirectoryDiff(before: list, after: list) -> list:
    return list(set(after) - set(before))


def ReceiveFile(conn: socket.socket, targetFolder="./") -> int:

    fileName = os.path.normpath((conn.recv(ChunkSize)).decode(FORMAT))
    fileName = os.path.join(targetFolder, fileName)

    conn.send(b"filename was received")

    try:
        os.makedirs(os.path.split(fileName)[0], exist_ok=True)
        file = open(fileName, "wb")
    except OSError:
        return 0

    while (data := conn.recv(ChunkSize)) != MSG.Null:
        file.write(data)
        conn.send(b"1")

    # print(f"file {fileName} was received")
    conn.send(b"done")
    file.close()

    return 1
