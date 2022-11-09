import sqlite3
import random
from faker import Faker

def main():
    dbinit()
    dbtestdata(10)

# Hashmap of software with name and links
software = {}
software["aspect"] = ['https://geodynamics.org/resources/1810/download/aspect-1.0.tar.gz', 
    'https://zenodo.org/record/1297145/files/geodynamics/aspect-v2.0.1.zip?download=1',
    'https://zenodo.org/record/5131909/files/geodynamics/aspect-v2.3.0.zip?download=1',
    'https://github.com/geodynamics/axisem/releases/tag/9f0be2f',
    'https://geodynamics.org/resources/1773/download/AXISEM_v1.1.tar.gz',
    'https://geodynamics.org/resources/1772/download/axisem-manual-1.3.pdf'
    ]
software["calypso"] = ['https://github.com/geodynamics/calypso/releases/tag/V1.2.0-p2',
    'https://geodynamics.org/resources/1575/download/calypso-1.2.0.tar.gz',
    'https://geodynamics.org/resources/1576/download/calypso-manual-1.2.pdf'
    ]
software["aagaard_pylith"] = ['/cig/community/workinggroups/seismo/workshops/spice07/presentations/aagaard_pylith.pdf/at_download/file']
software["cig_science_gateways"] = ['http://geodynamics.org/resources/543/']

# Using faker
faker = Faker()

def dbtestdata(numberOfIp):
    dbconn = sqlite3.connect("tracking.db", timeout=60)
    cursor = dbconn.cursor()

    for i in range(0, numberOfIp):
        softwareKeys = list(software.keys())
        randSelectedSoftware = random.choice(softwareKeys)
        randDate = faker.date_between(start_date='-30d')
        randIpAdd = faker.ipv4()

        arrLink = list(software[randSelectedSoftware])
        randSelectedSoftwareLink = random.choice(arrLink)

        cursor.execute("INSERT INTO tool_download_count (tool_name, date_download, ip_address, ip_lat, ip_long, country, region, city, zip, source) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (randSelectedSoftware, randDate, randIpAdd, i, i, i, i, i, i, randSelectedSoftwareLink) \
                )

    dbconn.commit()

    print(numberOfIp, "test records created successfully")

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
            ("count_id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "tool_name" TEXT NOT NULL,
            "date_download" DATE NOT NULL,
            "ip_address" VARCHAR(32) NOT NULL,
            "ip_lat" FLOAT NOT NULL,
            "ip_long" FLOAT NOT NULL,
            "country" VARCHAR(32) NOT NULL,
            "region" VARCHAR(32) NOT NULL,
            "city" VARCHAR(32) NOT NULL,
            "zip" VARCHAR(32) NOT NULL,
            "source" TEXT NOT NULL,
            "coord_updated" BOOLEAN NOT NULL DEFAULT 0);
        '''

        print("Table created successfully")

        cursor.execute(createTable)

    dbconn.close()


# Call main
if __name__ == "__main__":
    main()