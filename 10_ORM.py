# ORM, API, JSON
# ORM - Object Relation Mapping - відображення даних
#  та їх зв'язків на об'єкти та їх зв'язки
#
# Віртуальне оточення (venv) дозволяє розділяти проекти
# з їх налаштуваннями та бібліотеками. Створюється як окрема
# директорія з локальними виконавчими кодами (Python) та
# додатковими модулями (бібліотеками). Традиційно вилучається
# з репозиторію (.gitignore). Для того щоб створити в.оточення
# подається команда
# > python -m venv .venv
# якщо є декілька python, то може знадобитись прямо вказати
# на конкретну версію
# > &"C:\path-to-python\python.exe" -m venv .venv
# Після встановлення оточення необхідно активувати.
# > .venv/Scripts/Activate.ps1
# (або відкрити новий термінал у VS Code, але
# в тому, що воно дійсно активувалось,
# у будь-якому разі
# обов'язково
# слід переконатись - за видом промпта).

# pip install requests
import requests
nbu_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"


class NbuRate :
    '''
    {
        "r030": 840,
        "txt": "Долар США",
        "rate": 45.0811,
        "cc": "USD",
        "exchangedate": "24.11.2026",
        "special": "N"
    },
    '''

    def __init__(self, nbu_rate:dict|None = None,
                 r030:int = 0, txt:str = "", rate:float = 0.0, cc:str = "", exchangedate:str = "", special:str = ""):
        if nbu_rate is not None :
            self.r030 = nbu_rate['r030']
            self.txt = nbu_rate['txt']
            self.rate = nbu_rate['rate']
            self.cc = nbu_rate['cc']
            self.exchangedate = nbu_rate['exchangedate']
            self.special = nbu_rate['special']
        else :
            self.r030 = r030
            self.txt = txt
            self.rate = rate
            self.cc = cc
            self.exchangedate = exchangedate
            self.special = special


    def __str__(self):
        return "%s (%s): %f UAH" % (self.cc, self.txt, self.rate)




def main() :
    response = requests.get(nbu_url)
    data = response.json()
    print("Loaded", len(data), "rates")
    rate = NbuRate(None, **data[0])
    print(rate)
    rate = NbuRate(data[1])
    print(rate)


if __name__ == "__main__":
    main()
