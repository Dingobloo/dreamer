from PySide import QtGui
from PySide import QtCore
from PySide.QtWebKit import QWebView

from pyside_dynamic import loadUi
import ui

class DreamWebView (QWebView):
    def __init__(self,*args):
        QWebView.__init__(self)
        print("initialized a web view");

    def mousePressEvent(self, event):
        print("Coordinates: " + str(event.x()) + "," + str(event.y()));
        self.page().mainFrame().evaluateJavaScript("$( 'div.header' ).css('position','absolute'); $( 'div.header' ).css('left',"+str(event.x())+");"+"$( 'div.header' ).css('top',"+str(event.y())+");")