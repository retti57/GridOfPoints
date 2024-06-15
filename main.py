from spiderpoints_classes.spiderpoints import SpiderPoints


if __name__ == '__main__':
    str_float = input("Podaj współrzędne w formacie >> 52.734683, 18.369269 << : ")
    occ = input("Podaj ilość punktów w jednej linii: ")
    dstnce = input("Podaj odległość od punktów: ")
    SpiderPoints(str_float, occ, dstnce).create_kml_gpx()
