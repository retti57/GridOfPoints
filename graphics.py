import sys
import tkinter as tk
from spiderpoints_classes.spiderpoints import SpiderPoints


def generate_kml():
    point_coord = entry_coord.get()
    occurrence = entry_occurrence.get()
    distance = entry_distance.get()
    # Tutaj umieść logikę generowania pliku KML na podstawie wprowadzonych danych

    SpiderPoints(
        initial_coordinates=point_coord,
        number_of_points=occurrence,
        distance_between_points=distance
    ).create_kml_gpx()
    sys.exit()


# Tworzenie głównego okna
root = tk.Tk()
root.title("Generator plików GPX i KML")

# Etykieta informacyjna
label_info = tk.Label(root, text="Podaj współrzędne w formacie DD.DDDDDD z google maps:")
label_info.pack()

# Pole tekstowe dla współrzędnych
entry_coord = tk.Entry(root)
entry_coord.pack()

# Etykieta i pole tekstowe dla ilości powtórzeń punktów
label_occurrence = tk.Label(root, text="Podaj ilość powtórzeń punktów:")
label_occurrence.pack()
entry_occurrence = tk.Entry(root)
entry_occurrence.pack()

# Etykieta i pole tekstowe dla odległości między punktami
label_distance = tk.Label(root, text="Podaj odległość między punktami:")
label_distance.pack()
entry_distance = tk.Entry(root)
entry_distance.pack()

# Przycisk "Generuj KML"
button_kml = tk.Button(root, text="KML i GPX", command=generate_kml)
button_kml.pack()

# Rozpoczęcie pętli głównej programu
root.mainloop()
