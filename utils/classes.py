from discord.ext import commands
from discord import Color
from typing import Dict
from random import choice

from res import hsk1


class ZhongWenBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.Zi = Zi.init()

        for color, RGB in kwargs.pop("colors").items():
            setattr(self, color, Color.from_rgb(*RGB))

        super().__init__(*args, **kwargs)

    async def setup_hook(self):
        print(f"Syncing app commands...")
        synced = await self.tree.sync()
        print(f"Synced {len(synced)} commands.")

    async def on_ready(self):
        print(f"{self.user.name} is ready.\n")


class Zi:
    hsk1: Dict[int, "Zi"] = {}

    def __init__(self, *, char: str, pinyin: str, translations: tuple, sentence: str, sentence_pinyin: str, sentence_meaning: str) -> None:
        self.id = id
        self.char = char
        self.pinyin = pinyin
        self.english = translations
        self.sentence = sentence
        self.sentence_pinyin = sentence_pinyin
        self.sentence_english = sentence_meaning

    def __repr__(self) -> str:
        return self.char
    
    @staticmethod
    def init():
        for char, data in hsk1.data.items():
            Zi.hsk1[data["id"]] = Zi(char=char, **data)

        return Zi
    
    @staticmethod
    def random():
        return choice(list(Zi.hsk1.values()))
