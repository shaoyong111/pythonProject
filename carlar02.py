# Eth10/33             10.159.255.125  protocol-up/link-up/admin-up
import re

show_if='Eth10/33             10.159.255.125  protocol-up/link-up/admin-up'
# re.match('^.*$',show_if)
# re.match('^[A-Z]\S+\d\s+\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+\S+$',show_if)
# re.match('^([A-Z]\S+\d)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+(\S+)$',show_if).groups()
re_result=re.match('^([A-Z]\S+\d)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+(\S+)/(\S+)/(\S+)$',show_if).groups()
# re.match('^[A-Z]\S+\d\s+\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',show_if)
# print(re_result)
# print(re_result)
if_inter=re_result[0]
if_ip=re_result[1]
if_pro=re_result[2]
if_link=re_result[3]
if_admin=re_result[4]
print(f'Interface:{if_inter:<20} IP Address:{if_ip:<20} link:{if_link:<20}')