from spiderpoints.spiderpoints import SpiderPoints



if __name__ == '__main__':
    str_float = input("Podaj współrzędne w formacie >> 52.734683, 18.369269 << : ")
    dstnce = input("Podaj odległość od punktów: ")
    occ = input("Podaj ilość punktów w jednej linii: ")
    SpiderPoints(str_float, dstnce, occ).create_kml_gpx()
