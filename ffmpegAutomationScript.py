import subprocess
from os import chdir
from os import walk
from re import sub
terms = 3  #filename, start time, end time
fnames = []
attributes = []

#index positions
posTitle = 0
posStart = 1
posEnd = 2

title = ''
tStart = 0
tEnd = 0

ipath = r'C:/FTEST/inputT/'
#alternatively ipath = r'C:\FTEST\test samples' "\\"    becaquse python can't handle a single backslash even in a string literal
opath = r'C:/FTEST/outputT/'
encPath = r'C:\FTEST\\' #path to ffmpeg, unused

#read the filenames into an array
for (dpath, dnames, filenames) in walk(ipath):
    for filename in filenames:
        attributes.append((filename.replace('.',' ')).split(" "))   #clean this up and get rid of the flv portion, find a better way to collect file name

        
#read the file names and work on seperating the attributes from the filename terms

#create a default string for launching ffmpeg including a formating point to insert the attributes from the filename
#loop through the array and call ffmpeg 
#using the shell = True flag is dangerous as it creates a vector for SHELL INJECTION and should be improved at a later time

for (title, tStart, tEnd, fType) in attributes:
    print("title, tstart, tEnd, tType")
    print(title, tStart, tEnd, fType)
    fInPath = ipath + title + " " + tStart + " " + tEnd +'.'+fType 
    attString = " -i " + '"' + fInPath + '"' + " -ss {} -to {}   -an -c:v libvpx -pix_fmt yuv420p -threads 12 -slices 8 -f webm -metadata title= {} -qmin 28 -crf 30 -qmax 32 -qcomp 1 -b:v 0   {}".format(tStart,tEnd, title, opath + title)

    Arguments =  -f nut -i pipe:0   -c:v libvpx -pix_fmt yuv420p -threads 12 -slices 8 -metadata title="MetaTitle" -ac 2 -c:a libvorbis -qmin 16 -crf 22 -qmax 28 -qcomp 1 -b:v 0 -qscale:a 10 -f webm -y "D:\videos\converted\NewFileName.webm"
    ffmpegInput =  -ss tStart -i fInPath 
    print("attString: ")
    print(attString)
    # ***-y overwrites output file without asking removed during testing***

    subprocess.call(encPath + 'ffmpeg' + attString , shell = True)

    print("subprocess call string: encPath + 'ffmpeg.exe' = attString")
    print(encPath + 'ffmpeg.exe' + attString)

    print("Now converting {} cutting from {} to {} ".format(title, tStart, tEnd))
    

print("All files converted, have a nice day :) ")
input("Press any key to continue . . . ")


#basic debug
print(fnames)
print(attributes)
print(attributes[1][2])
