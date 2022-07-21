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
VERSION = "3.0.99"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.99',
    'huaweicloudsdkantiddos==3.0.99',
    'huaweicloudsdkaom==3.0.99',
    'huaweicloudsdkapig==3.0.99',
    'huaweicloudsdkapm==3.0.99',
    'huaweicloudsdkas==3.0.99',
    'huaweicloudsdkbcs==3.0.99',
    'huaweicloudsdkbms==3.0.99',
    'huaweicloudsdkbss==3.0.99',
    'huaweicloudsdkbssintl==3.0.99',
    'huaweicloudsdkcampusgo==3.0.99',
    'huaweicloudsdkcbh==3.0.99',
    'huaweicloudsdkcbr==3.0.99',
    'huaweicloudsdkcbs==3.0.99',
    'huaweicloudsdkcc==3.0.99',
    'huaweicloudsdkcce==3.0.99',
    'huaweicloudsdkccm==3.0.99',
    'huaweicloudsdkcdm==3.0.99',
    'huaweicloudsdkcdn==3.0.99',
    'huaweicloudsdkces==3.0.99',
    'huaweicloudsdkcgs==3.0.99',
    'huaweicloudsdkclassroom==3.0.99',
    'huaweicloudsdkcloudbuild==3.0.99',
    'huaweicloudsdkclouddeploy==3.0.99',
    'huaweicloudsdkcloudide==3.0.99',
    'huaweicloudsdkcloudpipeline==3.0.99',
    'huaweicloudsdkcloudrtc==3.0.99',
    'huaweicloudsdkcloudtable==3.0.99',
    'huaweicloudsdkcloudtest==3.0.99',
    'huaweicloudsdkcodecheck==3.0.99',
    'huaweicloudsdkcodecraft==3.0.99',
    'huaweicloudsdkcodehub==3.0.99',
    'huaweicloudsdkcpts==3.0.99',
    'huaweicloudsdkcse==3.0.99',
    'huaweicloudsdkcsms==3.0.99',
    'huaweicloudsdkcss==3.0.99',
    'huaweicloudsdkcts==3.0.99',
    'huaweicloudsdkdas==3.0.99',
    'huaweicloudsdkdbss==3.0.99',
    'huaweicloudsdkdcs==3.0.99',
    'huaweicloudsdkddm==3.0.99',
    'huaweicloudsdkdds==3.0.99',
    'huaweicloudsdkdeh==3.0.99',
    'huaweicloudsdkdevstar==3.0.99',
    'huaweicloudsdkdgc==3.0.99',
    'huaweicloudsdkdli==3.0.99',
    'huaweicloudsdkdms==3.0.99',
    'huaweicloudsdkdns==3.0.99',
    'huaweicloudsdkdrs==3.0.99',
    'huaweicloudsdkdsc==3.0.99',
    'huaweicloudsdkdws==3.0.99',
    'huaweicloudsdkecs==3.0.99',
    'huaweicloudsdkeip==3.0.99',
    'huaweicloudsdkelb==3.0.99',
    'huaweicloudsdkeps==3.0.99',
    'huaweicloudsdkevs==3.0.99',
    'huaweicloudsdkfrs==3.0.99',
    'huaweicloudsdkfunctiongraph==3.0.99',
    'huaweicloudsdkgaussdb==3.0.99',
    'huaweicloudsdkgaussdbfornosql==3.0.99',
    'huaweicloudsdkgaussdbforopengauss==3.0.99',
    'huaweicloudsdkges==3.0.99',
    'huaweicloudsdkgsl==3.0.99',
    'huaweicloudsdkhilens==3.0.99',
    'huaweicloudsdkhss==3.0.99',
    'huaweicloudsdkiam==3.0.99',
    'huaweicloudsdkiec==3.0.99',
    'huaweicloudsdkief==3.0.99',
    'huaweicloudsdkies==3.0.99',
    'huaweicloudsdkimage==3.0.99',
    'huaweicloudsdkimagesearch==3.0.99',
    'huaweicloudsdkims==3.0.99',
    'huaweicloudsdkiotanalytics==3.0.99',
    'huaweicloudsdkiotda==3.0.99',
    'huaweicloudsdkiotedge==3.0.99',
    'huaweicloudsdkivs==3.0.99',
    'huaweicloudsdkkafka==3.0.99',
    'huaweicloudsdkkms==3.0.99',
    'huaweicloudsdkkps==3.0.99',
    'huaweicloudsdklive==3.0.99',
    'huaweicloudsdklts==3.0.99',
    'huaweicloudsdkmeeting==3.0.99',
    'huaweicloudsdkmoderation==3.0.99',
    'huaweicloudsdkmpc==3.0.99',
    'huaweicloudsdkmrs==3.0.99',
    'huaweicloudsdknat==3.0.99',
    'huaweicloudsdknlp==3.0.99',
    'huaweicloudsdkocr==3.0.99',
    'huaweicloudsdkoms==3.0.99',
    'huaweicloudsdkosm==3.0.99',
    'huaweicloudsdkprojectman==3.0.99',
    'huaweicloudsdkrabbitmq==3.0.99',
    'huaweicloudsdkrds==3.0.99',
    'huaweicloudsdkres==3.0.99',
    'huaweicloudsdkrms==3.0.99',
    'huaweicloudsdkrocketmq==3.0.99',
    'huaweicloudsdkroma==3.0.99',
    'huaweicloudsdksa==3.0.99',
    'huaweicloudsdkscm==3.0.99',
    'huaweicloudsdksdrs==3.0.99',
    'huaweicloudsdkservicestage==3.0.99',
    'huaweicloudsdksfsturbo==3.0.99',
    'huaweicloudsdksis==3.0.99',
    'huaweicloudsdksmn==3.0.99',
    'huaweicloudsdksms==3.0.99',
    'huaweicloudsdkswr==3.0.99',
    'huaweicloudsdktms==3.0.99',
    'huaweicloudsdkugo==3.0.99',
    'huaweicloudsdkvas==3.0.99',
    'huaweicloudsdkvcm==3.0.99',
    'huaweicloudsdkvod==3.0.99',
    'huaweicloudsdkvpc==3.0.99',
    'huaweicloudsdkvpcep==3.0.99',
    'huaweicloudsdkvss==3.0.99',
    'huaweicloudsdkwaf==3.0.99',
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
