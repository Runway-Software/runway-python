from setuptools import setup, find_packages

setup(
      name='runway',
      version='1.0',
      description='Runway Python SDK',
      author='Runway Internal Development Team',
      url='https://github.com/pjv4yj/python-sdk',
      packages=['runway'],
      install_requires=['azure-core','msrest']
    )
