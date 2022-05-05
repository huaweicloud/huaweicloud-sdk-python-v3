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
VERSION = "3.0.87"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.87',
    'huaweicloudsdkantiddos==3.0.87',
    'huaweicloudsdkaom==3.0.87',
    'huaweicloudsdkapig==3.0.87',
    'huaweicloudsdkapm==3.0.87',
    'huaweicloudsdkas==3.0.87',
    'huaweicloudsdkbcs==3.0.87',
    'huaweicloudsdkbms==3.0.87',
    'huaweicloudsdkbss==3.0.87',
    'huaweicloudsdkbssintl==3.0.87',
    'huaweicloudsdkcampusgo==3.0.87',
    'huaweicloudsdkcbh==3.0.87',
    'huaweicloudsdkcbr==3.0.87',
    'huaweicloudsdkcbs==3.0.87',
    'huaweicloudsdkcc==3.0.87',
    'huaweicloudsdkcce==3.0.87',
    'huaweicloudsdkccm==3.0.87',
    'huaweicloudsdkcdm==3.0.87',
    'huaweicloudsdkcdn==3.0.87',
    'huaweicloudsdkces==3.0.87',
    'huaweicloudsdkcgs==3.0.87',
    'huaweicloudsdkclassroom==3.0.87',
    'huaweicloudsdkcloudbuild==3.0.87',
    'huaweicloudsdkclouddeploy==3.0.87',
    'huaweicloudsdkcloudide==3.0.87',
    'huaweicloudsdkcloudpipeline==3.0.87',
    'huaweicloudsdkcloudrtc==3.0.87',
    'huaweicloudsdkcloudtable==3.0.87',
    'huaweicloudsdkcloudtest==3.0.87',
    'huaweicloudsdkcodecheck==3.0.87',
    'huaweicloudsdkcodecraft==3.0.87',
    'huaweicloudsdkcodehub==3.0.87',
    'huaweicloudsdkcpts==3.0.87',
    'huaweicloudsdkcse==3.0.87',
    'huaweicloudsdkcsms==3.0.87',
    'huaweicloudsdkcss==3.0.87',
    'huaweicloudsdkcts==3.0.87',
    'huaweicloudsdkdas==3.0.87',
    'huaweicloudsdkdbss==3.0.87',
    'huaweicloudsdkdcs==3.0.87',
    'huaweicloudsdkddm==3.0.87',
    'huaweicloudsdkdds==3.0.87',
    'huaweicloudsdkdeh==3.0.87',
    'huaweicloudsdkdevstar==3.0.87',
    'huaweicloudsdkdgc==3.0.87',
    'huaweicloudsdkdms==3.0.87',
    'huaweicloudsdkdns==3.0.87',
    'huaweicloudsdkdrs==3.0.87',
    'huaweicloudsdkdsc==3.0.87',
    'huaweicloudsdkdws==3.0.87',
    'huaweicloudsdkecs==3.0.87',
    'huaweicloudsdkeip==3.0.87',
    'huaweicloudsdkelb==3.0.87',
    'huaweicloudsdkeps==3.0.87',
    'huaweicloudsdkevs==3.0.87',
    'huaweicloudsdkfrs==3.0.87',
    'huaweicloudsdkfunctiongraph==3.0.87',
    'huaweicloudsdkgaussdb==3.0.87',
    'huaweicloudsdkgaussdbfornosql==3.0.87',
    'huaweicloudsdkgaussdbforopengauss==3.0.87',
    'huaweicloudsdkges==3.0.87',
    'huaweicloudsdkgsl==3.0.87',
    'huaweicloudsdkhilens==3.0.87',
    'huaweicloudsdkhss==3.0.87',
    'huaweicloudsdkiam==3.0.87',
    'huaweicloudsdkiec==3.0.87',
    'huaweicloudsdkief==3.0.87',
    'huaweicloudsdkies==3.0.87',
    'huaweicloudsdkimage==3.0.87',
    'huaweicloudsdkimagesearch==3.0.87',
    'huaweicloudsdkims==3.0.87',
    'huaweicloudsdkiotanalytics==3.0.87',
    'huaweicloudsdkiotda==3.0.87',
    'huaweicloudsdkiotedge==3.0.87',
    'huaweicloudsdkivs==3.0.87',
    'huaweicloudsdkkafka==3.0.87',
    'huaweicloudsdkkms==3.0.87',
    'huaweicloudsdkkps==3.0.87',
    'huaweicloudsdklive==3.0.87',
    'huaweicloudsdklts==3.0.87',
    'huaweicloudsdkmeeting==3.0.87',
    'huaweicloudsdkmoderation==3.0.87',
    'huaweicloudsdkmpc==3.0.87',
    'huaweicloudsdkmrs==3.0.87',
    'huaweicloudsdknat==3.0.87',
    'huaweicloudsdknlp==3.0.87',
    'huaweicloudsdkocr==3.0.87',
    'huaweicloudsdkoms==3.0.87',
    'huaweicloudsdkosm==3.0.87',
    'huaweicloudsdkprojectman==3.0.87',
    'huaweicloudsdkrabbitmq==3.0.87',
    'huaweicloudsdkrds==3.0.87',
    'huaweicloudsdkres==3.0.87',
    'huaweicloudsdkrms==3.0.87',
    'huaweicloudsdkroma==3.0.87',
    'huaweicloudsdksa==3.0.87',
    'huaweicloudsdkscm==3.0.87',
    'huaweicloudsdksdrs==3.0.87',
    'huaweicloudsdkservicestage==3.0.87',
    'huaweicloudsdksfsturbo==3.0.87',
    'huaweicloudsdksis==3.0.87',
    'huaweicloudsdksmn==3.0.87',
    'huaweicloudsdksms==3.0.87',
    'huaweicloudsdkswr==3.0.87',
    'huaweicloudsdktms==3.0.87',
    'huaweicloudsdkvas==3.0.87',
    'huaweicloudsdkvod==3.0.87',
    'huaweicloudsdkvpc==3.0.87',
    'huaweicloudsdkvpcep==3.0.87',
    'huaweicloudsdkvss==3.0.87',
    'huaweicloudsdkwaf==3.0.87',
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
