# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HAHA.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

def Bool(string):
    if string == 'True':
        return True
    else:
        return False

# True Output
# False Input
# True High
# False Low
# False Pullup
# True High Impedence

List = []
def newConfigs():
    global List
    List = []
    for port in range(0,4):
        Pins = []
        for pin in range(0,32):
            # [I/O Out In UseName Name]
            Pins.append([False, True, True, True, ''])
        List.append(Pins)
newConfigs()
class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1016, 602)
        font = QFont()
        font.setBold(True)
        font.setWeight(75);
        font.setStrikeOut(False)
        Form.setFont(font)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 90, 961, 331))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 230, 91, 31))
        self.nameLE = QLineEdit(self.groupBox)
        self.nameLE.setObjectName(u"nameLE")
        self.nameLE.setGeometry(QRect(50, 270, 351, 31))
        self.nameLE.setEnabled(False)
        self.defNameCB = QCheckBox(self.groupBox)
        self.defNameCB.setObjectName(u"defNameCB")
        self.defNameCB.setGeometry(QRect(550, 270, 191, 41))
        self.defNameCB.setChecked(True)
        self.outGB = QGroupBox(self.groupBox)
        self.outGB.setObjectName(u"outGB")
        self.outGB.setEnabled(False)
        self.outGB.setGeometry(QRect(500, 30, 411, 91))
        self.highRB = QRadioButton(self.outGB)
        self.highRB.setObjectName(u"highRB")
        self.highRB.setGeometry(QRect(40, 40, 83, 18))
        self.highRB.setChecked(True)
        self.lowRB = QRadioButton(self.outGB)
        self.lowRB.setObjectName(u"lowRB")
        self.lowRB.setGeometry(QRect(250, 40, 83, 18))
        self.inGB = QGroupBox(self.groupBox)
        self.inGB.setObjectName(u"inGB")
        self.inGB.setGeometry(QRect(500, 150, 411, 80))
        self.pullupRB = QRadioButton(self.inGB)
        self.pullupRB.setObjectName(u"pullupRB")
        self.pullupRB.setGeometry(QRect(40, 40, 83, 18))
        self.highImpRB = QRadioButton(self.inGB)
        self.highImpRB.setObjectName(u"highImpRB")
        self.highImpRB.setGeometry(QRect(260, 40, 111, 18))
        self.highImpRB.setChecked(True)
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(50, 30, 171, 191))
        self.inputRB = QRadioButton(self.groupBox_4)
        self.inputRB.setObjectName(u"inputRB")
        self.inputRB.setGeometry(QRect(30, 130, 83, 18))
        self.inputRB.setChecked(True)
        self.outputRB = QRadioButton(self.groupBox_4)
        self.outputRB.setObjectName(u"outputRB")
        self.outputRB.setGeometry(QRect(30, 50, 83, 18))
        self.outputRB.setChecked(False)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 440, 101, 21))
        self.pathLE = QLineEdit(Form)
        self.pathLE.setObjectName(u"pathLE")
        self.pathLE.setGeometry(QRect(40, 480, 681, 31))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(780, 480, 151, 31))
        self.portCB = QComboBox(Form)
        self.portCB.addItem(str())
        self.portCB.addItem(str())
        self.portCB.addItem(str())
        self.portCB.addItem(str())
        self.portCB.setObjectName(u"portCB")
        self.portCB.setGeometry(QRect(130, 30, 171, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.portCB.setFont(font1)
        self.portCB.setMaxVisibleItems(4)
        self.pinCB = QComboBox(Form)
        self.pinCB.addItem(str())
        self.pinCB.addItem(str())
        self.pinCB.addItem(str())
        self.pinCB.addItem(str())
        self.pinCB.addItem(str())
        self.pinCB.addItem(str())
        self.pinCB.addItem(str())
        self.pinCB.addItem(str())
        self.pinCB.setObjectName(u"pinCB")
        self.pinCB.setGeometry(QRect(540, 30, 191, 31))
        self.pinCB.setFont(font1)
        self.pinCB.setMaxVisibleItems(10)
        self.savePB = QPushButton(Form)
        self.savePB.setObjectName(u"savePB")
        self.savePB.setGeometry(QRect(620, 550, 141, 31))
        self.loadPB = QPushButton(Form)
        self.loadPB.setObjectName(u"loadPB")
        self.loadPB.setGeometry(QRect(810, 550, 151, 31))
        self.newPB = QPushButton(Form)
        self.newPB.setObjectName(u"newPB")
        self.newPB.setGeometry(QRect(80, 550, 141, 31))

        self.retranslateUi(Form)
        self.outputRB.toggled.connect(self.inGB.setDisabled)
        self.inputRB.toggled.connect(self.inGB.setEnabled)
        self.outputRB.toggled.connect(self.outGB.setEnabled)
        self.inputRB.toggled.connect(self.outGB.setDisabled)
        self.defNameCB.toggled.connect(self.nameLE.setDisabled)

        self.portCB.currentIndexChanged.connect(self.PPChange)
        self.pinCB.currentIndexChanged.connect(self.PPChange)
        
        self.outputRB.toggled.connect(self.change)
        self.highRB.toggled.connect(self.change)
        self.pullupRB.toggled.connect(self.change)
        self.nameLE.textChanged.connect(self.change)
        self.defNameCB.toggled.connect(self.change)

        self.savePB.clicked.connect(self.save)
        self.loadPB.clicked.connect(self.load)
        self.newPB.clicked.connect(self.clearCfg)

        self.pushButton.clicked.connect(self.gen)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def gen(self):
        path = self.pathLE.text()
        if path != '':
            file = open(path+'\PORT_Config.h','w')
        else: 
            file = open('PORT_Config.h','w')
        file.write('#ifndef\tDIO_CONFIG_H\n#define\tDIO_CONFIG_H\n\n')
        file.write('#define\tHIGH\t\t1\n')
        file.write('#define\tLOW\t\t0\n')
        file.write('#define\tHIGH_IMPEDANCE\t\t0\n')
        file.write('#define\tPULL_UP\t\t1\n')
        file.write('#define\tOUTPUT\t\t1\n')
        file.write('#define\tINPUT\t\t0\n\n\n')
        letters = ['A','B','C','D']
        direction = ''
        value = ''
        for i in range(0,4):
            for j in range(0,8):
                if List[i][j][0] == True:
                    direction = 'OUTPUT'
                    if List[i][j][1] == True:
                        value = 'High'
                    else:
                        value = 'LOW'
                else:
                    direction = 'INPUT'
                    if List[i][j][2] == True:
                        value = 'HIGH_IMPEDANCE'
                    else:
                        value = 'PULL_UP'
                if List[i][j][3] == True:
                    file.write('#define\tPORT'+letters[i]+'_PIN'+ str(j) + '_DIR\t\t'+direction+'\n')
                    file.write('#define\tPORT'+letters[i]+'_PIN'+ str(j) + '_VAL\t\t'+value+'\n\n')
                else:
                    file.write('#define\tPORT'+letters[i]+'_'+ List[i][j][4] + '_DIR\t\t'+direction+'\n')
                    file.write('#define\tPORT'+letters[i]+'_'+ List[i][j][4] + '_VAL\t\t'+value+'\n\n')
        file.write('\n#endif')

                

    def save(self):
        file = open('testSave.bin','w')
        for i in range(0,4):
            for j in range(0,8):
                for k in range(0,5):
                    file.write(str(List[i][j][k])+'\n')
        file.close()

    def load(self):
        file = open('testSave.bin','r')
        for i in range(0,4):
            for j in range(0,8):
                List[i][j][0] = Bool(file.readline().strip())
                List[i][j][1] = Bool(file.readline().strip())
                List[i][j][2] = Bool(file.readline().strip())
                List[i][j][3] = Bool(file.readline().strip())
                List[i][j][4] = file.readline().strip()
        file.close()
        self.PPChange()

    def change(self):
        pin = self.pinCB.currentIndex()
        port = self.portCB.currentIndex()
        List[port][pin][0] = self.outputRB.isChecked()
        List[port][pin][1] = self.highRB.isChecked()
        List[port][pin][2] = self.highImpRB.isChecked()
        List[port][pin][3] = self.defNameCB.isChecked()
        List[port][pin][4] = self.nameLE.text()

    def clearCfg(self):
        self.pinCB.setCurrentIndex(0)
        self.portCB.setCurrentIndex(0)
        self.outputRB.setChecked(False)
        self.inputRB.setChecked(True)
        self.highRB.setChecked(True)
        self.lowRB.setChecked(False)
        self.highImpRB.setChecked(True)
        self.pullupRB.setChecked(False)
        self.defNameCB.setChecked(True)
        self.nameLE.setEnabled(False)
        self.nameLE.setText('')
        newConfigs()


    def PPChange(self):
        self.outputRB.toggled.disconnect(self.change)
        self.highRB.toggled.disconnect(self.change)
        self.pullupRB.toggled.disconnect(self.change)
        self.nameLE.textChanged.disconnect(self.change)
        self.defNameCB.toggled.disconnect(self.change)

        pin = self.pinCB.currentIndex()
        port = self.portCB.currentIndex()
        self.outputRB.setChecked(List[port][pin][0])
        self.inputRB.setChecked(not List[port][pin][0])
        self.highRB.setChecked(List[port][pin][1])
        self.lowRB.setChecked(not List[port][pin][1])
        self.highImpRB.setChecked(List[port][pin][2])
        self.pullupRB.setChecked(not List[port][pin][2])
        self.defNameCB.setChecked(List[port][pin][3])
        self.nameLE.setEnabled(not List[port][pin][3])
        self.nameLE.setText(List[port][pin][4])

        self.outputRB.toggled.connect(self.change)
        self.highRB.toggled.connect(self.change)
        self.pullupRB.toggled.connect(self.change)
        self.nameLE.textChanged.connect(self.change)
        self.defNameCB.toggled.connect(self.change)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"DIO Driver Creator", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Settings", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Pin Name", None))
        self.nameLE.setText("")
        self.nameLE.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Pin Name Here", None))
        self.defNameCB.setText(QCoreApplication.translate("Form", u"Use Default Name", None))
        self.outGB.setTitle(QCoreApplication.translate("Form", u"Output Level", None))
        self.highRB.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowRB.setText(QCoreApplication.translate("Form", u"Low", None))
        self.inGB.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.pullupRB.setText(QCoreApplication.translate("Form", u"Pull Up", None))
        self.highImpRB.setText(QCoreApplication.translate("Form", u"High Impedance", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"I/O", None))
        self.inputRB.setText(QCoreApplication.translate("Form", u"Input", None))
        self.outputRB.setText(QCoreApplication.translate("Form", u"Output", None))
        self.label.setText(QCoreApplication.translate("Form", u"Output Path", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.portCB.setItemText(0, QCoreApplication.translate("Form", u"Port A", None))
        self.portCB.setItemText(1, QCoreApplication.translate("Form", u"Port B", None))
        self.portCB.setItemText(2, QCoreApplication.translate("Form", u"Port C", None))
        self.portCB.setItemText(3, QCoreApplication.translate("Form", u"Port D", None))

        self.pinCB.setItemText(0, QCoreApplication.translate("Form", u"Pin 0", None))
        self.pinCB.setItemText(1, QCoreApplication.translate("Form", u"Pin 1", None))
        self.pinCB.setItemText(2, QCoreApplication.translate("Form", u"Pin 2", None))
        self.pinCB.setItemText(3, QCoreApplication.translate("Form", u"Pin 3", None))
        self.pinCB.setItemText(4, QCoreApplication.translate("Form", u"Pin 4", None))
        self.pinCB.setItemText(5, QCoreApplication.translate("Form", u"Pin 5", None))
        self.pinCB.setItemText(6, QCoreApplication.translate("Form", u"Pin 6", None))
        self.pinCB.setItemText(7, QCoreApplication.translate("Form", u"Pin 7", None))

        self.savePB.setText(QCoreApplication.translate("Form", u"Save Configurations", None))
        self.loadPB.setText(QCoreApplication.translate("Form", u"Load Configurations", None))
        self.newPB.setText(QCoreApplication.translate("Form", u"New Configurations", None))
    # retranslateUi

app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())