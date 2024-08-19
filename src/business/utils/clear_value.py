# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def clear_value(value):
    int_value = ''

    for word in value:
        try:
            if word.isdigit():
                int_value += word
        except:
            continue

    try:
        int_value = int(int_value)
    except:
        pass

    return int_value
