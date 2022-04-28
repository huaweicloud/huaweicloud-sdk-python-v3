# coding= utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http=//www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

from os import path

from setuptools import setup, find_packages

NAME = "huaweicloudsdkall"
VERSION = "3.0.86"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.86',
    'huaweicloudsdkantiddos==3.0.86',
    'huaweicloudsdkaom==3.0.86',
    'huaweicloudsdkapig==3.0.86',
    'huaweicloudsdkapm==3.0.86',
    'huaweicloudsdkas==3.0.86',
    'huaweicloudsdkbcs==3.0.86',
    'huaweicloudsdkbms==3.0.86',
    'huaweicloudsdkbss==3.0.86',
    'huaweicloudsdkbssintl==3.0.86',
    'huaweicloudsdkcampusgo==3.0.86',
    'huaweicloudsdkcbh==3.0.86',
    'huaweicloudsdkcbr==3.0.86',
    'huaweicloudsdkcbs==3.0.86',
    'huaweicloudsdkcc==3.0.86',
    'huaweicloudsdkcce==3.0.86',
    'huaweicloudsdkccm==3.0.86',
    'huaweicloudsdkcdm==3.0.86',
    'huaweicloudsdkcdn==3.0.86',
    'huaweicloudsdkces==3.0.86',
    'huaweicloudsdkcgs==3.0.86',
    'huaweicloudsdkclassroom==3.0.86',
    'huaweicloudsdkcloudbuild==3.0.86',
    'huaweicloudsdkclouddeploy==3.0.86',
    'huaweicloudsdkcloudide==3.0.86',
    'huaweicloudsdkcloudpipeline==3.0.86',
    'huaweicloudsdkcloudrtc==3.0.86',
    'huaweicloudsdkcloudtable==3.0.86',
    'huaweicloudsdkcloudtest==3.0.86',
    'huaweicloudsdkcodecheck==3.0.86',
    'huaweicloudsdkcodecraft==3.0.86',
    'huaweicloudsdkcodehub==3.0.86',
    'huaweicloudsdkcpts==3.0.86',
    'huaweicloudsdkcse==3.0.86',
    'huaweicloudsdkcsms==3.0.86',
    'huaweicloudsdkcss==3.0.86',
    'huaweicloudsdkcts==3.0.86',
    'huaweicloudsdkdas==3.0.86',
    'huaweicloudsdkdbss==3.0.86',
    'huaweicloudsdkdcs==3.0.86',
    'huaweicloudsdkddm==3.0.86',
    'huaweicloudsdkdds==3.0.86',
    'huaweicloudsdkdeh==3.0.86',
    'huaweicloudsdkdevstar==3.0.86',
    'huaweicloudsdkdgc==3.0.86',
    'huaweicloudsdkdms==3.0.86',
    'huaweicloudsdkdns==3.0.86',
    'huaweicloudsdkdrs==3.0.86',
    'huaweicloudsdkdsc==3.0.86',
    'huaweicloudsdkdws==3.0.86',
    'huaweicloudsdkecs==3.0.86',
    'huaweicloudsdkeip==3.0.86',
    'huaweicloudsdkelb==3.0.86',
    'huaweicloudsdkeps==3.0.86',
    'huaweicloudsdkevs==3.0.86',
    'huaweicloudsdkfrs==3.0.86',
    'huaweicloudsdkfunctiongraph==3.0.86',
    'huaweicloudsdkgaussdb==3.0.86',
    'huaweicloudsdkgaussdbfornosql==3.0.86',
    'huaweicloudsdkgaussdbforopengauss==3.0.86',
    'huaweicloudsdkges==3.0.86',
    'huaweicloudsdkgsl==3.0.86',
    'huaweicloudsdkhilens==3.0.86',
    'huaweicloudsdkhss==3.0.86',
    'huaweicloudsdkiam==3.0.86',
    'huaweicloudsdkiec==3.0.86',
    'huaweicloudsdkief==3.0.86',
    'huaweicloudsdkies==3.0.86',
    'huaweicloudsdkimage==3.0.86',
    'huaweicloudsdkimagesearch==3.0.86',
    'huaweicloudsdkims==3.0.86',
    'huaweicloudsdkiotanalytics==3.0.86',
    'huaweicloudsdkiotda==3.0.86',
    'huaweicloudsdkiotedge==3.0.86',
    'huaweicloudsdkivs==3.0.86',
    'huaweicloudsdkkafka==3.0.86',
    'huaweicloudsdkkms==3.0.86',
    'huaweicloudsdkkps==3.0.86',
    'huaweicloudsdklive==3.0.86',
    'huaweicloudsdklts==3.0.86',
    'huaweicloudsdkmeeting==3.0.86',
    'huaweicloudsdkmoderation==3.0.86',
    'huaweicloudsdkmpc==3.0.86',
    'huaweicloudsdkmrs==3.0.86',
    'huaweicloudsdknat==3.0.86',
    'huaweicloudsdknlp==3.0.86',
    'huaweicloudsdkocr==3.0.86',
    'huaweicloudsdkoms==3.0.86',
    'huaweicloudsdkosm==3.0.86',
    'huaweicloudsdkprojectman==3.0.86',
    'huaweicloudsdkrabbitmq==3.0.86',
    'huaweicloudsdkrds==3.0.86',
    'huaweicloudsdkres==3.0.86',
    'huaweicloudsdkrms==3.0.86',
    'huaweicloudsdkroma==3.0.86',
    'huaweicloudsdksa==3.0.86',
    'huaweicloudsdkscm==3.0.86',
    'huaweicloudsdksdrs==3.0.86',
    'huaweicloudsdkservicestage==3.0.86',
    'huaweicloudsdksfsturbo==3.0.86',
    'huaweicloudsdksis==3.0.86',
    'huaweicloudsdksmn==3.0.86',
    'huaweicloudsdksms==3.0.86',
    'huaweicloudsdkswr==3.0.86',
    'huaweicloudsdktms==3.0.86',
    'huaweicloudsdkvas==3.0.86',
    'huaweicloudsdkvod==3.0.86',
    'huaweicloudsdkvpc==3.0.86',
    'huaweicloudsdkvpcep==3.0.86',
    'huaweicloudsdkvss==3.0.86',
    'huaweicloudsdkwaf==3.0.86',
]

OPTIONS = {
    'bdist_wheel': {
        'universal': True
    }
}

setup(
    name=NAME,
    version=VERSION,
    options=OPTIONS,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache LICENSE 2.0",
    url=URL,
    keywords=["huaweicloud", "sdk", "all"],
    packages=find_packages(),
    platforms=['any'],
    install_requires=INSTALL_REQUIRES,
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development'
    ]
)
