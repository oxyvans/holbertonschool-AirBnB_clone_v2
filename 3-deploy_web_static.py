#!/usr/bin/python3
""" task 3 """

from datetime import datetime
from fabric.api import local
from os.path import isdir
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['107.23.23.248', '107.21.59.242']


def do_pack():
    """ tgz """
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        res = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static".format(res))
        return res

    except():
        return None


def do_deploy(archive_path):
    """ distribute files """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except():
        return False


def deploy():
    """ deploys """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
