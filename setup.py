from distutils.core import setup
from playwindow import __version__

setup(
    name='playwindow',
    version=__version__,
    description='Easy-to-use tool to simple GUI programming in synchronous style',
    long_description=(
        'This tool dedicated to all better and to make GUI programming easy and '
        'funny for kids and for peoples who never programming before. It allows '
        'you to get noticeable result extremely quickly and move forward with pleasure.'
    ),
    url='https://github.com/michurin/playwindow',
    author='Alexey Michurin',
    author_email='a.michurin@gmail.com',
    maintainer='Alexey Michurin',
    maintainer_email='a.michurin@gmail.com',
    keywords=['GUI', 'beginner', 'learning'],
    license='MIT',
    packages=['playwindow'],
    platforms=['any']
)
