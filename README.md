# Changes made in this fork:
This is my first attempt at working on a github script. This is a fork from rishbobb/video2video which added Controlnet and direct Video support came from Filarius/video2video fork. Happy to be corrected

## Backgound 
Install Automatic1111 before proceeding to install the video2video script. Automatic1111 can be installed following the instructions at https://github.com/AUTOMATIC1111/stable-diffusion-webui/ 

## Installation
To install the video2video package from its Github repository on Windows, you can follow these steps. Remember to hit enter/return key on each command:

1. **Install Git for Windows**: Go to the Git for Windows website (https://git-scm.com/download/win) and download and install the latest version of Git for Windows.

2. **Update the example video2video installation destination with your Automatic1111 installation directory path**. For example on my computer this is found in this location "C:\Vid-Extract\stable-diffusion-webui" adjust this to suit your computer.
```shell
C:\>cd "C:\Vid-Extract\stable-diffusion-webui"   <---- Enter in your Automatic1111 installation directory path in the quotations. Then hit enter
C:\Vid-Extract\stable-diffusion-webui            <---- The prompt should now show your
```
3. **Clone the video2video repository to Automatic1111 location on your computer.**
In this example the above "C:\Vid-Extract\stable-diffusion-webui" is where Automatic1111 was installed, run the following command to clone the video2video repository. This will download the video2video github repository to your local machine.
```shell
git clone https://github.com/bencoster/video2video.git
```
When you type the above at the commandline on Windows in this example it will look like this at the command prompt:
C:\Vid-Extract\stable-diffusion-webui\git clone https://github.com/bencoster/video2video.git

For this example the newly created video2video installation is now at:
```shell
C:\Vid-Extract\stable-diffusion-webui\video2video
```
4. **Install the required python packages:** 
Navigate to the root directory of the video2video repository and run the following command to install the required Python packages:
```shell
cd C:\Vid-Extract\stable-diffusion-webui\video2video
```
This will install all the required packages listed in the requirements.txt file.
```shell
pip install -r requirements.txt
```
The pip install command above resulted in this successfull install message on my Windows 11 computer
```shell
C:\Vid-Extract\stable-diffusion-webui\video2video>pip install -r requirements.txt
Collecting sk-video
  Downloading sk_video-1.1.10-py2.py3-none-any.whl (2.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 7.5 MB/s eta 0:00:00
Requirement already satisfied: scipy in c:\users\bcost\appdata\local\programs\python\python310\lib\site-packages (from sk-video->-r requirements.txt (line 1)) (1.9.3)
Requirement already satisfied: numpy in c:\users\bcost\appdata\local\programs\python\python310\lib\site-packages (from sk-video->-r requirements.txt (line 1)) (1.24.0)
Installing collected packages: sk-video
Successfully installed sk-video-1.1.10
```
5. **Installing dependency FFMPEG**
To install the latest compiled FFmpeg for Linux, Windows, and macOS, follow the instructions for each operating system below:
**Linux**
For Ubuntu and other Debian-based systems, you can use the following commands:
```shell
sudo add-apt-repository ppa:jonathonf/ffmpeg-4
sudo apt-get update
sudo apt-get install ffmpeg
```
For Fedora, use the following commands:
```shell
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install ffmpeg
```
For CentOS and RHEL, use the following commands:
```shell
sudo yum localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
sudo yum install ffmpeg
```
**Windows**
Visit the FFmpeg official website's download page at https://ffmpeg.org/download.html.
Under the "Windows" section, click on the link for "Windows Builds" provided by gyan.dev or BtbN.
Download the appropriate build for your system (32-bit or 64-bit) in either a static or shared version.
Extract the downloaded zip file to a folder of your choice (e.g., C:\ffmpeg).
Add the FFmpeg bin folder to the Windows PATH:
Press the Windows key and type "Environment Variables," then click on "Edit the system environment variables."
Click on the "Environment Variables" button.
Under "System variables," find the variable named "Path," select it, and click on "Edit."
Click on "New" and add the path to the bin folder within the extracted FFmpeg folder (e.g., C:\ffmpeg\bin).
Click "OK" to save the changes.
Now, you can use FFmpeg from the command prompt.

**macOS**
Using Homebrew, you can install FFmpeg on macOS by running the following commands in the Terminal:

```shell
brew update
brew install ffmpeg
```
*If you don't have Homebrew installed, you can install it by following the instructions at https://brew.sh/.
After the installation is complete, you can use FFmpeg from the Terminal.*

6. Installation complete and now continue with the Support for ControlNet.

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
automatic1111 *<--- See Installation Notes above*
git       *<--- See Installation Notes above*
ffmpeg    *<--- See Installation Notes above*
skvideo   *<--- See Installation Notes above or run in a terminal/command prompt: pip install sk-video*

## TODO

Bug: latent blending will work right only for batch_size = 1
