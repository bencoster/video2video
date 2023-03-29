# Changes made in this fork:
This is my first attempt at working on a github script. This is a fork from rishbobb/video2video which added Controlnet support to Filarius/video2video fork. 

## Installation 
To install the video2video package from its Github repository on Windows, you can follow these steps:

1. Install Git for Windows: Go to the Git for Windows website (https://gitforwindows.org/) and download and install the latest version of Git for Windows.

2. Update the installation destination directory path: Navigate to the directory where you want to install video2video, for example "C:\Vid-Extract\stable-diffusion-webui". Then, clone the video2video repository by running the following command:

git clone https://github.com/bencoster/video2video.git

This will download the video2video repository to your local machine. The newly created video2video installation will be located at:

C:\Vid-Extract\stable-diffusion-webui\video2video

3. Install the required packages: Navigate to the root directory of the video2video repository and run the following command to install the required Python packages:

cd C:\Vid-Extract\stable-diffusion-webui\video2video
pip install -r requirements.txt

This will install all the required packages listed in the requirements.txt file.

4. Installation complete and now continue with the Support for ControlNet.
Note: Remember to hit enter/return key on each command when running the above commands on the Windows command line.

# Support for ControlNet:

How to use:
When generating, enable the ControlNet tab (Make sure you have ControlNet extension installed), and select your settings
Then check the "Using ControlNet" tab in the script settings
Generate and it will use ControlNet

# Automatic1111 Stable Diffusion WebUI Video2Video Extension

## Pluging for img2img video processing
- No more image files on hard disk.
- Video fps can be set as original, or changed.
- Now with latent space temporal blending.

Result saved to **output** folder **img2img-video** as MP4 file in H264 encoding (no audio). 

Added optional temporal blending for latent space. Applied per each step between previous and current frame.

Need a FFmpeg. For OS Windows implemented automatic installation of FFmpeg.

Under development, bugs applied.

## Dependencies
git
ffmpeg

skvideo (pip install sk-video)

## TODO

Bug: latent blending will work right only for batch_size = 1
