from setuptools import (
    setup,
    find_packages  # what it says on the tin
)

setup(
    name='urlfetch',
    version='0.1.0',
    description='Fetches URLs! Web browsers hate it!',
    install_requires=['requests'],  # could also read a requirements.txt file to populate list
    packages=find_packages(),
    license='wtfpl',
    entry_points={  # you can create really cool things here
        'console_scripts': [
            'fetch_url=urlgetter:command_line'
        ]
    },
)
