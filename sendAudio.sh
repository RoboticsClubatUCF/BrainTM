#!bin/bash

num=0
while [ $num -le 4 ]
do
    Python tts.py
    mp3FileName=tempFile.mp3
    scp $mp3FileName TMBrain@192.168.137.46:/home/TMBrain/Desktop
    printf "File has been sent\n"
    ssh TMBrain@192.168.137.46 'mpg123 /home/TMBrain/Desktop/tempFile.mp3;rm /home/TMBrain/Desktop/tempFile.mp3 ' 
done
rm $mp3FileName

