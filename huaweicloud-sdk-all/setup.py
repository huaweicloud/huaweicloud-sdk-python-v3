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
VERSION = "3.0.88"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.88',
    'huaweicloudsdkantiddos==3.0.88',
    'huaweicloudsdkaom==3.0.88',
    'huaweicloudsdkapig==3.0.88',
    'huaweicloudsdkapm==3.0.88',
    'huaweicloudsdkas==3.0.88',
    'huaweicloudsdkbcs==3.0.88',
    'huaweicloudsdkbms==3.0.88',
    'huaweicloudsdkbss==3.0.88',
    'huaweicloudsdkbssintl==3.0.88',
    'huaweicloudsdkcampusgo==3.0.88',
    'huaweicloudsdkcbh==3.0.88',
    'huaweicloudsdkcbr==3.0.88',
    'huaweicloudsdkcbs==3.0.88',
    'huaweicloudsdkcc==3.0.88',
    'huaweicloudsdkcce==3.0.88',
    'huaweicloudsdkccm==3.0.88',
    'huaweicloudsdkcdm==3.0.88',
    'huaweicloudsdkcdn==3.0.88',
    'huaweicloudsdkces==3.0.88',
    'huaweicloudsdkcgs==3.0.88',
    'huaweicloudsdkclassroom==3.0.88',
    'huaweicloudsdkcloudbuild==3.0.88',
    'huaweicloudsdkclouddeploy==3.0.88',
    'huaweicloudsdkcloudide==3.0.88',
    'huaweicloudsdkcloudpipeline==3.0.88',
    'huaweicloudsdkcloudrtc==3.0.88',
    'huaweicloudsdkcloudtable==3.0.88',
    'huaweicloudsdkcloudtest==3.0.88',
    'huaweicloudsdkcodecheck==3.0.88',
    'huaweicloudsdkcodecraft==3.0.88',
    'huaweicloudsdkcodehub==3.0.88',
    'huaweicloudsdkcpts==3.0.88',
    'huaweicloudsdkcse==3.0.88',
    'huaweicloudsdkcsms==3.0.88',
    'huaweicloudsdkcss==3.0.88',
    'huaweicloudsdkcts==3.0.88',
    'huaweicloudsdkdas==3.0.88',
    'huaweicloudsdkdbss==3.0.88',
    'huaweicloudsdkdcs==3.0.88',
    'huaweicloudsdkddm==3.0.88',
    'huaweicloudsdkdds==3.0.88',
    'huaweicloudsdkdeh==3.0.88',
    'huaweicloudsdkdevstar==3.0.88',
    'huaweicloudsdkdgc==3.0.88',
    'huaweicloudsdkdms==3.0.88',
    'huaweicloudsdkdns==3.0.88',
    'huaweicloudsdkdrs==3.0.88',
    'huaweicloudsdkdsc==3.0.88',
    'huaweicloudsdkdws==3.0.88',
    'huaweicloudsdkecs==3.0.88',
    'huaweicloudsdkeip==3.0.88',
    'huaweicloudsdkelb==3.0.88',
    'huaweicloudsdkeps==3.0.88',
    'huaweicloudsdkevs==3.0.88',
    'huaweicloudsdkfrs==3.0.88',
    'huaweicloudsdkfunctiongraph==3.0.88',
    'huaweicloudsdkgaussdb==3.0.88',
    'huaweicloudsdkgaussdbfornosql==3.0.88',
    'huaweicloudsdkgaussdbforopengauss==3.0.88',
    'huaweicloudsdkges==3.0.88',
    'huaweicloudsdkgsl==3.0.88',
    'huaweicloudsdkhilens==3.0.88',
    'huaweicloudsdkhss==3.0.88',
    'huaweicloudsdkiam==3.0.88',
    'huaweicloudsdkiec==3.0.88',
    'huaweicloudsdkief==3.0.88',
    'huaweicloudsdkies==3.0.88',
    'huaweicloudsdkimage==3.0.88',
    'huaweicloudsdkimagesearch==3.0.88',
    'huaweicloudsdkims==3.0.88',
    'huaweicloudsdkiotanalytics==3.0.88',
    'huaweicloudsdkiotda==3.0.88',
    'huaweicloudsdkiotedge==3.0.88',
    'huaweicloudsdkivs==3.0.88',
    'huaweicloudsdkkafka==3.0.88',
    'huaweicloudsdkkms==3.0.88',
    'huaweicloudsdkkps==3.0.88',
    'huaweicloudsdklive==3.0.88',
    'huaweicloudsdklts==3.0.88',
    'huaweicloudsdkmeeting==3.0.88',
    'huaweicloudsdkmoderation==3.0.88',
    'huaweicloudsdkmpc==3.0.88',
    'huaweicloudsdkmrs==3.0.88',
    'huaweicloudsdknat==3.0.88',
    'huaweicloudsdknlp==3.0.88',
    'huaweicloudsdkocr==3.0.88',
    'huaweicloudsdkoms==3.0.88',
    'huaweicloudsdkosm==3.0.88',
    'huaweicloudsdkprojectman==3.0.88',
    'huaweicloudsdkrabbitmq==3.0.88',
    'huaweicloudsdkrds==3.0.88',
    'huaweicloudsdkres==3.0.88',
    'huaweicloudsdkrms==3.0.88',
    'huaweicloudsdkrocketmq==3.0.88',
    'huaweicloudsdkroma==3.0.88',
    'huaweicloudsdksa==3.0.88',
    'huaweicloudsdkscm==3.0.88',
    'huaweicloudsdksdrs==3.0.88',
    'huaweicloudsdkservicestage==3.0.88',
    'huaweicloudsdksfsturbo==3.0.88',
    'huaweicloudsdksis==3.0.88',
    'huaweicloudsdksmn==3.0.88',
    'huaweicloudsdksms==3.0.88',
    'huaweicloudsdkswr==3.0.88',
    'huaweicloudsdktms==3.0.88',
    'huaweicloudsdkvas==3.0.88',
    'huaweicloudsdkvod==3.0.88',
    'huaweicloudsdkvpc==3.0.88',
    'huaweicloudsdkvpcep==3.0.88',
    'huaweicloudsdkvss==3.0.88',
    'huaweicloudsdkwaf==3.0.88',
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
