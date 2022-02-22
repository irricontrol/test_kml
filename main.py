from pathlib import Path
import simplekml
import pandas as pd
from polycircles import polycircles

BASE_DIR = Path(__file__).resolve().parent

"""
Plot Point
Create simple point
"""
point_kml = simplekml.Kml()
point_kml.newpoint(name='Itajubá', coords=[(-45.45265450985259, -22.417578569401623)])
point_kml_path = f'{BASE_DIR}/outputs/point_kml.kml'
point_kml.save(point_kml_path)

"""
Plot Points
Create simples points
"""
names = [
    'Itajubá',
    'Taubaté',
]
longitudes = [-45.45265450985259, -45.57056842974935]
latitudes = [-22.417578569401623, -23.01992498902612]

locations = pd.DataFrame({
    'names': names,
    'longitudes': longitudes,
    'latitudes': latitudes
})

points_kml = simplekml.Kml()
for i in locations.itertuples():
    points_kml.newpoint(name=i.names, coords=[(i.longitudes, i.latitudes)])
points_kml_path = f'{BASE_DIR}/outputs/points_kml.kml'
points_kml.save(points_kml_path)

"""
Plot Lines
Create lines point to point
"""
lines_kml = simplekml.Kml()
lines = lines_kml.newlinestring(name='Path',
                                description='Caminho de Taubaté a Itajubá',
                                coords=[
                                    (-45.45265450985259, -22.417578569401623),
                                    (-45.57056842974935, -23.01992498902612),
                                ])

# change line width and color
lines.style.linestyle.width = 5
lines.style.linestyle.color = simplekml.Color.aqua

lines_kml_path = f'{BASE_DIR}/outputs/lines_kml.kml'
lines_kml.save(lines_kml_path)

"""
Plot Circle
Create lines point to point

# radius - circle radius in meters
"""
polycircle = polycircles.Polycircle(longitude=-45.45265450985259,
                                    latitude=-22.417578569401623,
                                    radius=200,
                                    number_of_vertices=60)

polycircle_kml = simplekml.Kml()
circle = polycircle_kml.newpolygon(name='Pivô', outerboundaryis=polycircle.to_kml())
circle.style.polystyle.color = simplekml.Color.changealphaint(200, simplekml.Color.green)
polycircle_kml_path = f'{BASE_DIR}/outputs/polycircle_kml.kml'
polycircle_kml.save(polycircle_kml_path)
