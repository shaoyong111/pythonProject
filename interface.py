import re

show_if1='Eth10/33             10.159.255.125  YES unset up                    up'
# re.match('^[A-Z]\S+\d',show_if1).groups()
# re.match('^[A-Z]\S+\d\s+\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+YES unset\s+\w+\s+\w+$',show_if1)
re.match('^([A-Z]\S+\d)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+YES unset\s+\w+\s+(\w+)$',show_if1).groups()
# re.match('^.*$',show_if1)