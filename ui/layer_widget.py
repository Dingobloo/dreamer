from PySide import QtGui
from PySide import QtCore

from pyside_dynamic import loadUi
import ui

ui_file_name = 'layer_widget.ui'
class LayerWidget(QtGui.QWidget):
    def __init__(self, *args):
        QtGui.QWidget.__init__(self)
        loadUi(ui.UI_RESOURCE_PATH + ui_file_name, self)

        #layer_list = ['duh', 'bluh', 'meh']
        #self.layer_model = LayerListModel(layer_list)
        #self.listView.setModel(self.layer_model)
        self.listView.setAlternatingRowColors(True)

    def set_model(self, model):
        self.layer_model = model
        self.listView.setModel(self.layer_model)

    def new_layer(self):
        #self.layer_model.setData(2, 'HI')
        self.layer_model.addItem('pleh')


class LayerListModel(QtCore.QAbstractListModel):
    def __init__(self, layers, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._layers = layers

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self._layers[index.row()].layer_name
        elif role == QtCore.Qt.EditRole:
            return self._layers[index.row()].layer_name

    def rowCount(self, parent):
        return len(self._layers)

    def flags(self, index):
        if(not index.isValid()):
            return QtCore.Qt.ItemIsEnabled

        return QtCore.QAbstractListModel.flags(self,index) | QtCore.Qt.ItemIsEditable
    
    def addItem(self, item):
        self.beginInsertRows(QtCore.QModelIndex(), len(self._layers), len(self._layers))
        self._layers.append(item)
        self.endInsertRows()
    
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            self._layers[index.row()].layer_name = value
            QtCore.QObject.emit(self, QtCore.SIGNAL("dataChanged(const QModelIndex&, const QModelIndex &)"), index, index)
            return True
        return False

class Layer:
    def __init__(self, layerName):
        self._layer_name = layerName

    @property
    def layer_name(self):
        return self._layer_name

    @layer_name.setter
    def layer_name(self, value):
        self._layer_name = value

