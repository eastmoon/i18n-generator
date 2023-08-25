import pyexcel
import copy
import os.path
import config
import datetime

# Declare variable
INTERFACE_COL_NUM=-1
IGNORE_SHEETS=["文件規則說明"]
INCLUDE_COLS=["State Code", "繁中", "英文", "日文"]

# Declare function
def cleanse_func(v):
    v = str(v)
    v = v.replace("\n", "")
    v = v.replace("&nbsp;", "")
    v = v.rstrip().strip()
    return v

def filter_include_col(col_index, col):
    return col[0] not in INCLUDE_COLS

def filter_empty_row(row_index, row):
    result = [element for element in row if element != '']
    return len(result) == 0

def gen_csv(name, sheet):
    # remove unnecessary column
    del sheet.column[filter_include_col]
    # clean data for each cell
    sheet.map(cleanse_func)
    # remove filter row
    del sheet.row[filter_empty_row]
    # save sheet to .csv file
    sheet.save_as(os.path.join(config.csv_dir(), name+".csv"), delimiter=";")

def conv(target_number, target_file):
    # 工作流描述：
    # 1. 基於 IGNORE_SHEETS 排除不指定的 Sheet
    # 2. 對需要的 Sheet 依據 INCLUDE_COLS 將內容轉換成 CSV 格式檔案
    if os.path.exists(target_file):
        print(">> Output CSV file :")
        # open file with book
        book = pyexcel.get_book(file_name=target_file)
        sheets = book.to_dict()
        count = 0
        # search target sheet
        for name in sheets.keys():
            if name not in IGNORE_SHEETS:
                # put list object into sheet object
                count += 1
                print(">> {0}-{1:03d}-{2}".format(target_number, count, name))
                sheet = pyexcel.Sheet(copy.deepcopy(sheets[name]))
                gen_csv("{0}-{1:03d}-{2}".format(target_number, count, name), sheet)
    else:
        print(">> Target file {0} is not exist".format(target_file))
