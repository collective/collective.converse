from setuptools import setup, find_packages
import os

version = '0.0.1.dev0'

setup(
    name='collective.converse',
    version=version,
    description="XMPP and Converse.js integration with Plone",
    long_description=open("README.rst").read() + "\n" +
                open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
    ],
    keywords='xmpp chat messaging converse.js',
    author='JC Brand',
    author_email='jc@opkode.com',
    url='https://github.com/collective/collective.converse',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['BeautifulSoup', 'pyotp', 'Plone'],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """
)
