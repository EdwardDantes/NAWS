try: 
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Naws: Not Another Web Scanner',
    'author': 'NotAnonymous',
    'url': 'www.github.com',
    'version': '0.1',
    'install_requires': ['napalm', 'pycurl', 'requests', 'python-nmap', 'xmltodict', 'wfuzz']
    'packages': ['NAWS'],
    'scripts':[],
    'name': 'NAWS'
}

setup(**config)
