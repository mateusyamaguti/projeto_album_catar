from models import Stickers
from models import Album

import pytest
import coverage

# Sticker class tests
def test_Stickers():
    obj = Stickers()
    assert isinstance(obj, Stickers)

def test_open_package_should_return_a_string_list_with_five_elements():
    obj = Stickers().open_package()
    assert isinstance(obj, list)
    assert isinstance(obj[0], str)
    assert len(obj) == 5

def test_get_all_stickers():
    obj = Stickers().get_all_stickers()
    assert isinstance(obj, list)
    assert isinstance(obj[0], str)
    assert len(obj) == 678

# Album class tests
def test_Album():
    obj = Album()
    assert isinstance(obj, Album)

def test_glue_sticker_should_add_one_element_in_stickers():
    obj = Album()
    obj.set_stickers(["QAT1"])
    assert len(obj.get_stickers_in_album()) == 1
    assert obj.get_stickers_in_album()[-1] == "QAT1"