from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow


class FormCheckerWinController(QMainWindow):
    def __init__(self, parent=None):
        super(FormCheckerWinController, self).__init__(parent)

    def clear_feedback(self):
        self.allOk = True
        self.ui.errorMsg.setHidden(True)
        self.ui.errorMsg.setText("")

    def invalid_input(self, msg, widget):
        self.allOk = False
        self.setFeedback(msg, widget)

    def setFeedback(self, msg, widget):
        self.show_error_msg(msg)
        self.set_error_style(widget)

    def show_error_msg(self, msg):
        curr_msg = self.ui.errorMsg.text()
        if curr_msg != "":
            curr_msg += "\n"
        self.ui.errorMsg.setText(curr_msg + msg)
        self.ui.errorMsg.adjustSize()
        self.ui.errorMsg.setHidden(False)

    # ☻ ☺ ☻ ♥ ♠ ♣ ♦ • ◘ ○
    def set_normal_style(self, widget):
        widget.setStyleSheet("border-width: 3px;\n"
                           "                                                    border-radius: 5px;\n"
                             "                                                    border-color: rgb(0, 0, 0);\n"
                             "                                                    border-style: solid;\n"
                             "                                                    background-color: rgb(188, 188, 188);\n"
                             "                                                    color: rgb(0, 0, 0);\n"
                             "                                                \n"
                             "")
        widget.update()

    def set_error_style(self, widget):
        widget.setStyleSheet("border-width: 3px;\n"
                             "                                                    border-radius: 5px;\n"
                             "                                                    border-color: rgb(170, 0, 0);\n"
                             "                                                    border-style: solid;\n"
                             "                                                    background-color: rgb(188, 188, 188);\n"
                             "                                                    color: rgb(0, 0, 0);\n"
                             "                                                \n"
                             "")
        widget.update()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = FormCheckerWinController()
    MainWindow.show()
    sys.exit(app.exec_())
