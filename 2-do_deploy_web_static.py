#!/usr/bin/python3
"""Distributes an archive to web servers,
using the function do_deploy."""
from fabric.api import env, put, run
import os


env.hosts = ['100.25.197.112', '34.224.4.126']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Deploys the web static files to the web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        # Extract the archive to the appropriate folder
        archive_filename = os.path.basename(archive_path)
        archive_name = os.path.splitext(archive_filename)[0]
        release_path = '/data/web_static/releases/{}/'.format(archive_name)
        run('sudo mkdir -p {}'.format(release_path))
        run('sudo tar -xzf /tmp/{} -C {}'.format(
            archive_filename, release_path))

        # Delete the temporary archive
        run('sudo rm /tmp/{}'.format(archive_filename))

        # Move the contents of the extracted folder to the web server's folder
        run('sudo mv {}web_static/* {}'.format(release_path, release_path))

        # Remove the empty web_static folder
        run('sudo rm -rf {}web_static'.format(release_path))

        # Update the symbolic link
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(release_path))

        print('New version deployed!')
        return True
    except Exception as excep:
        return False
