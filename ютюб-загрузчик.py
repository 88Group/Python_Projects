from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Ошибка")
    print("Загруза завершена")


link = input("Введи ссылку на ютюб: ")
Download(link)