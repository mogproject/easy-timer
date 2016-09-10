import sys
from setuptools import setup, find_packages

SRC_DIR = 'src'


def get_version():
    sys.path[:0] = [SRC_DIR]
    return __import__('easy_timer').__version__


setup(
    name='easy-timer',
    version=get_version(),
    description='Super Simple Command-line Countdown Timer',
    author='mogproject',
    author_email='mogproj@gmail.com',
    license='Apache 2.0 License',
    url='https://github.com/mogproject/easy-timer',
    install_requires=[
        'six',
        'mog-commons >= 0.2.0',
    ],
    tests_require=[
    ],
    package_dir={'': SRC_DIR},
    packages=find_packages(SRC_DIR),
    include_package_data=True,
    test_suite='tests',
    entry_points="""
    [console_scripts]
    easy-timer = easy_timer.easy_timer:main
    """,
)
