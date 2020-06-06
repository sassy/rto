from setuptools import setup, find_packages

setup(
    name='rto',
    version='1.0',
    description='Open Redmine ticket of myself to browser.',
    packages=find_packages(),
    install_requires=['cliff'],
    entry_points={
        'console_scripts':
            'rto = rto.main:rto_main'
    },
    zip_safe=False,
    classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python'
    ],
    author='Satoshi Watanabe',
    author_email='sassy.watanabe@gmail.com',
    url='https://github.com/sassy/rto',
    license='MIT',
)
