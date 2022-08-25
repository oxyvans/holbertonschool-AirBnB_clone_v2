#!/usr/bin/python3
""" Write a Fabric script """

from datetime import datetime
from fabric.api import local
from os.path import isdir


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
