# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def add_links_from_sql(links, BotDB):
    for link in links:
        try:
            BotDB.add_link(link)
        except:
            continue

    return True
