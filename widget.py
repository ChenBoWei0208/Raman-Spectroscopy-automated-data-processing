# This Python file uses the following encoding: utf-8
import sys
# 1. 統一全部從 PySide6 匯入（不要混用 PyQt6）
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QWidget

# Important:
# pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Widget



# class Widget(QWidget):
#     i=0
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = Ui_Widget()
#         self.ui.setupUi(self)

#         # 2. 【最關鍵的一行】手動將按鈕點擊事件連接到您的函式
#         # 請檢查您的 UI 檔案裡，按鈕的 objectName 是不是真的叫 pushBottom
#         # self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

#     @Slot()  # 3. 改用 PySide6 的 @Slot() 裝飾器
#     def on_pushButton_clicked(self):
#         self.i += 1
#         self.ui.textEdit.setPlainText(str(self.i))


class Widget(QWidget):
    def __init__(self, i, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.i = i

        # 2. 【最關鍵的一行】手動將按鈕點擊事件連接到您的函式
        # 請檢查您的 UI 檔案裡，按鈕的 objectName 是不是真的叫 pushBottom
        # self.ui.pushButton.clicked.connect(self.on_pushButton_clicked)

    @Slot()  # 3. 改用 PySide6 的 @Slot() 裝飾器
    def on_pushButton_clicked(self):
        self.i += 1
        self.ui.textEdit.setPlainText(str(self.i))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget(0)
    widget.show()
    sys.exit(app.exec())
