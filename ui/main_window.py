from PySide import QtGui
from PySide import QtCore
from PySide import QtUiTools
from PySide.QtWebKit import QWebView
from PySide.QtCore import QUrl
from PySide.QtCore import QFile
from PySide.QtCore import QIODevice
from PySide.QtCore import QAbstractItemModel

from pyside_dynamic import loadUi
import ui
from layer_widget import LayerWidget
from page_widget import PageWidget
from dream_web_view import DreamWebView

ui_file_name = 'main_window.ui'

class MainWindow(QtGui.QMainWindow):
    def __init__(self, *args):
        QtGui.QMainWindow.__init__(self)

        loadUi(ui.UI_RESOURCE_PATH + ui_file_name, self)

        self._pages_widget = PageWidget(self)
        self.pages_dock.setWidget(self._pages_widget)

        self._layer_widget = LayerWidget(self)
        self.layer_dock.setWidget(self._layer_widget)

        self._web_view = DreamWebView(self)
        self._web_view.setUrl(":ui/resources/startup.html")
        self.setCentralWidget(self._web_view)

        self._web_view.loadFinished.connect(self.webLoadFinished)

        #self.propertiesTable.setModel(self)
        item = PropertiesItemModel(self)
        #print(dir(item))

    def webLoadFinished(self, loaded):
        print("We loaded a web page")

        infile = QFile(self)
        infile.setFileName("ui/resources/jquery-1.9.1.js")

        if not infile.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            print("Error opening file: " + infile.errorString())

        stream = QtCore.QTextStream(infile)
        self.jQuery = stream.readAll()
        infile.close()

        print("We loaded jQuery")

        self._web_view.page().mainFrame().evaluateJavaScript(self.jQuery)

        print("We evaluated jQuery")

        self._web_view.page().mainFrame().evaluateJavaScript("$( 'h1.header' ).css( '-webkit-transition', '-webkit-transform 2s'); $( 'h1.header' ).css('-webkit-transform', 'rotate(360deg)')")

        print("Run some simple jQuery")

    @QtCore.Slot()
    def _on_action_new_layer(self):
        self._layer_widget.new_layer()
        print("A new layer was added")


class PropertiesItemModel(QAbstractItemModel):
    def __init(self):
        print("Initialising an item model")
