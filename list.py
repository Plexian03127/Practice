songs = ["a노래","b노래","c노래","d노래"]

print(songs)
print(songs[0])
print(songs[1])
print(songs[2])
print(songs[3])

for song in songs:
    print(song)

song1 = "a노래"
song2 = "b노래"
song3 = "c노래"
song4 = "d노래"

print(song1)
print(song2)
print(song3)
print(song4)

import random
import time
print("AI야 노래 한 곡만 추천해줘")
print("알겠습니다. 제가 열심히 분석해서 고객님께 노래를 한 곡 추천합니다.")
ai_song = random.choice(songs)
dd = time.sleep(1)
print("두구두구둥...")
dd = time.sleep(3)
print(f"제가 추천하는 노래는 {ai_song}입니다.")