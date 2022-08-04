import requests
import socket
import threading
from twitchio.ext import commands
import json

try:
    with open("config.json", "r") as f:
        data = json.load(f)
        osu_nickname = data["osu_nickname"]
        osu_token = data["osu_IRC_token"]
        clientID = data["osu_client_id"]
        client_secret = data["osu_client_secret"]
        twitch_username = data["twitch_username"]
        twitch_token = data["twitch_client_secret"]
except FileNotFoundError:
    osu_nickname = input("osu! nickname: ")
    osu_token = input("osu! IRC password: ")
    clientID = input("osu! client ID: ")
    client_secret = input("osu! client secret: ")
    twitch_username = input("Twitch username: ")
    twitch_token = input("Twitch client secret: ")
    data = {
        "osu_nickname": osu_nickname,
        "osu_IRC_token": osu_token,
        "osu_client_id": clientID,
        "osu_client_secret": client_secret,
        "twitch_username": twitch_username,
        "twitch_client_secret": twitch_token,
    }

    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)


SERVER = "irc.ppy.sh"
PORT = 6667
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def get_osuApi_token():
    data = {
        "client_id": clientID,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
        "scope": "public",
    }

    response = requests.post("https://osu.ppy.sh/oauth/token", data=data)
    return response.json()["access_token"]

def get_beatmap_data(beatmap_id):
    token = get_osuApi_token()
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(f"https://osu.ppy.sh/api/v2/beatmaps/{beatmap_id}", headers=headers).json()
    beatmap_data = f"{response['beatmapset']['artist']} - {response['beatmapset']['title']} [{response['version']}]"
    return beatmap_data

def osu_irc_login(username, password):
    irc.connect((SERVER, PORT))
    irc.sendall(f"PASS {password}\n".encode())
    irc.sendall(f"USER {username}\n".encode())
    irc.sendall(f"NICK {username}\n".encode())
    data = irc.recv(2048).decode()
    if "001" in data:
        print(f"Logged in to Bancho as {username}")
        listener()
        return True
    elif "464" in data:
        irc.close()
        print("Couldn't connect to Bancho")
        print("Bad authentication token")
        return False

def listener(running=False):
    if not running:
        threading.Thread(target=listener, args=(True,)).start()
    else:
        started = True
        buffer = ""
        data = ""

        while started:
            while True:
                part = irc.recv(1024).decode()
                data += part
                if len(part) != 1024:
                    break
            buffer = data.split("\n")
            for i in buffer:
                msg = i.replace("!cho@ppy.sh", "")
                if "PING" in msg:
                    irc.sendall(f"{msg.replace('PING', 'PONG')}\n".encode())

            data = ""


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=twitch_token, prefix='!', initial_channels=[twitch_username])
        self.mods = ["EZ", "NF", "HT", "HR", "SD", "PF", "DT", "NC", "HD", "FL", "RX", "AP", "SO", "AT", "SV2"]

    async def event_ready(self):
        print(f'Logged in to Twitch as {self.nick}')
        print("Bot running")

    async def sendPM(self, beatmapLink: str, author, mods):

        beatmap_id = beatmapLink.split("/")[-1]
        beatmap_data = get_beatmap_data(beatmap_id=beatmap_id)
        request = f"{author} -  [{beatmapLink} {beatmap_data}] {mods}"

        irc.sendall((f"PRIVMSG {osu_nickname.lower()} :{request}\r\n").encode())
        print(f"Beatmap requested: {author} - {beatmap_data} {mods}")

    async def event_message(self, message):
        msg = str(message.content).split()
        mods_req = ""
        for word in msg:
            if "osu.ppy.sh/beatmapsets" in word:
                beatmapLink = word
            if "+" in word:
                mods_comb = word[1:]
                mods_comb = [mods_comb[i:i+2].upper() for i in range(0, len(mods_comb), 2)]
                for mod in mods_comb:
                    if mod in self.mods:
                        mods_req += mod
        
        if mods_req != "":
            mods_req = f"+{mods_req}"

        if beatmapLink != "":
            await self.sendPM(beatmapLink, message.author.display_name, mods_req)


if __name__ == "__main__":
    twitchBot = Bot()
    osu_irc_login(osu_nickname, osu_token)
    twitchBot.run()
