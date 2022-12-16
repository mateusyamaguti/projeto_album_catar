from models import Stickers, Album

import pytest
import coverage

# Sticker class tests
def test_create_class_Stickers():
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
def test_create_class_Album():
    obj = Album()
    assert isinstance(obj, Album)

def test_glue_sticker_should_add_one_element_in_stickers():
    obj = Album()
    obj.set_stickers(["QAT1"])
    assert len(obj.get_stickers_in_album()) == 1
    assert obj.get_stickers_in_album()[-1] == "QAT1"

def test_add_repeated_sticker_in_list_repeated_sticker_false():
    sticker_list = Album()
    assert sticker_list.verify_sticker_in_album('QAT1') == False
    sticker_list.set_stickers(['QAT1'])
    assert sticker_list.verify_sticker_in_album('QAT1') == True

def test_set_stickert_in_album():
    pass

def test_get_sticker_in_album_one_should_return_one_sticker():
    sticker_list = Album()
    sticker_list.set_stickers(["QAT1"])
    assert sticker_list.get_stickers_in_album() == ['QAT1']

def test_get_repeated_sticker__should_one_sticker_repeated():
    sticker_list = Album()
    sticker_list.set_stickers(["QAT1", "QAT1", "BRA1"])
    assert isinstance(sticker_list.get_repeated_stickers(), dict)
    assert sticker_list.get_repeated_stickers() == {'QAT1':1}