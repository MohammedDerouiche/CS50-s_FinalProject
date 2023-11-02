import requests
from bs4 import BeautifulSoup
import time

# proxies = []
# for page in range(1, 6):
#     response = requests.get(f"http://free-proxy.cz/en/proxylist/country/all/https/ping/all/{page}")
#     soup = BeautifulSoup(response, 'html.parser')
    

# List of proxy IP addresses and ports]
proxies= [
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
    "67.43.228.251:18181"
]
def test_proxy(proxy):
    try:
        start_time = time.time()
        response = requests.get('https://www.example.com', proxies={'http': proxy, 'https': proxy}, timeout=10)
        response_time = time.time() - start_time
        if response.status_code == 200:
            return True, response_time
    except requests.exceptions.RequestException:
        pass
    return False, None

def main():
    for proxy in proxies:
        is_working, response_time = test_proxy(proxy)
        if is_working:
            print(f"Proxy {proxy} is working. Response time: {response_time:.2f} seconds.")
        else:
            print(f"Proxy {proxy} is not working.")

if __name__ == "__main__":
    main()
