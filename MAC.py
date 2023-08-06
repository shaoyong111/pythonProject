#!/usr/bin/python3
# _*_ coding=utf-8 _*_
# From CarlarShao


if __name__ == '__main__':
    pass
# Eth10/33             10.159.255.125  protocol-up/link-up/admin-up
# pattern = r'^[A-Z][a-z]+\S+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\S+/\S+/\S+'

import re
# re.match('cmd.exe','cmd.exe')
# re.match('cmd.exe','cmdaexe')
# re.match('cmd.exe','cmd1exe')
# re.match('cmd\.exe','cmd1exe')
# show_if='Eth10/33             10.159.255.125  protocol-up/link-up/admin-up'
show_if1='Eth10/33             10.159.255.125  YES unset up                    up'
# re_result=re.match('^([A-Z][a-z]+\S+\d)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+(\S+/\S+/\S+)',show_if).group()
# re_result1=re.match('^([A-Za-z]+\d)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+YES unset\s+\w+\s+(\w+)$',show_if1).groups()
# re_result1=re.match('^([A-Za-z]+\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+YES DHCP\s+(\w+)\s+(\w+)$',show_if1).groups()
re_result1=re.match('^([A-Z]\S+\d)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+YES unset\s+\w+\s+(\w+)$',show_if1).groups()
# print(re_result)
print(re_result1)
if_name=re_result1[0]
if_inter=re_result1[1]
if_status=re_result1[2]
print(f'Interface Name: {if_name:<20} IP Address: {if_inter:<20} State: {if_status:<20}')