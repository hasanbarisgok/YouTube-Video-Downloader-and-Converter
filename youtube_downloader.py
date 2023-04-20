from pytube import YouTube
import moviepy.editor as mp 
import os 
import streamlit as st 


class converter():
    
    def __init__(self):
        
        
        #Input the url from user. (st.text_input = text_area)
        self.url : str = st.text_input("Enter the video url.")

        #Format types, and we're using the list in select_box function.
        self.format_types = ["Mp4","Only Audio"]
        
        if self.url:
            self.general_info()
        
        
    def general_info(self):
        
        #Creating the YT Variable using PyTube Library. We're using the link in all our process.
        self.yt = YouTube(self.url)
        
        #The title of the video
        #self.title = self.yt.title
        
        #The duration of the video in seconds
        #self.duration = self.yt.length
        
        #The author/channel name of the video
        #self.author = self.yt.author
        
        #The video description of the video.
        #self.description = self.yt.description
        
        #The published date of the video.
        #self.published_date = self.yt.publish_date
        
        #The tags of the video meta which are using.
        #self.tags = self.yt.keywords 
        
        #The thumbnail image of the video.
        #self.img = self.yt.thumbnail_url
        
        self.select_format()
            
    def select_format(self):
        self.selected_format = st.selectbox("Please select a format:", self.format_types)
        
        # Starting download process as option user wanted.
        if st.button("Download"):
            
            self.download_mp4()
            
    def download_mp4(self):
        
        
        with st.spinner("Downloading..."):
        
        
            # Downloading for mp4
            self.stream = self.yt.streams.filter(
                progressive=True,
                file_extension="mp4"
            ).order_by("resolution").desc().first()
            self.stream.download(output_path="./hbg_musics")
            
        st.success("Download completed. (mp4)")
        
        if self.selected_format == self.format_types[1]: #mp3
            
        
        # Converting mp4 to mp3
            with st.spinner("Converting... (mp4 to mp3)"):
                
                self.mp4_file = f"./hbg_musics/{self.stream.default_filename}"
                self.mp3_file = f"./hbg_musics/{self.stream.default_filename}.mp3"
                
                clip = mp.AudioFileClip(self.mp4_file)
                clip.write_audiofile(self.mp3_file)
                clip.close()
            st.success("Converting completed.")
            
            # Remove the original mp4 file
            os.remove(self.mp4_file)
            
        

abc = converter()
