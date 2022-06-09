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
VERSION = "3.0.92"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.92',
    'huaweicloudsdkantiddos==3.0.92',
    'huaweicloudsdkaom==3.0.92',
    'huaweicloudsdkapig==3.0.92',
    'huaweicloudsdkapm==3.0.92',
    'huaweicloudsdkas==3.0.92',
    'huaweicloudsdkbcs==3.0.92',
    'huaweicloudsdkbms==3.0.92',
    'huaweicloudsdkbss==3.0.92',
    'huaweicloudsdkbssintl==3.0.92',
    'huaweicloudsdkcampusgo==3.0.92',
    'huaweicloudsdkcbh==3.0.92',
    'huaweicloudsdkcbr==3.0.92',
    'huaweicloudsdkcbs==3.0.92',
    'huaweicloudsdkcc==3.0.92',
    'huaweicloudsdkcce==3.0.92',
    'huaweicloudsdkccm==3.0.92',
    'huaweicloudsdkcdm==3.0.92',
    'huaweicloudsdkcdn==3.0.92',
    'huaweicloudsdkces==3.0.92',
    'huaweicloudsdkcgs==3.0.92',
    'huaweicloudsdkclassroom==3.0.92',
    'huaweicloudsdkcloudbuild==3.0.92',
    'huaweicloudsdkclouddeploy==3.0.92',
    'huaweicloudsdkcloudide==3.0.92',
    'huaweicloudsdkcloudpipeline==3.0.92',
    'huaweicloudsdkcloudrtc==3.0.92',
    'huaweicloudsdkcloudtable==3.0.92',
    'huaweicloudsdkcloudtest==3.0.92',
    'huaweicloudsdkcodecheck==3.0.92',
    'huaweicloudsdkcodecraft==3.0.92',
    'huaweicloudsdkcodehub==3.0.92',
    'huaweicloudsdkcpts==3.0.92',
    'huaweicloudsdkcse==3.0.92',
    'huaweicloudsdkcsms==3.0.92',
    'huaweicloudsdkcss==3.0.92',
    'huaweicloudsdkcts==3.0.92',
    'huaweicloudsdkdas==3.0.92',
    'huaweicloudsdkdbss==3.0.92',
    'huaweicloudsdkdcs==3.0.92',
    'huaweicloudsdkddm==3.0.92',
    'huaweicloudsdkdds==3.0.92',
    'huaweicloudsdkdeh==3.0.92',
    'huaweicloudsdkdevstar==3.0.92',
    'huaweicloudsdkdgc==3.0.92',
    'huaweicloudsdkdms==3.0.92',
    'huaweicloudsdkdns==3.0.92',
    'huaweicloudsdkdrs==3.0.92',
    'huaweicloudsdkdsc==3.0.92',
    'huaweicloudsdkdws==3.0.92',
    'huaweicloudsdkecs==3.0.92',
    'huaweicloudsdkeip==3.0.92',
    'huaweicloudsdkelb==3.0.92',
    'huaweicloudsdkeps==3.0.92',
    'huaweicloudsdkevs==3.0.92',
    'huaweicloudsdkfrs==3.0.92',
    'huaweicloudsdkfunctiongraph==3.0.92',
    'huaweicloudsdkgaussdb==3.0.92',
    'huaweicloudsdkgaussdbfornosql==3.0.92',
    'huaweicloudsdkgaussdbforopengauss==3.0.92',
    'huaweicloudsdkges==3.0.92',
    'huaweicloudsdkgsl==3.0.92',
    'huaweicloudsdkhilens==3.0.92',
    'huaweicloudsdkhss==3.0.92',
    'huaweicloudsdkiam==3.0.92',
    'huaweicloudsdkiec==3.0.92',
    'huaweicloudsdkief==3.0.92',
    'huaweicloudsdkies==3.0.92',
    'huaweicloudsdkimage==3.0.92',
    'huaweicloudsdkimagesearch==3.0.92',
    'huaweicloudsdkims==3.0.92',
    'huaweicloudsdkiotanalytics==3.0.92',
    'huaweicloudsdkiotda==3.0.92',
    'huaweicloudsdkiotedge==3.0.92',
    'huaweicloudsdkivs==3.0.92',
    'huaweicloudsdkkafka==3.0.92',
    'huaweicloudsdkkms==3.0.92',
    'huaweicloudsdkkps==3.0.92',
    'huaweicloudsdklive==3.0.92',
    'huaweicloudsdklts==3.0.92',
    'huaweicloudsdkmeeting==3.0.92',
    'huaweicloudsdkmoderation==3.0.92',
    'huaweicloudsdkmpc==3.0.92',
    'huaweicloudsdkmrs==3.0.92',
    'huaweicloudsdknat==3.0.92',
    'huaweicloudsdknlp==3.0.92',
    'huaweicloudsdkocr==3.0.92',
    'huaweicloudsdkoms==3.0.92',
    'huaweicloudsdkosm==3.0.92',
    'huaweicloudsdkprojectman==3.0.92',
    'huaweicloudsdkrabbitmq==3.0.92',
    'huaweicloudsdkrds==3.0.92',
    'huaweicloudsdkres==3.0.92',
    'huaweicloudsdkrms==3.0.92',
    'huaweicloudsdkrocketmq==3.0.92',
    'huaweicloudsdkroma==3.0.92',
    'huaweicloudsdksa==3.0.92',
    'huaweicloudsdkscm==3.0.92',
    'huaweicloudsdksdrs==3.0.92',
    'huaweicloudsdkservicestage==3.0.92',
    'huaweicloudsdksfsturbo==3.0.92',
    'huaweicloudsdksis==3.0.92',
    'huaweicloudsdksmn==3.0.92',
    'huaweicloudsdksms==3.0.92',
    'huaweicloudsdkswr==3.0.92',
    'huaweicloudsdktms==3.0.92',
    'huaweicloudsdkvas==3.0.92',
    'huaweicloudsdkvod==3.0.92',
    'huaweicloudsdkvpc==3.0.92',
    'huaweicloudsdkvpcep==3.0.92',
    'huaweicloudsdkvss==3.0.92',
    'huaweicloudsdkwaf==3.0.92',
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
