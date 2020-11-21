# TorBot

A YIFY torrent movie downloader extension that automates the boring process of downloading movies from torrent. Just select/highlight a movie along with its year or type in the movie in the extension and it will begin downloading the movie on your torrent client!

## Feature
  - Download and save the movie in a single click.

### Tech
1. Python
2. Selenium
3. HTML / CSS / JS

### Installation steps
TorBot requires Python.

1. Install the install.bat file.
2. Load unpacked extension from [Chrome extensions](chrome://extensions) by first turning on the dev mode and then selecting the Chrome Extension folder in the repository.
3. Pin the extension to use its UI.
4. Setup a virtual environment by running below steps in your project root.
5. Download webdriver for your browser. Here is the link for [Chromium-based browsers](https://chromedriver.chromium.org/downloads).
6. Add the path to your driver by changing the following line of code in tor.py
    ```py
    chrome_driver_binary = "Path\\to\\webdriver.exe"
    ```
7. Change the below line of code and the path to your browser's executable file.
    ```py
    options.binary_location = "Path\\to\\browser.exe"
    ```
8. And finally, change the below line of code to set up default download location.
    ```py
    prefs = {'download.default_directory': 'Path\\to\\Downloads', 'download.prompt_for_download': False}
    ```


### Python and selenium setup
```sh
pip install virtualenv
py -m venv env
..\env\Scripts\activate
pip install -r requirements.txt
```
This will get you started with the extension.

### How to use
There are primarily 2 ways to use the extension
1. UI / Popup mode- After pinning the extension, you can click on the button to view its UI and enter the movie name and the year itself. Press download to start the download.
2. The much more intuitive way- Let's say you google a movie, you like it. You can download it right away by selecting the movie name and year in a single selection and right clicking on it. This will open the browser's menu where you must get an option to download movie. Click on it. It must start your download right away. Yeah, that easy!

### Known bugs
1. Ads!!! Due to weird popup ads on torrent sites, selenium loses the context and fails due to which the download fails as well.


### Todos
 - Add movie to watchlist and periodically download movies when computer lacks space

License
----

Apache
