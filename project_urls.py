import json, os, re
import ETL

if __name__ == '__main__':
    etl = ETL.ETL()

    rawData_path = 'rawData/repositories.json'
    rawData = etl.read_json(rawData_path)
    projects_url = []
    i = 0
    projects_url_50 = []
    for rd in rawData:
        projects_url_50.append(rd['clone_url'])
        if len(projects_url_50) % 50 == 0:
            projects_url.append(projects_url_50)
            projects_url_50 = []
    for urls in projects_url:
        print(str(urls).replace("'", '"').replace(',', ''))
