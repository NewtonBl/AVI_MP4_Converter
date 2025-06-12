from moviepy import VideoFileClip

def avi_to_mp4(input_path, output_path):
    """
    Converts an AVI video file to MP4 format.

    Args:
        input_path (str): Path to the input .avi file.
        output_path (str): Path to save the output .mp4 file.
    """
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    clip.close()

if __name__ == "__main__":
    avi_to_mp4("I:\\39 Blake Newton\Other\\Vince's Mirra Backrest Test\\04.02\\04.02 Crack Formation.AVI", "04.02 Crack Formation.mp4")