from models import Stickers, Album

stickers = Stickers()
album = Album()

for _ in range(100):
    op = stickers.open_package()
    album.verify_if_i_have_the_sticker(op)

album.stickers_in_album
album.repeated_stickers