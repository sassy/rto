from setuptools import setup, find_packages

setup(
    name='rto',
    version='0.1',
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
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
    ],
)
