import sqlite3
import re
import pandas as pd
import plotly.express as px
import requests

def main():
    # mapCountryData()
    # Should create mkdir method
    ipList = retrieveAllIpAddress()

    if (len(ipList) > 0): 
        ipHashMap = mapIpToCoordinates(ipList)
        updateDatabaseWithCoordinates(ipHashMap)
    else:
        print("no ip addresses needed to retrieve coordinates")
    
    mapCountryDataWithDb()
    groupDataByMonths()

def retrieveAllIpAddress():
    print("retrieving ip addresses from table")

    dbconn = sqlite3.connect("tracking.db", timeout=60)
    cursor = dbconn.cursor()

    select_all_ips_query = "SELECT ip_address FROM tool_download_count WHERE coord_updated IS FALSE"
    ipList_raw = cursor.execute(select_all_ips_query)

    ipList = [i[0] for i in ipList_raw]

    return ipList

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def requestIpApi(listofIp, ipToMetaMap):
    url = 'http://ip-api.com/batch'

    response = requests.post(url, json=listofIp)
    if response: 
        responseJson = response.json()
        if responseJson:
            for obj in responseJson:
                ip = obj['query']
                ipToMetaMap[ip] = obj
        else:
            print('status raise', response.raise_for_status())
    else: 
        print('status code', response.status_code)

    return ipToMetaMap

# 100 IP address MAX
MAX_API_BATCH_SIZE = 50

def mapIpToCoordinates(listofIp):
    print("batch conversion of Ip address by 100")
    
    ipToMetaMap = {}
    for batch in chunks(listofIp, MAX_API_BATCH_SIZE):
        batch_done = requestIpApi(batch, ipToMetaMap)
        ipToMetaMap.update(batch_done)

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
                         lon='ip_long', hover_name="city",
                         width=800, height=400)

    fig.update_layout(plot_bgcolor="rgba(0, 0, 0, 0)", paper_bgcolor="rgba(0, 0, 0, 0)", margin=dict(l=0, r=0, t=0, b=0))

    fig.show()

    # Using kaleido - export in PNG
    fig.write_image("map/images/output.png")

    # Export in HTML
    fig.write_html("map/html/output.html")

def groupDataByMonths():
    dbconn = sqlite3.connect("tracking.db", timeout=60)

    df = pd.read_sql_query("SELECT * FROM tool_download_count WHERE coord_updated IS TRUE", dbconn)

    df['Year'] = pd.to_datetime(df['date_download']).dt.year
    df['Month'] = pd.to_datetime(df['date_download']).dt.month

    g = df.groupby([('Year'), ('Month')]).sum().to_json(r"map/json/map_months.json")
    # print(g)

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
