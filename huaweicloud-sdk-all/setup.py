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
VERSION = "3.0.102"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.102',
    'huaweicloudsdkantiddos==3.0.102',
    'huaweicloudsdkaom==3.0.102',
    'huaweicloudsdkapig==3.0.102',
    'huaweicloudsdkapm==3.0.102',
    'huaweicloudsdkas==3.0.102',
    'huaweicloudsdkbcs==3.0.102',
    'huaweicloudsdkbms==3.0.102',
    'huaweicloudsdkbss==3.0.102',
    'huaweicloudsdkbssintl==3.0.102',
    'huaweicloudsdkcampusgo==3.0.102',
    'huaweicloudsdkcbh==3.0.102',
    'huaweicloudsdkcbr==3.0.102',
    'huaweicloudsdkcbs==3.0.102',
    'huaweicloudsdkcc==3.0.102',
    'huaweicloudsdkcce==3.0.102',
    'huaweicloudsdkccm==3.0.102',
    'huaweicloudsdkcdm==3.0.102',
    'huaweicloudsdkcdn==3.0.102',
    'huaweicloudsdkces==3.0.102',
    'huaweicloudsdkcgs==3.0.102',
    'huaweicloudsdkclassroom==3.0.102',
    'huaweicloudsdkcloudbuild==3.0.102',
    'huaweicloudsdkclouddeploy==3.0.102',
    'huaweicloudsdkcloudide==3.0.102',
    'huaweicloudsdkcloudpipeline==3.0.102',
    'huaweicloudsdkcloudrtc==3.0.102',
    'huaweicloudsdkcloudtable==3.0.102',
    'huaweicloudsdkcloudtest==3.0.102',
    'huaweicloudsdkcodecheck==3.0.102',
    'huaweicloudsdkcodecraft==3.0.102',
    'huaweicloudsdkcodehub==3.0.102',
    'huaweicloudsdkcpts==3.0.102',
    'huaweicloudsdkcse==3.0.102',
    'huaweicloudsdkcsms==3.0.102',
    'huaweicloudsdkcss==3.0.102',
    'huaweicloudsdkcts==3.0.102',
    'huaweicloudsdkdas==3.0.102',
    'huaweicloudsdkdbss==3.0.102',
    'huaweicloudsdkdcs==3.0.102',
    'huaweicloudsdkddm==3.0.102',
    'huaweicloudsdkdds==3.0.102',
    'huaweicloudsdkdeh==3.0.102',
    'huaweicloudsdkdevstar==3.0.102',
    'huaweicloudsdkdgc==3.0.102',
    'huaweicloudsdkdli==3.0.102',
    'huaweicloudsdkdms==3.0.102',
    'huaweicloudsdkdns==3.0.102',
    'huaweicloudsdkdrs==3.0.102',
    'huaweicloudsdkdsc==3.0.102',
    'huaweicloudsdkdws==3.0.102',
    'huaweicloudsdkecs==3.0.102',
    'huaweicloudsdkeip==3.0.102',
    'huaweicloudsdkelb==3.0.102',
    'huaweicloudsdkeps==3.0.102',
    'huaweicloudsdkevs==3.0.102',
    'huaweicloudsdkfrs==3.0.102',
    'huaweicloudsdkfunctiongraph==3.0.102',
    'huaweicloudsdkgaussdb==3.0.102',
    'huaweicloudsdkgaussdbfornosql==3.0.102',
    'huaweicloudsdkgaussdbforopengauss==3.0.102',
    'huaweicloudsdkges==3.0.102',
    'huaweicloudsdkgsl==3.0.102',
    'huaweicloudsdkhilens==3.0.102',
    'huaweicloudsdkhss==3.0.102',
    'huaweicloudsdkiam==3.0.102',
    'huaweicloudsdkiec==3.0.102',
    'huaweicloudsdkief==3.0.102',
    'huaweicloudsdkies==3.0.102',
    'huaweicloudsdkimage==3.0.102',
    'huaweicloudsdkimagesearch==3.0.102',
    'huaweicloudsdkims==3.0.102',
    'huaweicloudsdkiotanalytics==3.0.102',
    'huaweicloudsdkiotda==3.0.102',
    'huaweicloudsdkiotedge==3.0.102',
    'huaweicloudsdkivs==3.0.102',
    'huaweicloudsdkkafka==3.0.102',
    'huaweicloudsdkkms==3.0.102',
    'huaweicloudsdkkps==3.0.102',
    'huaweicloudsdklive==3.0.102',
    'huaweicloudsdklts==3.0.102',
    'huaweicloudsdkmeeting==3.0.102',
    'huaweicloudsdkmoderation==3.0.102',
    'huaweicloudsdkmpc==3.0.102',
    'huaweicloudsdkmrs==3.0.102',
    'huaweicloudsdknat==3.0.102',
    'huaweicloudsdknlp==3.0.102',
    'huaweicloudsdkocr==3.0.102',
    'huaweicloudsdkoms==3.0.102',
    'huaweicloudsdkosm==3.0.102',
    'huaweicloudsdkprojectman==3.0.102',
    'huaweicloudsdkrabbitmq==3.0.102',
    'huaweicloudsdkrds==3.0.102',
    'huaweicloudsdkres==3.0.102',
    'huaweicloudsdkrms==3.0.102',
    'huaweicloudsdkrocketmq==3.0.102',
    'huaweicloudsdkroma==3.0.102',
    'huaweicloudsdksa==3.0.102',
    'huaweicloudsdkscm==3.0.102',
    'huaweicloudsdksdrs==3.0.102',
    'huaweicloudsdkservicestage==3.0.102',
    'huaweicloudsdksfsturbo==3.0.102',
    'huaweicloudsdksis==3.0.102',
    'huaweicloudsdksmn==3.0.102',
    'huaweicloudsdksms==3.0.102',
    'huaweicloudsdkswr==3.0.102',
    'huaweicloudsdktms==3.0.102',
    'huaweicloudsdkugo==3.0.102',
    'huaweicloudsdkvas==3.0.102',
    'huaweicloudsdkvcm==3.0.102',
    'huaweicloudsdkvod==3.0.102',
    'huaweicloudsdkvpc==3.0.102',
    'huaweicloudsdkvpcep==3.0.102',
    'huaweicloudsdkvss==3.0.102',
    'huaweicloudsdkwaf==3.0.102',
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
