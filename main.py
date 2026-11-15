import os
from highrise import BaseBot, Highrise

class Bobo(BaseBot):
    async def on_start(self, session_metadata) -> None:
        print("Bobo is online! 💖")
        await self.highrise.chat("Bobo is online! 💖✨")

    async def on_chat(self, user, message: str) -> None:
        print(f"{user.username}: {message}")
        msg = message.lower().strip()

        if msg == "hi" or msg == "hello":
            await self.highrise.chat(f"Hi {user.username}! 💖")
        elif msg == "!bobo":
            await self.highrise.chat("Yes? I'm here! ✨ What do you need?")
        elif msg == "!dance":
            await self.highrise.emote("dance-tiktok", user.id)
        elif msg == "!hug":
            await self.highrise.chat(f"{user.username} gets a big hug from Bobo! 🤗💖")

if __name__ == "__main__":
    bot = Bobo()
    Highrise(bot).run_with_websocket(
        os.getenv("ROOM_ID"),
        os.getenv("BOT_TOKEN")
    )
