import requests

url = 'http://users.bugred.ru/tasks/rest/doregister'
myobj = {'email': 'restpython2@gmail.com',
          'name':'NameName2',
         'password':'pass'}

x = requests.post(url, data = myobj)
assert x.status_code==200





