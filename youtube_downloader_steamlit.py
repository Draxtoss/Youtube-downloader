import streamlit as st
from pytube import YouTube
import requests
import os
downloads_folder = os.path.expanduser("~\Downloads")
pattern = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"'
def main():
    st.title("YouTube Downloader")
    
    # Get YouTube video URL from user input
    link = st.text_input("Enter the video link: ")
    if st.button("Download Audio"):
        if try_site(link):
            yt = YouTube(link)
            yt.streams.filter(only_audio=True).first().download(downloads_folder)
            st.success("Audio downloaded successfully!")
        else:
            st.error("Invalid YouTube video or audio URL")
    
    if st.button("Download Video"):
        if try_site(link):
            yt = YouTube(link)
            streams = yt.streams.filter(file_extension='mp4')
            st.write("Available Quality Options:")
            streams = yt.streams.filter(progressive=True).order_by('resolution').desc()
            resolutions = [stream.resolution for stream in streams]
            for i, res in enumerate(resolutions):
                st.write(f"{i+1}. {res}")
            choice = st.number_input("Enter the number of the desired quality option: ", value=1, min_value=1, max_value=len(resolutions), step=1)
            streams.get_by_resolution(resolutions[choice-1]).download(downloads_folder)
            st.success("Video downloaded successfully!")
        else:
            st.error("Invalid YouTube video URL")
            

def try_site(url):
    request = requests.get(url)
    return False if pattern in request.text else True

if __name__ == '__main__':
    main()
