import os
import xlwt
from config import basedir


class XLSWriter():
    """Import/export Tool"""

    def __init__(self, sheet_name='default', file_name='default'):
        self.sheet_name = sheet_name
        self.file_name = file_name
        self.wb = xlwt.Workbook(encoding='utf-8')
        self.ws = self.wb.add_sheet(self.sheet_name)

    def export(self, json_list):
        # 填写表头
        th = list(json_list[0].keys())
        self.feeder(line=0, td_list=th)

        # 填写表内容
        for index, json in enumerate(json_list):
            td_list = list(json.values())
            line = index + 1
            self.feeder(line=line, td_list=td_list)

        self.save()

    def feeder(self, line, td_list):
        """
        :param line: 行号
        :param td_list: 待填入单元格列表
        :return:
        """
        for i in range(len(td_list)):
            self.ws.write(line, i, td_list[i])

    def save(self):
        file = os.path.join(basedir, self.file_name + '.xls')
        if os.path.exists(file):
            os.remove(file)
        self.wb.save(self.file_name + '.xls')
