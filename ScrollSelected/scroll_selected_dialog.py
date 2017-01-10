# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ScrollSelectedDialog
                                 A QGIS plugin
 Opens a UI for the user to flip through selected features
                             -------------------
        begin                : 2016-11-08
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Chris Lowrie
        email                : lowriech@msu.edu
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

from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'scroll_selected_dialog_base.ui'))


class ScrollSelectedDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ScrollSelectedDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
