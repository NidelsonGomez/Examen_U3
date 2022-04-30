# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LatLonCalcDialog
                                 A QGIS plugin
 Calculadora para convertir Coordenadas Geografocias a Decimales 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-04-29
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Nidelson Gomez
        email                : nidelson.gomez@unah.hn
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

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'latloncalc_dialog_base.ui'))


class LatLonCalcDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(LatLonCalcDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
	
	#disparadores de latitud
        self.spbLatD.valueChanged.connect(self.latDMStoDD)
        self.spbLatM.valueChanged.connect(self.latDMStoDD)
        self.spbLatS.valueChanged.connect(self.latDMStoDD)
        self.cmbLatH.currentTextChanged.connect(self.latDMStoDD)
        
        #Disparador para grados decimales
        self.spbLatDD.editingFinished.connect (self.latDDtoDMS)
        
        
        #disparadores de longitud
        self.spbLonD.valueChanged.connect(self.lonDMStoDD)
        self.spbLonM.valueChanged.connect(self.lonDMStoDD)
        self.spbLonS.valueChanged.connect(self.lonDMStoDD)
        self.cmbLonH.currentTextChanged.connect(self.lonDMStoDD)
        
        #Disparador para grados decimales
        self.spbLonDD.editingFinished.connect (self.lonDDtoDMS)
        
    def latDMStoDD(self):
        ideg = self.spbLatD.value()
        imin = self.spbLatM.value()
        dseg = self.spbLatS.value()
        sHem = self.cmbLatH.currentText()
        
        dDD = float(ideg) + imin/60 + dseg/3600
        
        if sHem == 'S':
            dDD = dDD * -1
        
        self.spbLatDD.setValue(dDD)
        
    def latDDtoDMS(self):
        dDD = self.spbLatDD.value()
        
        ideg = int(dDD)
        dMin = (dDD - ideg) * 60
        imin = int(dMin)
        dseg = (dMin - imin) * 60
        
        self.spbLatD.setValue(abs(ideg))
        self.spbLatM.setValue(abs(imin))
        self.spbLatS.setValue(abs(dseg))
        
        if dDD < 0:
            self.cmbLatH.setCurrentText("S")
        else:
            self.cmbLatH.setCurrentText("N")
            
    
       
    def lonDMStoDD(self):
        ideg = self.spbLonD.value()
        imin = self.spbLonM.value()
        dseg = self.spbLonS.value()
        sHem = self.cmbLonH.currentText()
        
        dDD = float(ideg) + imin/60 + dseg/3600
        
        if sHem == 'W':
            dDD = dDD * -1
        
        self.spbLonDD.setValue(dDD)
        
    def lonDDtoDMS(self):
        dDD = self.spbLonDD.value()
        
        ideg = int(dDD)
        dmin = (dDD - ideg) * 60
        imin = int(dmin)
        dseg = (dmin - imin) * 60
        
        self.spbLonD.setValue(abs(ideg))
        self.spbLonM.setValue(abs(imin))
        self.spbLonS.setValue(abs(dseg))
        
        if dDD < 0:
            self.cmbLonH.setCurrentText("O")
        else:
            self.cmbLonH.setCurrentText("E")