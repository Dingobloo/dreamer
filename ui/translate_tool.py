from PySide import QtGui
from PySide import QtCore

from pyside_dynamic import loadUi
import ui

class TranslateTool (QtCore.QObject):
    def __init__(self,DreamWebView):
        QtCore.QObject.__init__(self)
        print("Creating the translate tool")
        #Listen to the web view for mouse events
        DreamWebView.mousePressSignal.connect(self.mousePress)
        DreamWebView.mouseMoveSignal.connect(self.mouseMove)
        DreamWebView.mouseReleaseSignal.connect(self.mouseRelease)

        self._web_view = DreamWebView

        self._mouseMove = False
        self.mouseX = 0
        self.mouseY = 0
        
    def mousePress(self,event):
        print("Starting mouse click: "+str(event.x())+ "," + str(event.y()))
        self._mouseMove = True
        self.document = self._web_view.page().mainFrame().documentElement()
        #need current layer (let the layer control the layer element)
        self.element = self.document.findFirst("div.header")
        #current layer position instead of self.MouseX initial
        self.mouseX = self.mouseX - event.x()
        self.mouseY = self.mouseY - event.y()

    def mouseMove(self,event):
        if self._mouseMove:
            #we should instead set the layer location and have the layer itself talk to the style/element
            self.element.setStyleProperty("position", "absolute")
            self.element.setStyleProperty("left", str(event.x() + self.mouseX))
            self.element.setStyleProperty("top",  str(event.y() + self.mouseY))

    def mouseRelease(self, event):
        #this might be redundant once hooked up
        self.mouseX = event.x() + self.mouseX
        self.mouseY = event.y() + self.mouseY
        self._mouseMove = False;

