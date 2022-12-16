from models import Stickers, Album
from utils import save_csv_file, read_csv_file
from os.path import exists

import pytest
import coverage

# Utils
# save_and_read_csv
def test_save_and_read_csv_should_create_a_csv_and_return_data():
    csv_name = "test.csv"
    data = [["A"], ["B"]]
    header = ["Letter"]
    save_csv_file(csv_name, data, header)
    data_in_csv = read_csv_file("teste.csv")
    assert exists("teste.csv")
    assert len(data_in_csv) == 3
    assert data_in_csv[0] == ["Letter"]
    assert data_in_csv[-1] == ["B"]

# read_csv
def test_read_a_file_that_doesnt_exist_should_return_none():
    assert not read_csv_file("test123.csv")

# Sticker class tests
def test_create_a_stickers_object_should_return_a_object():
    obj = Stickers()
    assert isinstance(obj, Stickers)

# open_package
def test_open_package_should_return_a_string_list_with_five_elements():
    obj = Stickers().open_package()
    assert isinstance(obj, list)
    assert isinstance(obj[0], str)
    assert len(obj) == 5

# get_all_stickers
def test_get_all_stickers_should_return_a_list_of_strings_with_678_elements():
    obj = Stickers().get_all_stickers()
    assert isinstance(obj, list)
    assert isinstance(obj[0], str)
    assert len(obj) == 678

# Album class tests
def test_create_a_album_object_should_return_a_object():
    obj = Album()
    assert isinstance(obj, Album)

# verify_sticker_in_album
def test_verify_sticker_in_album_should_return_true_if_exists_in_stickers():
    obj = Album()
    obj.set_stickers(["QAT1"])
    assert obj.verify_sticker_in_album("QAT1")

# verify_sticker_in_album
def test_verify_sticker_in_album_should_return_false_if_not_exists_in_stickers():
    obj = Album()
    assert not obj.verify_sticker_in_album("URU3")

# verify_sticker_in_repeated_stickers
def test_verify_sticker_in_repeated_should_return_true_if_exists_in_repeateds():
    obj = Album()
    obj.set_stickers(["QAT1", "QAT1"])
    assert obj.verify_sticker_in_repeated_stickers("QAT1")

# verify_sticker_in_repeated_stickers
def test_verify_sticker_in_repeated_should_return_false_if_not_exists_in_repeateds():
    obj = Album()
    assert not obj.verify_sticker_in_repeated_stickers("QAT1")

# set_stickers__glue_sticker
def test_set_sticker_should_add_one_element_in_stickers_if_not_exists():
    obj = Album()
    obj.set_stickers(["QAT1"])
    assert len(obj.get_stickers_in_album()) == 1
    assert obj.get_stickers_in_album()[-1] == "QAT1"

# set_stickers__add_in_repeateds
def test_set_sticker_should_add_one_element_in_repeated_if_not_exists_in_stickers():
    obj = Album()
    obj.set_stickers(["QAT1", "QAT1"])
    assert len(obj.get_repeated_stickers()) == 1
    assert obj.get_repeated_stickers() == {"QAT1": 1}

# set_stickers__add_in_repeateds
def test_set_sticker_should_add_more_one_element_in_repeated_if_exists_in_repeateds():
    obj = Album()
    obj.set_stickers(["QAT1", "QAT1", "QAT1"])
    assert len(obj.get_repeated_stickers()) == 1
    assert obj.get_repeated_stickers()["QAT1"] == 2

# get_stickers_in_album
def test_get_sticker_in_album_should_return_stickers_in_album():
    obj = Album()
    obj.set_stickers(["QAT1"])
    assert obj.get_stickers_in_album() == ['QAT1']
    assert len(obj.get_stickers_in_album()) == 1

# get_repeated_stickers
def test_get_repeated_sticker_should_return_repeated_stickers():
    obj = Album()
    obj.set_stickers(["QAT1", "QAT1", "BRA1"])
    assert isinstance(obj.get_repeated_stickers(), dict)
    assert obj.get_repeated_stickers() == {'QAT1':1}

# get_missing_stickers
def test_get_missing_stickers_should_return_a_list_with_missing_stickers():
    obj = Album()
    obj.set_stickers(["QAT1", "BRA1"])
    all_stickers = ["URU3", "QAT1", "FWC27", "BRA1"]
    missing_stickers = obj.get_missing_stickers(all_stickers)
    assert len(missing_stickers) == 2
    assert missing_stickers == ["URU3", "FWC27"]

# create_stickers_in_album_report
def test_stickers_in_album_report_should_create_and_read_and_csv():
    obj = Album()
    obj.set_stickers(["QAT1", "BRA1"])
    obj.create_stickers_in_album_report()
    report = obj.read_stickers_in_album_report()
    assert exists("stickers_in_album.csv")
    assert isinstance(report, list)
    assert len(report) == 3
    assert report[-1] == ["BRA1"]

# missing_stickers_in_album_report
def test_missing_stickers_report_should_create_and_read_and_csv():
    obj = Album()
    obj.set_stickers(["QAT1", "BRA1"])
    all_stickers = ["URU3", "QAT1", "FWC27", "BRA1"]
    obj.create_missing_stickers_in_album_report(all_stickers)
    report = obj.read_missing_stickers_in_album_report()
    assert exists("missing_stickers.csv")
    assert isinstance(report, list)
    assert len(report) == 3
    assert report[-1] == ["FWC27"]

# repeated_stickers_report
def test_repeated_stickers_report_should_create_and_read_and_csv():
    obj = Album()
    obj.set_stickers(["QAT1", "QAT1"])
    obj.create_repeated_stickers_report()
    report = obj.read_repeated_stickers_report()
    assert exists("repeated_stickers.csv")
    assert isinstance(report, list)
    assert len(report) == 2
    assert report[-1] == ["QAT1", "1"]

# change_sticker
def test_change_sticker_should_remove_one_repeated_sticker():
    obj = Album()
    obj.set_stickers(["QAT1", "QAT1", "QAT1"])
    repeated_stickers = obj.get_repeated_stickers()
    obj.change_sticker("QAT1")
    assert repeated_stickers["QAT1"] == 1

# change_sticker
def test_change_sticker_should_remove_the_sticker_if_qty_equal_0():
    obj = Album()
    obj.set_stickers(["QAT1", "QAT1"])
    repeated_stickers = obj.get_repeated_stickers()
    assert obj.change_sticker("QAT1")
    assert not repeated_stickers.get("QAT1")

# change_sticker
def test_change_sticker_should_return_false_if_the_sticker_not_exists():
    obj = Album()
    assert not obj.change_sticker("QAT1")

