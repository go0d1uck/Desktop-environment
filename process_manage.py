from PyQt5.QtWidgets import *  # NOQA
from PyQt5.QtGui import *  # NOQA
from PyQt5.QtCore import *  # NOQA
import ps
import time


class Table(QWidget):  # NOQA
    def __init__(self, arg=None):
        super(Table, self).__init__(arg)
        self.setWindowTitle("Process Manager")
        self.resize(500, 300)
        data = ps.getStatus()
        self.model = QStandardItemModel(len(data), 6)  # NOQA
        self.model.setHorizontalHeaderLabels(['id', 'name', 'status', 'memory_info', 'threads_num', 'create_time'])
        for row in range(len(data)):
            for column in range(6):
                if(column == 5):
                    time_local = time.localtime(int(data[row][column]))
                    date = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                    item = QStandardItem("%s" % (date))  #NOQA
                else:
                    item = QStandardItem("%s" % (data[row][column])) #NOQA
                self.model.setItem(row, column, item)
        self.tableView = QTableView()  #NOQA
        self.tableView.setModel(self.model)
        dlgLayout = QVBoxLayout()  #NOQA
        dlgLayout.addWidget(self.tableView)
        self.setLayout(dlgLayout)
