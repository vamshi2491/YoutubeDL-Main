import pytube
from pytube import YouTube

# Function to download a video from YouTube
def download_video(link):
    try:
        # Attempt to download the first stream of the video
        YouTube(link).streams.first().download(r"C:\Users\misandfo\Downloads")
        print("Video downloaded successfully")
    except pytube.exceptions.PytubeError as e:
        # Handle any exceptions thrown by pytube
        print("An error occurred: ", e)
    except Exception as e:
        # Handle any other exceptions
        print("An unexpected error occurred: ", e)

# Main function
def main():
    # Prompt the user for a video link
    link = input("Enter the link of the video you want to download: ")
    # Download the video
    download_video(link)

# If this script is the main entry point, run the main function
if __name__ == "__main__":
    main()
