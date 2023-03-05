from robot.models import Movie, Serial
from django.db import models
import random
from typing import Union, ClassVar, Optional

async def get_by_id(id) ->Union[Movie, Serial]:
    res = await Movie.objects.aget(id=id)
    return res


async def get_random_movie(genre) -> Optional[Movie]:
    movies = await get_by_genre(Movie, genre)
    if len(movies) == 0:
        return None
    return random.choice(movies)

async def get_random_serial(genre) -> Serial:
    series = await get_by_genre(Serial, genre)
    return random.choice(series)

async def get_random_oscar(genre) -> Union[Movie, Serial]:
    candidates = []
    async for film in Movie.objects.filter(has_oscar=True):
        candidates.append(film)
    async for film in Movie.objects.filter(has_oscar=True):
        candidates.append(film)
    return random.choice(candidates)


async def get_by_genre(mod, genre) -> list:
    res = []
    async for film in mod.objects.filter(genre=genre):
        res.append(film)
    return res

