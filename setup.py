from setuptools import setup

setup(name='blog', version='1.0',
      description='OpenShift Python-2.7 Community Cartridge based application',
      author='Harshit agarwal', author_email='harshit.py@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['MySQL-python','Django==1.3.1',
                        #  'pymongo',
                        #  'psycopg2',
      ],
     )
