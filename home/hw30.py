import json
from random import choice


def gen_person():
    num = '0'
    name = ''
    tel = ''

    nums1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(num) != 10:
        num += choice(nums1)

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {num: {
            'name': name,
            'tel': tel
        }
    }
    return person


def write_json(person_dict):
    try:
        data = json.load(open('person.json'))
    except FileNotFoundError:
        data = []

    data.append(person_dict)
    with open('person.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
