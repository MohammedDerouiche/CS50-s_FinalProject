
locations = {'South East Englasd':[{"86465":"Kent"},{"86437":"Hampshire"},{"86463":"Surrey"},{"86395":"Buckinghamshire"},{"86466":"East Sussex"},{"86411":"Oxfordshire"},{"86434":"West Sussex"},{"86464":"Berkshire"},{"86476":"West Berkshire"},{"86469":"Isle Of Wight"},{"86447":"Windsor & Maidenhead"}],
            'North West Englasd':[{"86397":"Greater Manchester"},{"86415":"Lancashire"},{"86419":"Merseyside"},{"86452":"Cheshire"},{"86417":"Cumbria"}],
            'London':[{"86510":"South West London"},{"86583":"South East London"},{"86592":"East London"},{"86588":"North West London"},{"86585":"North London"},{"86590":"Central London"},{"86602":"Harrow"},{"86591":"Uxbridge"},{"86608":"Sutton"},{"86600":"Enfield"},{"86594":"Orpington"},{"86597":"Croydon"},{"86589":"Hounslow"},{"86596":"Mitcham"},{"86601":"Surbiton"},{"86604":"Twickenham"},{"86595":"West Drayton"},{"86607":"Pinner"},{"86599":"Wallington"},{"86603":"Greenford"},{"86606":"Hayes"},{"86598":"Ruislip"},{"86605":"Feltham"},{"67725":"Coulsdon"}],
            'South West England':[{"56201":"Bristol"},{"86409":"Devon"},{"86459":"Wiltshire"},{"86404":"Dorset"},{"86406":"Gloucestershire"},{"86448":"Somerset"},{"86456":"Cornwall"},{"77819":"Plymouth"},{"86393":"Bath & N E Somerset"},{"86440":"North Somerset"},{"86430":"Isles of Scilly"}],
            'Eastern England':[{"86458":"Essex"},{"86414":"Hertfordshire"},{"86455":"Norfolk"},{"86472":"Suffolk"},{"86420":"Cambridgeshire"},{"86413":"Bedfordshire"},{"77712":"Peterborough"}],
            'West Midlands':[{"83620":"Birmingham"},{"86416":"Staffordshire"},{"86446":"Shropshire"},{"86435":"Worcestershire"},{"83714":"Warwickshire"},{"":"Wolverhampton"},{"83714":"Coventry"},{"86454":"Herefordshire"},{"83849":"Walsall"},{"83787":"Solihull"},{"83826":"Sutton"},{"83759":"Dudley"},{"83871":"West Bromwich"},{"83780":"Oldbury"},{"83807":"Stourbridge"},{"83868":"Wednesbury"},{"83844":"Tipton"},{"83709":"Brierley Hill"},{"83769":"Halesowen"},{"83784":"Smethwick"},{"83877":"Willenhall"},{"83615":"Bilston"},{"83776":"Kingswinford"},{"83782":"Rowley Regis"}],
            'Yorkshire And The Humber':[{"86390":"West Yorkshire"},{"86391":"South Yorkshire"},{"86403":"North Yorkshire"},{"86398":"East Riding"},{"86418":"North East Lincolnshire"},{"86387":"North Lincolnshire"}],
            'East Midlands':[{"86547":"Nottinghamshire"},{"86421":"Derbyshire"},{"86402":"Leicestershire"},{"86412":"Northamptonshire"},{"86449":"Lincolnshire"},{"86577":"Rutland"},{"86615":"Northants"}],
            'Scotland':[{"86470":"Glasgow"},{"86566":"Edinburgh"},{"86433":"Aberdeenshire"},{"86494":"Highlands"},{"86485":"Midlothian"},{"86477":"North Lanarkshire"},{"86493":"Fife"},{"86468":"South Lanarkshire"},{"86487":"West Lothian"},{"86496":"Perth & Kinross"},{"62895":"Dundee"},{"86552":"Falkirk County"},{"86480":"Renfrewshire"},{"86498":"Argyll & Bute"},{"86535":"East Lothian"},{"86515":"County Stirling"},{"86471":"South Ayrshire"},{"86542":"Moray"},{"86479":"Dumfries & Galloway"},{"86467":"North Ayrshire"},{"86492":"East Ayrshire"},{"86497":"Borders"},{"192065":"East Dunbartonshire"},{"192064":"East Renfrewshire"},{"86560":"Angus"},{"86518":"Inverclyde"},{"86462":"West Dunbartonshire"},{"86563":"Shetland Islands"},{"86556":"Orkney Islands"},{"86483":"Western Isles"},{"86545":"Clackmannanshire"}],
            'Wales':[{"86500":"Cardiff County"},{"82564":"Swansea"},{"86551":"Powys"},{"86481":"Rhondda Cynon Taff"},{"86444":"Carmarthenshire"},{"86491":"Bridgend County"},{"73474":"Newport"},{"86280":"Wrexham"},{"86533":"Denbighshire"},{"86524":"Gwynedd"},{"86509":"Flintshire"},{"86508":"Neath Port Talbot"},{"86506":"Pembrokeshire"},{"86544":"Ceredigion"},{"86450":"The Vale of Glamorgan"},{"86522":"Conwy County"},{"86439":"Monmouthshire"},{"86475":"Caerphilly County"},{"86495":"Torfaen"},{"86558":"Merthyr Tydfil County"},{"86532":"Blaenau Gwent"},{"82693":"Swansea Enterprise Park"},{"86519":"Isle Of Anglesey"},{"82694":"Swansea Vale"}],
            'North East England':[{"86389":"Tyne & Wear"},{"86405":"County Durham"},{"86410":"Northumberland"}],
            'Northern Ireland':[{"55926":"Belfast"},{"86549":"County Antrim"},{"86575":"Derry"},{"86534":"County Down"},{"72912":"Lisburn"},{"59483":"Craigavon"},{"86474":"Newry & Mourne"},{"86567":"North Down"},{"86424":"Fermanagh"},{"86546":"County Tyrone"},{"76676":"Omagh"},{"86550":"Ards"},{"56460":"Carrickfergus"},{"58193":"Coleraine"},{"55554":"Ballymena"},{"55531":"Armagh"},{"71699":"Larne"},{"58294":"Cookstown"},{"72927":"Magherafelt"},{"81749":"Strabane"},{"55599":"Ballymoney"},{"72032":"Limavady"}],
            'Channel Islands':[{"86570":"Jersey"},{"86530":"Guernsey"}],
            'Isle Of Man':[{"70503":"Douglas"}],
            }

import requests
from bs4 import BeautifulSoup
session = requests.Session()
locations = {}
url = "https://findajob.dwp.gov.uk/search?loc=86383"
while True:
    try:
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        break
    except:
        continue
statesTags = soup.find_all('li', class_="i2 na")
for stateTag in statesTags:
    stateTag = stateTag.find('a')
    stateName = stateTag.text
    stateHref = stateTag['href']
    stateId = stateHref.split("=")[-1]
    print(stateName)
    print(stateHref)
    print(stateId)
    locations[stateName] = []
    while True:
        try:
            response = session.get(stateHref)
            soup = BeautifulSoup(response.text,'html.parser')
            break
        except:
            continue
    citiesTags = soup.find_all('li', class_='i3 na')
    for citytag in citiesTags:
        cityTag = citytag.find('a')
        cityName = cityTag.text
        cityHref = cityTag['href']
        cityId = cityHref.split("=")[-1]
        print('\t',cityName)
        print('\t',cityHref)
        print('\t',cityId)
        cityDict = {cityId:cityName}
        locations[stateName].append(cityDict)

print(locations)