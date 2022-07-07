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
VERSION = "3.0.97"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.97',
    'huaweicloudsdkantiddos==3.0.97',
    'huaweicloudsdkaom==3.0.97',
    'huaweicloudsdkapig==3.0.97',
    'huaweicloudsdkapm==3.0.97',
    'huaweicloudsdkas==3.0.97',
    'huaweicloudsdkbcs==3.0.97',
    'huaweicloudsdkbms==3.0.97',
    'huaweicloudsdkbss==3.0.97',
    'huaweicloudsdkbssintl==3.0.97',
    'huaweicloudsdkcampusgo==3.0.97',
    'huaweicloudsdkcbh==3.0.97',
    'huaweicloudsdkcbr==3.0.97',
    'huaweicloudsdkcbs==3.0.97',
    'huaweicloudsdkcc==3.0.97',
    'huaweicloudsdkcce==3.0.97',
    'huaweicloudsdkccm==3.0.97',
    'huaweicloudsdkcdm==3.0.97',
    'huaweicloudsdkcdn==3.0.97',
    'huaweicloudsdkces==3.0.97',
    'huaweicloudsdkcgs==3.0.97',
    'huaweicloudsdkclassroom==3.0.97',
    'huaweicloudsdkcloudbuild==3.0.97',
    'huaweicloudsdkclouddeploy==3.0.97',
    'huaweicloudsdkcloudide==3.0.97',
    'huaweicloudsdkcloudpipeline==3.0.97',
    'huaweicloudsdkcloudrtc==3.0.97',
    'huaweicloudsdkcloudtable==3.0.97',
    'huaweicloudsdkcloudtest==3.0.97',
    'huaweicloudsdkcodecheck==3.0.97',
    'huaweicloudsdkcodecraft==3.0.97',
    'huaweicloudsdkcodehub==3.0.97',
    'huaweicloudsdkcpts==3.0.97',
    'huaweicloudsdkcse==3.0.97',
    'huaweicloudsdkcsms==3.0.97',
    'huaweicloudsdkcss==3.0.97',
    'huaweicloudsdkcts==3.0.97',
    'huaweicloudsdkdas==3.0.97',
    'huaweicloudsdkdbss==3.0.97',
    'huaweicloudsdkdcs==3.0.97',
    'huaweicloudsdkddm==3.0.97',
    'huaweicloudsdkdds==3.0.97',
    'huaweicloudsdkdeh==3.0.97',
    'huaweicloudsdkdevstar==3.0.97',
    'huaweicloudsdkdgc==3.0.97',
    'huaweicloudsdkdli==3.0.97',
    'huaweicloudsdkdms==3.0.97',
    'huaweicloudsdkdns==3.0.97',
    'huaweicloudsdkdrs==3.0.97',
    'huaweicloudsdkdsc==3.0.97',
    'huaweicloudsdkdws==3.0.97',
    'huaweicloudsdkecs==3.0.97',
    'huaweicloudsdkeip==3.0.97',
    'huaweicloudsdkelb==3.0.97',
    'huaweicloudsdkeps==3.0.97',
    'huaweicloudsdkevs==3.0.97',
    'huaweicloudsdkfrs==3.0.97',
    'huaweicloudsdkfunctiongraph==3.0.97',
    'huaweicloudsdkgaussdb==3.0.97',
    'huaweicloudsdkgaussdbfornosql==3.0.97',
    'huaweicloudsdkgaussdbforopengauss==3.0.97',
    'huaweicloudsdkges==3.0.97',
    'huaweicloudsdkgsl==3.0.97',
    'huaweicloudsdkhilens==3.0.97',
    'huaweicloudsdkhss==3.0.97',
    'huaweicloudsdkiam==3.0.97',
    'huaweicloudsdkiec==3.0.97',
    'huaweicloudsdkief==3.0.97',
    'huaweicloudsdkies==3.0.97',
    'huaweicloudsdkimage==3.0.97',
    'huaweicloudsdkimagesearch==3.0.97',
    'huaweicloudsdkims==3.0.97',
    'huaweicloudsdkiotanalytics==3.0.97',
    'huaweicloudsdkiotda==3.0.97',
    'huaweicloudsdkiotedge==3.0.97',
    'huaweicloudsdkivs==3.0.97',
    'huaweicloudsdkkafka==3.0.97',
    'huaweicloudsdkkms==3.0.97',
    'huaweicloudsdkkps==3.0.97',
    'huaweicloudsdklive==3.0.97',
    'huaweicloudsdklts==3.0.97',
    'huaweicloudsdkmeeting==3.0.97',
    'huaweicloudsdkmoderation==3.0.97',
    'huaweicloudsdkmpc==3.0.97',
    'huaweicloudsdkmrs==3.0.97',
    'huaweicloudsdknat==3.0.97',
    'huaweicloudsdknlp==3.0.97',
    'huaweicloudsdkocr==3.0.97',
    'huaweicloudsdkoms==3.0.97',
    'huaweicloudsdkosm==3.0.97',
    'huaweicloudsdkprojectman==3.0.97',
    'huaweicloudsdkrabbitmq==3.0.97',
    'huaweicloudsdkrds==3.0.97',
    'huaweicloudsdkres==3.0.97',
    'huaweicloudsdkrms==3.0.97',
    'huaweicloudsdkrocketmq==3.0.97',
    'huaweicloudsdkroma==3.0.97',
    'huaweicloudsdksa==3.0.97',
    'huaweicloudsdkscm==3.0.97',
    'huaweicloudsdksdrs==3.0.97',
    'huaweicloudsdkservicestage==3.0.97',
    'huaweicloudsdksfsturbo==3.0.97',
    'huaweicloudsdksis==3.0.97',
    'huaweicloudsdksmn==3.0.97',
    'huaweicloudsdksms==3.0.97',
    'huaweicloudsdkswr==3.0.97',
    'huaweicloudsdktms==3.0.97',
    'huaweicloudsdkugo==3.0.97',
    'huaweicloudsdkvas==3.0.97',
    'huaweicloudsdkvod==3.0.97',
    'huaweicloudsdkvpc==3.0.97',
    'huaweicloudsdkvpcep==3.0.97',
    'huaweicloudsdkvss==3.0.97',
    'huaweicloudsdkwaf==3.0.97',
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
