# Import the requered libraries
# -------------------------------------
import requests # To make requests
from bs4 import BeautifulSoup
import lxml # To parse HTML data
import csv # To save data into CSV file
import os 
from random import choice
import time
# requests.Timeout = 120

# The web scraper
# -------------------------------------
def main():
    session = requests.Session()
    url = "https://findajob.dwp.gov.uk/search" # The job search first page URL
    headers = staticHeadersRotator()
    locations = {'South East England': [{'86465': 'Kent'}, {'86437': 'Hampshire'}, {'86463': 'Surrey'}, {'86395': 'Buckinghamshire'}, {'86411': 'Oxfordshire'}, {'86466': 'East Sussex'}, {'86434': 'West Sussex'}, {'86464': 'Berkshire'}, {'86476': 'West Berkshire'}, {'86469': 'Isle Of Wight'}, {'86447': 'Windsor & Maidenhead'}], 'North West England': [{'86397': 'Greater Manchester'}, {'86415': 'Lancashire'}, {'86452': 'Cheshire'}, {'86419': 'Merseyside'}, {'86417': 'Cumbria'}], 
                 'London': [{'86510': 'South West London'}, {'86583': 'South East London'}, {'86592': 'East London'}, {'86588': 'North West London'}, {'86593': 'West London'}, {'86590': 'Central London'}, {'86585': 'North London'}, {'86597': 'Croydon'}, {'86602': 'Harrow'}, {'86591': 'Uxbridge'}, {'86589': 'Hounslow'}, {'86600': 'Enfield'}, {'86608': 'Sutton'}, {'86594': 'Orpington'}, {'86595': 'West Drayton'}, {'86596': 'Mitcham'}, {'86604': 'Twickenham'}, {'86606': 'Hayes'}, {'86601': 'Surbiton'}, {'86605': 'Feltham'}, {'86607': 'Pinner'}, {'86603': 'Greenford'}, {'86599': 'Wallington'}, {'86598': 'Ruislip'}, {'67725': 'Coulsdon'}], 
                 'South West England': [{'56201': 'Bristol'}, {'86406': 'Gloucestershire'}, {'86409': 'Devon'}, {'86459': 'Wiltshire'}, {'86404': 'Dorset'}, {'86448': 'Somerset'}, {'86456': 'Cornwall'}, {'77819': 'Plymouth'}, {'86393': 'Bath & N E Somerset'}, {'86440': 'North Somerset'}, {'86430': 'Isles of Scilly'}], 
                 'Eastern England': [{'86458': 'Essex'}, {'86414': 'Hertfordshire'}, {'86455': 'Norfolk'}, {'86472': 'Suffolk'}, {'86420': 'Cambridgeshire'}, {'86413': 'Bedfordshire'}, {'77712': 'Peterborough'}], 
                 'West Midlands': [{'83620': 'Birmingham'}, {'86416': 'Staffordshire'}, {'86446': 'Shropshire'}, {'86435': 'Worcestershire'}, {'86436': 'Warwickshire'}, {'83714': 'Coventry'}, {'83878': 'Wolverhampton'}, {'86454': 'Herefordshire'}, {'83849': 'Walsall'}, {'83787': 'Solihull'}, {'83826': 'Sutton Coldfield'}, {'83759': 'Dudley'}, {'83871': 'West Bromwich'}, {'83780': 'Oldbury'}, {'83868': 'Wednesbury'}, {'83844': 'Tipton'}, {'83807': 'Stourbridge'}, {'83769': 'Halesowen'}, {'83709': 'Brierley Hill'}, {'83784': 'Smethwick'}, {'83877': 'Willenhall'}, {'83615': 'Bilston'}, {'83776': 'Kingswinford'}, {'83782': 'Rowley Regis'}], 
                 'Yorkshire And The Humber': [{'86390': 'West Yorkshire'}, {'86391': 'South Yorkshire'}, {'86403': 'North Yorkshire'}, {'86398': 'East Riding'}, {'86418': 'North East Lincolnshire'}, {'86387': 'North Lincolnshire'}], 
                 'East Midlands': [{'86457': 'Nottinghamshire'}, {'86421': 'Derbyshire'}, {'86402': 'Leicestershire'}, {'86412': 'Northamptonshire'}, {'86449': 'Lincolnshire'}, {'86577': 'Rutland'}, {'86615': 'Northants'}], 
                 'Scotland': [{'86566': 'Edinburgh'}, {'86470': 'Glasgow'}, {'86443': 'Aberdeenshire'}, {'86494': 'Highlands'}, {'86485': 'Midlothian'}, {'86477': 'North Lanarkshire'}, {'86493': 'Fife'}, {'86468': 'South Lanarkshire'}, {'86496': 'Perth & Kinross'}, {'86487': 'West Lothian'}, {'62895': 'Dundee'}, {'86552': 'Falkirk County'}, {'86480': 'Renfrewshire'}, {'86498': 'Argyll & Bute'}, {'86535': 'East Lothian'}, {'86515': 'County Stirling'}, {'86542': 'Moray'}, {'86471': 'South Ayrshire'}, {'86467': 'North Ayrshire'}, {'86479': 'Dumfries & Galloway'}, {'86492': 'East Ayrshire'}, {'86497': 'Borders'}, {'192065': 'East Dunbartonshire'}, {'86560': 'Angus'}, {'192064': 'East Renfrewshire'}, {'86518': 'Inverclyde'}, {'86462': 'West Dunbartonshire'}, {'86556': 'Orkney Islands'}, {'86563': 'Shetland Islands'}, {'86483': 'Western Isles'}, {'86545': 'Clackmannanshire'}], 
                 'Wales': [{'86500': 'Cardiff County'}, {'82564': 'Swansea'}, {'86551': 'Powys'}, {'86481': 'Rhondda Cynon Taff'}, {'86444': 'Carmarthenshire'}, {'86491': 'Bridgend County'}, {'73474': 'Newport'}, {'86280': 'Wrexham'}, {'86533': 'Denbighshire'}, {'86509': 'Flintshire'}, {'86524': 'Gwynedd'}, {'86508': 'Neath Port Talbot'}, {'86544': 'Ceredigion'}, {'86506': 'Pembrokeshire'}, {'86439': 'Monmouthshire'}, {'86450': 'The Vale of Glamorgan'}, {'86522': 'Conwy County'}, {'86475': 'Caerphilly County'}, {'86495': 'Torfaen'}, {'86558': 'Merthyr Tydfil County'}, {'86532': 'Blaenau Gwent'}, {'82693': 'Swansea Enterprise Park'}, {'86519': 'Isle Of Anglesey'}, {'82694': 'Swansea Vale'}], 
                 'North East England': [{'86389': 'Tyne & Wear'}, {'86405': 'County Durham'}, {'86410': 'Northumberland'}], 
                 'Northern Ireland': [{'55926': 'Belfast'}, {'86575': 'Derry'}, {'86549': 'County Antrim'}, {'86534': 'County Down'}, {'72912': 'Lisburn'}, {'59483': 'Craigavon'}, {'86474': 'Newry & Mourne'}, {'86567': 'North Down'}, {'86424': 'Fermanagh'}, {'57460': 'Carrickfergus'}, {'55554': 'Ballymena'}, {'86546': 'County Tyrone'}, {'86550': 'Ards'}, {'58193': 'Coleraine'}, {'76676': 'Omagh'}, {'55531': 'Armagh'}, {'71699': 'Larne'}, {'72927': 'Magherafelt'}, {'58294': 'Cookstown'}, {'81749': 'Strabane'}, {'72032': 'Limavady'}, {'55599': 'Ballymoney'}], 
                 'Channel Islands': [{'86570': 'Jersey'}, {'86530': 'Guernsey'}], 
                 'Isle Of Man': [{'70503': 'Douglas'}]}
    categories = [{"12":"Healthcare & Nursing Jobs"},{"19":"Other/General Jobs"},{"27":"Teaching Jobs"},{"16":"Logistics & Warehouse Jobs"},{"26":"Social Work Jobs"},{"9":"Engineering Jobs"},{"7":"Domestic Help & Cleaning Jobs"},{"13":"Hospitality & Catering Jobs"},{"177":"Social Care Jobs"},{"23":"Sales Jobs"},{"22":"Retail Jobs"},{"2":"Admin Jobs"},{"18":"Manufacturing Jobs"},{"1":"Accounting & Finance Jobs"},{"28":"Trade & Construction Jobs"},{"17":"Maintenance Jobs"},{"11":"HR & Recruitment Jobs"},{"6":"Customer Services Jobs"},{"5":"Creative & Design Jobs"},{"25":"Security & Protective Services Jobs"},{"14":"IT Jobs"},{"24":"Scientific & QA Jobs"},{"8":"Energy, Oil & Gas Jobs"},{"20":"PR, Advertising & Marketing Jobs"},{"15":"Legal Jobs"},{"21":"Property Jobs"},{"10":"Graduate Jobs"},{"4":"Consultancy Jobs"},{"3":"Agriculture, Fishing & Forestry Jobs"},{"29":"Travel Jobs"}]
    allJobs = 0
    for state in list(locations.keys()):
        print("="*20)
        print("="*20)
        print("         GOV.UK Web Scraper V2 Starts")
        print("="*20)
        print("="*20)
        print("Jobs from:", state, "state")

        for city in list(locations[state]):
            cityId = list(city.keys())[0]
            cityName = city[cityId]
            print("--Jobs from:", cityName, "city")
            print(f"--{allJobs} jobs collected so far.")
            for category in categories:
                categoryId = list(category.keys())[0]
                categoryName = category[categoryId]
                positions = get_website_structure(url, headers=headers, params={'loc': cityId, 'cat': categoryId, 'p': '1', 'pp': '50'}, session=session)
                pageSize = 50
                print('----',categoryName)
                print('------All positions:', positions)
                print('------Page size:', pageSize)
                jobsCount = 0
                for i, page in enumerate(range(1, 2+int(positions/pageSize)),1): # Loob through every page
                    print(f'------Page: {i}')
                    print(f'------{jobsCount} jobs collected.')
                    params = {
                        'loc': cityId,
                        'cat': categoryId,
                        'p': str(page),
                        'pp': str(pageSize)
                    }
                    while True: # Keep looping
                        try: # Try to reqeust a page
                            mainReponce = session.get(f"https://findajob.dwp.gov.uk/search", headers=headers, params=params)
                            mainSoup = BeautifulSoup(mainReponce.text, 'lxml')
                            mainData = mainSoup.find_all("div", class_="search-result")
                            if len(mainData) == 0:
                                print('--------Bad response')
                                headers = staticHeadersRotator()
                            print("--------Page request Succeed ")
                            break # Until the the requeset secceed
                        except: # Otherwise 
                            print("--------Page request failled")
                            headers = staticHeadersRotator() # Change the request headers 
                            continue # And Loob again

                    for n, job in enumerate(mainData, 1): # Loop trough every job post in the current page
                            if jobsCount == positions:
                                print("----Done")
                                break
                            print(f"----------Job: {n}")
                            while True: # Keep looping
                                try: # Try to request a job
                                    subResponce = session.get(job.h3.a['href'], headers=headers)
                                    subSoup = BeautifulSoup(subResponce.text, 'lxml')
                                    print("----------Job request succeed")
                                    break # Untill the request succeed
                                except: # Otherwese
                                    headers = staticHeadersRotator() # Change the request headers
                                    print("----------Job request failled")
                                    continue # And Loop Again

                            id = str((i-1)*50 + n)
                            try:
                                title = subSoup.find("h1", class_="govuk-heading-l govuk-!-margin-top-8").text.strip()
                            except:
                                title = "None"

                            details = subSoup.find_all("tr", class_="govuk-table__row")
                            detailsDict = {}
                            for detail in details:
                                detailsDict[detail.th.text.strip()[:-1]] = detail.td.text.strip()
                            try:
                                postingDate = detailsDict['Posting date']
                            except:
                                postingDate = "None"
                            try:
                                Salary = detailsDict['Salary']
                            except:
                                Salary = "None"
                            try:
                                Hours = detailsDict['Hours']
                            except:
                                Hours = "None"
                            try:
                                closingDate = detailsDict['Closing date']
                            except:
                                closingDate = "None"
                            try:
                                Location = detailsDict['Location']
                            except:
                                Location = "None"
                            try:
                                Company = detailsDict['Company']
                            except:
                                Company = "None"
                            try:
                                jobType = detailsDict['Job type']
                            except:
                                jobType = "None"
                            try:
                                jobReference = detailsDict['Job reference']
                            except:
                                jobReference = "None"
                            try:
                                additionalSalaryInf = detailsDict['Additional salary information']
                            except:
                                additionalSalaryInf = "None"
                            print("----------Seccess scraping")
                            save_job_info(id,
                                        title,          # Send the scraped data into the save function
                                        postingDate,
                                        Salary,
                                        Hours,
                                        closingDate,
                                        Location,
                                        state,
                                        cityName,
                                        Company,
                                        jobType,
                                        categoryName,
                                        jobReference,
                                        additionalSalaryInf)
                            jobsCount +=1
                allJobs +=jobsCount


def get_website_structure(url, headers, params, session):
    while True: # keep looping
        try: # Request for page sturcture
            responce = session.get(url, headers=headers, params=params)
            if responce.status_code !=200: # If request not succeed
                print('--Structure reqeust failled')
                headers = staticHeadersRotator() # Change the request headers
                continue # Retry
            print("--Sturcture request succeed")
            break # Break otherwise
        except: # If error happens (timeout error for instanse)
            print('--Structure reqeust failled')
            headers = staticHeadersRotator() # Change the request headers
            continue # And Loop Again
    soup = BeautifulSoup(responce.text, 'lxml')
    data = soup.find('h1', class_="govuk-heading-l")
    try:
        allPositions = int(data.text.strip().split(' ')[0].replace(',', ''))
    except:
        return 1
    return allPositions

def save_job_info(id,title,postingDate,salary,hours,closingDate,location,state,city,company,jobType,category,jobReference,additionalSalaryInf):
    """Saves job data to a CSV file."""
    if os.path.exists('GOVUKJobs.csv'): # If the csv file excists
        with open('GOVUKJobs.csv', 'a', newline='', encoding='utf-8') as csvfile: # append data
            writer = csv.writer(csvfile)
            writer.writerow([id,title,postingDate,salary,hours,closingDate,location,state,city,company,jobType,category,jobReference,additionalSalaryInf])
    else: # If not
        with open('GOVUKJobs.csv', 'w', newline='', encoding='utf-8') as csvfile: # Create one and write the column name
            writer = csv.writer(csvfile)
            writer.writerow(["id","title","postingDate","salary","hours","closingDate","location","state","city","company","jobType","category","jobReference","additionalSalaryInf"])
            writer.writerow([id,title,postingDate,salary,hours,closingDate,location,state,city,company,jobType,category,jobReference,additionalSalaryInf])

def staticUserAgentRotator():
        user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
        "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
        "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/15.4 Safari/537.75.14",
        "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        ]
        return {'User-Agent': choice(user_agents)}

def staticHeadersRotator():
    headers = [
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'sec-ch-ua': 'Microsoft Edge;v="87", "Chromium";v="87", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Windows', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en-US,en;q=0.9,es;q=0.5'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'macOS', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en-US,fr;q=0.5'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Google Chrome;v="90", "Chromium";v="90", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'macOS', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip', 'accept-language': 'en-US,es;q=0.8'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Windows', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en-US,en;q=0.9,fr;q=0.8'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'sec-ch-ua': 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'macOS', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip', 'accept-language': 'en-US,en;q=0.9,fr;q=0.8'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Google Chrome;v="84", "Chromium";v="84", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Windows', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip', 'accept-language': 'en-US,en;q=0.7'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'sec-ch-ua': 'Google Chrome;v="83", "Chromium";v="83", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'macOS', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip', 'accept-language': 'en-US,en;q=0.9,es;q=0.8'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Microsoft Edge;v="87", "Chromium";v="87", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Windows', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip', 'accept-language': 'en'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Google Chrome;v="89", "Chromium";v="89", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Windows', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en'}, 
        {'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'sec-ch-ua': 'Google Chrome;v="86", "Chromium";v="86", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'macOS', 'sec-fetch-site': 'none', 'sec-fetch-mod': '', 'sec-fetch-user': '?1', 'accept-encoding': 'gzip', 'accept-language': 'en-US,it;q=0.7'}
        ]

    return choice(headers)

def apiheadersRotator():
    response = requests.get('https://headers.scrapeops.io/v1/browser-headers',params={'api_key': apiKey,'num_headers': '10'})
    headers = response.json()['result']
    return choice(headers)

if __name__== "__main__":
    startTime = time.time()
    main()
    print('\n\tTotal time taken:', time.time()-startTime)