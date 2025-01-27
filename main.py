import sys
import re
import docker
import socket
from PySide6 import QtWidgets, QtGui
from MainWindow_ui import Ui_MainWindow
import rexelLib as rl

UseLocalHost = True
ContainerPort = rl.port


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

    def RefreshRunButton(self):
        if IPPort and MainFile:
            self.RunButton.setEnabled(True)
        else:
            self.RunButton.setEnabled(False)

    def IPEditHandler(self):
        if re.match(ipAndPortRe, self.IPEdit.text()):
            self.TryConnectButton.setEnabled(True)
        else:
            self.TryConnectButton.setEnabled(False)

    def TryConnect(self):
        global container, desktop, IPPort
        self.TryConnectButton.setEnabled(False)
        self.ConnectionStatus.setPixmap(tryConnectPixmap)

        IPPort = self.IPEdit.text()

        try:
            if UseLocalHost:
                desktop = docker.DockerClient(base_url="tcp://localhost:2375")
            else:
                desktop = docker.DockerClient(base_url=f"tcp://{IPPort}")

            if desktop.ping():
                container = desktop.containers.run(
                    image="rexelserv",
                    ports={"10500": ("localhost", ContainerPort)},
                    detach=True,
                )

                self.ConnectionStatus.setPixmap(successConnectPixmap)
                
        except Exception as ex:
            self.ConnectionStatus.setPixmap(failConnectPixmap)
            IPPort = ""
            print(ex)

        self.TryConnectButton.setEnabled(True)
        self.RefreshRunButton()

    def ResetIP(self):
        global desktop, IPPort, container

        self.IPEdit.setText("")
        self.TryConnectButton.setEnabled(False)
        self.ConnectionStatus.clear()

        desktop = None
        IPPort = ""

        if container:
            try:
                container.kill()
            except Exception:
                pass

        self.RefreshRunButton()
        self.InstallResponseButton.setEnabled(False)
        self.DirDiffList.clear()
        self.serverOutput.clear()

    def ChooseMainFile(self):

        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите исполняемый файл", filter="Python File (*.py)"
        )
        if fileName:
            global MainFile
            MainFile = fileName
            self.MainFileLabel.setText(f"Исполняемый файл: {MainFile}")
        self.RefreshRunButton()

    def ResetMainFile(self):
        self.MainFileLabel.setText("Исполняемый файл: -")
        global MainFile
        MainFile = ""
        self.RefreshRunButton()

    def ChooseReq(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите requirements", filter="Text file (*.txt)"
        )
        if fileName:
            global ReqFile
            ReqFile = fileName
            self.ReqLabel.setText(f"Файл requirements: {ReqFile}")

    def ResetReq(self):
        global ReqFile
        self.ReqLabel.setText("Файл requirements: -")
        ReqFile = ""

    def AddExtraFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Выберите файл")
        if fileName:
            for item in fileName:
                self.listFileWidget.addItem(item)

    def RemoveExtraFile(self):
        if self.listFileWidget.selectedItems():
            for item in self.listFileWidget.selectedItems():
                self.listFileWidget.takeItem(self.listFileWidget.row(item))

    def GoExecute(self):
        global container, sock

        ip = IPPort.split(":")[0]
        sock = socket.socket()

        if UseLocalHost:
            sock.connect(("localhost", ContainerPort))
        else:
            sock.connect((ip, ContainerPort))

        sendFiles = [
            self.listFileWidget.item(i).text()
            for i in range(self.listFileWidget.count())
        ]

        conf = rl.Config(ReqFile, MainFile, sendFiles)
        try:
            exitCodeReq, exitCodeMain, dirDiff = rl.goExecute(sock, conf)
        except Exception:
            pass

        output = str(container.logs(), encoding="utf-8")
        self.serverOutput.setText(output)

        self.DirDiffList.clear()
        if dirDiff:
            for item in dirDiff:
                self.DirDiffList.addItem(item)

        self.InstallResponseButton.setEnabled(True)
        self.RunButton.setEnabled(False)

    def InstallResponseFile(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Выберите куда сохранить файл"
        )
        files = [i.text() for i in self.DirDiffList.selectedItems()]

        rl.ReceiveFilesBack(sock, files, path)

    def closeEvent(self, event):
        global container
        try:
            container.kill()
        except Exception:
            pass


ipAndPortRe = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\:([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))$"

app = QtWidgets.QApplication(sys.argv)

tryConnectPixmap = QtGui.QPixmap(":/icons/icons/tryConnect.png")
successConnectPixmap = QtGui.QPixmap(":/icons/icons/successConnect.png")
failConnectPixmap = QtGui.QPixmap(":/icons/icons/failConnect.png")

MainFile = ""
ReqFile = ""
IPPort = ""
desktop = None
container = None
localhost = "localhost"

window = MainWindow()

window.IPEdit.textEdited.connect(window.IPEditHandler)
window.TryConnectButton.clicked.connect(window.TryConnect)
window.ResetIPButton.clicked.connect(window.ResetIP)

window.ChooseMainFileButton.clicked.connect(window.ChooseMainFile)
window.MainFileResetButton.clicked.connect(window.ResetMainFile)

window.ReqChooseButton.clicked.connect(window.ChooseReq)
window.ReqResetButton.clicked.connect(window.ResetReq)

window.AddFileButton.clicked.connect(window.AddExtraFile)
window.RemoveButton.clicked.connect(window.RemoveExtraFile)

window.RunButton.clicked.connect(window.GoExecute)

window.InstallResponseButton.clicked.connect(window.InstallResponseFile)


window.show()
app.exec()
