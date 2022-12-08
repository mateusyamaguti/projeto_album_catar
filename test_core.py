from core import Album
from core import create_control
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

def test_create_control():
    obj = create_control()
    assert isinstance(create_control()[0], tuple)