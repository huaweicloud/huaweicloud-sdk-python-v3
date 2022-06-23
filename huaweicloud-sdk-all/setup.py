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
VERSION = "3.0.94"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.94',
    'huaweicloudsdkantiddos==3.0.94',
    'huaweicloudsdkaom==3.0.94',
    'huaweicloudsdkapig==3.0.94',
    'huaweicloudsdkapm==3.0.94',
    'huaweicloudsdkas==3.0.94',
    'huaweicloudsdkbcs==3.0.94',
    'huaweicloudsdkbms==3.0.94',
    'huaweicloudsdkbss==3.0.94',
    'huaweicloudsdkbssintl==3.0.94',
    'huaweicloudsdkcampusgo==3.0.94',
    'huaweicloudsdkcbh==3.0.94',
    'huaweicloudsdkcbr==3.0.94',
    'huaweicloudsdkcbs==3.0.94',
    'huaweicloudsdkcc==3.0.94',
    'huaweicloudsdkcce==3.0.94',
    'huaweicloudsdkccm==3.0.94',
    'huaweicloudsdkcdm==3.0.94',
    'huaweicloudsdkcdn==3.0.94',
    'huaweicloudsdkces==3.0.94',
    'huaweicloudsdkcgs==3.0.94',
    'huaweicloudsdkclassroom==3.0.94',
    'huaweicloudsdkcloudbuild==3.0.94',
    'huaweicloudsdkclouddeploy==3.0.94',
    'huaweicloudsdkcloudide==3.0.94',
    'huaweicloudsdkcloudpipeline==3.0.94',
    'huaweicloudsdkcloudrtc==3.0.94',
    'huaweicloudsdkcloudtable==3.0.94',
    'huaweicloudsdkcloudtest==3.0.94',
    'huaweicloudsdkcodecheck==3.0.94',
    'huaweicloudsdkcodecraft==3.0.94',
    'huaweicloudsdkcodehub==3.0.94',
    'huaweicloudsdkcpts==3.0.94',
    'huaweicloudsdkcse==3.0.94',
    'huaweicloudsdkcsms==3.0.94',
    'huaweicloudsdkcss==3.0.94',
    'huaweicloudsdkcts==3.0.94',
    'huaweicloudsdkdas==3.0.94',
    'huaweicloudsdkdbss==3.0.94',
    'huaweicloudsdkdcs==3.0.94',
    'huaweicloudsdkddm==3.0.94',
    'huaweicloudsdkdds==3.0.94',
    'huaweicloudsdkdeh==3.0.94',
    'huaweicloudsdkdevstar==3.0.94',
    'huaweicloudsdkdgc==3.0.94',
    'huaweicloudsdkdli==3.0.94',
    'huaweicloudsdkdms==3.0.94',
    'huaweicloudsdkdns==3.0.94',
    'huaweicloudsdkdrs==3.0.94',
    'huaweicloudsdkdsc==3.0.94',
    'huaweicloudsdkdws==3.0.94',
    'huaweicloudsdkecs==3.0.94',
    'huaweicloudsdkeip==3.0.94',
    'huaweicloudsdkelb==3.0.94',
    'huaweicloudsdkeps==3.0.94',
    'huaweicloudsdkevs==3.0.94',
    'huaweicloudsdkfrs==3.0.94',
    'huaweicloudsdkfunctiongraph==3.0.94',
    'huaweicloudsdkgaussdb==3.0.94',
    'huaweicloudsdkgaussdbfornosql==3.0.94',
    'huaweicloudsdkgaussdbforopengauss==3.0.94',
    'huaweicloudsdkges==3.0.94',
    'huaweicloudsdkgsl==3.0.94',
    'huaweicloudsdkhilens==3.0.94',
    'huaweicloudsdkhss==3.0.94',
    'huaweicloudsdkiam==3.0.94',
    'huaweicloudsdkiec==3.0.94',
    'huaweicloudsdkief==3.0.94',
    'huaweicloudsdkies==3.0.94',
    'huaweicloudsdkimage==3.0.94',
    'huaweicloudsdkimagesearch==3.0.94',
    'huaweicloudsdkims==3.0.94',
    'huaweicloudsdkiotanalytics==3.0.94',
    'huaweicloudsdkiotda==3.0.94',
    'huaweicloudsdkiotedge==3.0.94',
    'huaweicloudsdkivs==3.0.94',
    'huaweicloudsdkkafka==3.0.94',
    'huaweicloudsdkkms==3.0.94',
    'huaweicloudsdkkps==3.0.94',
    'huaweicloudsdklive==3.0.94',
    'huaweicloudsdklts==3.0.94',
    'huaweicloudsdkmeeting==3.0.94',
    'huaweicloudsdkmoderation==3.0.94',
    'huaweicloudsdkmpc==3.0.94',
    'huaweicloudsdkmrs==3.0.94',
    'huaweicloudsdknat==3.0.94',
    'huaweicloudsdknlp==3.0.94',
    'huaweicloudsdkocr==3.0.94',
    'huaweicloudsdkoms==3.0.94',
    'huaweicloudsdkosm==3.0.94',
    'huaweicloudsdkprojectman==3.0.94',
    'huaweicloudsdkrabbitmq==3.0.94',
    'huaweicloudsdkrds==3.0.94',
    'huaweicloudsdkres==3.0.94',
    'huaweicloudsdkrms==3.0.94',
    'huaweicloudsdkrocketmq==3.0.94',
    'huaweicloudsdkroma==3.0.94',
    'huaweicloudsdksa==3.0.94',
    'huaweicloudsdkscm==3.0.94',
    'huaweicloudsdksdrs==3.0.94',
    'huaweicloudsdkservicestage==3.0.94',
    'huaweicloudsdksfsturbo==3.0.94',
    'huaweicloudsdksis==3.0.94',
    'huaweicloudsdksmn==3.0.94',
    'huaweicloudsdksms==3.0.94',
    'huaweicloudsdkswr==3.0.94',
    'huaweicloudsdktms==3.0.94',
    'huaweicloudsdkvas==3.0.94',
    'huaweicloudsdkvod==3.0.94',
    'huaweicloudsdkvpc==3.0.94',
    'huaweicloudsdkvpcep==3.0.94',
    'huaweicloudsdkvss==3.0.94',
    'huaweicloudsdkwaf==3.0.94',
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
