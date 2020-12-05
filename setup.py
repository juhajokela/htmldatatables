from setuptools import (
    find_packages,
    setup,
)

setup(
    name='htmldatatables',
    version='0.0.1',
    description='HTML Data Tables.',
    url='http://github.com/juhajokela/htmldatatables',
    author='Juha Jokela',
    author_email='juha@britebit.net',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    include_package_data=True,
    package_data={
        "htmldatatables": ["templates/*.html"],
    }
)
