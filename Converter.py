from moviepy import VideoFileClip

# Assign filepaths to the below variables
input_file_path = None
output_file_path = None


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
    avi_to_mp4(input_file_path, output_file_path)