#! python3

"""
/***************************************************************************
 AreaAlongVector
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import os.path
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from areaalongvectordialog import AreaAlongVectorDialog
#Import own classes and tools
from parallelpolygon import *
import cadutils


class AreaAlongVector:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'test_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        self.dlg = AreaAlongVectorDialog(self.iface)
        #self.dlg = AreaAlongVectorDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/areaalongvector/icon.png"), "Area along vector", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Area along vector", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Area along vector", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.init_before_show()
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            self.draw_side_areas()

    def draw_side_areas(self):
        # Parameters

        # Chosen input layer
        line_vlayer = self.dlg.vlayer
        # Output file name
        shapefileOutputName = self.dlg.ui.lineEdit_outputfile.text()
        # Drawing parameters
        userminlimit = float(self.dlg.ui.lineEdit_minvalue.text())
        usermaxlimit = float(self.dlg.ui.lineEdit_maxvalue.text())
        userminwidth = float(self.dlg.ui.lineEdit_minvaluewidth.text())
        usermaxwidth = float(self.dlg.ui.lineEdit_maxvaluewidth.text())

        # New fields
        fields = QgsFields()
        fields.append(QgsField("WAY", QVariant.Int))
        fields.append(QgsField("VAL", QVariant.Int))
        #fields.append(QgsField( "desc", QVariant.String ))

        # Create an instance of vector file writer, it will create the vector file.
        writer = QgsVectorFileWriter(shapefileOutputName, "utf-8", fields, QGis.WKBPolygon, None, "ESRI Shapefile")
        if writer.hasError() != QgsVectorFileWriter.NoError:
            self.iface.messageBar().pushMessage("Error", "Error when creating shapefile:{0}\n".format(shapefileOutputName), level=QgsMessageBar.CRITICAL, duration=5)
            return

        # Get back and forth fields name
        f1_name = self.dlg.ui.comboBox_forthfield.currentText()
        f2_name = self.dlg.ui.comboBox_backfield.currentText()

        # retreive every feature with its geometry and attributes
        #feat = QgsFeature()
        features = line_vlayer.getFeatures()
        number_of_features = line_vlayer.featureCount()
        feat_counter = 0
        for feat in features:
            # Update progressBar
            feat_counter += 1
            percent = feat_counter * 100 / number_of_features
            self.iface.mainWindow().statusBar().showMessage("Processed {} %".format(int(percent)))

            # fetch geometry
            geom = feat.geometry()

            # get information about the feature
            if geom.type() == QGis.Line:
                x = geom.asPolyline()
                for i in range(0, len(x) - 1):

                    # Read field values as int
                    fieldValueForth = feat[f1_name]
                    fieldValueBack = feat[f2_name]

                    # Distance calculation
                    distR = calculateDistance(fieldValueForth, userminlimit, userminwidth, usermaxlimit, usermaxwidth)
                    distL = calculateDistance(fieldValueBack, userminlimit, userminwidth, usermaxlimit, usermaxwidth)

                    # add right rectangle
                    fields = line_vlayer.pendingFields()
                    fetR = QgsFeature(fields)
                    fetR.setGeometry(QgsGeometry.fromPolygon([calculateRightPolygon(x[i], x[i + 1], distR)]))
                    fetR[0] = 1
                    fetR[1] = fieldValueForth
                    writer.addFeature(fetR)

                    # add left rectangle
                    fetL = QgsFeature(fields)
                    fetL.setGeometry(QgsGeometry.fromPolygon([calculateLeftPolygon(x[i], x[i + 1], distL)]))
                    fetL[0] = 2
                    fetL[1] = fieldValueBack
                    writer.addFeature(fetL)
            else:
                self.iface.messageBar().pushMessage("Error", "Bad layer type", level=QgsMessageBar.CRITICAL, duration=5)

        # delete the writer to flush features to disk (optional)
        del writer

        # hide progressbar
        self.iface.mainWindow().statusBar().clearMessage()

        # Show new layer
        self.iface.addVectorLayer(shapefileOutputName, "Volumes", "ogr")
        #self.canvas.refresh()

        # Inform user end of process
        self.iface.messageBar().pushMessage("Info", "Plugin ended successufully", level=QgsMessageBar.INFO, duration=5)

        #END












