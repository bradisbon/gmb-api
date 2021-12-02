import typing

from gmb_api import schema
from gmb_api.auth import Session


def get_accounts(session:Session) -> typing.List[schema.Account]:
    r = session.get('https://mybusinessaccountmanagement.googleapis.com/v1/accounts')
    r.raise_for_status()

    return [schema.Account(**a) for a in r.json()['accounts']]


def get_locations(account_name:str,session:Session) -> typing.List[schema.Location]:
    page_r = session.get(f'https://mybusiness.googleapis.com/v4/{account_name}/locations')
    page_j = page_r.json()
    page_r.raise_for_status()

    page = schema.Locations(**page_r.json())
    locations = page.locations
    while page.next_page_token:
        page_r = session.get(
            f'https://mybusiness.googleapis.com/v4/{account_name}/locations',
            params={'pageToken':page.next_page_token})
        page_r.raise_for_status()
        page = schema.Locations(**page_r.json())
        locations.extend(page.locations)
    return locations
