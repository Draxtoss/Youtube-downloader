from pytube import YouTube
import os
import requests
import ffmpeg
downloads_folder = os.path.expanduser("~\Downloads")
pattern = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"'


def try_site(url):
    request = requests.get(url)
    return False if pattern in request.text else True

def video_downloader():
    video_link = input("Enter the video link: ")
    if try_site(video_link):
        yt = YouTube(video_link)
        streams = yt.streams.filter(file_extension='mp4')
        print("Available Quality Options:")
        streams = yt.streams.filter()(progressive=True).order_by('resolution').desc()
        resolutions = [stream.resolution for stream in streams]
        for i, res in enumerate(resolutions):
            print(f"{i+1}. {res}")
        choice = int(input("Enter the number of the desired quality option: "))
        streams.get_by_resolution(resolutions[choice-1]).download(downloads_folder)
        print(f"Video downloaded to {downloads_folder}")
        menu_downloader()

def audio_downloader():
    audio_link = input("Enter the link: ")
    if try_site(audio_link):
        yt = YouTube(audio_link)
        yt.streams.filter(only_audio=True).first().download(downloads_folder)
        print(f"Audio downloaded to {downloads_folder}")
        menu_downloader()
def menu_downloader():

    while True:
        print("1. Video Downloader")
        print("2. Audio Downloader")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            video_downloader()
        elif choice == 2:
            audio_downloader()
        elif choice == 3:
            break
        else:
            print("Invalid choice")
    print("Exiting...")
menu_downloader()
        
        