#!/usr/bin/env python3
'''Fabric script to pack web_static contents and upload to remote server'''
from fabric.api import *
from datetime import datetime


def do_pack():
    '''Create a compress file'''
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        local('mkdir -p versions')
        filename = 'versions/web_static_' + time + '.tgz'
        local('tar -cvzf {} web_static'.format(filename))
        print('web_static packed: {}'.format(filename))
        return 'web_static packed: {}'.format(filename)
    except:
        return None
