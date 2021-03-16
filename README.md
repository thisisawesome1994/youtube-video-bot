# youtube-video-bot

<b>- To launch the executable<b>

Install dotnet35 and all versions of 4.0(4.0, 4.7, 4.8 etc)</br>
Install c++ redistributables: https://www.techpowerup.com/download/visual-c-redistributable-runtime-package-all-in-one/</br>
Install Google Chrome: www.google.com/chrome</br>
Install coresponding chromedriver in same directory as the bot: https://chromedriver.chromium.org/</br>

To launch, open bat scripts, and adjust arguments.</br>

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


[Runs both www.youtube.com/watch as music.youtube.com/watch links!!, not working like that anymore.]

Note: launch.exe launches 60 threads using launch.bat, and requires dotnet 4.8, and a 12 core/24 thread processor. Passmark as of 4-9-2020 should be around 13k.
I included the visual studio code file, so you can create your own launch.exe adjusted to your situation. (compile your own C# launcher using developer kit)

Note 2: Readme is for old version. Now you can just run exe from shell:startup, and can add reboot script if wanted.
Links open random now, like proxies. Wait times are hardcoded but can be changed in python file.
I used "pyinstaller -F YoutubeBot.py" to compile bot.

Requirements:
pip install selenium requests pyinstaller
