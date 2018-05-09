import os
import sys

suffixes={1000:["KB","MB","GB","TB"],
                1024:["KiB","MiB","GiB","TiB"]}

def approximate_size(filePath,yardstickIs1024=True):
    """
    Returns approximate size of the file at file_path
    :param filePath:path of the file
    :param yardstickIs1024: 1kb=1024 bytes or 1000 bytes
    :return: size of the file

    """
    if not os.path.exists(filePath):
        raise FileExistsError("The file you requested does not exists.")

    sizeOfFile=os.path.getsize(filePath)

    yardstick = 1024 if yardstickIs1024 else 1000

    for suffix in suffixes[yardstick]:
        sizeOfFile = sizeOfFile / yardstick

        if sizeOfFile > yardstick:
            continue
        else:
            return '{0:.1f} {1}'.format(sizeOfFile,suffix)

#if __name__=="__main__":
#    print(approximate_size("/Users/jasdeepsinghchhabra/improving_python/importSaga/dataAndCaller/data/video.mp4",True))




