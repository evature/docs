'''
Created on Aug 30, 2016

@author: tal
'''
from __future__ import unicode_literals, division, print_function

import os
from subprocess import Popen, PIPE, check_output, STDOUT
import sphinx_bootstrap_theme
# import sphinx

def validate_configuration():
    """Make sure we configured our system correctly before running the tests"""
#     assert sphinx.__version__ == '1.4.5' # Sorry - we must all use the same code.
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

def upload_documentation_w_boto():
    """Upload documentation to S3"""
    print("Uploading documentation to S3")
    import boto
    from core.eva_setting import EVA_ROOT_PATH
    from core.api_versions import LATEST_AND_GREATEST
    from boto.s3.key import Key
    # Log into Amazon S3 service:
    s3_service = boto.connect_s3() # Credentials use environment variables
    # Done. Getting the bucket:
    bucket_name = "eva_docs_" + LATEST_AND_GREATEST
    try:
        bucket = s3_service.create_bucket(bucket_name) # Will create a bucket (if one doesn't exists)
    except boto.exception.S3CreateError:
        bucket = s3_service.get_bucket(bucket_name) # Will return the existing bucket (if one exists)
    documentation_dir = os.path.join(EVA_ROOT_PATH, "docs", "_build", "html") # eva/docs/_build/html
    a_key = Key(bucket)
    for path, _dir, files in os.walk(documentation_dir):
        for a_file in files:
            a_key.key = os.path.relpath(os.path.join(path, a_file), documentation_dir)
            a_key.set_contents_from_filename(os.path.join(path, a_file))
            bucket.set_acl('public-read', a_key.key)
    print("See the docs here: https://s3.amazonaws.com/eva_docs_{}/index.html".format(LATEST_AND_GREATEST))


def main():
    """Update docs AND upload to S3"""
    validate_configuration()
    update_documentation()
    upload_documentation()

if __name__ == '__main__':
    main()
