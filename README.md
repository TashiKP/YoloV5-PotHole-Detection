<h1 align = "center"><samp>About</samp></h1>
<h4><samp>This model is used to detect potholes. The name of the pretrained model is "pothole.pt". This model is trained using a public dataset which had a collection 
of 665 images of roads with the potholes labeled. I will share the link to the dataset at the end! It has one class annotated which is "pothole". I have trained this model 
using the YOLOv5 model using 100 epochs and a batch size of 8. The metrics of the training will also be attached here.
</samp></h4>

<h1 align = "center"><samp>Setup</samp></h1>
<h4><samp>1) Clone this repository. </samp></h4>
<h4><samp>2) Change the working directory to this repository. </samp></h4>
<h4><samp>3) you can directly run the "main.py" file. This file will firstly get the required dependencies from the "requirements.txt". You will also have to change or modify the main file for inference. If you are doing it for video, you can directly put the file path. If you are doing it for images or live video feed, you will have to modify the file accordingly. </samp></h4>
<h4><samp>Note: After running the "main.py" file once, you can remove the part where you get the dependencies!</samp></h4>

<h1 align = "center"><samp>Training Information</samp></h1>
<h4><samp>I will share the training metrics here. The images in the dataset are put into a 70/20/10 train-valid-test split. </samp></h4>
<img src = "https://github.com/TashiKP/YoloV5-PotHole-Detection/blob/main/Training%20Information/results.png" width = "100%">
<img src = "https://github.com/TashiKP/YoloV5-PotHole-Detection/blob/main/Training%20Information/val_batch0_pred.jpg" width = "100%">
<h4><samp>The model shows steady improvement in both training and validation losses, indicating successful learning. While the validation loss fluctuates slightly, this is expected when evaluating unseen data. Precision and recall both improve, with precision reducing false positives and recall ensuring most objects are detected. The mAP metrics (0.5 and 0.5:0.95) also improve, suggesting the model performs well across different detection thresholds</samp></h4>


