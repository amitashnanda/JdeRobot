#
#  Copyright (C) 1997-2016 JDE Developers Team
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see http://www.gnu.org/licenses/.
#  Authors :
#       Alberto Martin Florido <almartinflorido@gmail.com>
#       Aitor Martinez Fernandez <aitor.martinez.fernandez@gmail.com>
#


from PyQt5.QtCore import pyqtSignal, Qt, QRect
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from gui.communicator import Communicator
from gui.imagesWidget import  ImagesWidget
from gui.controlWidget import  ControlWidget
from  sensors.cameraFilter import RGBLimits, YUVLimits, HSVLimits

class MainWindow(QMainWindow):
    
    updGUI=pyqtSignal()
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Color tuner")

        self.iWidget = ImagesWidget(self)
        self.cWidget = ControlWidget(self)
        
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QRect(20, 30, 361, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.vLayout.setObjectName("vLayout")
        self.vLayout.addWidget(self.iWidget)
        self.vLayout.addWidget(self.cWidget)

        self.iWidget.setVisible(True)
        self.cWidget.setVisible(True)

        self.updGUI.connect(self.updateGUI)

        #self.controlCommunicator=Communicator()
        #self.imageCommunicator=Communicator()

        #self.setLayout(self.vLayout)
        self.setCentralWidget(self.verticalLayoutWidget)

        self.filt = 'Orig'

        self.rgbLimits = RGBLimits()
        self.yuvLimits = YUVLimits()
        self.hsvLimits = HSVLimits()


      
    def getCamera(self):
        return self.camera

    def setCamera(self,camera):
        self.camera = camera

    def getFilter(self):
        return self.filt

    def setFilter(self,filt):
        self.filt = filt
    
    def updateGUI(self):
        self.iWidget.imageUpdate.emit()
        #self.cWidget.controlUpdate.emit()

    def closeEvent(self, event):
        self.camera.stop()
        event.accept()