# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import json


def check_blacks(name):
    black_specifications = ['страна', 'цвет', 'тип товара', 'артикул', 'производитель', 'гарантийный срок']

    for black in black_specifications:
        if black in name:
            return True

    return False


def formate_all_specifications(products_list):
    full_specifications = []

    for product in products_list:
        try:
            specifications = json.loads(product[11])
        except:
            continue

        for spec in specifications:
            name = spec['name']

            try:
                lower_name = name.lower()
            except:
                lower_name = name

            is_black = check_blacks(lower_name)

            if is_black:
                continue

            full_specifications.append(name)

        full_specifications = list(set(full_specifications))

    return full_specifications
