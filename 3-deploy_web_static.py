#!/usr/bin/python3
'''Fabric script to pack web_static contents and upload to remote server'''
from fabric.api import *
from datetime import datetime
import os
import re

env.hosts = ['18.232.152.253', '34.207.245.172']
env.user = 'ubuntu'


def do_pack():
    '''Create a compress file'''
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        local('mkdir -p versions')
        filename = 'versions/web_static_' + time + '.tgz'
        local('tar -cvzf {} web_static'.format(filename))
        print('web_static packed: {}'.format(filename))
        return filename
    except:
        return None


def do_deploy(archive_path):
    '''Deploy file to server'''
    if os.path.exists(archive_path) is False:
        return False
    parse_path = re.split('[/.]', archive_path)
    filename = parse_path[1]
    try:
        put(archive_path, '/tmp/')
        run('sudo mkdir -p /data/web_static/releases/{}'.format(filename))
        run('sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'.
            format(filename, filename))
        run('sudo rm /tmp/{}.tgz'.format(filename))
        run('sudo rm /data/web_static/current')
        run('sudo ln -sf /data/web_static/releases/{}/web_static\
            /data/web_static/current'
            .format(filename))
        return True
    except:
        return False


def deploy():
    '''Use do_pack and do_deploy to delopy static site'''
    path = do_pack()
    try:
        result = do_deploy(path)
        return result
    except:
        return False
