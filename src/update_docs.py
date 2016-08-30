'''
Created on Aug 30, 2016

@author: tal
'''
from __future__ import unicode_literals, division, print_function

import os
from subprocess import Popen, PIPE, check_output, STDOUT
import sphinx_bootstrap_theme
import sphinx

def validate_configuration():
    """Make sure we configured our system correctly before running the tests"""
    assert sphinx.__version__ == '1.4.5' # Sorry - we must all use the same code.
    assert sphinx_bootstrap_theme.__version__ == '0.4.12'


def update_documentation():
    """Update our documentation using Sphinx"""
    # Generate / Refresh all documentation:
    if os.name == 'nt':
        child = Popen("make.bat html", cwd=r'..\docs', stdout=PIPE, shell=True)
        child.wait()
        print(child.stdout.read())
        assert child.returncode == 0
    else: # Linux version has make (and not make.bat) and forward slashes
        docs_path = os.path.join(os.path.normpath(os.path.join(os.path.dirname(__file__), '..')), "docs")
        print(check_output(["make", "html"], cwd=docs_path, stderr=STDOUT))
    return True


def upload_documentation():
    """Uploads docs to S3"""
    if os.name != 'nt':
        docs_path = os.path.join(os.path.normpath(os.path.join(os.path.dirname(__file__), '..')), "docs", "_build", "html")
        print(check_output(["aws", "s3", "sync", ".", "s3://docs.evature.com", "--acl", "public-read"], cwd=docs_path,
                           stderr=STDOUT))

def main():
    """Update docs AND upload to S3"""
    validate_configuration()
    update_documentation()
    upload_documentation()

if __name__ == '__main__':
    main()
