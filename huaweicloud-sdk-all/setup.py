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
VERSION = "3.0.105"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.105',
    'huaweicloudsdkantiddos==3.0.105',
    'huaweicloudsdkaom==3.0.105',
    'huaweicloudsdkapig==3.0.105',
    'huaweicloudsdkapm==3.0.105',
    'huaweicloudsdkas==3.0.105',
    'huaweicloudsdkbcs==3.0.105',
    'huaweicloudsdkbms==3.0.105',
    'huaweicloudsdkbss==3.0.105',
    'huaweicloudsdkbssintl==3.0.105',
    'huaweicloudsdkcampusgo==3.0.105',
    'huaweicloudsdkcbh==3.0.105',
    'huaweicloudsdkcbr==3.0.105',
    'huaweicloudsdkcbs==3.0.105',
    'huaweicloudsdkcc==3.0.105',
    'huaweicloudsdkcce==3.0.105',
    'huaweicloudsdkccm==3.0.105',
    'huaweicloudsdkcdm==3.0.105',
    'huaweicloudsdkcdn==3.0.105',
    'huaweicloudsdkces==3.0.105',
    'huaweicloudsdkcgs==3.0.105',
    'huaweicloudsdkclassroom==3.0.105',
    'huaweicloudsdkcloudbuild==3.0.105',
    'huaweicloudsdkclouddeploy==3.0.105',
    'huaweicloudsdkcloudide==3.0.105',
    'huaweicloudsdkcloudpipeline==3.0.105',
    'huaweicloudsdkcloudrtc==3.0.105',
    'huaweicloudsdkcloudtable==3.0.105',
    'huaweicloudsdkcloudtest==3.0.105',
    'huaweicloudsdkcodecheck==3.0.105',
    'huaweicloudsdkcodecraft==3.0.105',
    'huaweicloudsdkcodehub==3.0.105',
    'huaweicloudsdkcph==3.0.105',
    'huaweicloudsdkcpts==3.0.105',
    'huaweicloudsdkcse==3.0.105',
    'huaweicloudsdkcsms==3.0.105',
    'huaweicloudsdkcss==3.0.105',
    'huaweicloudsdkcts==3.0.105',
    'huaweicloudsdkdas==3.0.105',
    'huaweicloudsdkdbss==3.0.105',
    'huaweicloudsdkdcs==3.0.105',
    'huaweicloudsdkddm==3.0.105',
    'huaweicloudsdkdds==3.0.105',
    'huaweicloudsdkdeh==3.0.105',
    'huaweicloudsdkdevstar==3.0.105',
    'huaweicloudsdkdgc==3.0.105',
    'huaweicloudsdkdli==3.0.105',
    'huaweicloudsdkdms==3.0.105',
    'huaweicloudsdkdns==3.0.105',
    'huaweicloudsdkdrs==3.0.105',
    'huaweicloudsdkdsc==3.0.105',
    'huaweicloudsdkdws==3.0.105',
    'huaweicloudsdkecs==3.0.105',
    'huaweicloudsdkeg==3.0.105',
    'huaweicloudsdkeip==3.0.105',
    'huaweicloudsdkelb==3.0.105',
    'huaweicloudsdkeps==3.0.105',
    'huaweicloudsdkevs==3.0.105',
    'huaweicloudsdkfrs==3.0.105',
    'huaweicloudsdkfunctiongraph==3.0.105',
    'huaweicloudsdkgaussdb==3.0.105',
    'huaweicloudsdkgaussdbfornosql==3.0.105',
    'huaweicloudsdkgaussdbforopengauss==3.0.105',
    'huaweicloudsdkges==3.0.105',
    'huaweicloudsdkgsl==3.0.105',
    'huaweicloudsdkhilens==3.0.105',
    'huaweicloudsdkhss==3.0.105',
    'huaweicloudsdkiam==3.0.105',
    'huaweicloudsdkiec==3.0.105',
    'huaweicloudsdkief==3.0.105',
    'huaweicloudsdkies==3.0.105',
    'huaweicloudsdkimage==3.0.105',
    'huaweicloudsdkimagesearch==3.0.105',
    'huaweicloudsdkims==3.0.105',
    'huaweicloudsdkiotanalytics==3.0.105',
    'huaweicloudsdkiotda==3.0.105',
    'huaweicloudsdkiotedge==3.0.105',
    'huaweicloudsdkivs==3.0.105',
    'huaweicloudsdkkafka==3.0.105',
    'huaweicloudsdkkms==3.0.105',
    'huaweicloudsdkkps==3.0.105',
    'huaweicloudsdklive==3.0.105',
    'huaweicloudsdklts==3.0.105',
    'huaweicloudsdkmeeting==3.0.105',
    'huaweicloudsdkmoderation==3.0.105',
    'huaweicloudsdkmpc==3.0.105',
    'huaweicloudsdkmrs==3.0.105',
    'huaweicloudsdknat==3.0.105',
    'huaweicloudsdknlp==3.0.105',
    'huaweicloudsdkocr==3.0.105',
    'huaweicloudsdkoms==3.0.105',
    'huaweicloudsdkosm==3.0.105',
    'huaweicloudsdkprojectman==3.0.105',
    'huaweicloudsdkrabbitmq==3.0.105',
    'huaweicloudsdkrds==3.0.105',
    'huaweicloudsdkres==3.0.105',
    'huaweicloudsdkrms==3.0.105',
    'huaweicloudsdkrocketmq==3.0.105',
    'huaweicloudsdkroma==3.0.105',
    'huaweicloudsdksa==3.0.105',
    'huaweicloudsdkscm==3.0.105',
    'huaweicloudsdksdrs==3.0.105',
    'huaweicloudsdkservicestage==3.0.105',
    'huaweicloudsdksfsturbo==3.0.105',
    'huaweicloudsdksis==3.0.105',
    'huaweicloudsdksmn==3.0.105',
    'huaweicloudsdksms==3.0.105',
    'huaweicloudsdkswr==3.0.105',
    'huaweicloudsdktms==3.0.105',
    'huaweicloudsdkugo==3.0.105',
    'huaweicloudsdkvas==3.0.105',
    'huaweicloudsdkvcm==3.0.105',
    'huaweicloudsdkvod==3.0.105',
    'huaweicloudsdkvpc==3.0.105',
    'huaweicloudsdkvpcep==3.0.105',
    'huaweicloudsdkvss==3.0.105',
    'huaweicloudsdkwaf==3.0.105',
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
