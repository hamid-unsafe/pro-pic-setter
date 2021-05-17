from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import InputPhoto

client_name = 'hamid'
API_ID = 1524689
API_HASH = '14d226885030df209468c3fe12979672'

client = TelegramClient(client_name, API_ID, API_HASH)

client.start()

while True:
  pics = client.get_profile_photos('me')

  if len(pics) == 0:
    break
  
  pic = pics[0]

  client(DeletePhotosRequest(
      id=[InputPhoto(
          id=pic.id,
          access_hash=pic.access_hash,
          file_reference=pic.file_reference
      )]
  ))