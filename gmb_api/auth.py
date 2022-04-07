import json
import os

import requests
from google_auth_oauthlib.flow import InstalledAppFlow


CREDENTIALS_PATH = os.path.expanduser('~/.credentials/gmb_credentials.json')
REFRESH_TOKEN_PATH = os.path.expanduser('~/.credentials/gmb_token_digital.json')


def get_token(credentials_path):
    flow = InstalledAppFlow.from_client_secrets_file(
        credentials_path,
        scopes = [
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/plus.business.manage',
        'https://www.googleapis.com/auth/business.manage',
        'openid'
    ]
    )
    token = flow.run_local_server(port=0)
    return token.to_json()


def refresh_token(refresh_token_path):
    token = json.load(open(refresh_token_path,'r'))
    data = {
        'client_id': token['client_id'],
        'client_secret': token['client_secret'],
        'refresh_token': token['refresh_token'],
        'grant_type': 'refresh_token'}
    r = requests.post('https://www.googleapis.com/oauth2/v4/token',
                        data=json.dumps(data))
    r.raise_for_status()
    return r.json()['access_token']
    
class Session(requests.Session):
    def __init__(self) -> None:
        super().__init__()
        # call raise_for_status on every request
        self.hooks = {
            'response': lambda r, *args, **kwargs: r.raise_for_status()
        }
        self.headers = {'Authorization': f'Bearer {refresh_token(REFRESH_TOKEN_PATH)}'}