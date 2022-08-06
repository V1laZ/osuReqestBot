# osuReqestBot
Simple bot that sends osu! beatmap requests from twitch chat to your osu! chat
## First start
When you first run the app it will require some information from you and create a config.json file with it for future starts. Do not share this file with anyone!

### How to obtain:
- **osu! nickname** - your osu! username. Replace spaces with underscores (e.g., `beppy master 1000` becomes `beppy_master_1000`)
- **osu! IRC password** - the password from [IRC Authentication](https://osu.ppy.sh/p/irc) page
- **osu! client ID** and **osu! client secret**  
	- Go to [settings](https://osu.ppy.sh/home/account/edit) in your osu! profile
    - Scroll down to OAuth and click **New OAuth Application**  
    - Name it whatever you want and leave Application Callback URL blank  
    - Click **Register application**  
    - Here you can see your **Client ID** and **Client Secret**  
- **Twitch username** - your twitch username
- **Twitch client secret**  
    - Go to https://twitchtokengenerator.com and login  
    - I am here to get a... **Bot Chat Token**  
    - Authorize the app  
    - Use **ACCESS TOKEN**  

## For users
Download .exe from [releases](https://github.com/V1laZ/osuReqestBot/releases/tag/v1.0)

## For developers
Open project folder in VS Code and type in terminal
```
pipenv shell
```
then to install project dependencies
```
pipenv install
```
open VS Code command pallete <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> and type
```
Python: Select Interpreter
```
select interpreter corresponding to project name which should be something like *osuReqestBot-O3zasd51*  
  
run the app with <kbd>F5</kbd>
