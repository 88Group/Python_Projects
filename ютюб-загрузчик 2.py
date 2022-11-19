# importing the module
from pytube import YouTube

# where to save

#SAVE_PATH = "C://Users/ZaFaR/Desktop/ютюб загрузчик/" #to_do
#E:/
# link of the video to be downloaded
link = input("Введи ссылку на ютюб: ")
SAVE_PATH = input("Введи путь куда сохранить: __E:/__ или так __C://Users/ZaFaR/Desktop/ютюб загрузчик/__")
#link="https://www.youtube.com/watch?v=xWOoBJUqlbI"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

d_video = yt.streams.get_highest_resolution()
try:
	# downloading the video
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')
