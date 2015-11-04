from setuptools import setup, find_packages
import subms_ja

setup(
    name='subms_ja',
    author='demmc',
    version=subms_ja.VERSION,
    description='A tool list japanese subreddits',
    license='GPL',
    url='https://github.com/demmc/subms_ja',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    keywords='reddit',
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'praw'],
    entry_points={
        'console_scripts': [
            'subms_ja=subms_ja:main',
        ],
    },
)
