from requests import get
from json import load

from settings import DIR_UPLOAD_FILE, FILE_DATA_JSON


def upload_photo(url_photo: str, number_photo: int):
    with open(f'{DIR_UPLOAD_FILE}\\{number_photo}.png', 'wb') as photo_write:
        res = get(url_photo).content
        photo_write.write(res)


def parse_url_photos(url_file_data_json):
    with open(f'{url_file_data_json}', 'r') as file_json:
        res = load(file_json)
        for i, item in enumerate(res['response']['items']):
            height = 0
            count = 0
            for num, size in enumerate(item['sizes']):
                if size['height'] >= height:
                    height = size['height']
                    count = num
            url_photo = item['sizes'][count]['url']
            upload_photo(url_photo, i)


if __name__ == '__main__':
    parse_url_photos(FILE_DATA_JSON)
