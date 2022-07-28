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
VERSION = "3.0.100"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.100',
    'huaweicloudsdkantiddos==3.0.100',
    'huaweicloudsdkaom==3.0.100',
    'huaweicloudsdkapig==3.0.100',
    'huaweicloudsdkapm==3.0.100',
    'huaweicloudsdkas==3.0.100',
    'huaweicloudsdkbcs==3.0.100',
    'huaweicloudsdkbms==3.0.100',
    'huaweicloudsdkbss==3.0.100',
    'huaweicloudsdkbssintl==3.0.100',
    'huaweicloudsdkcampusgo==3.0.100',
    'huaweicloudsdkcbh==3.0.100',
    'huaweicloudsdkcbr==3.0.100',
    'huaweicloudsdkcbs==3.0.100',
    'huaweicloudsdkcc==3.0.100',
    'huaweicloudsdkcce==3.0.100',
    'huaweicloudsdkccm==3.0.100',
    'huaweicloudsdkcdm==3.0.100',
    'huaweicloudsdkcdn==3.0.100',
    'huaweicloudsdkces==3.0.100',
    'huaweicloudsdkcgs==3.0.100',
    'huaweicloudsdkclassroom==3.0.100',
    'huaweicloudsdkcloudbuild==3.0.100',
    'huaweicloudsdkclouddeploy==3.0.100',
    'huaweicloudsdkcloudide==3.0.100',
    'huaweicloudsdkcloudpipeline==3.0.100',
    'huaweicloudsdkcloudrtc==3.0.100',
    'huaweicloudsdkcloudtable==3.0.100',
    'huaweicloudsdkcloudtest==3.0.100',
    'huaweicloudsdkcodecheck==3.0.100',
    'huaweicloudsdkcodecraft==3.0.100',
    'huaweicloudsdkcodehub==3.0.100',
    'huaweicloudsdkcpts==3.0.100',
    'huaweicloudsdkcse==3.0.100',
    'huaweicloudsdkcsms==3.0.100',
    'huaweicloudsdkcss==3.0.100',
    'huaweicloudsdkcts==3.0.100',
    'huaweicloudsdkdas==3.0.100',
    'huaweicloudsdkdbss==3.0.100',
    'huaweicloudsdkdcs==3.0.100',
    'huaweicloudsdkddm==3.0.100',
    'huaweicloudsdkdds==3.0.100',
    'huaweicloudsdkdeh==3.0.100',
    'huaweicloudsdkdevstar==3.0.100',
    'huaweicloudsdkdgc==3.0.100',
    'huaweicloudsdkdli==3.0.100',
    'huaweicloudsdkdms==3.0.100',
    'huaweicloudsdkdns==3.0.100',
    'huaweicloudsdkdrs==3.0.100',
    'huaweicloudsdkdsc==3.0.100',
    'huaweicloudsdkdws==3.0.100',
    'huaweicloudsdkecs==3.0.100',
    'huaweicloudsdkeip==3.0.100',
    'huaweicloudsdkelb==3.0.100',
    'huaweicloudsdkeps==3.0.100',
    'huaweicloudsdkevs==3.0.100',
    'huaweicloudsdkfrs==3.0.100',
    'huaweicloudsdkfunctiongraph==3.0.100',
    'huaweicloudsdkgaussdb==3.0.100',
    'huaweicloudsdkgaussdbfornosql==3.0.100',
    'huaweicloudsdkgaussdbforopengauss==3.0.100',
    'huaweicloudsdkges==3.0.100',
    'huaweicloudsdkgsl==3.0.100',
    'huaweicloudsdkhilens==3.0.100',
    'huaweicloudsdkhss==3.0.100',
    'huaweicloudsdkiam==3.0.100',
    'huaweicloudsdkiec==3.0.100',
    'huaweicloudsdkief==3.0.100',
    'huaweicloudsdkies==3.0.100',
    'huaweicloudsdkimage==3.0.100',
    'huaweicloudsdkimagesearch==3.0.100',
    'huaweicloudsdkims==3.0.100',
    'huaweicloudsdkiotanalytics==3.0.100',
    'huaweicloudsdkiotda==3.0.100',
    'huaweicloudsdkiotedge==3.0.100',
    'huaweicloudsdkivs==3.0.100',
    'huaweicloudsdkkafka==3.0.100',
    'huaweicloudsdkkms==3.0.100',
    'huaweicloudsdkkps==3.0.100',
    'huaweicloudsdklive==3.0.100',
    'huaweicloudsdklts==3.0.100',
    'huaweicloudsdkmeeting==3.0.100',
    'huaweicloudsdkmoderation==3.0.100',
    'huaweicloudsdkmpc==3.0.100',
    'huaweicloudsdkmrs==3.0.100',
    'huaweicloudsdknat==3.0.100',
    'huaweicloudsdknlp==3.0.100',
    'huaweicloudsdkocr==3.0.100',
    'huaweicloudsdkoms==3.0.100',
    'huaweicloudsdkosm==3.0.100',
    'huaweicloudsdkprojectman==3.0.100',
    'huaweicloudsdkrabbitmq==3.0.100',
    'huaweicloudsdkrds==3.0.100',
    'huaweicloudsdkres==3.0.100',
    'huaweicloudsdkrms==3.0.100',
    'huaweicloudsdkrocketmq==3.0.100',
    'huaweicloudsdkroma==3.0.100',
    'huaweicloudsdksa==3.0.100',
    'huaweicloudsdkscm==3.0.100',
    'huaweicloudsdksdrs==3.0.100',
    'huaweicloudsdkservicestage==3.0.100',
    'huaweicloudsdksfsturbo==3.0.100',
    'huaweicloudsdksis==3.0.100',
    'huaweicloudsdksmn==3.0.100',
    'huaweicloudsdksms==3.0.100',
    'huaweicloudsdkswr==3.0.100',
    'huaweicloudsdktms==3.0.100',
    'huaweicloudsdkugo==3.0.100',
    'huaweicloudsdkvas==3.0.100',
    'huaweicloudsdkvcm==3.0.100',
    'huaweicloudsdkvod==3.0.100',
    'huaweicloudsdkvpc==3.0.100',
    'huaweicloudsdkvpcep==3.0.100',
    'huaweicloudsdkvss==3.0.100',
    'huaweicloudsdkwaf==3.0.100',
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
