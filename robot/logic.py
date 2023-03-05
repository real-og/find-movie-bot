from robot.models import Movie, Serial
from django.db import models
import random
from typing import Union, Optional
from asgiref.sync import sync_to_async

async def get_by_id(id) -> Union[Movie, Serial, None]:
    res = None
    try:
        res = await Movie.objects.aget(id=id)
        return res
    except:
        pass
    try:
        res = await Serial.objects.aget(id=id)
        return res
    except:
        pass
    return res
    
async def get_by_code(code: str) -> Union[Movie, Serial, None]:
    res = None
    try:
        res = await Movie.objects.aget(code=code)
        return res
    except:
        pass
    try:
        res = await Serial.objects.aget(code=code)
        return res
    except:
        pass
    return res


async def get_random_movie(genre) -> Optional[Movie]:
    movies = await get_by_genre(Movie, genre)
    if len(movies) == 0:
        return None
    return random.choice(movies)

async def get_random_serial(genre) -> Optional[Movie]:
    series = await get_by_genre(Serial, genre)
    if len(series) == 0:
        return None
    return random.choice(series)

async def get_random_oscar() -> Union[Movie, Serial, None]:
    candidates = []
    async for film in Movie.objects.filter(has_oscar=True):
        candidates.append(film)
    async for film in Movie.objects.filter(has_oscar=True):
        candidates.append(film)
    if len(candidates) == 0:
        return None
    return random.choice(candidates)


async def get_by_genre(mod, genre) -> list:
    res = []
    async for film in mod.objects.filter(genre=genre):
        res.append(film)
    return res

async def get_by_codes(ids):
    queryset = Movie.objects.filter(id__in=ids)
    records = await sync_to_async(list)(queryset)
    queryset = Serial.objects.filter(id__in=ids)
    records2 = await sync_to_async(list)(queryset)
    return records + records2

