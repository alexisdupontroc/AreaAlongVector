# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AreaAlongVector
                                 A QGIS plugin
 Create area along vectors from field values
                             -------------------
        begin                : 2014-04-18
        copyright            : (C) 2014 by Alexis Dupont-Roc
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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load AreaAlongVector class from file AreaAlongVector
    from areaalongvector import AreaAlongVector
    return AreaAlongVector(iface)
