import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.e-service.admin.ch/competency-app-download/eCH-0135.xml'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'xml')

with open('data.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Écrit les en-têtes de colonnes
    writer.writerow(['validTo', 'validFrom', 'placeOfOriginId','historyMunicipalityId','placeOfOriginName', 'cantonAbbreviation', 'successorId'])

    # Parcourt tous les éléments placeOfOrigin
    for placeOfOrigin in soup.find_all('placeOfOrigin'):
        validTo = placeOfOrigin.find('validTo')
        if validTo is not None:
            validTo = validTo.text
        else:
            validTo = ''
        validFrom = placeOfOrigin.find('validFrom')
        if validFrom is not None:
            validFrom = validFrom.text
        else:
            validFrom = ''
        placeOfOriginId = placeOfOrigin.find('placeOfOriginId').text
        historyMunicipalityId = placeOfOrigin.find('historyMunicipalityId')
        if historyMunicipalityId is not None:
            historyMunicipalityId = historyMunicipalityId.text
        else:
            historyMunicipalityId = ''
        placeOfOriginName = placeOfOrigin.find('placeOfOriginName').text
        cantonAbbreviation = placeOfOrigin.find('cantonAbbreviation').text
        successorId = placeOfOrigin.find('successorId')
        if successorId is not None:
            successorId = successorId.text
        else:
            successorId = ''

        # Écrit une ligne dans le fichier CSV pour chaque élément placeOfOrigin
        writer.writerow([validTo, validFrom, placeOfOriginId, historyMunicipalityId,placeOfOriginName, cantonAbbreviation, successorId])

for placeOfOrigin in soup.find_all('placeOfOrigin'):
    validTo = placeOfOrigin.find('validTo')
    if validTo is not None:
        validTo = validTo.text
    else:
        validTo = ''
    validFrom = placeOfOrigin.find('validFrom')
    if validFrom is not None:
        validFrom = validFrom.text
    else:
        validFrom = ''
    placeOfOriginId = placeOfOrigin.find('placeOfOriginId').text
    historyMunicipalityId = placeOfOrigin.find('historyMunicipalityId')
    if historyMunicipalityId is not None:
        historyMunicipalityId = historyMunicipalityId.text
    else:
        historyMunicipalityId = ''
    placeOfOriginName = placeOfOrigin.find('placeOfOriginName').text
    cantonAbbreviation = placeOfOrigin.find('cantonAbbreviation').text
    successorId = placeOfOrigin.find('successorId')
    if successorId is not None:
        successorId = successorId.text
    else:
        successorId = ''

    print(f"validTo = {validTo}, validFrom = {validFrom}, placeOfOriginId : {placeOfOriginId}, placeOfOriginName : {placeOfOriginName}, cantonAbbreviation : {cantonAbbreviation}, successorId : {successorId}, historyMunicipalityId : {historyMunicipalityId}")
