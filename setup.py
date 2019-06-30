from setuptools import setup

__VERSION__ = '0.0.1'

setup(
    name='dca',
    version=__VERSION__,
    description=(
        'Automagically gerenrates Django CRUD Automation'),
    long_description='''
        Tool to create CRUD operations.
    ''',
    author='Priyanshu Jain',
    author_email='priyanahu@pm.me',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Database',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='django orm grpc protobuf microservice database rpc dca',
    packages=['dca'],
    entry_points='',
    install_requires=[
        "django>=2.0",
        "inflect==0.3.1",
        "orm-choices==1.0.0",
    ],
)
