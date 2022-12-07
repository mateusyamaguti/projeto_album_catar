from core import Album
import pytest

def test_album():
    obj = Album()
    assert isinstance(obj, Album)

def test_create_countries():
    obj = Album()._create_countries()
    assert isinstance(obj, list)
    assert len(obj) == 32
    assert obj[0] == 'QAT' and obj[-1] == 'COR'

def test_create_figure():
    obj = Album()._create_figure()
    assert isinstance(obj, list)
    assert len(obj) == 678
    assert obj[0] == '00'