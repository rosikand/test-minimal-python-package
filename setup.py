from setuptools import setup
import os 


def read_requirements_file(filename):
    # source: https://github.com/ikostrikov/jaxrl/blob/main/setup.py#L11 
    req_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 filename)
    with open(req_file_path) as f:
        return [line.strip() for line in f]



setup(name='test_minimal_python_package',
      version='0.0.2',
      description='The most minimal python package in the world',
      url='https://github.com/rosikand/test_minimal_python_package',
      author='Rohan Sikand',
      author_email='rsikand29@gmail.com',
      license='MIT',
      packages=['test_minimal_python_package'],
      install_requires=read_requirements_file('requirements.txt'),
      zip_safe=False)
