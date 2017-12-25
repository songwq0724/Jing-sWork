import os
import fnmatch

def FindFiles(path, fnexp,isIncludeRoot=False):
    fileList = []
    fileFullName = ''
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, fnexp):
            if(isIncludeRoot):
                fileFullName = os.path.join(root,filename)
            else:
                fileFullName = filename
            fileList.append(fileFullName)
    return fileList