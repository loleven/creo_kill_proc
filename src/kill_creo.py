#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

"""XXXXXXX.py: Description of what XXXXXXX does.

Testing
"""

import psutil
import sys
import os
import configparser
import json

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import (QThread, pyqtSignal)

import gui_kill_creo

__author__ = "Lars-Olof Levén"
__copyright__ = "Copyright 2016, Lars-Olof Levén"
__license__ = "The MIT License"
__version__ = "1.0.0"
__maintainer__ = "Lars-Olof Levén"
__email__ = "lars-olof.leven@lwdot.se"
__status__ = "Development"


class OptFile:
    def __init__(self):
        self.items = []
        self.script_file = os.path.basename(os.path.abspath(sys.argv[0])).split('.')
        self.ini_file = '{0}.opt'.format(self.script_file[0])
        self.script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    def default_ini_values(self):
        ini_items = {}

        items_size = {'height': 300, 'width': 400}
        ini_items['Size'] = items_size

        ini_position = {'x': 0, 'y': 0}
        ini_items['Position'] = ini_position

        items_general = {
            'process': 'ptc_win_gecko_server.exe,pro_comm_msg.exe,xtop.exe,parametric.exe,nmsd.exe,creoagent.exe'}
        ini_items['General'] = items_general

        return ini_items

    def read_ini_file(self):

        if os.path.exists(r'{0}\{1}'.format(self.script_dir, self.ini_file)):
            with open(r'{0}\{1}'.format(self.script_dir, self.ini_file)) as opt_file:
                ini_items = json.load(opt_file)
        else:
            ini_items = self.default_ini_values()

        return ini_items

    def save_ini_file(self, ini_items):
        with open(r'{0}\{1}'.format(self.script_dir, self.ini_file), 'w') as outfile:
            str_ = json.dumps(ini_items,
                              indent=4, sort_keys=True,
                              separators=(',', ':'), ensure_ascii=False)
            outfile.write(str_)


class ShowUI(QtWidgets.QWidget, gui_kill_creo.Ui_frm_kill_creo):
    def __init__(self, parent=None):
        super(ShowUI, self).__init__(parent)

        self.scriptDir = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.module_name = os.path.basename(sys.argv[0])
        self.thread_started = False

        self.kill_creo_thread = ''
        self.ini_items = ''

        self.setupUi(self)

    def closeEvent(self, event):

        if self.thread_started:
            event.ignore()
        else:
            self.ini_items['Position']['x'] = self.pos().x()
            self.ini_items['Position']['y'] = self.pos().y()

            self.ini_items['Size']['width'] = self.size().width()
            self.ini_items['Size']['height'] = self.size().height()

            event.accept()

    def update_ui(self):
        self.move(self.ini_items['Position']['x'], self.ini_items['Position']['y'])
        self.resize(QSize(self.ini_items['Size']['width'], self.ini_items['Size']['height']))

        self.btn_kill.clicked.connect(self.start_kill)

        self.kill_creo_thread = KillCreo()
        self.kill_creo_thread.mySignal.connect(self.add_info)
        self.kill_creo_thread.finished.connect(self.end_import)

    def start_kill(self):
        if not self.thread_started:
            self.list_result.clear()
            self.thread_started = True
            self.kill_creo_thread.ini_items = self.ini_items
            self.kill_creo_thread.start()

    def end_import(self):

        self.kill_creo_thread.terminate()
        QMessageBox.information(self, 'Information', 'Finish', QMessageBox.Ok)
        self.thread_started = False

    def add_info(self, str_info):
        self.list_result.addItem(str_info)


class KillCreo(QThread):
    mySignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.creo_proc = []
        self.ini_items = ''

    def run(self):
        self.kill_proc()

    def create_patterns(self):
        for ext in self.ini_items['General']['process'].split(','):
            self.creo_proc.append(ext)

    def kill_proc(self):
        self.create_patterns()

        for proc in psutil.process_iter():
            if proc.name() in self.creo_proc:
                proc.kill()
                self.mySignal.emit('Killed {0} - {1}'.format(proc.name(), proc.pid))


def list_proc():
    creo_proc = ["ptc_win_gecko_server.exe", "pro_comm_msg.exe", "xtop.exe", "parametric.exe", "creoagent.exe",
                 "nmsd.exe"]
    proc_exist = False

    for proc in psutil.process_iter():
        if proc.name() in creo_proc:
            print('{0} - {1}'.format(proc.name(), proc.pid))
            proc_exist = True

            # return proc_exist


def main():
    ini_file = OptFile()

    ini_items = ini_file.read_ini_file()

    app = QtWidgets.QApplication(sys.argv)

    form = ShowUI()
    form.ini_items = ini_items
    form.update_ui()
    form.show()
    result = app.exec_()

    ini_file.save_ini_file(ini_items)


if __name__ == "__main__":
    main()
