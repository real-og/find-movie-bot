from robot.models import Movie, Serial
from django.db import models
import random
from typing import Union, ClassVar


async def get_random_movie() -> Movie:
    movies = await get_all(Movie)
    return random.choice(movies)

async def get_random_serial() -> Serial:
    series = await get_all(Serial)
    return random.choice(series)

async def get_random_oscar() -> Union[Movie, Serial]:
    candidates = []
    async for film in Movie.objects.filter(has_oscar=True):
        candidates.append(film)
    async for film in Movie.objects.filter(has_oscar=True):
        candidates.append(film)
    return random.choice(candidates)


async def get_all(mod) -> list:
    res = []
    async for film in mod.objects.filter():
        res.append(film)
    return res

