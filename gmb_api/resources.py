import typing
from gmb_api.auth import Session


def get_accounts(session:Session) -> typing.List[dict]:
    return session.get('https://mybusinessaccountmanagement.googleapis.com/v1/accounts').json()['accounts']


def get_locations(account_name:str,session:Session) -> typing.List[dict]:
    first_locs = session.get(f'https://mybusiness.googleapis.com/v4/{account_name}/locations').json()
    locations = []
    locations.extend(first_locs['locations'])
    page_token = first_locs.get('nextPageToken')
    while page_token:
        page = session.get(
            f'https://mybusiness.googleapis.com/v4/{account_name}/locations',
            params={'pageToken':page_token}).json()
        locations.extend(page['locations'])
        page_token = page.get('nextPageToken')
    return locations
