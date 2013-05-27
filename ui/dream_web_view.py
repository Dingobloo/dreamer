from PySide import QtGui
from PySide import QtCore
from PySide.QtWebKit import QWebView
from PySide.QtWebKit import QWebElement

from pyside_dynamic import loadUi
import ui

class DreamWebView (QWebView):
    #Need to expose the mouse events as signals to loosely couple the tools to the view
    mousePressSignal = QtCore.Signal(QtGui.QMouseEvent)
    mouseMoveSignal = QtCore.Signal(QtGui.QMouseEvent)
    mouseReleaseSignal = QtCore.Signal(QtGui.QMouseEvent)

    def __init__(self,*args):
        QWebView.__init__(self)
        #self._mouseMove = False
        #self.mouseX = 0
        #self.mouseY = 0

    def mousePressEvent(self, event):
        self.mousePressSignal.emit(event);
        #self._mouseMove = True
        #self.document = self.page().mainFrame().documentElement()
        #self.element = self.document.findFirst("div.header")
        #self.mouseX = self.mouseX - event.x()
        #self.mouseY = self.mouseY - event.y()

    def mouseMoveEvent(self, event):
        self.mouseMoveSignal.emit(event);
        #if self._mouseMove:
            #self.element.setStyleProperty("position", "absolute")
            #self.element.setStyleProperty("left", str(event.x() + self.mouseX))
            #self.element.setStyleProperty("top",  str(event.y() + self.mouseY))

    def mouseReleaseEvent(self, event):
        self.mouseReleaseSignal.emit(event);
        #self.mouseX = event.x() + self.mouseX
        #self.mouseY = event.y() + self.mouseY
        #self._mouseMove = False;
