try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='eyvind',
    version="0.1",
    description='Eyvind is an authentication middleware and application for openplans.',
    author='David Turner',
    author_email='novalis@openplans.org',
    license = "GPLv3 or any later version",
    #url='',
    install_requires=["Pylons>=0.9.6.1"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'eyvind': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors = {'eyvind': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},
    entry_points="""
    [paste.app_factory]
    main = eyvind.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
