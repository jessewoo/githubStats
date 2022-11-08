import sqlite3
import re
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame


def main():
    mapdata()


def mapdata():
    dbconn = sqlite3.connect("tracking.db", timeout=60)
    cursor = dbconn.cursor()

    select_query = "SELECT * FROM tool_download_count"

    listQuery = list(cursor.execute(select_query))

    # print(listQuery)
    # Strip out coordinate from dataset

    # https://stackoverflow.com/questions/53233228/plot-latitude-longitude-from-csv-in-python-3-6


# Call main
if __name__ == "__main__":
    main()
