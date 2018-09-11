# -*- coding: utf-8 -*-
import sys
# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class FileWidget(QWidget):
    def __init__(self):
        super().__init__()
        # QWidget部件是PyQt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
        # 创建一个文件系统模型
        self.file_model = QFileSystemModel()
        # 设置目录为当前工作目录
        self.file_model.setRootPath(QDir.currentPath())
        # 创建树视图，构建文件目录视图
        self.treeview = QTreeView()
        # 绑定此文件模型
        self.treeview.setModel(self.file_model)
        '''
        设置当前勾结点索引为当前工作目录
        如果想从整个文件系统根节点开始浏览视图，
        简单删掉此行即可
        '''
        self.treeview.setRootIndex(self.file_model.index(QDir.currentPath()))
        # 头部显示排序戳
        self.treeview.header().setSortIndicatorShown(True)

        # 底部按钮布局
        self.mkdirButton = QPushButton("Make Directory...")
        self.rmButton = QPushButton("Remove")
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.mkdirButton)
        buttonLayout.addWidget(self.rmButton)

        #文件管理界面布局
        layout = QVBoxLayout()
        layout.addWidget(self.treeview)
        layout.addLayout(buttonLayout)

        # resize()方法调整窗口的大小。600px宽300px高
        self.resize(600, 300)
        # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
        self.move(300, 300)
        # 设置窗口的标题
        self.setWindowTitle('File Manage')
        # 设置窗口的图标
        self.setWindowIcon(QIcon('File-Explorer.png'))
        self.setLayout(layout)


if __name__ == '__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
    widget = FileWidget()
    widget.show()
    sys.exit(app.exec_())
