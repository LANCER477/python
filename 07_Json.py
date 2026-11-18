# Робота з JSON
import json

# Основні правила JSON:
# 1. Валідним JSON є примітиви:
#    string - "The String" - тільки у ""
#    number - 10, 0.1, 1.2e3
#    bool - true, false
#    null
# 2. Комплексними типами є:
#    array - [JSON, JSON, JSON]
#    object - {"key1": JSON, "key2": JSON }
#
# У Python не всі JSON примітиви відповідають
# внутрішнім типам даних: null <-> None, true/false <-> True/False
# array <-> tuple/list, object <-> dict, number/bignumber <-> int/float
# а також різнотипні дані у масивах

json_str = '''{
    "k1": "The String",
    "Ї": "Ґранд вітання!",
    "k2": 10,
    "k3": 0.1,
    "k4": 1.2e3,
    "k5": 12345678901234567890123,
    "k6": true,
    "k7": false,
    "k8": null,
    "arr1": [1, 2, 3, 4, 5],
    "arr2": [1, "2", "true", null, 0.5],
    "obj": {
        "o1": 0.12345678901234568,
        "o2": "null"
    }
}'''


json_str_2 = '''
{
    "k1": "The String",
    "\\u0407": "\\u0490\\u0440\\u0430\\u043d\\u0434 \\u0432\\u0456\\u0442\\u0430\\u043d\\u043d\\u044f!",
    "k2": 10,
    "k3": 0.1,
    "k4": 1200.0,
    "k5": 12345678901234567890123,
    "k6": true,
    "k7": false,
    "k8": null,
    "arr1": [
        1,
        2,
        3,
        4,
        5
    ],
    "arr2": [
        1,
        "2",
        "true",
        null,
        0.5
    ],
    "obj": {
        "o1": 0.12345678901234568,
        "o2": "null"
    }
}
'''



def main() :
    json_data = json.loads(json_str)
    for k,v in json_data.items() :
        print(k, type(v), v)
        if isinstance(v, dict) :
            for k2, v2 in v.items() :
                print(k2, type(v2), v2)
    # data -> str
    data_str = json.dumps(json_data, indent=4)
    print("------------")
    print(data_str)
    # str -> data
    print("------------")
    json_data_2 = json.loads(json_str_2)
    print(json_data_2)
    print(json_data_2['Ї'] == json_data['Ї'], json_data['Ї'])
    # data -> file
    # зазначення кодування "utf-8" при відкритті файлу
    # не змінює екранування Юнікод-символів
    with open("data_2.json", "w", encoding="utf-8") as file :
        json.dump(json_data_2, file, indent=4)
    with open("data_3.json", "w", encoding="utf-8") as file :
        # для вимкнення екранування символів Юнікоду
        # встановлюється параметр ensure_ascii=False
        json.dump(json_data_2, file, indent=4, ensure_ascii=False)
    # file -> data
    with open("data_2.json", "r", encoding="utf-8") as file :
        json_data_3 = json.load(file)
        print(json_data_3['Ї'] == json_data['Ї'], json_data_3['Ї'])
    with open("data_3.json", "r", encoding="utf-8") as file :
        json_data_4 = json.load(file)
        print(json_data_4['Ї'] == json_data['Ї'], json_data_4['Ї'])


if __name__ == "__main__" :
    main()

# Підсумки:
# запис дробового числа .5 не приймається, тільки 0.5
# інженерний запис 1.2e3 приймається, але не впливає на правила
