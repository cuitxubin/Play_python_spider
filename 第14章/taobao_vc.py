from PyQt5 import QtCore, QtGui, QtWidgets
#导入taobao.py的Ui_Dialog
from taobao_v import Ui_Dialog
from taobao_c import get_info
import sys
#继承taobao.py的Ui_Dialog
class taobao_control(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(taobao_control, self).__init__(parent)
        self.setupUi(self)
        #添加响应事件
        self.pushButton.clicked.connect(self.collect_data)

    def collect_data(self):
        #获取多个关键字，返回关键字列表
        get_keyword_list = self.plainTextEdit.toPlainText().split('\n')
        #获取采集的页数
        get_page = (self.comboBox.currentIndex()+1)*5
        #每一页的数据要请求44次
        get_page = get_page*44
        get_info(get_keyword_list,get_page,[])
        print('Done')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    taobao_control = taobao_control()
    taobao_control.show()
    sys.exit(app.exec_())