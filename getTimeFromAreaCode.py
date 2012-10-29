#!/usr/bin/python
#
# As single area code can be used across multiple timezones there
# is no guarantee that the time of a location can be determined
# from an area code, moreover, the map of area codes to timezones
# has not been thoroughly validated and may contain bogus entries.
# 

import sys
import os
import datetime
import pytz

# Sources:
#  NANPA - http://www.nanpa.com/area_code_maps/ac_map_static.html
#  CNA - http://www.cnac.ca/npa_codes/npa_map.htm

area_codes = {'201': 'US/Eastern',
              '202': 'US/Eastern',
              '203': 'US/Eastern',
              '204': 'Canada/Central',
              '205': 'US/Central',
              '206': 'US/Pacific',
              '207': 'US/Eastern',
              '208': 'US/Mountain',
              '209': 'US/Pacific',
              '210': 'US/Central',
              '212': 'US/Eastern',
              '213': 'US/Pacific',
              '214': 'US/Central',
              '215': 'US/Eastern',
              '216': 'US/Eastern',
              '217': 'US/Central',
              '218': 'US/Central',
              '219': 'US/Eastern',
              '224': 'US/Central',
              '225': 'US/Central',
              '226': 'Canada/Eastern',
              '227': 'US/Eastern',
              '228': 'US/Central',
              '229': 'US/Eastern',
              '231': 'US/Eastern',
              '234': 'US/Eastern',
              '236': 'Canada/Pacific',
              '239': 'US/Eastern',
              '240': 'US/Eastern',
              '242': 'US/Eastern',
              '246': 'CET',
              '248': 'US/Eastern',
              '249': 'Canada/Eastern',
              '250': 'Canada/Pacific',
              '251': 'US/Central',
              '252': 'US/Eastern',
              '253': 'US/Pacific',
              '254': 'US/Central',
              '256': 'US/Central',
              '260': 'US/Eastern',
              '262': 'US/Central',
              '264': 'CET',
              '267': 'US/Eastern',
              '268': 'CET',
              '269': 'US/Eastern',
              '270': 'US/Eastern',
              '272': 'US/Eastern',
              '274': 'US/Central',
              '276': 'US/Eastern',
              '281': 'US/Central',
              '283': 'US/Eastern',
              '284': 'CET',
              '289': 'Canada/Eastern',
              '301': 'US/Eastern',
              '302': 'US/Eastern',
              '303': 'US/Mountain',
              '304': 'US/Eastern',
              '305': 'US/Eastern',
              '306': 'Canada/Central',
              '307': 'US/Mountain',
              '308': 'US/Central',
              '309': 'US/Central',
              '310': 'US/Pacific',
              '312': 'US/Central',
              '313': 'US/Eastern',
              '314': 'US/Central',
              '315': 'US/Eastern',
              '316': 'US/Central',
              '317': 'US/Eastern',
              '318': 'US/Central',
              '319': 'US/Central',
              '320': 'US/Central',
              '321': 'US/Eastern',
              '323': 'US/Pacific',
              '325': 'US/Central',
              '327': 'US/Central',
              '330': 'US/Eastern',
              '331': 'US/Central',
              '334': 'US/Central',
              '336': 'US/Eastern',
              '337': 'US/Central',
              '339': 'US/Eastern',
              '340': 'CET',
              '343': 'Canada/Eastern',
              '345': 'US/Eastern',
              '347': 'US/Eastern',
              '351': 'US/Eastern',
              '352': 'US/Eastern',
              '360': 'US/Pacific',
              '361': 'US/Central',
              '365': 'Canada/Eastern',
              '380': 'US/Eastern',
              '385': 'US/Mountain',
              '386': 'US/Eastern',
              '401': 'US/Eastern',
              '402': 'US/Central',
              '403': 'Canada/Mountain',
              '404': 'US/Eastern',
              '405': 'US/Central',
              '406': 'US/Mountain',
              '407': 'US/Eastern',
              '408': 'US/Pacific',
              '409': 'US/Central',
              '410': 'US/Eastern',
              '412': 'US/Eastern',
              '413': 'US/Eastern',
              '414': 'US/Central',
              '415': 'US/Pacific',
              '416': 'Canada/Eastern',
              '417': 'US/Central',
              '418': 'Canada/Eastern',
              '419': 'US/Eastern',
              '423': 'US/Eastern',
              '424': 'US/Pacific',
              '425': 'US/Pacific',
              '430': 'US/Central',
              '431': 'Canada/Central',
              '432': 'US/Central',
              '434': 'US/Eastern',
              '435': 'US/Mountain',
              '437': 'Canada/Eastern',
              '438': 'Canada/Eastern',
              '440': 'US/Eastern',
              '441': 'CET',
              '442': 'US/Pacific',
              '443': 'US/Eastern',
              '447': 'US/Central',
              '450': 'Canada/Eastern',
              '458': 'US/Mountain',
              '464': 'US/Central',
              '469': 'US/Central',
              '470': 'US/Eastern',
              '473': 'CET',
              '475': 'US/Eastern',
              '478': 'US/Eastern',
              '479': 'US/Central',
              '480': 'US/Mountain',
              '484': 'US/Eastern',
              '501': 'US/Central',
              '502': 'US/Eastern',
              '503': 'US/Pacific',
              '504': 'US/Central',
              '505': 'US/Mountain',
              '506': 'Canada/Eastern',
              '507': 'US/Central',
              '508': 'US/Eastern',
              '509': 'US/Pacific',
              '510': 'US/Pacific',
              '512': 'US/Central',
              '513': 'US/Eastern',
              '514': 'Canada/Eastern',
              '515': 'US/Central',
              '516': 'US/Eastern',
              '517': 'US/Eastern',
              '518': 'US/Eastern',
              '519': 'Canada/Eastern',
              '520': 'US/Mountain',
              '530': 'US/Pacific',
              '531': 'US/Central',
              '534': 'US/Central',
              '539': 'US/Central',
              '540': 'US/Eastern',
              '541': 'US/Mountain',
              '551': 'US/Eastern',
              '557': 'US/Central',
              '559': 'US/Pacific',
              '561': 'US/Eastern',
              '562': 'US/Pacific',
              '563': 'US/Central',
              '564': 'US/Pacific',
              '567': 'US/Eastern',
              '570': 'US/Eastern',
              '571': 'US/Eastern',
              '573': 'US/Central',
              '574': 'US/Eastern',
              '575': 'US/Mountain',
              '579': 'Canada/Eastern',
              '580': 'US/Central',
              '581': 'Canada/Eastern',
              '585': 'US/Eastern',
              '586': 'US/Eastern',
              '587': 'Canada/Mountain',
              '601': 'US/Central',
              '602': 'US/Mountain',
              '603': 'US/Eastern',
              '604': 'US/Pacific',
              '605': 'US/Central',
              '606': 'US/Eastern',
              '607': 'US/Eastern',
              '608': 'US/Central',
              '609': 'US/Eastern',
              '610': 'US/Eastern',
              '612': 'US/Central',
              '613': 'Canada/Eastern',
              '614': 'US/Eastern',
              '615': 'US/Central',
              '616': 'US/Eastern',
              '617': 'US/Eastern',
              '618': 'US/Central',
              '619': 'US/Pacific',
              '620': 'US/Central',
              '623': 'US/Mountain',
              '626': 'US/Pacific',
              '630': 'US/Central',
              '631': 'US/Eastern',
              '636': 'US/Central',
              '639': 'Canada/Central',
              '641': 'US/Central',
              '646': 'US/Eastern',
              '647': 'Canada/Eastern',
              '649': 'US/Eastern',
              '650': 'US/Pacific',
              '651': 'US/Central',
              '657': 'US/Pacific',
              '659': 'US/Central',
              '660': 'US/Central',
              '661': 'US/Pacific',
              '662': 'US/Central',
              '664': 'Etc/GMT+4',
              '667': 'US/Eastern',
              '669': 'US/Pacific',
              '678': 'US/Eastern',
              '679': 'US/Eastern',
              '681': 'US/Eastern',
              '682': 'US/Central',
              '689': 'US/Eastern',
              '701': 'US/Central',
              '702': 'US/Pacific',
              '703': 'US/Eastern',
              '704': 'US/Eastern',
              '705': 'Canada/Eastern',
              '706': 'US/Eastern',
              '707': 'US/Pacific',
              '708': 'US/Central',
              '709': 'Canada/Newfoundland',
              '712': 'US/Central',
              '713': 'US/Central',
              '714': 'US/Pacific',
              '715': 'US/Central',
              '716': 'US/Eastern',
              '717': 'US/Eastern',
              '718': 'US/Eastern',
              '719': 'US/Mountain',
              '720': 'US/Mountain',
              '721': 'CET',
              '724': 'US/Eastern',
              '727': 'US/Eastern',
              '730': 'US/Central',
              '731': 'US/Central',
              '732': 'US/Eastern',
              '734': 'US/Eastern',
              '737': 'US/Central',
              '740': 'US/Eastern',
              '747': 'US/Pacific',
              '754': 'US/Eastern',
              '757': 'US/Eastern',
              '758': 'CET',
              '760': 'US/Pacific',
              '762': 'US/Eastern',
              '763': 'US/Central',
              '765': 'US/Eastern',
              '767': 'CET',
              '769': 'US/Central',
              '770': 'US/Eastern',
              '772': 'US/Eastern',
              '773': 'US/Central',
              '774': 'US/Eastern',
              '775': 'US/Pacific',
              '778': 'Canada/Pacific',
              '779': 'US/Central',
              '780': 'Canada/Mountain',
              '781': 'US/Eastern',
              '782': 'CET',
              '784': 'CET',
              '785': 'US/Central',
              '786': 'US/Eastern',
              '787': 'CET',
              '801': 'US/Mountain',
              '802': 'US/Eastern',
              '803': 'US/Eastern',
              '804': 'US/Eastern',
              '805': 'US/Pacific',
              '806': 'US/Central',
              '807': 'Canada/Eastern',
              '808': 'US/Hawaii',
              '809': 'US/Eastern',
              '810': 'US/Eastern',
              '812': 'US/Eastern',
              '813': 'US/Eastern',
              '814': 'US/Eastern',
              '815': 'US/Central',
              '816': 'US/Central',
              '817': 'US/Central',
              '818': 'US/Pacific',
              '819': 'Canada/Eastern',
              '828': 'US/Eastern',
              '829': 'US/Eastern',
              '830': 'US/Central',
              '831': 'US/Pacific',
              '832': 'US/Central',
              '843': 'US/Eastern',
              '845': 'US/Eastern',
              '847': 'US/Central',
              '848': 'US/Eastern',
              '849': 'US/Eastern',
              '850': 'US/Eastern',
              '856': 'US/Eastern',
              '857': 'US/Eastern',
              '858': 'US/Pacific',
              '859': 'US/Eastern',
              '860': 'US/Eastern',
              '862': 'US/Eastern',
              '863': 'US/Eastern',
              '864': 'Canada/Yukon',
              '865': 'US/Eastern',
              '867': 'CST6CDT',
              '868': 'CET',
              '869': 'CET',
              '870': 'US/Central',
              '872': 'US/Central',
              '873': 'Canada/Eastern',
              '876': 'US/Eastern',
              '878': 'US/Eastern',
              '901': 'US/Central',
              '902': 'Canada/Newfoundland',
              '903': 'US/Central',
              '904': 'US/Eastern',
              '905': 'Canada/Eastern',
              '906': 'US/Eastern',
              '907': 'US/Alaska',
              '908': 'US/Eastern',
              '909': 'US/Pacific',
              '910': 'US/Eastern',
              '912': 'US/Eastern',
              '913': 'US/Central',
              '914': 'US/Eastern',
              '915': 'US/Central',
              '916': 'US/Pacific',
              '917': 'US/Eastern',
              '918': 'US/Central',
              '919': 'US/Eastern',
              '920': 'US/Central',
              '925': 'US/Pacific',
              '928': 'US/Mountain',
              '929': 'US/Eastern',
              '931': 'US/Eastern',
              '936': 'US/Central',
              '937': 'US/Eastern',
              '938': 'US/Central',
              '939': 'CET',
              '940': 'US/Central',
              '941': 'US/Eastern',
              '947': 'US/Eastern',
              '949': 'US/Pacific',
              '951': 'US/Pacific',
              '952': 'US/Central',
              '954': 'US/Eastern',
              '956': 'US/Central',
              '959': 'US/Eastern',
              '970': 'US/Mountain',
              '971': 'US/Pacific',
              '972': 'US/Central',
              '973': 'US/Eastern',
              '975': 'US/Central',
              '978': 'US/Eastern',
              '979': 'US/Central',
              '980': 'US/Eastern',
              '984': 'US/Eastern',
              '985': 'US/Central',
              '989': 'US/Eastern',
              }

def getTimeFromAreaCode(areacode):
    zone = area_codes[areacode]
    tz = pytz.timezone(zone)
    zone_time = datetime.datetime.now(tz)
    return zone_time

def main(args):
    if len(args) != 2:
        print "Usage: %s <area code>" % os.path.basename(sys.argv[0])
        sys.exit(1)

    area_code = args[1]
    if not area_code in area_codes:
        print "Could not find timezone for area code `%s'" % area_code
        sys.exit(1)

    print getTimeFromAreaCode(area_code).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print "User interrupted."
        sys.exit(1)
