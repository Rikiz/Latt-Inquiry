# -*- coding: utf-8 -*-

import sys
from io import open
from os import path
from shutil import copy
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import form
from utils import latitude_getter
from utils import result_export
from utils import file_util

class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = form.Ui_Widget()
        self.ui.setupUi(self)
        self._api_key = None
        self._exporter = result_export.Exporter()
        self._addressUtil  = file_util.AddressUtil()

    def onClickSubmit(self):
        self._api_key = self.ui.textEdit1.toPlainText()
        if self._api_key == None or self._api_key == "":
            alert = QMessageBox()
            alert.setText('Please enter the api key!')
            alert.exec_()
            return
        address = self.ui.textEdit.toPlainText()
        isfile = False
        # if address.startswith("file://"):
        if self._addressUtil.isFile(address):
            isfile = True
        if isfile:
            # filename = re.sub("^file://(.*)$", "\g<1>", address)
            filename = self._addressUtil.getFileName(address)
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
                maxValue = len(lines)
                index = 1
                for line in lines:
                    line = line.strip()
                    res = latitude_getter.geocode(line, self._api_key)
                    if res != "":
                        longtitude, latitude = res["longtitude"], res["latitude"]
                        self._exporter.append_to_result(line.strip(), str(longtitude).strip(), str(latitude).strip())
                    index += 1
                    self.updateProcessBar(100 * index/maxValue)

        else:
            address_list = address.split("\n")
            maxValue = len(address_list)
            index = 1
            for line in address_list:
                line = line.strip()
                res = latitude_getter.geocode(line, self._api_key)
                if res != "":
                    longtitude, latitude = res["longtitude"], res["latitude"]
                    self._exporter.append_to_result(line.strip(), str(longtitude).strip(), str(latitude).strip())
                index += 1
                self.updateProcessBar(100 * index/maxValue)

        
    def onClickOutput(self):
        out_path = self.ui.textEdit_2.toPlainText()
        if out_path == None or out_path == "":
            alert = QMessageBox()
            alert.setText('Please enter a output path!')
            alert.exec_()
            return
        if self._addressUtil.isFile(out_path):
            out_path = self._addressUtil.getFileName(out_path)
        out_path = path.dirname(out_path)
        result_file = path.join(out_path, "result.csv")
        error_file = path.join(out_path, "error.txt")
        
        try:
            copy("result.csv", result_file)
            copy("error.txt", error_file)
        except:
            alert = QMessageBox()
            alert.setText('Error Occur, Please contect with Ms Fan')
            alert.exec_()


    def updateProcessBar(self, percent):
        processBar = self.ui.progressBar.setProperty("value", percent)

if __name__ =="__main__":
    myapp = QApplication(sys.argv)
    mainview = MainDialog()
    mainview.show()
    sys.exit(myapp.exec_())