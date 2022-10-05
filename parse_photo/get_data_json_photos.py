from requests import get
from json import dump

from settings import URL_ALL_PHOTOS_VK


def get_data_json_photos_vk(url: str):
    res = get(url)

    with open('data_photos.json', 'w') as data_json_photos:
        dump(res.json(), data_json_photos, indent=4)

    with open('data_photos.txt', 'w') as data_json_photos_txt:
        dump(res.json(), data_json_photos_txt, indent=4)

    return res


if __name__ == '__main__':
    get_data_json_photos_vk(URL_ALL_PHOTOS_VK)
