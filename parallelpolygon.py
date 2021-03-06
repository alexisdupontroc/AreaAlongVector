#! python3
# -*- coding: utf-8 -*-

"""
/***************************************************************************
 ParallelPolygon
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


def calculateDistance(fieldValue, minV, minW, maxV, maxW):
    # Min and Max drawing width
    #maxRectangleWidth = 100.0
    #minRectangleWidth = 0.5
    maxRectangleWidth = maxW
    minRectangleWidth = minW
    # over maxFieldLimit, draw a rectangle width of maxRectangleWidth
    #maxFieldLimit = 5000.0
    maxFieldLimit = maxV
    # under minFieldLimit, draw a rectangle width of minRectangleWidth
    #minFieldLimit = 50.0
    minFieldLimit = minV
    if fieldValue <= minFieldLimit:
        return minRectangleWidth
    elif fieldValue >= maxFieldLimit:
        return maxRectangleWidth
    else:
        return fieldValue * maxRectangleWidth / maxFieldLimit


def calculateRightPolygon(p1, p2, dist):

    if dist == 0:
        points = [p1, p2, p2, p1]
        return points

    dn = ((p1.x() - p2.x()) ** 2 + (p1.y() - p2.y()) ** 2) ** 0.5
    if dn == 0:
        points = [p1, p2, p2, p1]
        return points

    # P3 = P2 to the right
    x3 = p2.x() + dist * (p2.y() - p1.y()) / dn
    y3 = p2.y() - dist * (p2.x() - p1.x()) / dn
    p3 = QgsPoint(x3, y3)

    # P4 = P1 to the right
    x4 = p1.x() + dist * (p2.y() - p1.y()) / dn
    y4 = p1.y() - dist * (p2.x() - p1.x()) / dn
    p4 = QgsPoint(x4, y4)

    points = [p1, p2, p3, p4]
    return points


def calculateLeftPolygon(p1, p2, dist):

    if dist == 0:
        points = [p1, p2, p2, p1]
        return points

    dn = ((p1.x() - p2.x()) ** 2 + (p1.y() - p2.y()) ** 2) ** 0.5
    if dn == 0:
        points = [p1, p2, p2, p1]
        return points

    # P3 = P2 to the left
    x3 = p2.x() - dist * (p2.y() - p1.y()) / dn
    y3 = p2.y() + dist * (p2.x() - p1.x()) / dn
    p3 = QgsPoint(x3, y3)

    # P4 = P1 to the left
    x4 = p1.x() - dist * (p2.y() - p1.y()) / dn
    y4 = p1.y() + dist * (p2.x() - p1.x()) / dn
    p4 = QgsPoint(x4, y4)

    points = [p2, p1, p4, p3]
    return points