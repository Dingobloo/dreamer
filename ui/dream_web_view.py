from PySide import QtGui
from PySide import QtCore
from PySide.QtWebKit import QWebView
from PySide.QtWebKit import QWebElement

from pyside_dynamic import loadUi
import ui

class DreamWebView (QWebView):
    def __init__(self,*args):
        QWebView.__init__(self)
        print("initialized a web view")
        self._mouseMove = False
        self.mouseX = 0
        self.mouseY = 0

    def mousePressEvent(self, event):
        self._mouseMove = True
        self.document = self.page().mainFrame().documentElement()
        self.element = self.document.findFirst("div.header")
        self.mouseX = self.mouseX - event.x()
        self.mouseY = self.mouseY - event.y()
        #self.element.setAttribute("style", "background-color: #f0f090");
        #I'd like to convert this to non-jquery accessing the CSS directly through it's element eventually.
        #self.page().mainFrame().evaluateJavaScript( "$( 'div.header' ).css('position','absolute'); \
        #                                             $( 'div.header' ).css('left'," + str(event.x()) + ");" +
        #                                            "$( 'div.header' ).css('top',"+str(event.y()) + ");")

    def mouseMoveEvent(self, event):
        if self._mouseMove:
            self.element.setAttribute("style","position: absolute; left: " + str(event.x() + self.mouseX) + "; top: " + str(event.y() + self.mouseY) + ";")
            #self.page().mainFrame().evaluateJavaScript( "$( 'div.header' ).css('position','absolute'); \
            #                                             $( 'div.header' ).css('left'," + str(event.x()) + ");" +
            #                                            "$( 'div.header' ).css('top',"+str(event.y()) + ");")
    def mouseReleaseEvent(self, event):
        #print("Coordinates: " + str(event.x()) + "," + str(event.y()))
        self.mouseX = event.x() + self.mouseX
        self.mouseY = event.y() + self.mouseY
        self._mouseMove = False;
