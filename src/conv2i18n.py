import os
import glob
import pyexcel
import json
import config

def filter_empty_row(row_index, row):
    result = [element for element in row if element != '']
    return len(row) > 1 and row[1] == ""

def filter_include_col(col_index, col):
    return col[0] not in INCLUDE_COLS

def gen_i18n(lang, filter_indices):
    print(">> Lang : {0}".format(lang))
    # Declare variable
    result = {}
    # Merge target csv file
    os.chdir(config.csv_dir())
    for file in glob.glob("*.csv"):
        #print(">>> - File : {0}".format(file))
        sheet = pyexcel.get_sheet(file_name=file, delimiter=";")
        # ignore empty csv file first
        if sheet.number_of_columns() > 0 and sheet.number_of_rows() > 1:
            # ignore column by parameter filter_indices, and title row
            del sheet.column[lambda i, r : not ( r[0] == sheet.row[0][0] or r[0] == filter_indices )]
            del sheet.row[0]
            #print(sheet.content)
            # delete row if value column is empty
            del sheet.row[filter_empty_row]
            # sheet convert to dict object
            if sheet.number_of_rows() > 0:
                # lock column 0 is key column
                sheet.name_rows_by_column(0)
                # sheet to dict
                sheet_dict = sheet.to_dict()
                # modify sheet_dict item
                for k, v in sheet_dict.items():
                    # value colunm can not array type
                    if isinstance(v, list) and len(v) > 0:
                        sheet_dict[k] = v[0]
                # merge sheet into result
                result.update(sheet_dict)
    #
    OUTPUT_DIR=os.path.join(config.i18n_dir())
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)
    with open(os.path.join(OUTPUT_DIR, "{0}.json".format(lang)), "w+", encoding='UTF-8') as fp:
        json.dump(result, fp, ensure_ascii=False)

def conv():
    print(">> Output i18n JSON file :")
    gen_i18n("zh-TW", "繁中")
    gen_i18n("en", "英文")
    gen_i18n("jp", "日文")
