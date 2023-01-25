import requests
api_key='AIzaSyBhF2HAdlN-cd3mWot8agM7AYzgHL6OpoQ'
test_url='https://developers.google.com'
api_url=f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={test_url}&key={api_key}'
respond=requests.get(api_url)
if respond.status_code==200:
    print(respond.json())
    # cls_score=data.get('cls_score')
    # print(cls_score)
  