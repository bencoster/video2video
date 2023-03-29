# Changes made in this fork:
This is my first attempt at working on a github script. This is a fork from rishbobb/video2video which added Controlnet support to Filarius/video2video fork. 

## Installation 
To install the video2video package from its Github repository on Windows, you can follow these steps. Remember to hit enter/return key on each command:

1. Install Git for Windows: Go to the Git for Windows website (https://gitforwindows.org/) and download and install the latest version of Git for Windows.
2. Update the following example video2video installation destination with your Automatic1111 installation directory path. For example on my computer this is found in this location "C:\Vid-Extract\stable-diffusion-webui" adjust this to suit your computer. 

  C:\>cd "C:\Vid-Extract\stable-diffusion-webui"         <---- Enter in your Automatic1111 installation directory path in the quoations. Then hit enter 
  C:\Vid-Extract\stable-diffusion-webui                  <---- The prompt should now show your 

3. To clone the video2video repository to Automatic1111 location on your computer. In this example the above "C:\Vid-Extract\stable-diffusion-webui" is where Automatic1111 was installed, run the following command to clone the video2video repository. This will download the video2video github repository to your local machine. 

  git clone https://github.com/bencoster/video2video.git

  When you type the above at the commandline on Windows in this example it will look like this at the command prompt:
  C:\Vid-Extract\stable-diffusion-webui\git clone https://github.com/bencoster/video2video.git

For this example the newly created video2video installation is now at: 
  C:\Vid-Extract\stable-diffusion-webui\video2video

4. Install the required packages: Navigate to the root directory of the video2video repository and run the following command to install the required Python packages:

  cd C:\Vid-Extract\stable-diffusion-webui\video2video
  
  This will install all the required packages listed in the requirements.txt file.
  pip install -r requirements.txt

5. Installation complete and now continue with the Support for ControlNet

Support for ControlNet:

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
