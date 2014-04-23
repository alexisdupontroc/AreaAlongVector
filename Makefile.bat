@echo off

pyrcc4 -py3 -o resources.py resources.qrc
pyuic4 -o ui_areaalongvector.py ui_areaalongvector.ui