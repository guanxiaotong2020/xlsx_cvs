# -*- coding: utf-8 -*-

import  xlrd
import  csv
def xls2csv(filename):
    xlsFileData = xlrd.open_workbook(filename)
    for i in range(len(xlsFileData.sheets())):
        table = xlsFileData.sheet_by_index(i)
        csvname = xlsFileData.sheet_names()[i]
        with open(csvname ,'w', encoding='utf-8') as fw:
            csvwrite = csv.writer(fw, dialect=("excel"))
            for line in range(table.nrows):
                line_value = table.row_values(line)
                csvwrite.writerow(line_value)

if __name__ == '__main__':
    xls2csv('C:/Users/29236/Desktop/1.xlsx')