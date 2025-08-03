from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='colorMindAsad',
    version='0.1.1',
    description='A Python library for color theory, moods, and palettes',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Asaduzzaman Asad',
    author_email='zyxmdasaduzzaman@gmail.com',  

    url='https://github.com/zyxasaduzzaman/MyColorMind',

    packages=find_packages(),

    python_requires='>=3.6',

    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Intended Audience :: Developers',
    ],

    project_urls={
        'Bug Reports': 'https://github.com/zyxasaduzzaman/MyColorMind/issues',
        'Source': 'https://github.com/zyxasaduzzaman/MyColorMind',
    },
)
