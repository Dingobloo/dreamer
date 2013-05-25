from PySide import QtGui
from PySide import QtCore

from pyside_dynamic import loadUi
import ui

ui_file_name = 'page_widget.ui'
class PageWidget(QtGui.QWidget):
    def __init__(self, *args):
        QtGui.QWidget.__init__(self)
        loadUi(ui.UI_RESOURCE_PATH + ui_file_name, self)

        page_list = ['Page1', 'Page2', 'Page3']
        self.page_model = PageListModel(page_list)
        self.listView.setModel(self.page_model)
        self.listView.setAlternatingRowColors(True)

    def new_layer(self):
        #self.layer_model.setData(2, 'HI')
        self.layer_model.addItem('pleh')


class PageListModel(QtCore.QAbstractListModel):
    def __init__(self, pages, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._pages = pages

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._pages[index.row()]
        elif role == QtCore.Qt.EditRole:
            return self._pages[index.row()]

    def rowCount(self, parent):
        return len(self._pages)

    def addItem(self, item):
        self.beginInsertRows(QtCore.QModelIndex(), len(self._pages), len(self._layers))
        self._pages.append(item)
        self.endInsertRows()
    
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            self._pages[index] = value
            QtCore.QObject.emit(self, QtCore.SIGNAL("dataChanged(const QModelIndex&, const QModelIndex &)"), index, index)
            return True
        return False
