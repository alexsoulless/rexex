# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.WindowModal)
        MainWindow.resize(551, 737)
        font = QFont()
        font.setFamilies([u"Ubuntu Mono"])
        font.setPointSize(14)
        font.setItalic(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/rexelLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ServerSettings = QGroupBox(self.centralwidget)
        self.ServerSettings.setObjectName(u"ServerSettings")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ServerSettings.sizePolicy().hasHeightForWidth())
        self.ServerSettings.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.ServerSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.IPLabel = QLabel(self.ServerSettings)
        self.IPLabel.setObjectName(u"IPLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.IPLabel.sizePolicy().hasHeightForWidth())
        self.IPLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.IPLabel)

        self.IPEdit = QLineEdit(self.ServerSettings)
        self.IPEdit.setObjectName(u"IPEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.IPEdit.sizePolicy().hasHeightForWidth())
        self.IPEdit.setSizePolicy(sizePolicy2)
        self.IPEdit.setMinimumSize(QSize(210, 25))
        self.IPEdit.setMaximumSize(QSize(210, 25))
        self.IPEdit.setFont(font)
        self.IPEdit.setFrame(True)
        self.IPEdit.setPlaceholderText(u"***.***.***.***:*****")
        self.IPEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.IPEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.TryConnectButton = QPushButton(self.ServerSettings)
        self.TryConnectButton.setObjectName(u"TryConnectButton")
        icon1 = QIcon(QIcon.fromTheme(u"mail-send-receive"))
        self.TryConnectButton.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.TryConnectButton)

        self.ResetIPButton = QPushButton(self.ServerSettings)
        self.ResetIPButton.setObjectName(u"ResetIPButton")
        icon2 = QIcon(QIcon.fromTheme(u"application-exit"))
        self.ResetIPButton.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.ResetIPButton)

        self.ConnectionStatus = QLabel(self.ServerSettings)
        self.ConnectionStatus.setObjectName(u"ConnectionStatus")
        self.ConnectionStatus.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ConnectionStatus.sizePolicy().hasHeightForWidth())
        self.ConnectionStatus.setSizePolicy(sizePolicy3)
        self.ConnectionStatus.setMaximumSize(QSize(25, 25))
        self.ConnectionStatus.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.ConnectionStatus)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addWidget(self.ServerSettings)

        self.CalcSettings = QGroupBox(self.centralwidget)
        self.CalcSettings.setObjectName(u"CalcSettings")
        self.CalcSettings.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.CalcSettings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.MainFileChoose = QHBoxLayout()
        self.MainFileChoose.setObjectName(u"MainFileChoose")
        self.MainFileLabel = QLabel(self.CalcSettings)
        self.MainFileLabel.setObjectName(u"MainFileLabel")
        self.MainFileLabel.setScaledContents(True)
        self.MainFileLabel.setWordWrap(True)

        self.MainFileChoose.addWidget(self.MainFileLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.MainFileChoose.addItem(self.horizontalSpacer_5)

        self.ChooseMainFileButton = QPushButton(self.CalcSettings)
        self.ChooseMainFileButton.setObjectName(u"ChooseMainFileButton")
        self.ChooseMainFileButton.setMaximumSize(QSize(95, 27))
        icon3 = QIcon(QIcon.fromTheme(u"folder-new"))
        self.ChooseMainFileButton.setIcon(icon3)

        self.MainFileChoose.addWidget(self.ChooseMainFileButton)

        self.MainFileResetButton = QPushButton(self.CalcSettings)
        self.MainFileResetButton.setObjectName(u"MainFileResetButton")
        self.MainFileResetButton.setMinimumSize(QSize(104, 27))
        self.MainFileResetButton.setMaximumSize(QSize(104, 27))
        self.MainFileResetButton.setIcon(icon2)

        self.MainFileChoose.addWidget(self.MainFileResetButton)


        self.verticalLayout_2.addLayout(self.MainFileChoose)

        self.ReqChoose = QHBoxLayout()
        self.ReqChoose.setObjectName(u"ReqChoose")
        self.ReqLabel = QLabel(self.CalcSettings)
        self.ReqLabel.setObjectName(u"ReqLabel")
        self.ReqLabel.setWordWrap(True)

        self.ReqChoose.addWidget(self.ReqLabel)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ReqChoose.addItem(self.horizontalSpacer_6)

        self.ReqChooseButton = QPushButton(self.CalcSettings)
        self.ReqChooseButton.setObjectName(u"ReqChooseButton")
        self.ReqChooseButton.setMaximumSize(QSize(95, 27))
        self.ReqChooseButton.setIcon(icon3)

        self.ReqChoose.addWidget(self.ReqChooseButton)

        self.ReqResetButton = QPushButton(self.CalcSettings)
        self.ReqResetButton.setObjectName(u"ReqResetButton")
        self.ReqResetButton.setMaximumSize(QSize(104, 27))
        self.ReqResetButton.setIcon(icon2)

        self.ReqChoose.addWidget(self.ReqResetButton)


        self.verticalLayout_2.addLayout(self.ReqChoose)

        self.line = QFrame(self.CalcSettings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.listFileLabel = QHBoxLayout()
        self.listFileLabel.setObjectName(u"listFileLabel")
        self.label_2 = QLabel(self.CalcSettings)
        self.label_2.setObjectName(u"label_2")

        self.listFileLabel.addWidget(self.label_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.listFileLabel.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.listFileLabel)

        self.listFileWidget = QListWidget(self.CalcSettings)
        self.listFileWidget.setObjectName(u"listFileWidget")
        self.listFileWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.listFileWidget.setSelectionRectVisible(False)

        self.verticalLayout_2.addWidget(self.listFileWidget)

        self.AddRemovw = QHBoxLayout()
        self.AddRemovw.setObjectName(u"AddRemovw")
        self.AddFileButton = QPushButton(self.CalcSettings)
        self.AddFileButton.setObjectName(u"AddFileButton")
        icon4 = QIcon(QIcon.fromTheme(u"list-add"))
        self.AddFileButton.setIcon(icon4)

        self.AddRemovw.addWidget(self.AddFileButton)

        self.RemoveButton = QPushButton(self.CalcSettings)
        self.RemoveButton.setObjectName(u"RemoveButton")
        self.RemoveButton.setIcon(icon2)

        self.AddRemovw.addWidget(self.RemoveButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.AddRemovw.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.AddRemovw)


        self.verticalLayout_5.addWidget(self.CalcSettings)

        self.RunButton = QPushButton(self.centralwidget)
        self.RunButton.setObjectName(u"RunButton")
        self.RunButton.setEnabled(False)
        self.RunButton.setMinimumSize(QSize(0, 35))
        self.RunButton.setBaseSize(QSize(0, 0))
        icon5 = QIcon(QIcon.fromTheme(u"media-playback-start"))
        self.RunButton.setIcon(icon5)
        self.RunButton.setCheckable(False)

        self.verticalLayout_5.addWidget(self.RunButton)

        self.Result = QGroupBox(self.centralwidget)
        self.Result.setObjectName(u"Result")
        self.Result.setFlat(False)
        self.verticalLayout_4 = QVBoxLayout(self.Result)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.Result)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy4)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.consoleOutput = QWidget()
        self.consoleOutput.setObjectName(u"consoleOutput")
        self.gridLayout = QGridLayout(self.consoleOutput)
        self.gridLayout.setObjectName(u"gridLayout")
        self.serverOutput = QTextEdit(self.consoleOutput)
        self.serverOutput.setObjectName(u"serverOutput")
        self.serverOutput.setReadOnly(True)

        self.gridLayout.addWidget(self.serverOutput, 0, 0, 1, 1)

        self.tabWidget.addTab(self.consoleOutput, "")
        self.files = QWidget()
        self.files.setObjectName(u"files")
        self.gridLayout_8 = QGridLayout(self.files)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.DirDiffList = QListWidget(self.files)
        self.DirDiffList.setObjectName(u"DirDiffList")
        self.DirDiffList.setAlternatingRowColors(False)
        self.DirDiffList.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.DirDiffList.setProperty("isWrapping", False)
        self.DirDiffList.setViewMode(QListView.ViewMode.ListMode)
        self.DirDiffList.setSelectionRectVisible(True)
        self.DirDiffList.setSortingEnabled(False)

        self.gridLayout_7.addWidget(self.DirDiffList, 0, 0, 1, 2)

        self.InstallResponseButton = QPushButton(self.files)
        self.InstallResponseButton.setObjectName(u"InstallResponseButton")
        self.InstallResponseButton.setEnabled(False)
        icon6 = QIcon(QIcon.fromTheme(u"document-save"))
        self.InstallResponseButton.setIcon(icon6)

        self.gridLayout_7.addWidget(self.InstallResponseButton, 1, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.files, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.verticalLayout_5.addWidget(self.Result)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.IPEdit, self.TryConnectButton)
        QWidget.setTabOrder(self.TryConnectButton, self.ResetIPButton)
        QWidget.setTabOrder(self.ResetIPButton, self.ChooseMainFileButton)
        QWidget.setTabOrder(self.ChooseMainFileButton, self.MainFileResetButton)
        QWidget.setTabOrder(self.MainFileResetButton, self.ReqChooseButton)
        QWidget.setTabOrder(self.ReqChooseButton, self.ReqResetButton)
        QWidget.setTabOrder(self.ReqResetButton, self.listFileWidget)
        QWidget.setTabOrder(self.listFileWidget, self.AddFileButton)
        QWidget.setTabOrder(self.AddFileButton, self.RemoveButton)
        QWidget.setTabOrder(self.RemoveButton, self.RunButton)
        QWidget.setTabOrder(self.RunButton, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.serverOutput)
        QWidget.setTabOrder(self.serverOutput, self.DirDiffList)
        QWidget.setTabOrder(self.DirDiffList, self.InstallResponseButton)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Rexex", None))
        self.ServerSettings.setTitle(QCoreApplication.translate("MainWindow", u"1. \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0435\u0440\u0432\u0435\u0440\u0430", None))
        self.IPLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 IP:port \u0430\u0434\u0440\u0435\u0441 \u0441\u0435\u0440\u0432\u0435\u0440\u0430:", None))
        self.IPEdit.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1:2375", None))
        self.TryConnectButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.ResetIPButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441", None))
        self.ConnectionStatus.setText("")
        self.CalcSettings.setTitle(QCoreApplication.translate("MainWindow", u"2. \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0439", None))
        self.MainFileLabel.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u043d\u044f\u0435\u043c\u044b\u0439 \u0444\u0430\u0439\u043b: -", None))
        self.ChooseMainFileButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.MainFileResetButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.ReqLabel.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b requirements: -", None))
        self.ReqChooseButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.ReqResetButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0444\u0430\u0439\u043b\u043e\u0432:", None))
        self.AddFileButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.RemoveButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u044c", None))
        self.RunButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
#if QT_CONFIG(accessibility)
        self.Result.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.Result.setTitle(QCoreApplication.translate("MainWindow", u"3. \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
#if QT_CONFIG(accessibility)
        self.consoleOutput.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.consoleOutput), QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0432\u043e\u0434 \u043a\u043e\u043d\u0441\u043e\u043b\u0438", None))
        self.InstallResponseButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.files), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b\u044b", None))
    # retranslateUi

