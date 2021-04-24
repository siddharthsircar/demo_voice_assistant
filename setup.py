from setuptools import setup
from distutils.core import setup
import py2exe

setup(
    name='jarvis_voiceai',
    version='1.0',
    packages=['gui', 'modules'],
    url='https://github.com/siddharthsircar/demo_voice_assistant',
    license='',
    author='Siddharth Sircar',
    author_email='sidsircar16@gmail.com',
    description='voice_assistant',
    console=['run_assistant.py']
)
