import asyncio
import os
import random
import re
import textwrap
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from youtubesearchpython.__future__ import VideosSearch
import numpy as np

from config import YOUTUBE_IMG_URL


def make_col():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def truncate(text):
    list = text.split(" ")
    text1 = ""
    text2 = ""
    for i in list:
        if len(text1) + len(i) < 30:
            text1 += " " + i
        elif len(text2) + len(i) < 30:
            text2 += " " + i

    text1 = text1.strip()
    text2 = text2.strip()
    return [text1, text2]


async def get_thumb(videoid):
    try:
        if os.path.isfile(f"cache/{videoid}.jpg"):
            return f"cache/{videoid}.jpg"

        url = f"https://www.youtube.com/watch?v={videoid}"
        if 1 == 1:
            results = VideosSearch(url, limit=1)
            for result in (await results.next())["result"]:
                try:
                    title = result["title"]
                    title = re.sub("\W+", " ", title)
                    title = title.title()
                except:
                    title = "Unsupported Title"
                try:
                    duration = result["duration"]
                except:
                    duration = "Unknown Mins"
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                try:
                    views = result["viewCount"]["short"]
                except:
                    views = "Unknown Views"
                try:
                    channel = result["channel"]["name"]
                except:
                    channel = "Unknown Channel"

            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"http://img.youtube.com/vi/{videoid}/maxresdefault.jpg"
                ) as resp:
                    if resp.status == 200:
                        f = await aiofiles.open(f"cache/thumb{videoid}.jpg", mode="wb")
                        await f.write(await resp.read())
                        await f.close()

            

            # title
        youtube = Image.open(f"thumb{videoid}.png")
        Mostafa = Image.open(f"{photo}")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(5))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        Xcenter = Mostafa.width / 2
        Ycenter = Mostafa.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = Mostafa.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.LANCZOS)
        logo = ImageOps.expand(logo, border=15, fill="white")
        background.paste(logo, (50, 100))
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("AFROTOMusic/assets/font.ttf", 40)
        font2 = ImageFont.truetype("AFROTOMusic/assets/font.ttf", 70)
        arial = ImageFont.truetype("AFROTOMusic/assets/font.ttf", 30)
        name_font = ImageFont.truetype("AFROTOMusic/assets/font.ttf", 30)
        para = textwrap.wrap(title, width=32)
        j = 0
        draw.text(
            (600, 150),
            "BELAL PLAYING",
            fill="white",
            stroke_width=2,
            stroke_fill="white",
            font=font2,
        )   
        
        
            # description
            views = f"Views : {views}"
            duration = f"Duration : {duration} Mins"
            channel = f"Channel : @UI_VM"

            image4.text((690, 450), text=views, fill="white", font=font4, align="left")
            image4.text(
                (690, 500), text=duration, fill="white", font=font4, align="left"
            )
            image4.text(
                (690, 550), text=channel, fill="white", font=font4, align="left"
            )

            image2 = ImageOps.expand(image2, border=20, fill=make_col())
            image2 = image2.convert("RGB")
            image2.save(f"cache/{videoid}.jpg")
            file = f"cache/{videoid}.jpg"
            return file
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL

