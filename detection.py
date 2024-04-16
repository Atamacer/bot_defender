import vk_api
from db_func import *
from vk_api.longpoll import VkLongPoll

with open('vk_config.txt') as file:
    token = [line.rstrip() for line in file][0]


class Detect:
    def __init__(self, main_token=token):
        self.vk_session = vk_api.VkApi(token=main_token)
        self.longpool = VkLongPoll(self.vk_session)
        self.vk = self.vk_session.get_api()

    # получение всех id и текстов их комментариев(по умолчанию)
    def get_comments(self, count: int = 5):
        res = []
        for owner_id in get_group_id():
            for walls in range(1, count + 1):
                for i in self.vk.wall.get(owner_id=owner_id, count=walls, offset=0)['items']:
                    post_id = str(i['id'])
                    response = self.vk.wall.getComments(owner_id=owner_id, post_id=post_id, sort='desc', offset=0)
                    res.extend([(i['from_id'], i['text']) for i in response['items']])

        return list(set(res))

    # поиск стоп-слов в комментарии
    def search_forbidden(self, user_id: int, text: str):
        for i in get_bad_words():
            if i in text:
                add_marked_user(user_id, text)


a = Detect()
print(a.get_comments())
