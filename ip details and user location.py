# import requests
# api_url='https://api.ipify.org/?format=json'
# response=requests.get(api_url)
# if response.status_code==200:
#     data=response.json()
#     ip=data.get('ip')
# ip_location_url=f'https://ipapi.co/{ip}/json/'
# res=requests.get(ip_location_url)
# if res.status_code==200:
#     ip_details=res.json()
#     city=ip_details.get('city')
#     region=ip_details.get('region')
#     country_name=ip_details.get('country name')
# sentence=f'ip {ip} is located in {city} {region} {country_name}'
# print(sentence)
# import requests
# api_url='https://api.ipify.org?format=json'
# response=requests.get(api_url)
# if response.status_code==200:
#     data=response.json()
#     ip=data.get('ip')
# ip_location=f'https://ipapi.co/{ip}/json/'
# res=requests.get(ip_location)
# if res.status_code==200:
#     ip_details=res.json()
#     city=ip_details.get('city')
#     region=ip_details.get('region')
#     country=ip_details.get('country')
# sen=f'this ip {ip} {city} {region} {country} is located'
# print(sen)
# import requests
# api_url=('https://api.ipify.org?format=json')
# rest=requests.get(api_url)
# if rest.status_code==200:
#     data=rest.json()
#     ip=data.get('ip')
#     # print(ip)
# ip_location=f'https://ipapi.co/{ip}/json/'
# respond=requests.get(ip_location)
# if respond.status_code==200:
#     print(respond.json())