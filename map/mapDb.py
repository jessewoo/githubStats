import sqlite3
import re
import pandas as pd
import plotly.express as px


def main():
    mapCountryData()
    # mapdata()


def mapCountryData():
    df = pd.read_csv("csv/countries.csv")

    fig = px.scatter_geo(df, lat='latitude',
                         lon='longitude', hover_name="name")
    fig.update_layout(title='World map', title_x=0.5)
    fig.show()


def mapdata():
    dbconn = sqlite3.connect("tracking.db", timeout=60)
    cursor = dbconn.cursor()

    select_query = "SELECT * FROM tool_download_count"

    listQuery = list(cursor.execute(select_query))

    # print(listQuery)
    # Strip out coordinate from dataset

    # https://stackoverflow.com/questions/53233228/plot-latitude-longitude-from-csv-in-python-3-6
    # https://stackoverflow.com/questions/1565555/plot-geoip-data-on-a-world-map


# Call main
if __name__ == "__main__":
    main()
