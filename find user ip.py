# import requests
# api_url='https://api.ipify.org/?format=json'
# res=requests.get(api_url)
# print(res.json())
# import requests
# api_url='https://api.ipify.org/?format=json'
# response=requests.get(api_url)
# print(response.json())
# import requests
# api_url='https://api.ipify.org/?format=json'
# r=requests.get(api_url)
# print(r.json())
# import requests
# api_url='https://api.ipify.org/?format=json'
# response=requests.get(api_url)
# if response.status_code==200:
#     data=response.json()
#     ip=data.get('ip')
#     print('your ip address',ip)
# import requests
# api_url='https://api.ipify.org/?format=json'
# r=requests.get(api_url)
# if r.status_code==200:
#     data=r.json()
#     ip=data.get('ip')
#     print('Your ip address is',ip)
# import requests
# api_url='https://api.ipify.org/?format=json'
# rspoinse=requests.get(api_url)
# if rspoinse.status_code==200:
#     data=rspoinse.json()
#     ip=data.get('ip')
#     print('your if address',ip)
#     # print(rspoinse.json())
# import requests
# api_url='https://api.ipify.org/?format=json'
# rest=requests.get(api_url)
# if rest.status_code==200:
#     data=rest.json()
#     ip=data.get('ip')
#     print('your ip address is',ip)
# # print(rest.json())
# import requests
# api_url='https://api.ipify.org/?format=json'
# rest=requests.get(api_url)
# if rest.status_code==200:
#     data=rest.json()
#     ip=data.get('ip')
#     print('You ip Address is ',ip)
# print(rest.json())
# import requests
# response=requests.get('https://jsonplaceholder.typicode.com/posts')
# print(response)
# print(response.json())
# import requests
# api_url='https://api.ipify.org/?format=json'
# rest=requests.get(api_url)
# if rest.status_code==200:
#     data=rest.json()
#     ip=data.get('ip')
#     print('your ip address',ip)
# # print(rest.json())
# import requests
# api_url='https://api.ipify.org/?format=json'
# rest=requests.get(api_url)
# if rest.status_code==200:
#     data=rest.json()
#     ip=data.get('ip')
#     print('your ip address',ip)
# # print(rest.json)
import requests
api_url='https://api.ipify.org/?format=json'
rest=requests.get(api_url)
if rest.status_code==200:
    data=rest.json()
    ip=data.get('ip')
    print(ip)

# print(rest.json())