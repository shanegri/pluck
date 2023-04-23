from setuptools import setup, find_packages

setup(
    name='pluck',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'yt-dlp>=2022.3.9',
        'moviepy>=1.0.3'
    ],
    entry_points={
        'console_scripts': [
            'pluck=pluck:main',
        ],
    },
)
