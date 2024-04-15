# Import the requered libraries
# -------------------------------------
import requests # To make requests
import lxml # To parse HTML data
import csv # To save data into CSV file
import json
import os 
from random import choice
# requests.Timeout = 120

# The web scraper
# -------------------------------------
def main():
    url = 'https://seeker-api.careerone.com.au/api/v1/search-job'
    headers = staticHeadersRotator()

    json_data = {
        'resultsPerPage': 1000,
        'page': 1,
        'job_type': [],
        'pay_min': None,
        'pay_max': None,
        'ad_type': [],
        'posted_within_days': {
            'days': 0,
            'value': 'Any time',
            'is_selected': True,
            'count': None,
        },
        'skills': [],
        'keywords': [],
        'brands': [],
        'sector': [],
        'industry': [],
        'company_size': [],
        'job_mode': [],
        'contract_type': [],
        'career_level': [],
        'perks': [],
        'work_authorisation': [],
        'education_level': [],
        'languages': [],
        'certifications': [],
        'include_surrounding_location': True,
        'search': '',
        'search_keywords': None,
        'categories': [],
        'location': {
            'id': 15299,
            'type': 'COUNTRY',
            'label': 'All Australia',
            'display_label': 'Australia',
            'region_name': None,
            'area_name': None,
            'state_name': None,
            'suburb_name': None,
            'suburb_location_id': 0,
            'area_location_id': 0,
            'region_location_id': 0,
            'state_location_id': 0,
            'country_location_id': 15299,
            'state_code': None,
            'country_name': 'Australia',
            'country_code': 'AU',
            'post_code': None,
            'slug': 'australia',
            'meta_robots': 'index',
        },
        'sort_by': 'activates_at',
        'source_code': [],
        'equal_opportunity_tags': [],
        'hiring_site': [],
        'hiring_platform': [],
        'job_title': [],
        'licenses': [],
        'employer_name': None,
        'parsed_filter': '1',
        'parsed': {
            'job_title': [],
            'occupations': [],
        },
        'locale': 'AU',
        'bucket_code': 'ORGANIC,PRIORITISE',
        'allow_backfill': True,
        'site_code': 'careerone',
        'platform_code': 'careerone',
        }
    
    ip = "34.229.218.102"
    port = "3128"
    proxies = {
    "http": f"http://{ip}:{port}",
    "https": f"http://{ip}:{port}"
    }
    # positions = get_website_structure(url, headers=headers, proxies=proxies, json=json_data)
    for page in range(11, int(151563/1000)+1):
        print(f'page {str(page)}, means {str((page-1)*1000)} jobs')
        json_data = {
        'resultsPerPage': 1000,
        'page': page,
        'job_type': [],
        'pay_min': None,
        'pay_max': None,
        'ad_type': [],
        'posted_within_days': {
            'days': 0,
            'value': 'Any time',
            'is_selected': True,
            'count': None,
        },
        'skills': [],
        'keywords': [],
        'brands': [],
        'sector': [],
        'industry': [],
        'company_size': [],
        'job_mode': [],
        'contract_type': [],
        'career_level': [],
        'perks': [],
        'work_authorisation': [],
        'education_level': [],
        'languages': [],
        'certifications': [],
        'include_surrounding_location': True,
        'search': '',
        'search_keywords': None,
        'categories': [],
        'location': {
            'id': 15299,
            'type': 'COUNTRY',
            'label': 'All Australia',
            'display_label': 'Australia',
            'region_name': None,
            'area_name': None,
            'state_name': None,
            'suburb_name': None,
            'suburb_location_id': 0,
            'area_location_id': 0,
            'region_location_id': 0,
            'state_location_id': 0,
            'country_location_id': 15299,
            'state_code': None,
            'country_name': 'Australia',
            'country_code': 'AU',
            'post_code': None,
            'slug': 'australia',
            'meta_robots': 'index',
        },
        'sort_by': 'activates_at',
        'source_code': [],
        'equal_opportunity_tags': [],
        'hiring_site': [],
        'hiring_platform': [],
        'job_title': [],
        'licenses': [],
        'employer_name': None,
        'parsed_filter': '1',
        'parsed': {
            'job_title': [],
            'occupations': [],
        },
        'locale': 'AU',
        'bucket_code': 'ORGANIC,PRIORITISE',
        'allow_backfill': True,
        'site_code': 'careerone',
        'platform_code': 'careerone',
        }
    
        while True:
            try:
                response = requests.get(url=url, headers=headers, proxies=proxies, json=json_data)
                if response.status_code != 200:
                    print('     request failed')
                    headers = staticHeadersRotator()
                    print('     header changed')
                    proxies = proxyRotator()
                    print('     proxy changed')
                    continue
                print('     request succeed')
                break
            except:
                print('     request failed')
                headers = staticHeadersRotator()
                print('     header changed')
                proxies = proxyRotator()
                print('     proxy changed')
                continue
        
        data = response.json()
        with open(f'careeroneJobs{page}.json', "w") as json_file:
            json.dump(data, json_file, indent=4)
        for i, job in enumerate(data['search_results']['jobs'],1):
            print("         Job "+ str(i))
            try:
                contract_type_id = job['contract_type_id']
            except:
                contract_type_id = "None"

            try:
                location_label = job['location_label']
            except:
                location_label = "None"

            try:
                location_level_2_slug = job['location_level_2_slug']
            except:
                location_level_2_slug = "None"

            try:
                group_uuid = job['group_uuid']
            except:
                group_uuid = "None"

            try:
                uuid = job['uuid']
            except:
                uuid = "None"

            try:
                location_id = job['location_id']
            except:
                location_id = "None"

            try:
                pay_max_normalised = job['pay_max_normalised']
            except:
                pay_max_normalised = "None"

            try:
                product_id = job['product_id']
            except:
                product_id = "None"

            try:
                location_level = job['location_level']
            except:
                location_level = "None"

            try:
                apply_type_id = job['apply_type_id']
            except:
                apply_type_id = "None"

            try:
                occupation_id = job['occupation_id']
            except:
                occupation_id = "None"

            try:
                id = job['id']
            except:
                id = "None"

            try:
                location_slug = job['location_slug']
            except:
                location_slug = "None"

            try:
                job_title = job['job_title']
            except:
                job_title = "None"

            try:
                occupation_470 = job['occupation_470']
            except:
                occupation_470 = "None"

            try:
                activates_at = job['activates_at']
            except:
                activates_at = "None"

            try:
                pay_min_normalised = job['pay_min_normalised']
            except:
                pay_min_normalised = "None"

            try:
                pay_min = job['pay_min']
            except:
                pay_min = "None"

            try:
                brand_id = job['brand_id']
            except:
                brand_id = "None"

            try:
                brand_slug = job['brand_slug']
            except:
                brand_id = "None"

            try:
                badge =job['badge']
            except:
                badge = "None"

            try:
                job_description = job['job_description']
            except:
                job_description = "None"

            try:
                company_name = job['company_name']
            except:
                company_name = "None"

            try:
                location_level_3_slug = job['location_level_3_slug']
            except:
                location_level_3_slug = "None"

            try:
                channel_id = job['channel_id']
            except:
                channel_id = "None"

            try:
                bucket_code = job['bucket_code']
            except:
                bucket_code = "None"

            try:
                category_label = job['category_label']
            except:
                category_label = "None"

            try:
                occupation_label = job['occupation_label']
            except:
                occupation_label = "None"

            try:
                job_type_label = job['job_type_label']
            except:
                job_type_label = "None"

            try:
                account_type_id = job['account_type_id']
            except:
                account_type_id = "None"

            try:
                contract_type_label = job['contract_type_label']
            except:
                contract_type_label = "None"

            try:
                job_type_id = job['job_type_id']
            except:
                job_type_id = "None"

            try:
                source_reference = job['source_reference']
            except:
                source_reference = "None"

            try:
                base_normalised_job_title_id = job['base_normalised_job_title_id']
            except:
                base_normalised_job_title_id = "None"

            try:
                base_normalised_job_title = job['base_normalised_job_title']
            except:
                base_normalised_job_title = "None"

            try:
                expires_at = job['expires_at']
            except:
                expires_at = "None"

            try:
                skillss = [skillSlag['slug'] for skillSlag in job['skills_details']]
            except:
                expires_at = "None"

            try:
                category_id = job['category_id']
            except:
                category_id = "None"

            try:
                refreshed_at = job['refreshed_at']
            except:
                refreshed_at = "None"

            try:
                account_name = job['account_name']
            except:
                account_name = "None"

            try:
                job_mode_id = job['job_mode_id']
            except:
                job_mode_id = "None"

            try:
                pay_max = job['pay_max']
            except:
                pay_max = "None"

            try:
                pay_type = job['pay_type']
            except:
                pay_type = "None"

            try:
                location_level_1_label = job['location_level_1_label']
            except:
                location_level_1_label = "None"

            try:
                occupation_slug = job['occupation_slug']
            except:
                occupation_slug = "None"

            try:
                job_mode_label = job['job_mode_label']
            except:
                job_mode_label = "None"

            try:
                location_level_5 = job['location_level_5']
            except:
                location_level_5 = "None"

            try:
                location_type = job['location_type']
            except:
                location_type = "None"

            try:
                account_id = job['account_id']
            except:
                account_id = "None"

            try:
                location_level_4 = job['location_level_4']
            except:
                location_level_4 = "None"

            try:
                location_level_3 = job['location_level_3']
            except:
                location_level_3 = "None"

            try:
                location_level_2 = job['location_level_2']
            except:
                location_level_2 = "None"

            try:
                location_level_1 = job['location_level_1']
            except:
                location_level_1 = "None"

            try:
                category_slug = job['category_slug']
            except:
                category_slug = "None"

            try:
                URL = job['URL']
            except:
                URL = "None"

            try:
                date_label = job['date_label']
            except:
                date_label = "None"

            try:
                location_lon = job['location']['lon']
            except:
                location_lon = "None"

            try:
                location_lat = job['location']['lat']
            except:
                location_lat = "None"

            try:
                updated_date = job['updated_date']
            except:
                updated_date = "None"

            try:
                refreshed_at = job['refreshed_at']
            except:
                refreshed_at = "None"

            try:
                skills = ','.join(job['skills'])
            except:
                skills = "None"

            try:
                perks_label = ','.join(job['perks_label'])
            except:
                perks_label = "None"
            
            try:
                job_bullets = '-'.join(job['job_bullets'])
            except:
                job_bullets = "None"
            
            try:
                work_authorisations_label = ','.join(job['work_authorisations_label'])
            except:
                work_authorisations_label = "None"
            

            if os.path.exists('NLEJobs.csv'):
                with open('careerOneJobs.csv', 'a', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([contract_type_id, location_label, location_level_2_slug, group_uuid, uuid, location_id, pay_max_normalised, product_id, location_level, apply_type_id, occupation_id, id, location_slug, job_title, occupation_470, activates_at, pay_min_normalised, pay_min, brand_id, brand_slug, badge, job_description, company_name, location_level_3_slug, channel_id, bucket_code, category_label, occupation_label, job_type_label, account_type_id, contract_type_label, job_type_id, source_reference, base_normalised_job_title_id, base_normalised_job_title, expires_at, skillss, category_id, refreshed_at, account_name, job_mode_id, pay_max, pay_type, location_level_1_label, occupation_slug, job_mode_label, location_level_5, location_type, account_id, location_level_4, location_level_3, location_level_2, location_level_1, category_slug, URL, date_label, location_lon, location_lat, updated_date, refreshed_at, skills, perks_label, job_bullets, work_authorisations_label])
            else:
                with open('careerOneJobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["contract_type_id", "location_label", "location_level_2_slug", "group_uuid", "uuid", "location_id", "pay_max_normalised", "product_id", "location_level", "apply_type_id", "occupation_id", "id", "location_slug", "job_title", "occupation_470", "activates_at", "pay_min_normalised", "pay_min", "brand_id", "brand_slug", "badge", "job_description", "company_name", "location_level_3_slug", "channel_id", "bucket_code", "category_label", "occupation_label", "job_type_label", "account_type_id", "contract_type_label", "job_type_id", "source_reference", "base_normalised_job_title_id", "base_normalised_job_title", "expires_at", "skillss", "category_id", "refreshed_at", "account_name", "job_mode_id", "pay_max", "pay_type", "location_level_1_label", "occupation_slug", "job_mode_label", "location_level_5", "location_type", "account_id", "location_level_4", "location_level_3", "location_level_2", "location_level_1", "category_slug", "URL", "date_label", "location_lon", "location_lat", "updated_date", "refreshed_at", "skills", "perks_label", "job_bullets", "work_authorisations_label"])
                    writer.writerow([contract_type_id, location_label, location_level_2_slug, group_uuid, uuid, location_id, pay_max_normalised, product_id, location_level, apply_type_id, occupation_id, id, location_slug, job_title, occupation_470, activates_at, pay_min_normalised, pay_min, brand_id, brand_slug, badge, job_description, company_name, location_level_3_slug, channel_id, bucket_code, category_label, occupation_label, job_type_label, account_type_id, contract_type_label, job_type_id, source_reference, base_normalised_job_title_id, base_normalised_job_title, expires_at, skillss, category_id, refreshed_at, account_name, job_mode_id, pay_max, pay_type, location_level_1_label, occupation_slug, job_mode_label, location_level_5, location_type, account_id, location_level_4, location_level_3, location_level_2, location_level_1, category_slug, URL, date_label, location_lon, location_lat, updated_date, refreshed_at, skills, perks_label, job_bullets, work_authorisations_label])
            print('job '+ str(i) + 'data saved successfuly')        

def proxyRotator():
    proxies = [
    "37.19.220.180:8443",
    "37.19.220.129:8443",
    "208.184.163.30:3129",
    "138.199.48.4:8443",
    "138.199.48.1:8443",
    "34.229.218.102:3128",
    "37.19.220.179:8443",
    "64.189.106.6:3129",
    "107.173.156.182:3000",
    "159.203.120.97:10009",
    "141.95.251.184:3128",
    "43.157.8.79:8888",
    "206.189.100.237:3128",
    "185.186.78.199:3128",
    "148.251.0.198:6588",
    "49.12.208.110:8000",
    "104.129.198.126:8800",
    "176.31.129.223:8080",
    "185.200.119.90:8443",
    "82.102.26.38:8443",
    "95.141.32.76:3128",
    "64.225.8.132:10008",
    "65.108.200.102:3128",
    "41.65.0.218:1981",
    "217.160.32.131:8080",
    "201.182.55.205:999",
    "154.236.189.23:1976",
    "194.165.140.122:3128",
    "5.188.168.19:8443",
    "5.188.168.199:8443",
    "193.122.76.102:8800",
    "64.225.4.81:10007",
    "217.52.247.79:1981",
    "96.95.164.43:3128",
    "67.43.228.251:18181",
]
    choose = choice(proxies)
    proxy = {
    "http": f"http://{choose}",
    "https": f"http://{choose}"
    }
    return proxy

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
    {
    'authority': 'seeker-api.careerone.com.au',
    'accept': 'application/json',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8,fr;q=0.7,fr-FR;q=0.6,en-GB;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://www.careerone.com.au',
    'platform-code': 'careerone',
    'referer': 'https://www.careerone.com.au/',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'site-code': 'careerone',
    'user-agent': "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
    }
]
    return choice(headers)

def apiheadersRotator():
    response = requests.get('https://headers.scrapeops.io/v1/browser-headers',params={'api_key': 'fba52e3f-8ad2-4af3-a04c-e2f567f1fe8e','num_headers': '10'})
    headers = response.json()['result']
    return choice(headers)

def get_website_structure(url, headers, proxies, json):
    '''This function purpose is to get the sturcture of the page, it returns:
        allPositions: count of all positions'''
    while True:
        try:
            response = requests.get(url, headers=headers,json=json,proxies=proxies,timeout=100)
            if response.status_code !=200:
                print('Structure reqeust failled')
                headers = staticUserAgentRotator()
                print('headers changed')
                proxies = proxyRotator()
                print('proxy changed')
                continue
            print("Sturcture request succeed")
            break
        except:
            print('Structure reqeust failled')
            headers = staticUserAgentRotator()
            print('headers changed')
            proxies = proxyRotator()
            print('proxy changed')
            continue
    data = response.json()    
    allPositions = int(data['search_results']['job_count'])
    return allPositions

if __name__== "__main__":
    main()