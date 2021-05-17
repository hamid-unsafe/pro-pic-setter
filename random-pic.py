from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import InputPhoto
import time
import random

sleep_time = 15 * 60
pics_length = 32

client_name = 'me'
API_ID = 1524689
API_HASH = '14d226885030df209468c3fe12979672'

client = TelegramClient(client_name, API_ID, API_HASH)

client.start()

prevNum = 0

while True:
  # clear current photo
  pics = client.get_profile_photos('me')

  if len(pics) != 0:
    pic = pics[0]
    
    client(DeletePhotosRequest(
      id=[InputPhoto(
        id = pic.id,
        access_hash = pic.access_hash,
        file_reference = pic.file_reference
      )]
    ))

  
  # get new random number
  newNum = random.randrange(1, pics_length + 1)
  
  # prevent repetetive pics
  if newNum == prevNum:
    continue
  
  client(UploadProfilePhotoRequest(
    client.upload_file(f'./pics/{newNum}.jpg')
  ))

  prevNum = newNum
  time.sleep(sleep_time + random.random())