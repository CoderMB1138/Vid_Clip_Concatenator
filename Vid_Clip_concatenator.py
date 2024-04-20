import os
import sys
from moviepy.editor import VideoFileClip, concatenate_videoclips

def concatenate_videos(input_dir, output_dir):
    # Get all .mp4 files in the input directory
    video_files = [os.path.join(input_dir, file) for file in os.listdir(input_dir) if file.endswith(".mp4")]
    
    #can handle other formats with (".mp4", ".avi", ".mov", ".wmv")

    if not video_files:
        print("No .mp4 files found in the input directory.")
        return

    # Output file name
    output_video_file = os.path.join(output_dir, "output.mp4")

    # Check if the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        # If output file already exists, append a numerical increment
        file_index = 1
        while os.path.exists(output_video_file):
            output_video_file = os.path.join(output_dir, f"output_{file_index}.mp4")
            file_index += 1

    # Load all video clips
    video_clips = [VideoFileClip(file) for file in video_files]

    # Get properties of the first clip
    first_clip = video_clips[0]
    width, height = first_clip.size
    fps = first_clip.fps

    # Concatenate the video clips
    final_clip = concatenate_videoclips(video_clips)

    # Write the concatenated video to the output file
    final_clip.write_videofile(output_video_file, codec="libx264", fps=fps, bitrate="5000k", threads=4)

    # Close the video clips
    for clip in video_clips:
        clip.close()

    print(f"Concatenated video saved to: {output_video_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python concatenate_videos.py <input_directory> <output_directory>")
    else:
        input_directory = sys.argv[1]
        output_directory = sys.argv[2]
        concatenate_videos(input_directory, output_directory)

