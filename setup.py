import setuptools

setuptools.setup(
    name='opencarp_analyzer',
    version='1.0',
    packages=setuptools.find_packages() ,
    url='https://github.com/regmibijay/opencarp-analyzer',
    license='MIT',
    author='Bijay Regmi',
    author_email='opencarp-analyzer@regdelivery.de',
    description='OpenCARP Trace Analyzer',
    install_requires = ['pandas','matplotlib'],
    entry_points = {'console_scripts': [
    'opencarp-analyzer=opencarp_analyzer.analyzer:main',
    'opencarp-plotter=opencarp_analyzer.plotter:main',
    ]},
    python_requires = '>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)