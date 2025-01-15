import os
import glob
from IPython.display import Image, display

# Install dependencies
os.system("pip install -r requirements.txt")

# Define the output folder
output_folder = "runs/detect/my_results"

# Perform inference on a test video 
os.system(f'python detect.py --source pothole_video.mp4 --weights PotHole.pt --project runs/detect --name my_results --exist-ok')

# Display the results
for imageName in glob.glob(f'{output_folder}/*.jpg'): 
    display(Image(filename=imageName))
