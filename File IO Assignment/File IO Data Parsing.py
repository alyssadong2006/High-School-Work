import csv

infoDict = {}

def calculateCountryGDP(filename):
    """provides list of countries and average GDP per capita"""
    with open(filename, 'r') as fileIn:
        GDPreader = csv.DictReader(fileIn)
        for line in GDPreader:
            GDPsum = 0
            count = 0
            for year in range(1960, 2023):
                if line[f'{year}'] != "":
                    GDPYear = line[f'{year}']
                    GDPsum += float(GDPYear)
                    count += 1
            if count == 0:
                count = 1
            Avg = GDPsum/count
            countryName = cleanData(",", line['Country Name'])
            infoDict[countryName] = {'CountryCode': line['Country Code'],'AvgGDPperCapita': Avg, 'Companies':[]}
            
def cleanData(target, info):
    """
    cleaning info by returning only the first half of the name
    Example:
    Gambia, The --> Gambia
    
    """
    cleanedInfo = info
    if target in info:
        infoList = info.strip().split(target)
        cleanedInfo = infoList[0]
    return cleanedInfo

def rankedCompaniesInfo(filename):
    """provides info of ranked companies according to country"""
    with open(filename, 'r') as fileIn:
        companyReader = csv.DictReader(fileIn)
        for line in companyReader:
            country = line['Country']
            if country in infoDict:
                info = (line['Company'],line['Global Rank']
                        , line['Profits ($billion)'],
                        line['Assets ($billion)'],
                        line['Market Value ($billion)']
                        )
                infoDict[country]['Companies'].append(info)

def writeOutput(filename, data):
    """writes into csv file, formatted"""
    string = ""
    with open(filename, 'w') as fileOut:       
        for country in data:
            string += f"{country}:\n\tAverage GDP per capita in US$: {data[country]['AvgGDPperCapita']:.2f}\n\tCompanies:\n"
            if data[country]['Companies'] == []:
                string += f'\t\tNone\n'
            for company in data[country]['Companies']:
                string += f'\t\t{company[0]} in Global Rank {company[1]}\n'
                string += f'\t\t\tProfits ($billion): {company[2]}\n'
                string += f'\t\t\tAssets ($billion): {company[3]}\n'
                string += f'\t\t\tMarket Value ($billion): {company[4]}\n'
                string += '\n'
            string += '\n\n'
        fileOut.write(string)
        
calculateCountryGDP('GDP.csv')
rankedCompaniesInfo('Top2000.csv')
writeOutput('Output.csv', infoDict)
