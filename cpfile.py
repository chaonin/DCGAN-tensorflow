#chaonin @2017/12/31
# to copy image from data/anime/faces/ to data/anime
import os
import shutil

def cpfile(srcPath, dstPath):
    if not os.path.exists(srcPath):
        print "src path not exist!"
        return 
    cnt = 1 
    for root,dirs,files in os.walk(srcPath): 
        for eachfile in files: 
            cnt = cnt + 1
            shutil.copy(os.path.join(root,eachfile),dstPath) 
            if cnt > 5000:
                return
            print eachfile+" copy succeeded"


cpfile("/Users/guochaonian/GIT/DCGAN-tensorflow/data/anime-backup/","/Users/guochaonian/GIT/DCGAN-tensorflow/data/anime/")
