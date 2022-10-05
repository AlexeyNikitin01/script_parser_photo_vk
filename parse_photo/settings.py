FILE_DATA_JSON = ''

TOKEN_APP = ''  # Request from VK APP

TOKEN_ACCESS = ''  # Request from VK

V = '5.131'
METHOD = 'photos.get'
OWNER_ID = int()
ALBUM_ID = 'saved'
PHOTO_SIZE = 1
COUNT = int()
OFFSET = 0

URL_ALL_PHOTOS_VK = f'https://api.vk.com/method/{METHOD}?access_token={TOKEN_ACCESS}&v={V}&owner_id={OWNER_ID}' \
                    f'&album_id={ALBUM_ID}&photo_sizes={PHOTO_SIZE}&count={COUNT}'

