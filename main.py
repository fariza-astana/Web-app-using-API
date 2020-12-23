from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests
app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get('/')
def home_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.get("/friend/{name}")
def hello_my_friend(name):
    return 'Hello, my friend, %s' % name.capitalize()

@app.get("/give-advice/{name}")
def give_advice(request: Request, name: str):
    url = 'https://api.adviceslip.com/advice'
    response = requests.get(url)

    my_list = ['Безвреден кто в гневе кричит. Бойся того, кто в гневе молчит.',
               'Худший человек из числа людей — это человек без стремлений.',
               'Воля, ты сильна, но пускай и тобой руководит сердце…',
               'Воспитывай волю — это броня, сохраняющая разум.',
               'Человек, запомнивший слова мудрых, сам становится благоразумным.',
               'Достоинство человека определяется его подходом к делу, а не завершением.',
               'Будь моя власть, я бы отрезал язык любому, кто уверждает, что человек неисправим.',
               'Кто отравил Сократа, сжег Жанну дАрк, распял Христа, закопал Мухаммеда в верблюжьих останках? Толпа. Значит, у толпы нет ума. Сумей направить ее на путь истины.',
               'Кричащий в гневе смешон, а страшен молчащий в гневе.',
               'Скромность, которая происходит от слабости, не достоинство.',
               'Человек - дитя своего времени. Если он плох, в этом виновны его современники.']
    import random
    random.choice(my_list)

    if response.status_code == 200:
        result = response.json()
        advice = result['slip']['advice']

        return templates.TemplateResponse('main.html', {
            'request': request,
            'advice': advice,
            'name': name.capitalize(),
            'poet': random.choice(my_list)
        })
    else:
        return 'Что-то не так, похоже сегодня ты останешься без совета.'
