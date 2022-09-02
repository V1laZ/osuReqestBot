# osuReqestBot
Simple bot that sends osu! beatmap requests from twitch chat to your osu! chat
## Table of contents
- [osuReqestBot](#osureqestbot)
  - [Table of contents](#table-of-contents)
  - [For users](#for-users)
  - [For developers](#for-developers)
    - [Prerequisities](#prerequisities)
    - [Install dependencies](#install-dependencies)
    - [Debug in VS Code](#debug-in-vs-code)
  - [First start](#first-start)
    - [Required information](#required-information)

## For users
Download .exe from [releases](https://github.com/V1laZ/osuReqestBot/releases/tag/v1.0)

Might get flagged as virus by some antiviruses. If it does happen either disable your antivirus or download the source code and run it with python directly.  

How to do it:
- Download and install [Python](https://www.python.org/downloads/)
- Open **cmd** and type
  ```
  pip install twitchio requests
  ```
- Download [source code](https://github.com/V1laZ/osuReqestBot/releases/tag/v1.0)
- Unzip it 
- Open **cmd** and `cd` to source code directory
- Type in **cmd**
  ```
  python main.py
  ```

## For developers
### Prerequisities
- [Python](https://www.python.org/downloads/)  
- [pipenv](https://pypi.org/project/pipenv/)   

### Install dependencies
- Start virtual environment
  ```
  pipenv shell
  ```
- Install dependencies
  ```
  pipenv install
  ```

### Debug in VS Code

- Open VS Code command pallete <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> and type
  ```
  Python: Select Interpreter
  ```
  select interpreter corresponding to project name which should be something like *osuReqestBot-O3zasd51*  
  
- run the app with <kbd>F5</kbd>

## First start
When you first run the app it will require some information from you and create a config.json file with it for future starts. Do not share this file with anyone!

### Required information
- **osu! nickname** - your osu! username. Replace spaces with underscores (e.g., *beppy master 1000* becomes *beppy_master_1000*)
- **osu! IRC password** - the password from [IRC Authentication](https://osu.ppy.sh/p/irc) page
- **osu! client ID** and **osu! client secret**  
	- Go to [settings](https://osu.ppy.sh/home/account/edit) in your osu! profile
    - Scroll down to OAuth and click **New OAuth Application**  
    - Name it whatever you want and leave Application Callback URL blank  
    - Click **Register application**  
    - Here you can see your **Client ID** and **Client Secret**  
- **Twitch username** - your twitch username
- **Twitch client secret**
    1. Go to https://twitchtokengenerator.com/ and login
    2. I am here to get a... **Bot Chat Token**
    3. Authorite the app
    4. Use **ACCESS TOKEN**
