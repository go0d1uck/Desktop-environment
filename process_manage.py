from PyQt5.QtWidgets import *  # NOQA
from PyQt5.QtGui import *  # NOQA
from PyQt5.QtCore import *  # NOQA
from PyQt5.QtCore import QEvent
import ps
import sys
import time


class Table(QWidget):  # NOQA
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Process Manager")
        self.resize(500, 300)
        data = ps.getStatus()
        conLayout = QHBoxLayout() #NOQA
        self.tableWidget = QTableWidget() #NOQA
        self.tableWidget.setRowCount(len(data))  # NOQA
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['Pid', 'Name', 'Status', 'Memory_info', 'Threads_num', 'Create_time'])
        for row in range(len(data)):
            for column in range(6):
                if(column == 5):
                    time_local = time.localtime(int(data[row][column]))
                    date = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                    item = "%s" % (date)  #NOQA
                    item = QTableWidgetItem(item)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                else:
                    item = "%s" % (data[row][column]) #NOQA
                    item = QTableWidgetItem(item)
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.tableWidget.setItem(row, column, item) #NOQA
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.sortItems(3,Qt.DescendingOrder)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()
        # QTableWidget.resizeColumnsToContents()
        # QTableWidget.resizeRowsToContents()
        conLayout.addWidget(self.tableWidget)
        self.setLayout(conLayout)
        self.timer =  QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(2000)

    def generateMenu(self, pos):
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num != -1:
            menu = QMenu()
            item = menu.addAction("DELETE")
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        if action == item:
            ps.killProcess(int(self.tableWidget.item(row_num, 0).text()))
        else:
            return

    def keyPressEvent(self, event):
        if(event.key() == Qt.Key_F4):
            self.close()

    def update(self):
            data = ps.getStatus()
            self.tableWidget.setRowCount(len(data))  # NOQA
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels(['Pid', 'Name', 'Status', 'Memory_info', 'Threads_num', 'Create_time'])
            for row in range(len(data)):
                for column in range(6):
                    if(column == 5):
                        time_local = time.localtime(int(data[row][column]))
                        date = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                        item = "%s" % (date)  #NOQA
                        item = QTableWidgetItem(item)
                        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    else:
                        item = "%s" % (data[row][column]) #NOQA
                        item = QTableWidgetItem(item)
                        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(row, column, item) #NOQA
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.tableWidget.sortItems(3,Qt.DescendingOrder)
            self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)  #NOQA
    table = Table()
    table.show()
    sys.exit(app.exec_())
