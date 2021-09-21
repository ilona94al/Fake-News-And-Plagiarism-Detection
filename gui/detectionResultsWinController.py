from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow


class DetectionResultsWinController(QMainWindow):
    def __init__(self, author_name, book_path, parent=None):
        super(DetectionResultsWinController, self).__init__(parent)
        # todo: find the relevant trained model(according to the author name)
        # todo: insert book path as input to the model and get detection results (graphs and etc.)
        # todo: show reaultson ui
        from gui.detection_results_window import Ui_DetectionResultsWindow
        self.ui = Ui_DetectionResultsWindow()
        self.ui.setupUi(self)
        self.ui.backBtn.clicked.connect(self.back_pressed)

    def back_pressed(self):
        self.close()
        from gui.plagiarismWinController import PlagiarismWinController
        self.window = PlagiarismWinController()
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = DetectionResultsWinController()
    MainWindow.show()
    sys.exit(app.exec_())
