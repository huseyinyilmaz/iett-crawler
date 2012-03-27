import requests
import bs4
import os
from itertools import count
import json
from collections import OrderedDict

XML_FILES_DIRECTORY = 'XML'

BUS_LIST_URL = 'http://harita.iett.gov.tr/'
# alternatively following could be found
# 'http://www.iett.gov.tr/ajaxh_kodu.php?getCountriesByLetters=1&letters='

BUSSTOP_LIST_URL = \
    os.path.join(XML_FILES_DIRECTORY, "%shatDurak.xml")

busstop_id_generator = count()

# global busstop dict
BUSSTOP_DICT = OrderedDict()

ERRORS = list()


def get_busstop_list(bus):
    """
    Get busstop list for given bus.
    """
    no = bus['code'].lower()
    bs = bs4.BeautifulSoup(open(BUSSTOP_LIST_URL % no))
    result = []
    for item in bs.findAll('item'):
        lng = item.find('geo:long').text
        lat = item.find('geo:lat').text
        item_key = (lng, lat)
        if item_key in BUSSTOP_DICT:
            # busstop on this location already entered.
            # use existing one
            busstop = BUSSTOP_DICT[item_key]
        else:
            busstop = {
                'id': next(busstop_id_generator),
                'long': item.find('geo:long').text,
                'lat': item.find('geo:lat').text,
                }
            BUSSTOP_DICT[item_key] = busstop

        result.append({
            'title': item.title.text,
            'descrition': item.description.text,
            'location_id': busstop['id']})

    return result


def get_bus_iter():
    """
    Return iterator for bus list
    """
    res = requests.post(BUS_LIST_URL)
    # result of the function
    if res.ok:
        bs = bs4.BeautifulSoup(res.text)
        for op in bs.find(id='hat').findAll('option'):
            code = op.get('value')
            if code == '0':
                continue
            no, route = op.text.split(' - ', 1)

            bus = {'code': code,
                   'no': no,
                   'route': route}
            try:
                bus['busstops'] = get_busstop_list(bus)
            except IOError:
                ERRORS.append({
                        'code': bus['code'],
                        'error': 'Could not find busstop information file'})
                continue

            # if there is no busstops for this bus
            # do not return it
            if len(bus['busstops']) > 0:
                yield bus
            else:
                ERRORS.append({
                        'code': bus['code'],
                        'error': 'There was no busstop found in \
busstop information file'})


def pull_data():
    result = {'buses': list(get_bus_iter()),
              'locations': list(BUSSTOP_DICT.values()),
              'errors': ERRORS}

    print(json.dumps(result))

if __name__ == '__main__':
    pull_data()
