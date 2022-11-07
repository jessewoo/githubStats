import sqlite3
import re


def main():
    dbinit()
    dbtestdata()
    #analyzeLog('./access_log', '/cig/software')


def dbtestdata():
    dbconn = sqlite3.connect("tracking.db", timeout=60)

    # Insert test statements with random IP addresses
    test_insert_statement = "INSERT INTO tool_download_count \
        (tool_name, date_download, ip_address, ip_lat, ip_long, source) \
        VALUES \
            ('aspect', '2022-10-31', '125.123.131.154', '32.733975', '-117.144544', 'https://geodynamics.org/resources/1810/download/aspect-1.0.tar.gz'), \
            ('aspect', '2022-11-01', '132.31.252.5', '32.8761', '-117.2318', 'https://zenodo.org/record/1297145/files/geodynamics/aspect-v2.0.1.zip?download=1'), \
            ('aspect', '2022-10-28', '184.130.196.172', '32.8761', '-117.2318', 'https://zenodo.org/record/5131909/files/geodynamics/aspect-v2.3.0.zip?download=1'), \
            ('aspect', '2022-10-29', '118.139.226.172', '32.8761', '-117.2318', 'https://zenodo.org/record/5131909/files/geodynamics/aspect-v2.3.0.zip?download=1'), \
            ('aspect', '2022-10-30', '246.4.35.174', '32.8761', '-117.2318', 'https://geodynamics.org/resources/1810/download/aspect-1.0.tar.gz'), \
            ('axisem', '2022-10-28', '204.187.214.209', '32.733975', '-117.144544', 'https://github.com/geodynamics/axisem/releases/tag/9f0be2f'), \
            ('axisem', '2022-11-02', '116.200.114.91', '32.8761', '-117.2318', 'https://geodynamics.org/resources/1773/download/AXISEM_v1.1.tar.gz'), \
            ('axisem', '2022-11-03', '202.68.114.196', '32.8761', '-117.2318', 'https://geodynamics.org/resources/1772/download/axisem-manual-1.3.pdf'), \
            ('calypso', '2022-10-15', '235.233.82.76', '32.733975', '-117.144544', 'https://github.com/geodynamics/calypso/releases/tag/V1.2.0-p2'), \
            ('calypso', '2022-11-04', '99.55.113.25', '32.8761', '-117.2318', 'https://geodynamics.org/resources/1575/download/calypso-1.2.0.tar.gz'), \
            ('calypso', '2022-11-01', '146.227.150.186', '32.8761', '-117.2318', 'https://geodynamics.org/resources/1576/download/calypso-manual-1.2.pdf') \
        "

    dbconn.execute(test_insert_statement)

    print("Test records created successfully")

    dbconn.commit()
    dbconn.close()


def dbinit():
    dbconn = sqlite3.connect('tracking.db', timeout=60)
    print("Opened database successfully")

    cursor = dbconn.cursor()

    checkTable = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name= 'tool_download_count'"
    cursor.execute(checkTable)

    if cursor.fetchone()[0] == 1:
        print('Table tool_download_count exists')
        #cursor.execute("drop table tool_download_count")
    else:
        print('Table tool_download_count does not exist, creating it')
        createTable = '''CREATE TABLE tool_download_count
            (count_id          INTEGER PRIMARY KEY     AUTOINCREMENT,
            tool_name          TEXT                NOT NULL,
            date_download      DATE                NOT NULL,
            ip_address         VARCHAR(32)         NOT NULL,
            ip_lat             FLOAT               NOT NULL,
            ip_long            FLOAT               NOT NULL,
            source             TEXT                NOT NULL );
        '''
        cursor.execute(createTable)

    print("Table created successfully")


# Call main
if __name__ == "__main__":
    main()
