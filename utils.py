import json
from datetime import datetime


def load():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def select(data):
    executed = []
    for item in data:
        try:
            if item['state'] == 'EXECUTED':
                executed.append(item)
        except KeyError:
            pass
    return executed


def sorted_operations(executed):
    sort = sorted(executed, key=lambda x: x["date"], reverse=True)
    return sort[:5]


def hide_numbers(data):
    number = data.split(' ')[-1]
    if len(number) == 20:
        return f'Cчет **{number[16:]}'
    else:
        card = ' '.join(data.split(" ")[:-1])
        return f'{card} {number[0:4]} {number[4:6]}** **** {number[12:]}'


def last_operations(last):
    operation_list = []
    for item in last:
        date = datetime.strptime(item['date'][:10], '%Y-%m-%d')
        d_format = date.strftime('%d.%m.%Y')
        try:
            operation = hide_numbers(item['from'])
        except KeyError:
            operation = ''
        operation_list.append(f"""
        {d_format} {item['description']} 
{operation} -> {hide_numbers(item['to'])}
{item["operationAmount"]['amount']} {item['operationAmount']['currency']['name']}\n""")
    return operation_list
