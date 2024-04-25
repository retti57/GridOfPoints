import random
from geopy.distance import distance
import pandas as pd
import simplekml
from spiderpoints.kml_to_gpx_converter import convert_to_gpx


class InputsParser:
    def __init__(self, first_point, number_of_points, distance_between_points):
        self.first_point = self.__coord_str_to_float_tuple(first_point)
        self.nums_points = number_of_points
        self.d = distance_between_points

    @staticmethod
    def __oblicz_wspolrzedne_p2(point: tuple[float, float], d: int, bearing: int = 90):
        # Pobierz współrzędne punktu point
        lat_p1, lon_p1 = point
        # Oblicz współrzędne punktu P2
        p2 = distance(kilometers=d).destination((lat_p1, lon_p1), bearing)
        lat_p2, lon_p2 = p2.latitude, p2.longitude

        return lat_p2, lon_p2

    @staticmethod
    def __coord_str_to_float_tuple(coordinates: str) -> tuple[float, float]:
        lat_grid, long_grid = coordinates.split(",")
        return float(lat_grid.strip()), float(long_grid.strip())

    def generate_points(self, *bearing) -> list:
        lista_punktow = [self.first_point]  # Dodajemy pierwszy punkt P1 do listy
        for _ in range(self.nums_points - 1):
            # Obliczamy współrzędne kolejnego punktu i dodajemy go do listy
            point = self.__oblicz_wspolrzedne_p2(self.first_point, self.d, *bearing)
            lista_punktow.append(point)
        return lista_punktow



class SpiderPoints:
    def __init__(self, initial_coordinates, number_of_points, distance_between_points):
        self.initial_coordinates = initial_coordinates
        self.number_of_points = number_of_points
        self.distance_between_points = distance_between_points

    def _list_points(self) -> list:
        inputs = InputsParser(
            self.initial_coordinates,
            self.number_of_points,
            self.distance_between_points
        )
        lista_punktow_bearing_90 = inputs.generate_points(90)
        # initial_coord = _coord_str_to_float_tuple(self.initial_coordinates)

        # lista_punktow_bearing_90 = generate_list_of_points(initial_coord, self.number_of_points,
        #                                                    self.distance_between_points,
        #                                                    90)
        grid = []
        for punkt in lista_punktow_bearing_90:
            punkty_w_dol = inputs.generate_points(180)

            grid.extend(punkty_w_dol)
        return grid

    def create_kml_gpx(self):
        """ Creates a KML file with based on given anchor point, number of points in each line of grid and
        distance between those points. The grid is created in directions form right to left( West to East) and
        from top to bottom ( North to South ) from the anchor point """
        grid = self._list_points()

        nazwa_pliku_kml = "punkty.kml"
        create_kml_file(grid, nazwa_pliku_kml, self.number_of_points)
        convert_to_gpx(nazwa_pliku_kml, "punkty.gpx")
        return len(grid)



def create_kml_file(list_of_points: list, filename: str, number_of_points):
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
