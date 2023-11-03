# Import the requered libraries
# -------------------------------------
import requests # To make requests
import lxml # To parse HTML data
import csv # To save data into CSV file
import os 
from random import choice
# requests.Timeout = 120

# The web scraper
# -------------------------------------
def main():
    print("="*20)
    url = 'https://www.usajobs.gov/Search/ExecuteSearch'
    departments = ['AG','AF','AR','CM','FQ','DD','ED','DN','EOP','GS','HE','HS','HU','IN','JL','DJ','DL','LL','NN','AH','NV','ZZ','OT','ST','TD','TR','VA']
    headers = getHeader()

    for department in departments:
        print(f'{department} department jobs')
        NumOfPages = get_website_structure(url, headers=headers, jsonData=getJsonParam(page=1, department=department))
        print(f"    NumOfPages: {NumOfPages}")
        for page in range(1, 1 + NumOfPages):
            print(f"      Page {page}")
            json_data = getJsonParam(page=page, department=department)
            while True:
                try:
                    response = requests.post(url, headers=headers, json=json_data, timeout= 10)
                    if response.status_code != 200:
                        print(f'      request failed: {response.status_code}')
                        headers = getHeader
                        print('      header changed')
                        continue
                    print(f'      request succeed: {response.status_code}')
                    break
                except:
                    print(f'      request error')
                    headers = getHeader()
                    print('      header changed')
                    continue
            

            data = response.json()
            for i, job in enumerate(data["Jobs"],1):
                print(f"       Job {i}") 
                try:
                    Title = job['Title']
                except:
                    Title = "None"
                try:
                    Agency = job['Agency']
                except:
                    Agency = "None"
                try:
                    Department = job['Department']
                except:
                    Department = "None"
                try:
                    SalaryDisplay = job['SalaryDisplay']
                except:
                    SalaryDisplay = "None"
                try:
                    DocumentID = job['DocumentID']
                except:
                    DocumentID = "None"
                try:
                    PositionID = job['PositionID']
                except:
                    PositionID = "None"
                try:
                    Location = job['Location']
                except:
                    Location = "None"
                try:
                    DateDisplay = job['DateDisplay']
                except:
                    DateDisplay = "None"
                try:
                    WorkSchedule = job['WorkSchedule']
                except:
                    WorkSchedule = "None"
                try:
                    WorkType = job['WorkType']
                except:
                    WorkType = "None"
                try:
                    ClockDisplay = job['ClockDisplay']
                except:
                    ClockDisplay = "None"
                try:
                    ShowMapIcon = job['ShowMapIcon']
                except:
                    ShowMapIcon = "None"
                try:
                    LocationLatitude = job['LocationLatitude']
                except:
                    LocationLatitude = "None"
                try:
                    LocationLongitude = job['LocationLongitude']
                except:
                    LocationLongitude = "None"
                try:
                    LowGrade = job['LowGrade']
                except:
                    LowGrade = "None"
                try:
                    HighGrade = job['HighGrade']
                except:
                    HighGrade = "None"
                try:
                    JobGrade = job['JobGrade']
                except:
                    JobGrade = "None"
                try:
                    LocationName = job['LocationName']
                except:
                    LocationName = "None"
                try:
                    PositionLocationCount = job['PositionLocationCount']
                except:
                    PositionLocationCount = "None"
                try:
                    PositionURI = job['PositionURI']
                except:
                    PositionURI = "None"
                try:
                    Relocation = job['Relocation']
                except:
                    Relocation = "None"
                try:
                    MinimumRange = job['MinimumRange']
                except:
                    MinimumRange = "None"
                try:
                    PositionEndDate = job['PositionEndDate']
                except:
                    PositionEndDate = "None"
                try:
                    PositionEndDate = job['PositionEndDate']
                except:
                    PositionEndDate = "None"
                try:
                    HiringPathCode = job['HiringPath'][0]['Code']
                except:
                    HiringPathCode = "None"
                try:
                    HiringPathTooltip = job['HiringPath'][0]['Tooltip']
                except:
                    HiringPathTooltip = "None"
                
                save_job_info(Title,Agency,Department,SalaryDisplay,DocumentID,PositionID,Location,DateDisplay,WorkSchedule,WorkType,ClockDisplay,ShowMapIcon,LocationLatitude,LocationLongitude,LowGrade,HighGrade,JobGrade,LocationName,PositionLocationCount,PositionURI,Relocation,MinimumRange,PositionEndDate,HiringPathCode,HiringPathTooltip)

def save_job_info(Title,Agency,Department,SalaryDisplay,DocumentID,PositionID,Location,DateDisplay,WorkSchedule,WorkType,ClockDisplay,ShowMapIcon,LocationLatitude,LocationLongitude,LowGrade,HighGrade,JobGrade,LocationName,PositionLocationCount,PositionURI,Relocation,MinimumRange,PositionEndDate,HiringPathCode,HiringPathTooltip):
    """Save job data to a CSV file."""
    if os.path.exists('USAJobs.tsv'): # If the csv file excists
        with open('USAJobs.tsv', 'a', newline='', encoding='utf-8') as tsvfile: # append data
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow([Title,Agency,Department,SalaryDisplay,DocumentID,PositionID,Location,DateDisplay,WorkSchedule,WorkType,ClockDisplay,ShowMapIcon,LocationLatitude,LocationLongitude,LowGrade,HighGrade,JobGrade,LocationName,PositionLocationCount,PositionURI,Relocation,MinimumRange,PositionEndDate,HiringPathCode,HiringPathTooltip])
    else: # If not
        with open('USAJobs.tsv', 'w', newline='', encoding='utf-8') as tsvfile: # Create one and write the column name
            writer = csv.writer(tsvfile, delimiter='\t')
            writer.writerow(["Title","Agency","Department","SalaryDisplay","DocumentID","PositionID","Location","DateDisplay","WorkSchedule","WorkType","ClockDisplay","ShowMapIcon","LocationLatitude","LocationLongitude","LowGrade","HighGrade","JobGrade","LocationName","PositionLocationCount","PositionURI","Relocation","MinimumRange","PositionEndDate","HiringPathCode", "HiringPathTooltip"])
            writer.writerow([Title,Agency,Department,SalaryDisplay,DocumentID,PositionID,Location,DateDisplay,WorkSchedule,WorkType,ClockDisplay,ShowMapIcon,LocationLatitude,LocationLongitude,LowGrade,HighGrade,JobGrade,LocationName,PositionLocationCount,PositionURI,Relocation,MinimumRange,PositionEndDate,HiringPathCode,HiringPathTooltip])

def getJsonParam(page, department):
    json_data = {
            'JobTitle': [
                '',
            ],
            'GradeBucket': [],
            'JobCategoryCode': [],
            'JobCategoryFamily': [],
            'LocationName': [
                '',
            ],
            'PostingChannel': [],
            'Department': [
                department,
                ],
            'Agency': [],
            'PositionOfferingTypeCode': [],
            'TravelPercentage': [],
            'PositionScheduleTypeCode': [],
            'SecurityClearanceRequired': [],
            'PositionSensitivity': [],
            'ShowAllFilters': [],
            'HiringPath': [],
            'SocTitle': [],
            'MCOTags': [],
            'CyberWorkRole': [],
            'CyberWorkGrouping': [],
            'JobGradeCode': [],
            'Page': str(page),
            'IsAuthenticated': False,
        }
    return json_data

def get_website_structure(url, headers, jsonData):
    print('    Getting Website Structure')
    while True:
        try:
            response = requests.post(url, headers=headers, json=jsonData)
            if response.status_code !=200:
                print('Structure reqeust failled')
                # headers = staticUserAgentRotator()
                continue
            print("    Sturcture request succeed")
            break
        except Exception as e:
            print(f'    Structure reqeust failled: {e}')
            # headers = staticUserAgentRotator()
            continue
    data = response.json()    
    NumOfPages = int(data['Pager']['NumberOfPages'])
    return NumOfPages

def getHeader():
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'ar',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=utf-8',
    'Origin': 'https://www.usajobs.gov',
    'Pragma': 'no-cache',
    'Referer': 'https://www.usajobs.gov/Search/Results?d=AG&p=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
    return headers

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
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        ]
        return choice(user_agents)

if __name__== "__main__":
    main()