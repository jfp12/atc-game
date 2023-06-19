from playsound import playsound
import threading


# if __name__ == "__main__":
#
#     threading.Thread(target=playsound, args=('0011756.mp3',), daemon=True).start()
#
#     i=0
#     while True:
#         i+=1
#         print(i)
#

from play_sounds import play_file, DEFAULT_SONG
from pathlib import Path

# play without blocking
play_file(Path("0011756.mp3"), block=False)

i=0
while True:
    i+=1
    print(i)
