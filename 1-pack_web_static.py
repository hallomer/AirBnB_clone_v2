#!/usr/bin/python3
"""Generates a tgz archive from the contents of web_static folder."""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Compresses the contents of web_static folder"""
    now = datetime.now()
    file_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    result = local("tar -cvzf versions/{} web_static".format(file_name))
    if result.failed:
        return None
    return "versions/{}".format(file_name)
