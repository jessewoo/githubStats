import pandas as pd
import plotly.express as px

# https://datascience.quantecon.org/applications/maps.html

df = pd.DataFrame({
    'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
    'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
    'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
    'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]
})

fig = px.scatter_mapbox(
    df,  # Our DataFrame
    lat="Latitude",
    lon="Longitude",
    # center={"lat": 19.43, "lon": -99.13},  # where map will be centered
    width=800,  # Width of map
    height=800,  # Height of map
    # what to display when hovering mouse over coordinate
    hover_data=["City"],
)

# adding beautiful street layout to map
fig.update_layout(mapbox_style="open-street-map")

fig.show()
