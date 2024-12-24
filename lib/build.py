# Created: 2022/12/29 @ 12:31 AM

"""
    Description: this file creates a DMG file that allows for usable application of GUI programs made in python,
    just copy this code into a new file named DMG_file_set_up and follow the below prompts
"""
# NOTE!!!! you need to be connected to a wifi source in order to run py2app
#


from setuptools import setup

APP = ['bulkifyWP.py']  # name of file (using.py) to convert to DMG
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],
}

setup(
    app= APP,  # NOQA
    options= {'py2app': OPTIONS},  # NOQA
    setup_requires= ['py2app']  # NOQA
)


# install in terminal (if not installed: pip3 install py2app)
# to create DMG file, make sure the dir is correct for this file then run command: python {file_name}.py py2app
