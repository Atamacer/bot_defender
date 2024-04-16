import mariadb

with open('db_config.txt') as file:
    lines = [line.rstrip() for line in file]

connect = mariadb.connect(
    user=lines[0],
    password=lines[1],
    host=lines[2],
    port=int(lines[3]),
    database=lines[4]
)

cur = connect.cursor()


# добавление группы в БД
def add_new_group(group_id: int, group_name: str):
    cur.execute('INSERT INTO groups (group_id, group_name) VALUES (?, ?)',
                (group_id, group_name))
    connect.commit()


# удаление группы из БД
def delete_group(group_id: int):
    cur.execute(f'DELETE FROM groups WHERE group_id = {group_id}')
    connect.commit()


# добавление подозрительного пользователся в БД
def add_marked_user(user_id: int, text: str):
    cur.execute('INSERT INTO marked_users (user_id, text) VALUES (?, ?)',
                (user_id, text))
    connect.commit()


def get_group_id():
    cur.execute('SELECT group_id FROM groups')
    data = [-int(abs(i[0])) for i in cur.fetchall()]

    return data


def get_bad_words():
    cur.execute('SELECT word FROM stop_words')
    data = [i[0] for i in cur.fetchall()]

    return data
