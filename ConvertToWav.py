import os
from pydub import AudioSegment

INPUT_DIR = "D:/Telechargement/genres"
OUTPUT_DIR = INPUT_DIR + "_wav"
FILE_TYPE = "au"


print("Creating new folder...")

os.mkdir(OUTPUT_DIR)
print("Converting files to wav format...")
i=0
for eachfolder in os.listdir(INPUT_DIR):
    opath=os.path.join(OUTPUT_DIR,eachfolder)
    os.mkdir(opath)
    i+=1
    for eachfile in os.listdir(INPUT_DIR+"/"+eachfolder) :
        song = AudioSegment.from_file(INPUT_DIR+"/"+eachfolder+"/" + eachfile, FILE_TYPE)
        song.export(os.path.join(opath,eachfile[:-3] + "_wav.wav"), format="wav")
    print("folder",i,"is done")
print("DONE!")
