# Import the requered libraries
# -------------------------------------
import requests # To make requests
from bs4 import BeautifulSoup
import lxml # To parse HTML data
import csv # To save data into CSV file
import os 
from random import choice
# requests.Timeout = 120

# The web scraper
# -------------------------------------
def main():
    url = "https://findajob.dwp.gov.uk/search" # The job search first page URL
    headers = staticHeadersRotator()
    positions = get_website_structure(url, headers=headers, params={'loc': '86383', 'p': '1', 'pp': '50'})
    pageSize = 50
    print('All positions:', positions)
    print('Page size:', pageSize)
    jobs = 0
    for i, page in enumerate(range(1, 1 + int(positions/pageSize)),1): # Loob through every page
        print(f'Page: {i}')
        print(f'    {jobs} jobs collected so far.')
        params = {
            'loc': '86383',
            'p': str(page),
            'pp': str(pageSize),
        }
        while True: # Keep looping
            try: # Try to reqeust a page
                mainReponce = requests.get(f"https://findajob.dwp.gov.uk/search", headers=headers, params=params)
                mainSoup = BeautifulSoup(mainReponce.text, 'lxml')
                mainData = mainSoup.find_all("div", class_="search-result")
                if len(mainData) == 0:
                    print('Bad response')
                    headers = staticHeadersRotator()
                print("    Page request Succeed ")
                break # Until the the requeset secceed
            except: # Otherwise 
                print("    Page request failled")
                headers = staticHeadersRotator() # Change the request headers 
                continue # And Loob again

        for n, job in enumerate(mainData, 1): # Loop trough every job post in the current page
                print(f"    Job: {n}")
                jobs+=len(mainData)
                while True: # Keep looping
                    try: # Try to request a job
                        subResponce = requests.get(job.h3.a['href'], headers=headers)
                        subSoup = BeautifulSoup(subResponce.text, 'lxml')
                        print("         Job request succeed")
                        break # Untill the request succeed
                    except: # Otherwese
                        headers = staticHeadersRotator() # Change the request headers
                        print("         Job request failled")
                        continue # And Loop Again

                id = str((i-1)*20 + n)
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
                print("         Seccess scraping")
                save_job_info(id,
                              title,          # Send the scraped data into the save function
                              postingDate,
                              Salary,
                              Hours,
                              closingDate,
                              Location,
                              Company,
                              jobType,
                              jobReference,
                              additionalSalaryInf)



def get_website_structure(url, headers, params):
    while True: # keep looping
        try: # Request for page sturcture
            responce = requests.get(url, headers=headers, params=params)
            if responce.status_code !=200: # If request not succeed
                print('Structure reqeust failled')
                headers = staticHeadersRotator() # Change the request headers
                continue # Retry
            print("Sturcture request succeed")
            break # Break otherwise
        except: # If error happens (timeout error for instanse)
            print('Structure reqeust failled')
            headers = staticHeadersRotator() # Change the request headers
            continue # And Loop Again
    soup = BeautifulSoup(responce.text, 'lxml')
    data = soup.find('h1', class_="govuk-heading-l")
    allPositions = int(data.text.strip().split(' ')[0].replace(',', ''))
    return allPositions

def save_job_info(id,title,postingDate,Salary,Hours,closingDate,Location,Company,jobType,jobReference,additionalSalaryInf):
    """Saves job data to a CSV file."""
    if os.path.exists('GOVUKJobs.csv'): # If the csv file excists
        with open('GOVUKJobs.csv', 'a', newline='', encoding='utf-8') as csvfile: # append data
            writer = csv.writer(csvfile)
            writer.writerow([id,title,postingDate,Salary,Hours,closingDate,Location,Company,jobType,jobReference,additionalSalaryInf])
    else: # If not
        with open('GOVUKJobs.csv', 'w', newline='', encoding='utf-8') as csvfile: # Create one and write the column name
            writer = csv.writer(csvfile)
            writer.writerow(["id","title","postingDate","Salary","Hours","closingDate","Location","Company","jobType","jobReference","additionalSalaryInf"])
            writer.writerow([id,title,postingDate,Salary,Hours,closingDate,Location,Company,jobType,jobReference,additionalSalaryInf])

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
    response = requests.get('https://headers.scrapeops.io/v1/browser-headers',params={'api_key': 'fba52e3f-8ad2-4af3-a04c-e2f567f1fe8e','num_headers': '10'})
    headers = response.json()['result']
    return choice(headers)

if __name__== "__main__":
    main()