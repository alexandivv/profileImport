import requests
from auxiliary import Auxiliary
from config import *


class Dolphin:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.token = ''

    def getToken(self):
        headers = {
            'Authorization': 'Bearer null',
        }
        jsonData = {
            'username': f'{self.email}',
            'password': f'{self.password}'
        }

        response = requests.post('https://anty-api.com/auth/login',
            headers=headers, json=jsonData)

        self.token = response.json().get('token')

        return self.token


    def getProfiles(self):
        self.token = self.getToken()
        headers = {
            'Authorization': f'Bearer {self.token}',
        }
        url = 'https://anty-api.com/browser_profiles'
        response = requests.get(
            url, headers=headers)

        listProfiles = response.json().get('data')
        return listProfiles
        

    def getProfileInfo(self, profileId):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        url = f'https://anty-api.com/browser_profiles/{profileId}'
        response = requests.get(
            url, headers=headers)
           
        result = response.json()

        return {
            'name': result['data']['name'],
            'tags': Auxiliary(result).getTags(),
            'os': Auxiliary(result).getOs(),
            'useragent': result['data']['useragent']['value'],
            'webrtc': Auxiliary(result).getWebrtc(),
            'canvas': Auxiliary(result).getCanvas(),
            'webgl':  Auxiliary(result).getWebgl(),
            'webGLInfo': Auxiliary(result).getWebGLInfo(),
            'clientRect': Auxiliary(result).getClientRect(),
            'proxy': Auxiliary(result).getProxy(),
            'cpu': result['data']['cpu']['value'],
            'memory': result['data']['memory']['value']
        }


class GoLogin:
    def __init__(self, token):
        self.token = token

    def createProfile(self, data):
        headers = {
            'Authorization': f'Bearer {self.token}',
            'User-Agent': 'Selenium-API'
        }

        os = data['os']
        url = f'https://api.gologin.com/browser/fingerprint?os={os}'
        response = requests.get(
            url, headers=headers)
           
        fingerprint = response.json()

        jsonData = {
            'name': data['name'],
            'browserType': 'chrome',
            'os': os,
            'navigator': {
                'userAgent': data['useragent'],
                'resolution': fingerprint['navigator']['resolution'],
                'language': fingerprint['navigator']['language'],
                'platform': fingerprint['navigator']['platform'],
                'hardwareConcurrency': data['cpu'],
                'deviceMemory': data['memory']
            },
            'proxy': data['proxy'],
            'canvas': {
                'mode': data['canvas']
            },
            'fonts': {
                'families': fingerprint['fonts'],
                'enableMasking': True,
                'enableDomRect': True
            },
            'mediaDevices': fingerprint['mediaDevices'],
            'webRTC': {
                'mode': data['webrtc']
            },
            'webGL': {
                'mode': data['webgl']
            },
            'webGLMetadata': data['webGLInfo']
        }

        url = 'https://api.gologin.com/browser'
        response = requests.post(
            url, headers=headers, json=jsonData)

        profileId = response.json().get('id')
        if data['tags']:
            urlTags = 'https://api.gologin.com/tags/addToProfiles'
            jsonTagsData = {
                "title": data['tags'][0],
                "color": "grey",
                "browserIds": [
                    profileId
                ]
            }

            response = requests.post(
                urlTags, headers=headers, json=jsonTagsData)
            
            return response
        else:
            return response
