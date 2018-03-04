import setuptools

setuptools.setup(
    name='cloudify-resource-management-plugin',
    version='0.0.1',
    author='Michael Shnizer',
    author_email='michaels@cloudify.co',
    description='Resources tracking & quotavalidation',
    packages=['cloudify_resources'],
    license='LICENSE',
    install_requires=[
        'cloudify-plugins-common>=3.4.2',
        'cloudify-rest-client>=4.0',
        'xmltodict']
)
