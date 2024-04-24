import random

from geopy.distance import distance
import pandas as pd
import simplekml
from kml_to_gpx_converter import convert_to_gpx
from time import sleep


def _oblicz_wspolrzedne_p2(point: tuple[float, float], d: int, bearing: int = 90):
    # Pobierz współrzędne punktu point
    lat_p1, lon_p1 = point
    # Oblicz współrzędne punktu P2
    p2 = distance(kilometers=d).destination((lat_p1, lon_p1), bearing)
    lat_p2, lon_p2 = p2.latitude, p2.longitude

    return lat_p2, lon_p2


def generate_list_of_points(point: tuple[float, float], nums_points, d, *bearing) -> list:
    lista_punktow = [point]  # Dodajemy pierwszy punkt P1 do listy
    for _ in range(nums_points - 1):
        # Obliczamy współrzędne kolejnego punktu i dodajemy go do listy
        point = _oblicz_wspolrzedne_p2(point, d, *bearing)
        lista_punktow.append(point)
    return lista_punktow


def create_kml(list_of_points: list, filename: str, number_of_points):
    import string
    letters = string.ascii_uppercase
    digits = list(range(number_of_points))
    letter_index = -1
    counter = 0

    kml = simplekml.Kml()
    for punkt in list_of_points:
        random.shuffle(digits)
        lat, lon = punkt
        if counter % number_of_points == 0 or len(digits) == 0:
            letter_index += 1
            counter = 0
            digits = list(range(1, number_of_points + 1))

        point_name = f'{letters[letter_index]}{digits.pop()}'
        newpoint = kml.newpoint(name=point_name, coords=[(lon, lat)])
        newpoint.style.iconstyle.color = simplekml.Color.aquamarine
        counter += 1
    kml.save(filename)
    print(f"Lista punktów została zapisana do pliku {filename}")


def save_to_txt(points: list[(float, float)]) -> None:
    """ Saves list of points to TXT file 'siatka.txt'"""
    gridy = pd.DataFrame(points, columns=['Latitude', 'Longitude'])
    gridy.to_csv('siatka.txt', index=False)


def main(initial_coordinates, number_of_points, distance_between_points):
    """ Creates a KML file with based on given anchor point, number of points in each line of grid and
    distance between those points. The grid is created in directions form right to left( West to East) and
    from top to bottom ( North to South ) from the anchor point """
    lista_punktow_bearing_90 = generate_list_of_points(initial_coordinates, number_of_points, distance_between_points,
                                                       90)
    grid = []
    for i, punkt in enumerate(lista_punktow_bearing_90, start=1):
        punkty_w_dol = generate_list_of_points(punkt, number_of_points, distance_between_points, 180)

        grid.extend(punkty_w_dol)
    # print("Lista wygenerowanych punktów: ", grid)
    print(len(grid))
    # Wywołanie funkcji do zapisu listy punktów do pliku KML
    nazwa_pliku_kml = "punkty.kml"
    create_kml(grid, nazwa_pliku_kml, number_of_points)


if __name__ == '__main__':
    # Przykładowe współrzędne punktu P1
    print('Współrzędne w formacie DD.DDDDD skopiowane z google maps, na przykład: "52.734683, 18.369269"')
    p1 = input('Podaj współrzędne:')
    d = int(input('Podaj odległość do kolejnego punktu w km, np "7": '))
    occurrence = int(input('Podaj ilość punktów, np "5": '))

    lat_grid, long_grid = p1.split(",")
    p1_point = float(lat_grid.strip()), float(long_grid.strip())
    # Generowanie pliku kml z punktami
    main(p1_point, occurrence, d)
    sleep(.05)
    convert_to_gpx("punkty.kml", "punkty.gpx")
