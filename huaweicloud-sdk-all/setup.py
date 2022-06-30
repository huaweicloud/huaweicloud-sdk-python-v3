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
VERSION = "3.0.96"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.96',
    'huaweicloudsdkantiddos==3.0.96',
    'huaweicloudsdkaom==3.0.96',
    'huaweicloudsdkapig==3.0.96',
    'huaweicloudsdkapm==3.0.96',
    'huaweicloudsdkas==3.0.96',
    'huaweicloudsdkbcs==3.0.96',
    'huaweicloudsdkbms==3.0.96',
    'huaweicloudsdkbss==3.0.96',
    'huaweicloudsdkbssintl==3.0.96',
    'huaweicloudsdkcampusgo==3.0.96',
    'huaweicloudsdkcbh==3.0.96',
    'huaweicloudsdkcbr==3.0.96',
    'huaweicloudsdkcbs==3.0.96',
    'huaweicloudsdkcc==3.0.96',
    'huaweicloudsdkcce==3.0.96',
    'huaweicloudsdkccm==3.0.96',
    'huaweicloudsdkcdm==3.0.96',
    'huaweicloudsdkcdn==3.0.96',
    'huaweicloudsdkces==3.0.96',
    'huaweicloudsdkcgs==3.0.96',
    'huaweicloudsdkclassroom==3.0.96',
    'huaweicloudsdkcloudbuild==3.0.96',
    'huaweicloudsdkclouddeploy==3.0.96',
    'huaweicloudsdkcloudide==3.0.96',
    'huaweicloudsdkcloudpipeline==3.0.96',
    'huaweicloudsdkcloudrtc==3.0.96',
    'huaweicloudsdkcloudtable==3.0.96',
    'huaweicloudsdkcloudtest==3.0.96',
    'huaweicloudsdkcodecheck==3.0.96',
    'huaweicloudsdkcodecraft==3.0.96',
    'huaweicloudsdkcodehub==3.0.96',
    'huaweicloudsdkcpts==3.0.96',
    'huaweicloudsdkcse==3.0.96',
    'huaweicloudsdkcsms==3.0.96',
    'huaweicloudsdkcss==3.0.96',
    'huaweicloudsdkcts==3.0.96',
    'huaweicloudsdkdas==3.0.96',
    'huaweicloudsdkdbss==3.0.96',
    'huaweicloudsdkdcs==3.0.96',
    'huaweicloudsdkddm==3.0.96',
    'huaweicloudsdkdds==3.0.96',
    'huaweicloudsdkdeh==3.0.96',
    'huaweicloudsdkdevstar==3.0.96',
    'huaweicloudsdkdgc==3.0.96',
    'huaweicloudsdkdli==3.0.96',
    'huaweicloudsdkdms==3.0.96',
    'huaweicloudsdkdns==3.0.96',
    'huaweicloudsdkdrs==3.0.96',
    'huaweicloudsdkdsc==3.0.96',
    'huaweicloudsdkdws==3.0.96',
    'huaweicloudsdkecs==3.0.96',
    'huaweicloudsdkeip==3.0.96',
    'huaweicloudsdkelb==3.0.96',
    'huaweicloudsdkeps==3.0.96',
    'huaweicloudsdkevs==3.0.96',
    'huaweicloudsdkfrs==3.0.96',
    'huaweicloudsdkfunctiongraph==3.0.96',
    'huaweicloudsdkgaussdb==3.0.96',
    'huaweicloudsdkgaussdbfornosql==3.0.96',
    'huaweicloudsdkgaussdbforopengauss==3.0.96',
    'huaweicloudsdkges==3.0.96',
    'huaweicloudsdkgsl==3.0.96',
    'huaweicloudsdkhilens==3.0.96',
    'huaweicloudsdkhss==3.0.96',
    'huaweicloudsdkiam==3.0.96',
    'huaweicloudsdkiec==3.0.96',
    'huaweicloudsdkief==3.0.96',
    'huaweicloudsdkies==3.0.96',
    'huaweicloudsdkimage==3.0.96',
    'huaweicloudsdkimagesearch==3.0.96',
    'huaweicloudsdkims==3.0.96',
    'huaweicloudsdkiotanalytics==3.0.96',
    'huaweicloudsdkiotda==3.0.96',
    'huaweicloudsdkiotedge==3.0.96',
    'huaweicloudsdkivs==3.0.96',
    'huaweicloudsdkkafka==3.0.96',
    'huaweicloudsdkkms==3.0.96',
    'huaweicloudsdkkps==3.0.96',
    'huaweicloudsdklive==3.0.96',
    'huaweicloudsdklts==3.0.96',
    'huaweicloudsdkmeeting==3.0.96',
    'huaweicloudsdkmoderation==3.0.96',
    'huaweicloudsdkmpc==3.0.96',
    'huaweicloudsdkmrs==3.0.96',
    'huaweicloudsdknat==3.0.96',
    'huaweicloudsdknlp==3.0.96',
    'huaweicloudsdkocr==3.0.96',
    'huaweicloudsdkoms==3.0.96',
    'huaweicloudsdkosm==3.0.96',
    'huaweicloudsdkprojectman==3.0.96',
    'huaweicloudsdkrabbitmq==3.0.96',
    'huaweicloudsdkrds==3.0.96',
    'huaweicloudsdkres==3.0.96',
    'huaweicloudsdkrms==3.0.96',
    'huaweicloudsdkrocketmq==3.0.96',
    'huaweicloudsdkroma==3.0.96',
    'huaweicloudsdksa==3.0.96',
    'huaweicloudsdkscm==3.0.96',
    'huaweicloudsdksdrs==3.0.96',
    'huaweicloudsdkservicestage==3.0.96',
    'huaweicloudsdksfsturbo==3.0.96',
    'huaweicloudsdksis==3.0.96',
    'huaweicloudsdksmn==3.0.96',
    'huaweicloudsdksms==3.0.96',
    'huaweicloudsdkswr==3.0.96',
    'huaweicloudsdktms==3.0.96',
    'huaweicloudsdkugo==3.0.96',
    'huaweicloudsdkvas==3.0.96',
    'huaweicloudsdkvod==3.0.96',
    'huaweicloudsdkvpc==3.0.96',
    'huaweicloudsdkvpcep==3.0.96',
    'huaweicloudsdkvss==3.0.96',
    'huaweicloudsdkwaf==3.0.96',
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
