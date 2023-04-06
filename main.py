from fastapi import FastAPI
import random
from datetime import datetime

app = FastAPI()


@app.get('/picture')
def get_picture():
    now_month = datetime.today().month

    if now_month in list(range(3, 6)):
        now_season = 'spring'
    elif now_month in list(range(6, 9)):
        now_season = 'summer'
    elif now_month in list(range(9, 12)):
        now_season = 'autumn'
    else:
        now_season = 'winter'

    f = open(f'./image_src/{now_season}_image.txt')
    images = f.readlines()

    random_image = random.choice(images)
    random_image = random_image.replace('\n', '')

    return random_image
