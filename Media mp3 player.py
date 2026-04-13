
#basic mp3 player, plays one song at a time and you must select what song you want to play due to the nature of using os directory
#dynamic more engaging program that uses your own device stored files, files mus end with .mp3

import pygame
import os
import random
import time

print("Hello, welcome to your mp3 media player. For this program you will need to know the pathname to the folder where your mp3 files are stored \n") 
path = input("Folder path: ").strip()
folder_path = path
   
pygame.mixer.init()#loop through every file and add mp3 files to list mp3_tunes
mp3_tunes =([file for file in os.listdir(folder_path) if file.endswith(".mp3")])
#pick a random track out of list to play
number_of_files = len(mp3_tunes)
print(f"You have {number_of_files} sound files in this playlist")
print("These are your current songa you can play\n")
print(mp3_tunes)

while True:
    
    track = input("\nPLease enter the exact name of the song: ").strip()
    if track not in mp3_tunes:
        print("Please enter the valid exact name of the file from the list above(copy and paste if necessary, do not include start and end quotes)")
    else:
        file_path = os.path.join(folder_path, track)
        pygame.mixer.music.load(file_path)
        
        while True:
            n = input("\nThere are 5 functions, \n'play', 'pause', 'unpause', 're-pick' and 'stop'\n ")
       
            if n == "play":
                pygame.mixer.music.play()
                print(f"\nPlaying: {track}")
            elif n == "pause":
                pygame.mixer.music.pause()
            elif n == "unpause":
                pygame.mixer.music.unpause()
            elif n == 're-pick':
                break
            elif n == "stop":
                print("Thank you for using the mp3 player")
                time.sleep(2)
                exit()
    


      


            
        
        
        




