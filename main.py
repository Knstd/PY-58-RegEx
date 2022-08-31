import re
from pprint import pprint
import csv


def format_phone_numbers(contacts_list):
    for row in contacts_list[1:]:
        pattern = r'(\+*\d)[\s(]*\(*(\d{3})[)|-]*\s*(\d{3})\-*\s*(\d{2})\-*\s*(\d{2})([\s(])*([доб.]*)\s*([\d{4}]*)(\))*'
        sub = r'+7(\2)\3-\4-\5 \7\8'
        row[5] = re.sub(pattern, sub, row[5]).strip()
    return contacts_list


def format_names(contacts_list):
    for row in contacts_list[1:]:
        new_row = ' '.join(row[:3]).split(' ')
        #   pattern = r'([А-Я]{1}[а-я]+)[\s|,]([А-Я]{1}[а-я]+)[\s|,](([А-Я]{1}[а-я]+)|)'
        #   sub = r'\1,\2,\3'
        #   result = re.sub(pattern, sub, res).strip()
        row[:3] = new_row[:3]
    return contacts_list


def merge_duplicates(contacts_list):
    merged_list = []
    for i in range(len(contacts_list)):
        for j in range(len(contacts_list)):
            if contacts_list[i][0] == contacts_list[j][0]:
                contacts_list[i] = list(x or y for x, y in zip(contacts_list[i], contacts_list[j]))
        if contacts_list[i] not in merged_list:
            merged_list.append(contacts_list[i])
    return merged_list


def read_file():
    with open('phonebook_raw.csv') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


def write_file(result):
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(result)


if __name__ == '__main__':
    file = read_file()
    result = (merge_duplicates(format_names(format_phone_numbers(file))))
    pprint(result)
    write_file(result)
