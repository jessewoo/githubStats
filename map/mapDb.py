import sqlite3
import re
import pandas as pd
import plotly.express as px
import requests

def main():
    # mapCountryData()
    # Should create mkdir method

    ipList = retrieveAllIpAddress()
    ipHashMap = mapIpToCoordinates(ipList)
    updateDatabaseWithCoordinates(ipHashMap)
    mapCountryDataWithDb()


def retrieveAllIpAddress():
    print("retrieve ip addresses from table")

    dbconn = sqlite3.connect("tracking.db", timeout=60)
    cursor = dbconn.cursor()

    select_all_ips_query = "SELECT ip_address FROM tool_download_count WHERE coord_updated IS FALSE"
    ipList_raw = cursor.execute(select_all_ips_query)

    ipList = [i[0] for i in ipList_raw]

    return ipList


def mapIpToCoordinates(listofIp):
    print("batch conversion of Ip address")

    url = 'http://ip-api.com/batch'
    postObj = listofIp

    response = requests.post(url, json=postObj)
    responseJson = response.json()

    ipToMetaMap = {}
    for obj in responseJson:
        ip = obj['query']
        ipToMetaMap[ip] = obj

    return ipToMetaMap


def updateDatabaseWithCoordinates(ipMap):
    print("update table with lat / lon coordinates")

    dbconn = sqlite3.connect("tracking.db", timeout=60)
    cursor = dbconn.cursor()

    for key in ipMap:
        ipx = key
        lat = ""
        lon = ""
        country = ""
        regionName = ""
        city = ""
        zip = ""

        if ipMap[key]['status'] == "success":
            lat = ipMap[ipx]['lat']
            lon = ipMap[ipx]['lon']
            country = ipMap[ipx]['country']
            regionName = ipMap[ipx]['regionName']
            city = ipMap[ipx]['city']
            zip = ipMap[ipx]['zip']

        cursor.execute(
            '''UPDATE tool_download_count SET ip_lat=?, ip_long=?, country=?, region=?, city=?, zip=?, coord_updated=?  \
                 WHERE ip_address=? AND coord_updated IS FALSE''', (lat, lon, country, regionName, city, zip, 1, ipx))

    dbconn.commit()

def mapCountryDataWithDb():
    # Testing panda scatter geo plot with select db import
    dbconn = sqlite3.connect("tracking.db", timeout=60)

    df = pd.read_sql_query("SELECT * FROM tool_download_count WHERE coord_updated IS TRUE", dbconn)

    fig = px.scatter_geo(df, lat='ip_lat',
                         lon='ip_long', hover_name="city")
    fig.update_layout(title='World map', title_x=0.5)
    fig.show()

    # Using kaleido - export in PNG
    fig.write_image("map/images/output.png")

    # Export in HTML
    fig.write_html("map/html/output.html")


def mapCountryData():
    # Testing panda scatter geo plot with csv import

    df = pd.read_csv("csv/countries.csv")

    fig = px.scatter_geo(df, lat='latitude',
                         lon='longitude', hover_name="name")
    fig.update_layout(title='World map', title_x=0.5)
    fig.show()


# Call main
if __name__ == "__main__":
    main()
