import typing

from pydantic import BaseModel, Field
from six import integer_types


class Account(BaseModel):
    name: str
    account_name: str = Field(alias='accountName')
    type: str
    verification_state: str = Field(alias='verificationState')
    vetted_state: str = Field(alias='vettedState')


class ServiceType(BaseModel):
    service_type_id: str = Field(alias='serviceTypeId')
    display_name: str = Field(alias='displayName')


class HoursType(BaseModel):
    hours_type_id: str = Field(alias='hoursTypeId')
    display_name: str = Field(alias='displayName')
    localized_display_name: str = Field(alias='localizedDisplayName')


class PrimaryCategory(BaseModel):
    display_name: str = Field(alias='displayName')
    category_id: str = Field(alias='categoryId')
    service_types: typing.Optional[typing.List[ServiceType]] = Field(alias='serviceTypes')
    more_hours_types: typing.List[HoursType] = Field(alias='moreHoursTypes')


class AdditionalCategory(BaseModel):
    display_name: str = Field(alias='displayName')
    category_id: str = Field(alias='categoryId')
    more_hours_types: typing.List[HoursType] = Field(alias='moreHoursTypes')
    

class TimeOfDay(BaseModel):
    hours: int
    minutes: int
    seconds: int
    nanos: int


class TimePeriod(BaseModel):
    open_day: str = Field(alias='openDay')
    open_time: TimeOfDay = Field(alias='openTime')
    close_day: str = Field(alias='closeDay')
    close_time: TimeOfDay = Field(alias='closeTime')


class BusinessHours(BaseModel):
    periods: typing.List[TimePeriod]


class PlaceInfo(BaseModel):
    name: str
    place_id: str = Field(alias='placeId')


class Places(BaseModel):
    place_infos: typing.List[PlaceInfo] = Field(alias='placeInfos')


class ServiceArea(BaseModel):
    business_type: str = Field(alias='businessType')
    places: Places


class LocationKey(BaseModel):
    place_id: typing.Optional[str] = Field(alias='placeId')
    request_id: typing.Optional[str] = Field(alias='requestId')


class LatLng(BaseModel):
    latitude: float
    longitude: float


class OpenInfo(BaseModel):
    status: str
    can_reopen: bool = Field(alias='canReopen')


class LocationState(BaseModel):
    is_google_updated: typing.Optional[bool] = Field(alias='isGoogleUpdated')
    can_update: bool = Field(alias='canUpdate')
    can_delete: bool = Field(alias='canDelete')
    is_verified: typing.Optional[bool] = Field(alias='isVerified')
    is_published: typing.Optional[bool] = Field(alias='isPublished')
    can_modify_service_list: typing.Optional[bool] = Field(alias='canModifyServiceList')


class URLValue(BaseModel):
    url: str


class Attribute(BaseModel):
    attribute_id: str = Field(alias='attributeId')
    value_type: str = Field(alias='valueType')
    values: typing.Optional[typing.List[bool]]
    url_values: typing.Optional[typing.List[URLValue]] = Field(alias='urlValues')


class Metadata(BaseModel):
    maps_url: typing.Optional[str] = Field(alias='mapsUrl')
    new_review_url: typing.Optional[str] = Field(alias='newReviewUrl')


class Label(BaseModel):
    diplay_name: str = Field(alias='displayName')


class Section(BaseModel):
    section_id: str = Field(alias='sectionId')
    labels: typing.List[Label]


class PriceList(BaseModel):
    price_list_id: str = Field(alias='priceListId')
    labels: typing.List[Label]
    sections: typing.List[Section]


class Address(BaseModel):
    region_code: str = Field(alias='regionCode')
    language_code: typing.Optional[str] = Field(alias='languageCode')
    postal_code: str = Field(alias='postalCode')
    administrative_area: str = Field(alias='administrativeArea')
    locality: str
    address_lines: typing.List[str] = Field(alias='addressLines')
    

class Profile(BaseModel):
    description: str


class Location(BaseModel):
    name: str
    store_code: typing.Optional[str] = Field(alias='storeCode')
    website_uri: str = Field('webiteUri')
    regular_hours: typing.Optional[BusinessHours] = Field(alias='regularHours')
    service_area: typing.Optional[ServiceArea] = Field(alias='serviceArea')
    location_key: LocationKey = Field(alias='locationKey')
    labels: typing.Optional[typing.List[str]]
    lat_lng: typing.Optional[LatLng] = Field(alias='latlng')
    open_info: OpenInfo = Field(alias='openInfo')
    location_state: LocationState = Field(alias='locationState')
    attributes: typing.Optional[typing.List[Attribute]]
    metadata: Metadata
    language_code: str = Field(alias='languageCode')
    price_lists: typing.Optional[typing.List[PriceList]] = Field(alias='priceLists')
    address: typing.Optional[Address]
    profile: typing.Optional[Profile]


class Locations(BaseModel):
    locations: typing.List[Location] = Field(default_factory=list)
    next_page_token: typing.Optional[str] = Field(alias='nextPageToken')
