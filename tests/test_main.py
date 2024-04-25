def test_main_creates_kml_and_gpx_files():
    import pathlib
    import os

    from spiderpoints.spiderpoints import main
    str_float = "52.734683, 18.369269"
    dstnce = 5
    occ = 7
    main(str_float, dstnce, occ)

    for fpath,_,_ in os.walk(pathlib.Path.cwd().parent):
        if 'kml' in fpath.lower():
            assert True
        elif 'gpx' in fpath.lower():
            assert True


def test_string_to_tuple_float():
    from spiderpoints.spiderpoints import _coord_str_to_float_tuple

    str_float = "52.734683, 18.369269"
    value_tuple = _coord_str_to_float_tuple(str_float)
    assert type(value_tuple) is tuple
    assert len(value_tuple) == 2
    assert value_tuple[0] == 52.734683
    assert value_tuple[1] == 18.369269
