from models import Stickers
from models import Album

import pytest
import coverage

'''Sticker class tests'''
def test_Stickers():
    obj = Stickers()
    assert isinstance(obj, Stickers)

def test_open_package():
    obj = Stickers().open_package()
    assert isinstance(obj, list)
    assert len(obj) == 5

def test_get_all_stickers():
    obj = Stickers().get_all_stickers()
    assert isinstance(obj, list)
    assert len(obj) == 678

'''Stickers class Album'''
def test_Album():
    obj = Album()
    assert isinstance(obj, Album)