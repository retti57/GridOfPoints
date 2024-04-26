""" Create an GPX file through conversion form KML format file """

import simplekml
import random
import gpxpy
import gpxpy.gpx


class KMLCreator:
    def __init__(self, list_of_points: list, filename: str, number_of_points: int):
        self.filename = filename
        self.list_of_points = list_of_points
        self.number_of_points = number_of_points
        self.kml = simplekml.Kml()

    def create_kml_file(self):
        """ Creates a file and saves it in the directory of current file """
        import string
        letters = string.ascii_uppercase
        digits = list(range(self.number_of_points))
        letter_index = -1
        counter = 0

        for punkt in self.list_of_points:
            random.shuffle(digits)
            lat, lon = punkt
            if counter % self.number_of_points == 0 or len(digits) == 0:
                letter_index += 1
                counter = 0
                digits = list(range(1, self.number_of_points + 1))

            point_name = f'{letters[letter_index]}{digits.pop()}'
            newpoint = self.kml.newpoint(name=point_name, coords=[(lon, lat)])
            newpoint.style.iconstyle.color = simplekml.Color.aquamarine
            counter += 1
        self.kml.save(self.filename)
        print(f"Lista punktów została zapisana do pliku {self.filename}")
        return self.filename


class Converter:

    def __init__(self, kml_filename: str):
        self.kml_filename = kml_filename

    def convert_to_gpx(self, gpx_filename):
        """ Opens a file and parse its KML content. The name and coordinates of each point are transitioned to new file.
        When finished, prints out message including filename"""
        with open(self.kml_filename, 'r', encoding='utf-8') as kml_file:
            # Tworzymy obiekt GPX
            gpx = gpxpy.gpx.GPX()

            # Parsujemy plik KML ręcznie
            point_name = ''
            for line in kml_file:
                if "<name>" in line:
                    point_name = line.split("<name>")[1].split("</name>")[0].strip()

                # Jeśli linia zawiera koordynaty punktu, dodajemy je do obiektu GPX
                if "<coordinates>" in line:
                    coords = line.split("<coordinates>")[1].split("</coordinates>")[0].strip().split(',')
                    lat, lon = float(coords[1]), float(coords[0])  # Kolejność jest odwrotna w KML
                    gpx_point = gpxpy.gpx.GPXWaypoint(lat, lon, name=point_name)
                    gpx.waypoints.append(gpx_point)

        # Zapisujemy obiekt GPX do pliku
        with open(gpx_filename, 'w', encoding='utf-8') as gpx_file:
            gpx_file.write(gpx.to_xml())
        print(f'Lista punktów została zapisana do pliku {gpx_filename}')



# def save_to_txt(points: list[(float, float)]) -> None:
#     """ Saves list of points to TXT file 'siatka.txt'"""
#     gridy = pd.DataFrame(points, columns=['Latitude', 'Longitude'])
#     gridy.to_csv('siatka.txt', index=False)
