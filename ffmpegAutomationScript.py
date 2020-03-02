import subprocess
from os import chdir
from os import walk
from re import sub
terms = 3  #filename, start time, end time
fnames = []
attributes = []

#index positions

title = ''
tStart = 0
tEnd = 0

iPath = r'C:/FTEST/inputT/'
#alternatively ipath = r'C:\FTEST\test samples' "\\"    because python can't handle a single backslash even in a string literal
oPath = r'C:/FTEST/outputT/'
encPath = r'C:\FTEST\\' #path to ffmpeg, unused

#read the filenames into an array
for (dpath, dnames, filenames) in walk(iPath):
    for filename in filenames:
        attributes.append((filename.replace('.',' ')).split(" "))   #clean this up and get rid of the flv portion, find a better way to collect file name

        
#read the file names and work on seperating the attributes from the filename terms

#create a default string for launching ffmpeg including a formating point to insert the attributes from the filename
#loop through the array and call ffmpeg 
#using the shell = True flag is dangerous as it creates a vector for SHELL INJECTION and should be improved at a later time

for (title, tStart, tEnd, fType) in attributes:
    

    # -i "C:/FTEST/inputT/g2tailbreak 00 06.flv" -ss 00 -to 06 -c:v libvpx -pix_fmt yuv420p -threads 12 -slices 8 -metadata title="g2tailbreak" -ac 2 -c:a libvorbis -qmin 16 -crf 22 -qmax 28 -qcomp 1 -b:v 0 -qscale:a 10 -f webm + "C:\FTEST\outputT\g2tailbreak.webm"
    # ***-y overwrites output file without asking removed during testing***
    
    qualitySettings = ' -c:v libvpx -pix_fmt yuv420p -threads 12 -slices 8 -metadata title="{}" -ac 2 -c:a libvorbis -qmin 16 -crf 22 -qmax 28 -qcomp 1 -b:v 0 -qscale:a 10 -f webm '.format(title)
    attString =  " -i " + '"' + iPath + title + " " + tStart + " " + tEnd +'.'+fType + '"' + " -ss " + tStart + " -to " + tEnd + qualitySettings + '"' + oPath + title + ".webm" + '"' 
    
    
    
    print("Now converting {} cutting from {} to {} ".format(title, tStart, tEnd))

    subprocess.call(encPath + 'ffmpeg' + attString , shell = True)  
    

print("All files converted, have a nice day :) ")
input("Press any key to continue . . . ")


#basic debug
print(fnames)
print(attributes)
print(attributes[1][2])
