# -*- coding: utf-8 -*-

# http://docs.fabfile.org/en/1.5/tutorial.html

from fabric.api import *

project = "biomics"

# the user to use for the remote commands
env.user = 'urushibata'
# the servers where the commands are executed
env.hosts = ['biomics.urushibata.com.br']

def pack():
    # create a new source distribution as tarball
    local('python setup.py sdist --formats=gztar', capture=False)

def reset():
    """
    Reset local debug env.
    """

    local("rm -rf /tmp/instance")
    local("mkdir /tmp/instance")
    # local("python manage.py initdb")


def setup():
    """
    Setup virtual env.
    """

    local("virtualenv env")
    activate_this = "env/bin/activate_this.py"
    execfile(activate_this, dict(__file__=activate_this))
    local("python setup.py install")
    reset()


def deploy():
    # figure out the release name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    # remote folder
    remote_path = '/home/urushibata/webapps/biomics'
    # upload the source tarball to the temporary folder on the server
    put('dist/%s.tar.gz' % dist, '%s/temp/%s.tar.gz' % (remote_path, project))
    # create a place where we can unzip the tarball, then enter
    # that directory and unzip it
    run('mkdir %s/tmp/yourapplication' % remote_path)
    with cd('%s/tmp/yourapplication' % remote_path):
        run('tar xzf %s/tmp/%s.tar.gz' % (remote_path, project))
        # now setup the package with our virtual environment's
        # python interpreter
        run('/var/www/yourapplication/env/bin/python setup.py install')

    run('touch app.wsgi')

def d():
    """
    Debug.
    """

    reset()
    local("python manage.py run")


def babel():
    """
    Babel compile.
    """

    local("python setup.py compile_catalog --directory `find -name translations` --locale br -f")