# import requests
# def res_data(url):
#     res=requests.get(url)
#     if res.status_code==200:
#         data=res.json()
#     return data
# api_url='https://api.ipify.org?format=json'
#  response=requests.get(api_url)
# # if response.status_code==200:
# #     data=response.json()
# data=res_data(api_url)
# ip=data.get('ip')
#     # print(ip)
# ip_url=f'https://ipapi.co/{ip}/json/'
# # r=requests.get(ip_url)
# # if r.status_code==200:
# #     ip_details=r.json()
# ip_details=res_data(ip_url)
# city=ip_details.get('city')
# region=ip_details.get('region')
# country_name=ip_details.get("country_name")
# sent=f'This ip address {ip} is located in {city} {country_name}'
# print(sent)
#     # print(r.json())
# import requests
# def res_data(url):
#     res=requests.get(url)
#     if res.status_code==200:
#         data=res.json()
#     return data
# api_url="https://api.ipify.org?format=json"
# data=res_data(api_url)
# ip=data.get('ip')
# ip_location_url=f'https://ipapi.co/{ip}/json/'
# details=res_data(ip_location_url)
# city=details.get('city')
# country_name=details.get("country_name")
# sentence=f'This ip address {ip} is located in {city} {country_name}'
# print(sentence)
import requests
def res_data(url):
    res=requests.get(url)
    if res.status_code==200:
        data=res.json()
    return data
ulu="https://api.ipify.org?format=json"
store=res_data(ulu)
ip=store.get('ip')
location=f'https://ipapi.co/{ip}/json/'
result=res_data(location)
city=result.get("city")
country_name=result.get("country_name")
sente=f'This ip address {ip} is located {city} in {country_name}'
print(sente)