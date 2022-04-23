import os
import shutil
import time
from datetime import datetime
import shutil
import glob
from pathlib import Path
from pathlib import Path

sourceFolder = r"E:\Tang\pic\hakonePhoto"
destinationFolder = r"D:\PicDT"

 # Get file list
files = glob.glob(sourceFolder + r'\**\*.*', recursive=True)
count = 1;
for filename in files:
    if Path((filename)).is_file():
        #Get file modified date 
        created = (os.path.getmtime(filename))
        createYmd = datetime.fromtimestamp(created).strftime("%Y-%m-%d")
        #Create destination folder if not exists 
        if not os.path.exists(os.path.join(destinationFolder, createYmd)):
            os.mkdir(os.path.join(destinationFolder, createYmd))
        #Copy file with meta info
        print("Copying [" + str(count) + "/" + str(len(files)) + "]  File Name: " + filename)
        shutil.copy2(filename, os.path.join(destinationFolder, createYmd ,Path(filename).name))
        count = count + 1


