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
VERSION = "3.0.98"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.98',
    'huaweicloudsdkantiddos==3.0.98',
    'huaweicloudsdkaom==3.0.98',
    'huaweicloudsdkapig==3.0.98',
    'huaweicloudsdkapm==3.0.98',
    'huaweicloudsdkas==3.0.98',
    'huaweicloudsdkbcs==3.0.98',
    'huaweicloudsdkbms==3.0.98',
    'huaweicloudsdkbss==3.0.98',
    'huaweicloudsdkbssintl==3.0.98',
    'huaweicloudsdkcampusgo==3.0.98',
    'huaweicloudsdkcbh==3.0.98',
    'huaweicloudsdkcbr==3.0.98',
    'huaweicloudsdkcbs==3.0.98',
    'huaweicloudsdkcc==3.0.98',
    'huaweicloudsdkcce==3.0.98',
    'huaweicloudsdkccm==3.0.98',
    'huaweicloudsdkcdm==3.0.98',
    'huaweicloudsdkcdn==3.0.98',
    'huaweicloudsdkces==3.0.98',
    'huaweicloudsdkcgs==3.0.98',
    'huaweicloudsdkclassroom==3.0.98',
    'huaweicloudsdkcloudbuild==3.0.98',
    'huaweicloudsdkclouddeploy==3.0.98',
    'huaweicloudsdkcloudide==3.0.98',
    'huaweicloudsdkcloudpipeline==3.0.98',
    'huaweicloudsdkcloudrtc==3.0.98',
    'huaweicloudsdkcloudtable==3.0.98',
    'huaweicloudsdkcloudtest==3.0.98',
    'huaweicloudsdkcodecheck==3.0.98',
    'huaweicloudsdkcodecraft==3.0.98',
    'huaweicloudsdkcodehub==3.0.98',
    'huaweicloudsdkcpts==3.0.98',
    'huaweicloudsdkcse==3.0.98',
    'huaweicloudsdkcsms==3.0.98',
    'huaweicloudsdkcss==3.0.98',
    'huaweicloudsdkcts==3.0.98',
    'huaweicloudsdkdas==3.0.98',
    'huaweicloudsdkdbss==3.0.98',
    'huaweicloudsdkdcs==3.0.98',
    'huaweicloudsdkddm==3.0.98',
    'huaweicloudsdkdds==3.0.98',
    'huaweicloudsdkdeh==3.0.98',
    'huaweicloudsdkdevstar==3.0.98',
    'huaweicloudsdkdgc==3.0.98',
    'huaweicloudsdkdli==3.0.98',
    'huaweicloudsdkdms==3.0.98',
    'huaweicloudsdkdns==3.0.98',
    'huaweicloudsdkdrs==3.0.98',
    'huaweicloudsdkdsc==3.0.98',
    'huaweicloudsdkdws==3.0.98',
    'huaweicloudsdkecs==3.0.98',
    'huaweicloudsdkeip==3.0.98',
    'huaweicloudsdkelb==3.0.98',
    'huaweicloudsdkeps==3.0.98',
    'huaweicloudsdkevs==3.0.98',
    'huaweicloudsdkfrs==3.0.98',
    'huaweicloudsdkfunctiongraph==3.0.98',
    'huaweicloudsdkgaussdb==3.0.98',
    'huaweicloudsdkgaussdbfornosql==3.0.98',
    'huaweicloudsdkgaussdbforopengauss==3.0.98',
    'huaweicloudsdkges==3.0.98',
    'huaweicloudsdkgsl==3.0.98',
    'huaweicloudsdkhilens==3.0.98',
    'huaweicloudsdkhss==3.0.98',
    'huaweicloudsdkiam==3.0.98',
    'huaweicloudsdkiec==3.0.98',
    'huaweicloudsdkief==3.0.98',
    'huaweicloudsdkies==3.0.98',
    'huaweicloudsdkimage==3.0.98',
    'huaweicloudsdkimagesearch==3.0.98',
    'huaweicloudsdkims==3.0.98',
    'huaweicloudsdkiotanalytics==3.0.98',
    'huaweicloudsdkiotda==3.0.98',
    'huaweicloudsdkiotedge==3.0.98',
    'huaweicloudsdkivs==3.0.98',
    'huaweicloudsdkkafka==3.0.98',
    'huaweicloudsdkkms==3.0.98',
    'huaweicloudsdkkps==3.0.98',
    'huaweicloudsdklive==3.0.98',
    'huaweicloudsdklts==3.0.98',
    'huaweicloudsdkmeeting==3.0.98',
    'huaweicloudsdkmoderation==3.0.98',
    'huaweicloudsdkmpc==3.0.98',
    'huaweicloudsdkmrs==3.0.98',
    'huaweicloudsdknat==3.0.98',
    'huaweicloudsdknlp==3.0.98',
    'huaweicloudsdkocr==3.0.98',
    'huaweicloudsdkoms==3.0.98',
    'huaweicloudsdkosm==3.0.98',
    'huaweicloudsdkprojectman==3.0.98',
    'huaweicloudsdkrabbitmq==3.0.98',
    'huaweicloudsdkrds==3.0.98',
    'huaweicloudsdkres==3.0.98',
    'huaweicloudsdkrms==3.0.98',
    'huaweicloudsdkrocketmq==3.0.98',
    'huaweicloudsdkroma==3.0.98',
    'huaweicloudsdksa==3.0.98',
    'huaweicloudsdkscm==3.0.98',
    'huaweicloudsdksdrs==3.0.98',
    'huaweicloudsdkservicestage==3.0.98',
    'huaweicloudsdksfsturbo==3.0.98',
    'huaweicloudsdksis==3.0.98',
    'huaweicloudsdksmn==3.0.98',
    'huaweicloudsdksms==3.0.98',
    'huaweicloudsdkswr==3.0.98',
    'huaweicloudsdktms==3.0.98',
    'huaweicloudsdkugo==3.0.98',
    'huaweicloudsdkvas==3.0.98',
    'huaweicloudsdkvcm==3.0.98',
    'huaweicloudsdkvod==3.0.98',
    'huaweicloudsdkvpc==3.0.98',
    'huaweicloudsdkvpcep==3.0.98',
    'huaweicloudsdkvss==3.0.98',
    'huaweicloudsdkwaf==3.0.98',
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
