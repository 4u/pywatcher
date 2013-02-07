import os
from setuptools import setup
from setuptools.command.develop import develop
from subprocess import check_call

DESCRIPTION = 'Python wrapper for watcher (http://github.com/4u/watcher)'

def install_deps():
    print "Installing dependencies"
    cdir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(cdir)
    check_call(['git', 'submodule', 'update', '--init', '--force'])
    os.chdir(os.path.join(cdir, 'pywatcher/watcher'))
    check_call(['npm', 'install', '.'])
    os.chdir(cdir)

class do_develop(develop):
    def run(self):
        install_deps()
        develop.run(self)


setup(
    cmdclass={'develop': do_develop,},
    name='pywatcher',
    version='0.1.1',
    packages=['pywatcher'],
    package_dir={'pywatcher': '.'},
    package_data={'pywatcher': ['pywatcher/*']},
    author='Max Nikitin',
    author_email='max@rururu.me',
    url='http://github.com/4u/pywatcher',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    platforms='any',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)