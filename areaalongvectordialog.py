#! python3
# -*- coding: utf-8 -*-

"""
/***************************************************************************
 AreaAlongVectorDialog
                                 A QGIS plugin
 Create an area along a vector depending on a field value. Right and left sides can be distinguished.
                             -------------------
        begin                : 2012-02-22
        copyright            : (C) 2012 by Alexis Dupont-Roc
        email                : alexis.dupont-roc@internet.lu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from ui_areaalongvector import Ui_AreaAlongVector
from math import *


# create the dialog for zoom to point
class AreaAlongVectorDialog(QtGui.QDialog, Ui_AreaAlongVector):
    def __init__(self, iface):
        QtGui.QDialog.__init__(self)
        #self.setupUi(self)
        # Set up the user interface from Designer.
        self.ui = Ui_AreaAlongVector()
        self.ui.setupUi(self)
        self.iface = iface
        self.settings = QSettings()
        
        # i18n support // Translation
        overrideLocale = QSettings().value("locale/overrideFlag", False)
        localeFullName = QLocale.system().name() if not overrideLocale else QSettings().value("locale/userLocale", "")
        self.localePath = os.path.dirname(__file__) + "/i18n/areaalongvector_" + localeFullName[0:2] + ".qm"
        if QFileInfo(self.localePath).exists():
            self.translator = QTranslator()
            self.translator.load(self.localePath)
            QCoreApplication.installTranslator(self.translator)
                
        self.mc = self.iface.mapCanvas()
        self.legend = self.iface.legendInterface()
        self.loaded_layers = self.legend.layers()
        # selected layer
        self.vlayer = self.mc.currentLayer()

        # Clear form
        self.ui.comboBox_inputlayer.clear()
        self.ui.lineEdit_minvalue.setText("0")
        self.ui.lineEdit_maxvalue.setText("0")
        self.ui.label_11.setText("0")
        self.ui.label_12.setText("0")

        # Default Parameters
        self.ui.lineEdit_minvaluewidth.setText("0.2")
        self.ui.lineEdit_maxvaluewidth.setText("10")

        # UI CCONNECTORS
        self.ui.buttonBox.accepted.connect(self.run)
        self.ui.buttonBox.rejected.connect(self.close)
        #self.ui.comboBox_inputlayer.currentIndexChanged.connect(self.update_fields)
        self.ui.comboBox_inputlayer.activated.connect(self.update_fields)
        self.ui.comboBox_forthfield.activated.connect(self.update_min_max_values)
        self.ui.comboBox_backfield.activated.connect(self.update_min_max_values)
        self.ui.pushButtonBrowseOutput.clicked.connect(self.output_shp_path)
        self.ui.pushButton_help.clicked.connect(self.show_help)

        # Get line layers from legend
        #vector_line_layers = self.get_useful_layers()

        # Populate comboboxes
        #self.ui.comboBox_inputlayer.addItems(vector_line_layers)
        #self.update_working_layer()
        #self.update_min_max_values()

    def init_before_show(self):
        # Get layers from legend
        self.mc = self.iface.mapCanvas()
        self.legend = self.iface.legendInterface()
        self.loaded_layers = self.legend.layers()

        # Populate comboboxes and fields
        self.ui.comboBox_inputlayer.clear()
        list_of_vlayers = self.get_useful_layers()
        if len(list_of_vlayers) > 0:
            self.ui.comboBox_inputlayer.addItems(list_of_vlayers)
            self.update_working_layer()
            self.update_fields()
        else:
            self.iface.messageBar().pushMessage("Error", "Plugin needs a valid vector layer loaded.", level=QgsMessageBar.CRITICAL, duration=5)

    def show_help(self):
        # Show help
        showPluginHelp()

    def update_working_layer(self):
        for layer in self.loaded_layers:
            if layer.name() == self.ui.comboBox_inputlayer.currentText():
                self.vlayer = layer
                break

    def get_useful_layers(self):
        """
        Code inspired from Alexandre Neto / Cascais Ambiente
        Purpose: iterate the map legend and return a list of line vector layers (with fields)
        and a list of raster layers.
        vector_line_layers is like {Layer1name:[Layer 1,[fileld1, field2, ...]], Layer2Name: [Layer 2,[fileld1, field2, ...]],...}
        """
        self.vector_line_layers = {}
        for layer in self.loaded_layers:
            fields_names = []
            # select line vector layers
            if (layer.type() == layer.VectorLayer) and (layer.geometryType() == QGis.Line):
                layer_info = [layer]
                provider = layer.dataProvider()
                fields = provider.fields()
                # get vector layer fields
                for field in fields:
                    if (field.type() == QVariant.Int or field.type() == QVariant.Double):
                        fields_names.append(field.name())
                layer_info += [fields_names]
                self.vector_line_layers[unicode(layer.name())] = layer_info
            else:
                pass
        vector_line_layers = list(self.vector_line_layers)
        return vector_line_layers

    def update_fields(self):
        self.update_working_layer()
        self.ui.comboBox_forthfield.clear()
        self.ui.comboBox_backfield.clear()
        line_layer_fields = self.vector_line_layers[self.ui.comboBox_inputlayer.currentText()][1]
        self.ui.comboBox_forthfield.addItems(line_layer_fields)
        self.ui.comboBox_backfield.addItems(line_layer_fields)
        # auto select UVP and R_UVP fields if they exist
        if 'UVP' in line_layer_fields:
            index = line_layer_fields.index('UVP')
            self.ui.comboBox_forthfield.setCurrentIndex(index)
        if 'R_UVP' in line_layer_fields:
            index = line_layer_fields.index('R_UVP')
            self.ui.comboBox_backfield.setCurrentIndex(index)
        # Update min and max values
        self.update_min_max_values()

    def run(self):
        pass
        return

    def output_shp_path(self):
        self.ui.lineEdit_outputfile.clear()
        lastDir = self.settings.value("/LabelLayer/lastDir")
        self.savelayerPath = QFileDialog.getSaveFileName(None, "Create output shapefile", lastDir, "*.shp")
        if not self.savelayerPath:
            return
        self.ui.lineEdit_outputfile.setText(self.savelayerPath)

        file_info = QFileInfo(self.savelayerPath)
        self.layer_name = file_info.completeBaseName()
        self.layer_dir = file_info.absolutePath()
        self.settings.setValue("/LabelLayer/lastDir", str(self.layer_dir))

    def update_min_max_values(self):
        if self.vlayer:

            f1 = self.ui.comboBox_forthfield.currentText()
            f2 = self.ui.comboBox_backfield.currentText()
            maxvalue = 0
            minvalue = 0

            # If no valid field found : set min and max to 0
            if (f1 != "" and f2 != ""):
                # else get min and max values from selected fields
                features = self.vlayer.getFeatures()
                for feat in features:
                    featf1value = feat[f1]
                    featf2value = feat[f2]
                    if not featf1value:
                        featf1value = 0
                    if not featf2value:
                        featf2value = 0
                    currentmaxvalue = max(featf1value, featf2value)
                    if (currentmaxvalue > maxvalue):
                        maxvalue = currentmaxvalue
                minvalue = maxvalue
                features = self.vlayer.getFeatures()
                for feat in features:
                    featf1value = feat[f1]
                    featf2value = feat[f2]
                    if not featf1value:
                        featf1value = 0
                    if not featf2value:
                        featf2value = 0
                    currentminvalue = min(featf1value, featf2value)
                    if (currentminvalue < minvalue):
                        minvalue = currentminvalue

            # update Form Labels and Fields
            self.ui.lineEdit_minvalue.setText(str(minvalue))
            self.ui.lineEdit_maxvalue.setText(str(maxvalue))
            self.ui.label_11.setText(str(minvalue))
            self.ui.label_12.setText(str(maxvalue))
