from setuptools import setup, find_packages

setup(
    name='opticspy',
    version='0.2.1',
    keywords = ('optics', 'lens', 'zernike','raytracing'),
    description='Python optics module',
    license = 'MIT License',
    install_requires = ['numpy>=1.9.3', 'matplotlib>=1.4.3', 'unwrap',
                        'pyyaml'],
    author='Xing Fan',
    author_email='marvin.fanxing@gmail.com',
    url='http://opticspy.org',
    packages = find_packages(),
    include_package_data = True,
)
