""" Create an GPX file through conversion form KML format file """
import gpxpy
import gpxpy.gpx


def convert_to_gpx(kml_filename, gpx_filename):
    """ Opens a file and parse its KML content. The name and coordinates of each point are transitioned to new file.
    When finished, prints out message including filename"""
    with open(kml_filename, 'r', encoding='utf-8') as kml_file:
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
