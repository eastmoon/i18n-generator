# library
import os.path
import platform

# Declare variable
ROOT_DIR=os.path.dirname(os.getcwd())
DATA_DIR=os.path.join(ROOT_DIR, 'cache') if platform.system() == "Windows" else "/data"
APP_DIR=ROOT_DIR if platform.system() == "Windows" else "/app"
RESOURCE_DIR="res"
CSV_SOURCE_DIR="csv"
I18N_SOURCE_DIR="i18n"

# Create data directory
if not os.path.exists(os.path.join(DATA_DIR, RESOURCE_DIR)): os.makedirs(os.path.join(DATA_DIR, RESOURCE_DIR))
if not os.path.exists(os.path.join(DATA_DIR, CSV_SOURCE_DIR)): os.makedirs(os.path.join(DATA_DIR, CSV_SOURCE_DIR))
if not os.path.exists(os.path.join(DATA_DIR, I18N_SOURCE_DIR)): os.makedirs(os.path.join(DATA_DIR, I18N_SOURCE_DIR))

# Declare function
def res_dir():
    return os.path.join(DATA_DIR, RESOURCE_DIR)
def csv_dir():
    return os.path.join(DATA_DIR, CSV_SOURCE_DIR)
def i18n_dir():
    return os.path.join(DATA_DIR, I18N_SOURCE_DIR)
