# youtube-video-bot

<b>- To launch the executable<b>

Install dotnet35 and all versions of 4.0(4.0, 4.7, 4.8 etc)</br>
Install c++ redistributables: https://www.techpowerup.com/download/visual-c-redistributable-runtime-package-all-in-one/</br>
Install Google Chrome: www.google.com/chrome</br>
Install coresponding chromedriver in same directory as the bot: https://chromedriver.chromium.org/</br>

To launch, open bat scripts, and adjust arguments.

-c  --cycles  | Amount of cycles to run application</br>
-t  --min     | Minimal time to run a view</br>
-m  --max     | Maximal time to run a view</br>

<b>- To run python script<b>

1. Install python3: https://www.python.org/
During install python3:
- Set as envirnoment in path
- Disable Path lenght

2. Open powershell inside folder of the bot(using shift+right mouse button)
Run these commands:
- pip install selenium
- pip install pyinstaller

3. ......


[Runs both www.youtube.com/watch as music.youtube.com/watch links!!]

Note: launch.exe launches 60 threads using launch.bat, and requires dotnet 4.8, and a 12 core/24 thread processor, or a dual socket 6 core 12 thread, making the total 12 core 24 thread. Passmark as of 4-9-2020 should be around 13k.
