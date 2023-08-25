# library
import os.path
import glob
import subprocess
import config
import conv2csv
import conv2i18n

# Declare variable

# Declare function
def show_path():
    print(">> Download resource path :\t", config.res_dir())
    print(">> CSV resource path :\t\t", config.csv_dir())
    print(">> i18n resource path :\t\t", config.i18n_dir())

# Execute script
#
# i18n converter:
# 1. load xlsx into script
# 2. read ecah sheet and generate csv file, it will ignore special sheet, and columns.
# 3. merge all csv, and put into key ( state code ) - value ( language ) JSON format, filename is (language).json
if __name__ == '__main__':
    show_path()
    os.chdir(config.res_dir())
    index = 1
    for file in glob.glob("*.xlsx"):
        conv2csv.conv(index, file)
        index+=1
    conv2i18n.conv()
