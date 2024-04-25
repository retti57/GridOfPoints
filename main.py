from spiderpoints.spiderpoints import SpiderPoints


if __name__ == '__main__':
    str_float = "52.734683, 18.369269"
    dstnce = 5
    occ = 7
    SpiderPoints(str_float,dstnce,occ).create_kml_gpx()

