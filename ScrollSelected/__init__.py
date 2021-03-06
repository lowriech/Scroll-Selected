# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ScrollSelected
                                 A QGIS plugin
 Opens a UI for the user to flip through selected features
                             -------------------
        begin                : 2016-11-08
        copyright            : (C) 2016 by Chris Lowrie
        email                : lowriech@msu.edu
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ScrollSelected class from file ScrollSelected.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .scroll_selected import ScrollSelected
    return ScrollSelected(iface)
