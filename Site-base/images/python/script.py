import os 
import shutil

if not os.listdir("./home/siteweb/"):
    shutil.copy("index.php","./home/siteweb/index.php")