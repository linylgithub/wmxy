#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: replace_link.py
@time: 2018/8/31 16:17
"""

import xlrd
import os

def get_intern_link(path):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    intern_dict = {}
    for i in range(nrows):
        intern_dict[table.cell(i,1).value] = table.cell(i,4).value.replace('\n\n','')
    return intern_dict

def crate_html(old_html,new_html,intren_dict):
    with open(old_html,'rb') as f:
        all_lines =f.readlines()
    with open(new_html,'ab') as c:
        for line in all_lines:
            if 'www.shixiseng.com/intern/' in line:
                key_uuid = line.split('/')[4].split('"')[0]
                line = """                                    <a href="{0}" class="clearfix">""".format(intern_dict[key_uuid])
                c.write(line)
            else:
                c.write(line)
if __name__ == '__main__':
    intern_dict = get_intern_link('shixiseng_job-0917.xls')
    o_path = 'sc_ycsx.html'
    n_path = 'new_sc_ycsx.html'
    crate_html(o_path,n_path,intern_dict)
