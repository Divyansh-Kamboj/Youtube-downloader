from pytube import YouTube

myVideo = YouTube("https://www.youtube.com/watch?v=M-xDEeGvlVQ")

print("\n")
print("********************** Title **************************")


print("Video Title :"+myVideo.title)

print("\n")
print("********************** Thumbnail **************************")

print(myVideo.thumbnail_url)

print("\n")
print("********************** Video Streams **************************")

print(myVideo.streams.all)

print("\n")
print("********************** Download Video **************************")
print("********************** Wait Untill Download Is Finished **************************")

myVideo.streams.first().download()

print("Video has been downloaded!!")