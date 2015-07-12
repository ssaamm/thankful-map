import json
import requests

def get_lat_lon(ip):
    print('getting lat lon')
    r = requests.get('http://ipinfo.io/{ip}/geo'.format(ip=ip))
    print('got lat lon')
    ipinfo = json.loads(r.text)
    try:
        lat = ipinfo['loc'].split()[0]
        lon = ipinfo['loc'].split()[1]
    except KeyError:
        lat = 31.5514
        lon = -97.1558
    return (lat, lon)
