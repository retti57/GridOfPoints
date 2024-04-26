from geopy.distance import distance
from spiderpoints.kml_to_gpx_converter import Converter, KMLCreator


class InputsParser:
    def __init__(self, first_point: str, number_of_points: int, distance_between_points:int):
        self.first_point = self.__coord_str_to_float_tuple(first_point)
        self.nums_points = number_of_points
        self.d = distance_between_points

    @staticmethod
    def __coord_str_to_float_tuple(coordinates: str) -> tuple[float, float]:
        lat_grid, long_grid = coordinates.split(",")
        return float(lat_grid.strip()), float(long_grid.strip())

    @staticmethod
    def __oblicz_wspolrzedne_p2(point: tuple[float, float], d: int, bearing: int = 90):
        # Pobierz współrzędne punktu point
        lat_p1, lon_p1 = point
        # Oblicz współrzędne punktu P2
        p2 = distance(kilometers=d).destination((lat_p1, lon_p1), bearing)
        lat_p2, lon_p2 = p2.latitude, p2.longitude

        return lat_p2, lon_p2

    def generate_points(self, point,  *bearing) -> list:
        lista_punktow = [point]  # Dodajemy pierwszy punkt P1 do listy
        for _ in range(self.nums_points - 1):
            # Obliczamy współrzędne kolejnego punktu i dodajemy go do listy
            point = self.__oblicz_wspolrzedne_p2(point, self.d, *bearing)
            lista_punktow.append(point)
        return lista_punktow


class SpiderPoints:
    """ Provide vars of type string."""

    def __init__(self, initial_coordinates: str, number_of_points: str, distance_between_points: str):
        self.initial_coordinates = initial_coordinates
        self.number_of_points = int(number_of_points)
        self.distance_between_points = int(distance_between_points)

    def _list_points(self) -> list:
        inputs = InputsParser(
            self.initial_coordinates,
            self.number_of_points,
            self.distance_between_points
        )
        lista_punktow_bearing_90 = inputs.generate_points(inputs.first_point, 90)

        grid = []
        for punkt in lista_punktow_bearing_90:
            punkty_w_dol = inputs.generate_points(punkt,180)

            grid.extend(punkty_w_dol)
        return grid

    def create_kml_gpx(self):
        """ Creates a KML file with based on given anchor point, number of points in each line of grid and
        distance between those points. The grid is created in directions form right to left( West to East) and
        from top to bottom ( North to South ) from the anchor point """
        grid = self._list_points()

        nazwa_pliku_kml = "punkty.kml"
        KMLCreator(
            list_of_points=grid,
            filename=nazwa_pliku_kml,
            number_of_points=self.number_of_points
        ).create_kml_file()
        Converter(
            kml_filename=nazwa_pliku_kml
        ).convert_to_gpx(gpx_filename="punkty.gpx")

        return len(grid)
