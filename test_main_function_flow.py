from spiderpoints_classes.spiderpoints import SpiderPoints, InputsParser


def test_main_creates_kml_and_gpx_files():
    import pathlib
    import os

    str_float = "52.734683, 18.369269"
    dstnce = 5
    occ = 7
    SpiderPoints(str_float, dstnce, occ)

    for fpath,_,_ in os.walk(pathlib.Path.cwd().parent):
        if 'kml' in fpath.lower():
            assert True
        elif 'gpx' in fpath.lower():
            assert True


def test_string_to_tuple_float():
    dstnce = 5
    occ = 7
    str_float = "52.734683, 18.369269"
    value_tuple = InputsParser(str_float,occ,dstnce)
    assert type(value_tuple.first_point) is tuple
    assert len(value_tuple.first_point) == 2
    assert value_tuple.first_point[0] == 52.734683
    assert value_tuple.first_point[1] == 18.369269
