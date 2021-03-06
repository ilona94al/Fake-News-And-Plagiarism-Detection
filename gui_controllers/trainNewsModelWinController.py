from PyQt5 import QtWidgets

from pathlib import Path

from gui_controllers.trainModelWinController import TrainModelWinController


class TrainNewsModelWinController(TrainModelWinController):
    def __init__(self, parent=None):
        super(TrainNewsModelWinController, self).__init__(parent)
        from gui_design.train_news_model_window import Ui_TrainNewsModelWindow
        self.ui = Ui_TrainNewsModelWindow()
        self.ui.setupUi(self)

        self.ui.radioButton2111.setChecked(True)
        self.show_one_file_form()

        self.set_buttons_handlers()

        self.clear_feedback()

    def set_buttons_handlers(self):
        self.ui.radioButton2111.clicked.connect(self.show_one_file_form)
        self.ui.radioButton2121.clicked.connect(self.show_two_files_form)

        self.ui.uploadBtn1212.clicked.connect(lambda: self.upload_file_pressed(widget=self.ui.inputPath1211))
        self.ui.uploadBtn1112.clicked.connect(lambda: self.upload_file_pressed(widget=self.ui.inputPath1111))
        self.ui.uploadBtn1122.clicked.connect(lambda: self.upload_file_pressed(widget=self.ui.inputPath1121))

        self.ui.backBtn.clicked.connect(self.back_pressed)
        self.ui.trainBtn.clicked.connect(self.train_pressed)

    def show_one_file_form(self):
        self.clear_feedback()
        self.two_files = False
        self.ui.verticalGroupBox12.setHidden(False)
        self.ui.verticalGroupBox11.setHidden(True)

    def show_two_files_form(self):
        self.clear_feedback()
        self.two_files = True
        self.ui.verticalGroupBox12.setHidden(True)
        self.ui.verticalGroupBox11.setHidden(False)

    def train_pressed(self):

        self.clear_feedback()

        epochs_widget = self.ui.inputEpoch3112
        epochs = str(epochs_widget.text())

        batch_size_widget = self.ui.inputBatchSz3114
        batch_size = str(batch_size_widget.text())

        if batch_size == "" or not batch_size.isnumeric() or int(batch_size) <= 0:
            self.invalid_input("Please fill valid batch size", batch_size_widget)
        else:
            self.set_normal_style(batch_size_widget)
        if epochs == "" or not epochs.isnumeric() or int(epochs) <= 0:
            self.invalid_input("Please fill number of epochs", epochs_widget)
        else:
            self.set_normal_style(epochs_widget)

        if self.two_files == True:
            real_file_path_widget = self.ui.inputPath1111
            real_file_path = str(real_file_path_widget.text())

            fakes_file_path_widget = self.ui.inputPath1121
            fakes_file_path = str(fakes_file_path_widget.text())

            text_col_name_widget = self.ui.inputTextColumnName113
            text_col_name = str(text_col_name_widget.text())

            if real_file_path == "" or real_file_path.split(".")[1] != "csv":
                self.invalid_input("path to 1st file is miss or not in csv format", real_file_path_widget)
            else:
                self.set_normal_style(real_file_path_widget)
            if fakes_file_path == ""or fakes_file_path.split(".")[1] != "csv":
                self.invalid_input("path to 2nd file is miss or not in csv format", fakes_file_path_widget)
            else:
                self.set_normal_style(fakes_file_path_widget)
            if text_col_name == "":
                self.invalid_input("text column name is miss", text_col_name_widget)
            else:
                self.set_normal_style(text_col_name_widget)

            if self.allOk == True:
                self.ui.trainBtn.setEnabled(False)

                from model.fake_news_tasks import FakeNewsTask2
                self.task = FakeNewsTask2(real_file_path, fakes_file_path, text_col_name, int(batch_size), int(epochs))
                if not self.task.error:
                    self.open_progress_win()
                else:
                    self.show_error_msg("Something went wrong\nverify that fields corresponded to files")
        else:
            file_path_widget = self.ui.inputPath1211
            file_path = str(file_path_widget.text())

            text_col_name_widget = self.ui.inputTextColumnName1221
            text_col_name = str(text_col_name_widget.text())

            label_col_name_widget = self.ui.inputLabelColumnName1231
            label_col_name = str(label_col_name_widget.text())

            fakes_label_val_widget = self.ui.inputFakeLabel1252
            fakes_label_val = str(fakes_label_val_widget.text())

            real_label_val_widget = self.ui.inputRealLabel1242
            real_label_val = str(real_label_val_widget.text())

            if file_path == "" or file_path.split(".")[1] != "csv":
                self.invalid_input("path to file is miss or not in csv format", file_path_widget)
            else:
                self.set_normal_style(file_path_widget)
            if text_col_name == "":
                self.invalid_input("text column name is miss", text_col_name_widget)
            else:
                self.set_normal_style(text_col_name_widget)
            if label_col_name == "":
                self.invalid_input("label column name is miss", label_col_name_widget)
            else:
                self.set_normal_style(label_col_name_widget)
            if fakes_label_val == "":
                self.invalid_input("fake label value is miss", fakes_label_val_widget)
            else:
                self.set_normal_style(fakes_label_val_widget)
            if real_label_val == "":
                self.invalid_input("real label value is miss", real_label_val_widget)
            else:
                self.set_normal_style(real_label_val_widget)

            if self.allOk == True:
                self.ui.trainBtn.setEnabled(False)

                from model.fake_news_tasks import FakeNewsTask1
                self.task = FakeNewsTask1(file_path, text_col_name, label_col_name, real_label_val, fakes_label_val,
                                          int(batch_size), int(epochs))
                if not self.task.error:
                    self.open_progress_win()
                else:
                    self.show_error_msg("Something went wrong\nverify that fields corresponded to file")

    @staticmethod
    def upload_file_pressed(widget):
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        widget.setText(file_path)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = TrainNewsModelWinController()
    MainWindow.show()
    sys.exit(app.exec_())
