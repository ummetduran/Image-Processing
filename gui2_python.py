# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ummet/OneDrive/Masaüstü/pyqt/gui2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog
import cv2 as cv
from pandas import np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1273, 839)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("#MainWindow { border-image: url(ip2.jpg) 0 0 0 0 stretch stretch; }\n"
                                 "font: 75 11pt \"MS Shell Dlg 2\";\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.orj_text_label = QtWidgets.QLabel(self.centralwidget)
        self.orj_text_label.setGeometry(QtCore.QRect(210, 110, 171, 61))
        self.orj_text_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"background:transparent")
        self.orj_text_label.setObjectName("orj_text_label")
        self.islenmis_text_label = QtWidgets.QLabel(self.centralwidget)
        self.islenmis_text_label.setGeometry(QtCore.QRect(850, 110, 201, 61))
        self.islenmis_text_label.setStyleSheet("background:transparent")
        self.islenmis_text_label.setObjectName("islenmis_text_label")
        self.orj_resim_label = QtWidgets.QLabel(self.centralwidget)
        self.orj_resim_label.setGeometry(QtCore.QRect(80, 210, 581, 511))
        self.orj_resim_label.setStyleSheet("background:transparent")
        self.orj_resim_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.orj_resim_label.setText("")
        self.orj_resim_label.setTextFormat(QtCore.Qt.PlainText)
        self.orj_resim_label.setWordWrap(False)
        self.orj_resim_label.setObjectName("orj_resim_label")
        self.islenmis_resim_label = QtWidgets.QLabel(self.centralwidget)
        self.islenmis_resim_label.setGeometry(QtCore.QRect(670, 210, 581, 511))
        self.islenmis_resim_label.setStyleSheet("background-color: rgba(255, 255, 255, 10);\n"
"background-color: rgba(255, 255, 255, 10);\n"
"background-color:rgba(182,159,64,230);\n"
"background:transparent\n"
"")
        self.islenmis_resim_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.islenmis_resim_label.setText("")
        self.islenmis_resim_label.setTextFormat(QtCore.Qt.PlainText)
        self.islenmis_resim_label.setWordWrap(False)
        self.islenmis_resim_label.setObjectName("islenmis_resim_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1273, 30))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuGoruntuyilestirme_islemleri = QtWidgets.QMenu(self.menubar)
        self.menuGoruntuyilestirme_islemleri.setObjectName("menuGoruntuyilestirme_islemleri")
        self.menuHistogram = QtWidgets.QMenu(self.menubar)
        self.menuHistogram.setObjectName("menuHistogram")
        self.menuUzaysal_Donusum_islemleri = QtWidgets.QMenu(self.menubar)
        self.menuUzaysal_Donusum_islemleri.setObjectName("menuUzaysal_Donusum_islemleri")
        self.menuYogunluk_Donum_islemleri = QtWidgets.QMenu(self.menubar)
        self.menuYogunluk_Donum_islemleri.setObjectName("menuYogunluk_Donum_islemleri")
        self.menuMorfolojikislemler = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.menuMorfolojikislemler.setFont(font)
        self.menuMorfolojikislemler.setObjectName("menuMorfolojikislemler")
        self.instagram_filter = QtWidgets.QMenu(self.menubar)
        self.menuGoruntuyilestirme_islemleri.setObjectName("menuinstagram_filter")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow.show())


        self.actionAc = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.actionAc.setFont(font)
        self.actionAc.setObjectName("actionAc")
        self.actionKaydet = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionKaydet.setFont(font)
        self.actionKaydet.setObjectName("actionKaydet")
        self.actionBlur = QtWidgets.QAction(MainWindow)
       # self.actionBlur.setCheckable(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionBlur.setFont(font)
        self.actionBlur.setVisible(True)
        self.actionBlur.setObjectName("actionBlur")
        self.actionCanny = QtWidgets.QAction(MainWindow)
        #self.actionCanny.setCheckable(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionCanny.setFont(font)
        self.actionCanny.setObjectName("actionCanny")
        self.actionBilateral = QtWidgets.QAction(MainWindow)
       # self.actionBilateral.setCheckable(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionBilateral.setFont(font)
        self.actionBilateral.setObjectName("actionBilateral")
        self.actionMedian = QtWidgets.QAction(MainWindow)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionMedian.setFont(font)
        self.actionMedian.setObjectName("actionMedian")
        self.actionGaussian = QtWidgets.QAction(MainWindow)
        #self.actionGaussian.setCheckable(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionGaussian.setFont(font)
        self.actionGaussian.setObjectName("actionGaussian")
        self.actionLaplace = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionLaplace.setFont(font)
        self.actionLaplace.setObjectName("actionLaplace")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        #self.actionSobel.setCheckable(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionSobel.setFont(font)
        self.actionSobel.setObjectName("actionSobel")
        self.actionFilter2D = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionFilter2D.setFont(font)
        self.actionFilter2D.setObjectName("actionFilter2D")
        self.actionSharpening = QtWidgets.QAction(MainWindow)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionSharpening.setFont(font)
        self.actionSharpening.setObjectName("actionSharpening")
        self.actionBoxFilter = QtWidgets.QAction(MainWindow)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionBoxFilter.setFont(font)
        self.actionBoxFilter.setObjectName("actionBoxFilter")
        self.actionGoruntuleme = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionGoruntuleme.setFont(font)
        self.actionGoruntuleme.setObjectName("actionGoruntuleme")
        self.actionEsitleme = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionEsitleme.setFont(font)
        self.actionEsitleme.setObjectName("actionEsitleme")
        self.actionCropping = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionCropping.setFont(font)
        self.actionCropping.setObjectName("actionCropping")
        self.actionResize = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionResize.setFont(font)
        self.actionResize.setObjectName("actionResize")
        self.actionFlip = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionFlip.setFont(font)
        self.actionFlip.setObjectName("actionFlip")
        self.action90_Rotate = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.action90_Rotate.setFont(font)
        self.action90_Rotate.setObjectName("action90_Rotate")
        self.action180_Rotate = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.action180_Rotate.setFont(font)
        self.action180_Rotate.setObjectName("action180_Rotate")
        self.actionLogaritmik = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionLogaritmik.setFont(font)
        self.actionLogaritmik.setObjectName("actionLogaritmik")
        self.actionGamma = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionGamma.setFont(font)
        self.actionGamma.setObjectName("actionGamma")
        self.actionConrast = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionConrast.setFont(font)
        self.actionConrast.setObjectName("actionConrast")
        self.actionDilation = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionDilation.setFont(font)
        self.actionDilation.setObjectName("actionDilation")
        self.actionOpening = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionOpening.setFont(font)
        self.actionOpening.setObjectName("actionOpening")
        self.actionClosing = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionClosing.setFont(font)
        self.actionClosing.setObjectName("actionClosing")
        self.actionCross = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionCross.setFont(font)
        self.actionCross.setObjectName("actionCross")
        self.actionElips = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionElips.setFont(font)
        self.actionElips.setObjectName("actionElips")
        self.actionGradient = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionGradient.setFont(font)
        self.actionGradient.setObjectName("actionGradient")
        self.actionTophat = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionTophat.setFont(font)
        self.actionTophat.setObjectName("actionTophat")
        self.actionErosion = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionErosion.setFont(font)
        self.actionErosion.setObjectName("actionErosion")
        self.actionBlackhat = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionBlackhat.setFont(font)
        self.actionBlackhat.setObjectName("actionBlackhat")
        self.actionRect = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionRect.setFont(font)
        self.actionRect.setObjectName("actionRect")
        self.actionFilter1=QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actionFilter1.setFont(font)
        self.actionFilter1.setObjectName("actionFilter1")

        self.menuEdit.addAction(self.actionAc)

        self.actionAc.triggered.connect(self.openFile)

        self.menuEdit.addAction(self.actionKaydet)
        self.actionKaydet.triggered.connect(self.saveFile)
        self.menuGoruntuyilestirme_islemleri.addAction(self.actionBlur)
        self.actionBlur.triggered.connect(self.Blur)
        self.menuGoruntuyilestirme_islemleri.addAction(self.actionCanny)
        self.actionCanny.triggered.connect(self.Canny)
        self.menuGoruntuyilestirme_islemleri.addAction(self.actionBilateral)
        self.actionBilateral.triggered.connect(self.Bilateral)
        self.menuGoruntuyilestirme_islemleri.addAction(self.actionMedian)
        self.actionMedian.triggered.connect(self.Median)
        self.menuGoruntuyilestirme_islemleri.addAction(self.actionGaussian)
        self.actionGaussian.triggered.connect(self.Gaussian)
        self.menuGoruntuyilestirme_islemleri.addAction(self.actionLaplace)
        self.actionLaplace.triggered.connect(self.Laplace)
        self.menuGoruntuyilestirme_islemleri.addAction(self.actionSobel)
        self.actionSobel.triggered.connect(self.Sobel)
        self.menuGoruntuyilestirme_islemleri.addAction(self.actionFilter2D)
        self.actionFilter2D.triggered.connect(self.Filter2D)
        self.menuGoruntuyilestirme_islemleri.addAction(self.actionSharpening)
        self.actionSharpening.triggered.connect(self.Sharpening)

        self.menuGoruntuyilestirme_islemleri.addAction(self.actionBoxFilter)
        self.actionBoxFilter.triggered.connect(self.BoxFilter)
        self.menuHistogram.addAction(self.actionGoruntuleme)
        self.menuHistogram.addAction(self.actionEsitleme)
        self.actionGoruntuleme.triggered.connect(self.HistogramGoruntuleme)
        self.actionEsitleme.triggered.connect(self.HistogramEsitleme)
        self.menuUzaysal_Donusum_islemleri.addAction(self.actionCropping)
        self.actionCropping.triggered.connect(self.Cropping)
        self.menuUzaysal_Donusum_islemleri.addAction(self.actionResize)
        self.actionResize.triggered.connect(self.Resize)
        self.menuUzaysal_Donusum_islemleri.addAction(self.actionFlip)
        self.actionFlip.triggered.connect(self.Flip)
        self.menuUzaysal_Donusum_islemleri.addAction(self.action90_Rotate)
        self.action90_Rotate.triggered.connect(self.DoksanRotate)
        self.menuUzaysal_Donusum_islemleri.addAction(self.action180_Rotate)
        self.action180_Rotate.triggered.connect(self.YuzseksenRotate)
        self.menuYogunluk_Donum_islemleri.addAction(self.actionLogaritmik)
        self.actionLogaritmik.triggered.connect(self.Logaritmik)
        self.menuYogunluk_Donum_islemleri.addAction(self.actionGamma)
        self.actionGamma.triggered.connect(self.Gamma)
        self.menuYogunluk_Donum_islemleri.addAction(self.actionConrast)
        self.actionConrast.triggered.connect(self.Contrast)
        self.menuMorfolojikislemler.addAction(self.actionDilation)
        self.actionDilation.triggered.connect(self.Dilation)
        self.menuMorfolojikislemler.addAction(self.actionOpening)
        self.actionOpening.triggered.connect(self.Opening)
        self.menuMorfolojikislemler.addAction(self.actionClosing)
        self.actionClosing.triggered.connect(self.Closing)
        self.menuMorfolojikislemler.addAction(self.actionCross)
        self.actionCross.triggered.connect(self.Cross)
        self.menuMorfolojikislemler.addAction(self.actionElips)
        self.actionElips.triggered.connect(self.Elipse)
        self.menuMorfolojikislemler.addAction(self.actionGradient)
        self.actionGradient.triggered.connect(self.Gradient)
        self.menuMorfolojikislemler.addAction(self.actionTophat)
        self.actionTophat.triggered.connect(self.Tophat)
        self.menuMorfolojikislemler.addAction(self.actionErosion)
        self.actionErosion.triggered.connect(self.Erosion)
        self.menuMorfolojikislemler.addAction(self.actionBlackhat)
        self.actionBlackhat.triggered.connect(self.BlackHat)
        self.menuMorfolojikislemler.addAction(self.actionRect)
        self.actionRect.triggered.connect(self.Rect)
        self.instagram_filter.addAction(self.actionFilter1)
        self.actionFilter1.triggered.connect(self.InstagramFilter)
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuGoruntuyilestirme_islemleri.menuAction())
        self.menubar.addAction(self.menuHistogram.menuAction())
        self.menubar.addAction(self.menuUzaysal_Donusum_islemleri.menuAction())
        self.menubar.addAction(self.menuYogunluk_Donum_islemleri.menuAction())
        self.menubar.addAction(self.menuMorfolojikislemler.menuAction())
        self.menubar.addAction(self.instagram_filter.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.orj_text_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Orjinal Resim</span></p></body></html>"))
        self.islenmis_text_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">İşlenmiş Resim</span></p></body></html>"))
        self.menuEdit.setTitle(_translate("MainWindow", "Dosya"))
        self.menuGoruntuyilestirme_islemleri.setTitle(_translate("MainWindow", "Görüntü İyileştrime İşlemleri"))
        self.menuHistogram.setTitle(_translate("MainWindow", "Histogram"))
        self.menuUzaysal_Donusum_islemleri.setTitle(_translate("MainWindow", "Uzaysal Dönüşüm İşlemleri"))
        self.menuYogunluk_Donum_islemleri.setTitle(_translate("MainWindow", "Yoğunluk Dönüşüm işlemleri"))
        self.menuMorfolojikislemler.setTitle(_translate("MainWindow", "Morfolojik İşlemler"))
        self.instagram_filter.setTitle(_translate("Main Window", "Instagram Filtresi"))
        self.actionAc.setText(_translate("MainWindow", "Aç"))
        self.actionKaydet.setText(_translate("MainWindow", "Kaydet"))
        self.actionBlur.setText(_translate("MainWindow", "Blur"))
        self.actionCanny.setText(_translate("MainWindow", "Canny"))
        self.actionBilateral.setText(_translate("MainWindow", "Bilateral"))
        self.actionMedian.setText(_translate("MainWindow", "Median"))
        self.actionGaussian.setText(_translate("MainWindow", "Gaussian"))
        self.actionLaplace.setText(_translate("MainWindow", "Laplace"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionFilter2D.setText(_translate("MainWindow", "Filter2D"))
        self.actionSharpening.setText(_translate("MainWindow", "Sharpening"))
        self.actionBoxFilter.setText(_translate("MainWindow", "BoxFilter"))
        self.actionGoruntuleme.setText(_translate("MainWindow", "Görüntüleme"))
        self.actionEsitleme.setText(_translate("MainWindow", "Eşitleme"))
        self.actionCropping.setText(_translate("MainWindow", "Cropping"))
        self.actionResize.setText(_translate("MainWindow", "Resize"))
        self.actionFlip.setText(_translate("MainWindow", "Flip"))
        self.action90_Rotate.setText(_translate("MainWindow", "90 Rotate"))
        self.action180_Rotate.setText(_translate("MainWindow", "180 Rotate"))
        self.actionLogaritmik.setText(_translate("MainWindow", "Logaritmik"))
        self.actionGamma.setText(_translate("MainWindow", "Gamma"))
        self.actionConrast.setText(_translate("MainWindow", "Conrast"))
        self.actionDilation.setText(_translate("MainWindow", "Dilation"))
        self.actionOpening.setText(_translate("MainWindow", "Opening"))
        self.actionClosing.setText(_translate("MainWindow", "Closing"))
        self.actionCross.setText(_translate("MainWindow", "Cross"))
        self.actionElips.setText(_translate("MainWindow", "Elips"))
        self.actionGradient.setText(_translate("MainWindow", "Gradient"))
        self.actionTophat.setText(_translate("MainWindow", "Tophat"))
        self.actionErosion.setText(_translate("MainWindow", "Erosion"))
        self.actionBlackhat.setText(_translate("MainWindow", "Blackhat"))
        self.actionRect.setText(_translate("MainWindow", "Rect"))
        self.actionFilter1.setText(_translate("MainWindow", "Filter1"))

    def openFile(self):
        MainWindow.show()
        fname, _ = QFileDialog.getOpenFileName(None, 'Fotograf Seciniz', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp )')
        if fname:
            with open(fname, "rb") as file:
                data = np.array(bytearray(file.read()))
                self.image = cv.imdecode(data, cv.IMREAD_UNCHANGED)
                self.image = self.olceklendir(self.image)
                self.openImage()
    def openImage(self):
        size = self.image.shape
        step = self.image.size / size[0]
        qformat = QImage.Format_Indexed8

        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(self.image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()

        self.orj_resim_label.setPixmap(QPixmap.fromImage(img))

    def processedImg(self):
        size = self.image.shape
        step = self.image.size / size[0]
        qformat = QImage.Format_Indexed8

        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(self.image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()
        self.islenmis_resim_label.setPixmap(QPixmap.fromImage(img))
        cv.waitKey(0)


#TODO: kontrol et
    def saveFile(self):
            fname=QFileDialog.getSaveFileName(None, "Save Image", "",
                         "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
            if fname == "":
                return
            self.image.save(fname)
            cv.imwrite(fname, self.image)

    def olceklendir(self, img):
            img = cv.resize(img, (600, 800))
            return img

    def Bilateral(self):
        if self.image is not None:
            self.image=cv.bilateralFilter(self.image,15,75,75)
            self.processedImg()


    def Blur(self):
        if self.image is not None:
            self.image=cv.blur(self.image,(5,5))
            self.processedImg()

    # TODO:
    def Laplace(self):
        src_gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        if self.image is not None:
            self.image=cv.Laplacian(src_gray, cv.CV_8U)
            self.processedImg()
    def Canny(self):
        if self.image is not None:
            self.image=cv.Canny(self.image, 100,200)
            self.processedImg()

    def Gaussian(self):

        if self.image is not None:
            self.image= cv.GaussianBlur(self.image,(5,5),0)
            self.processedImg()
    def Median(self):

        if self.image is not None:
            self.image= cv.medianBlur(self.image, ksize=5)
            self.processedImg()

    def Sobel(self):
        if self.image is not None:
            self.image=cv.Sobel(self.image, cv.CV_8U,1,0,ksize=5)
            self.processedImg()

    def Filter2D(self):
        if self.image is not None:
            kernel=np.ones((5,5),np.float32)/25
            self.image=cv.filter2D(self.image,-1,kernel)
            self.processedImg()

    def Sharpening(self):
        if self.image is not None:
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            self.image = cv.filter2D(self.image, -1, kernel)
            self.processedImg()

    def BoxFilter(self):
        if self.image is not None:
            self.image = cv.boxFilter(self.image, 0, (3, 3), self.image, (-1, -1), False, cv.BORDER_DEFAULT)
            self.processedImg()
    def HistogramEsitleme(self):
        if self.image is not None:
            src = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
            self.image=cv.equalizeHist(src)
            self.processedImg()
    def HistogramGoruntuleme(self):
        from matplotlib import pyplot as plt
        if self.image is not None:
            plt.hist(self.image.ravel(),256,[0,256])
            plt.show()
            self.processedImg()

    def Resize(self):
        from skimage.transform import resize
        if self.image is not None:
            self.image = resize(self.image, (350, 350), order=0, preserve_range=True, anti_aliasing=False).astype('uint8')
            self.processedImg()
    def Cropping(self):
        if self.image is not None:

            self.image = self.image[1:250 ,1:250]
            self.image =cv.resize(self.image,(500,500))
            self.processedImg()

    def Flip(self):
        if self.image is not None:
            self.image = cv.flip(self.image, 1, None)
            self.processedImg()

    def DoksanRotate(self):
        if self.image is not None:
            (h, w) = self.image.shape[:2]
            center = (w / 2, h / 2)
            M = cv.getRotationMatrix2D(center, 90, 1)
            self.image = cv.warpAffine(self.image, M, (h, w))
            self.processedImg()

    def YuzseksenRotate(self):
        if self.image is not None:
            (h, w) = self.image.shape[:2]
            center = (w / 2, h / 2)
            M = cv.getRotationMatrix2D(center, 180, 1)
            self.image = cv.warpAffine(self.image, M, (h, w))
            self.processedImg()

    def Dilation(self):
        if self.image is not None:
            kernelDilation = np.ones((15, 15), np.uint8)
            self.image = cv.dilate(self.image, kernelDilation, iterations=1)
            self.processedImg()

    def Opening(self):
        if self.image is not None:
            kernelDilation = np.ones((15, 15), np.uint8)
            self.image=cv.morphologyEx(self.image, cv.MORPH_OPEN, kernelDilation)
            self.processedImg()

    def Closing(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv.morphologyEx(self.image, cv.MORPH_CLOSE, kernel)
            self.processedImg()

    def Cross(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv.morphologyEx(self.image, cv.MORPH_CROSS, kernel)
            self.processedImg()

    def Elipse(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv.morphologyEx(self.image, cv.MORPH_ELLIPSE, kernel)
            self.processedImg()

    def Gradient(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv.morphologyEx(self.image, cv.MORPH_GRADIENT, kernel)
            self.processedImg()

    def Tophat(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv.morphologyEx(self.image, cv.MORPH_TOPHAT, kernel)
            self.processedImg()

    def Erosion(self):
        if self.image is not None:
            kernelErosion = np.ones((5, 5), np.uint8)
            self.image = cv.erode(self.image, kernelErosion, iterations=1)
            self.processedImg()

    def BlackHat(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv.morphologyEx(self.image, cv.MORPH_BLACKHAT, kernel)
            self.processedImg()

    def Rect(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.image = cv.morphologyEx(self.image, cv.MORPH_RECT, kernel)
            self.processedImg()
    def Logaritmik(self):
        if self.image is not None:
            log_degeri=int(input("Logaritmik değeri giriniz: "))
            c = log_degeri / (np.log10(1 + np.max(self.image)))
            self.log_transformed = c * np.log10(1 + self.image)
            self.image = np.array(self.log_transformed, dtype=np.uint8)
            self.processedImg()

    def Gamma(self):
        if self.image is not None:
            gamma=float(input("Gamma: "))
            gamma_corrected = np.array(255 * (self.image / 255) ** gamma, dtype='uint8')
            self.image=gamma_corrected
            self.processedImg()
    def Contrast(self):
        if self.image is not None:
            self.image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
            r1 = int(input("r1 : "))
            s1 = int(input("s1 : "))
            r2 = int(input("r2 : "))
            s2 = int(input("s2 : "))

            def pixelVal(pix, r1, s1, r2, s2):
                if (0 <= pix and pix <= r1):
                    return (s1 / r1) * pix
                elif (r1 < pix and pix <= r2):
                    return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
                else:
                    return ((255 - s2) / (255 - r2)) * (pix - r2) + s2

            pixelVal_vec = np.vectorize(pixelVal)

            contrast_stretched = pixelVal_vec(self.image, r1, s1, r2, s2)
            cv.imshow("Contrast", contrast_stretched)
    def InstagramFilter(self):
        self.HistogramEsitleme()
        self.Sharpening()
        self.Gaussian()
        self.Gamma()
        self.processedImg()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ex = Ui_MainWindow()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
