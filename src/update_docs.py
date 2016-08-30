'''
Created on Aug 30, 2016

@author: tal
'''
from __future__ import unicode_literals, division, print_function

import os
from subprocess import Popen, PIPE, check_output, STDOUT

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
    update_documentation()
    upload_documentation()

if __name__ == '__main__':
    main()
