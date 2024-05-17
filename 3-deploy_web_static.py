#!/usr/bin/python3
"""Creates and distributes an archive to your web servers,
using the function deploy."""
from fabric.api import env, local, put, run
from datetime import datetime
import os


env.hosts = ['100.25.197.112', '34.224.4.126']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """Compresses the contents of web_static folder"""
    now = datetime.now()
    file_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    result = local("tar -cvzf versions/{} web_static".format(file_name))
    if result.failed:
        return None
    return "versions/{}".format(file_name)


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


def deploy():
    """Performs a full deployment."""
    global archive_path
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
