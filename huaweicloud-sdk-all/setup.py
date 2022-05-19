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
VERSION = "3.0.89"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.89',
    'huaweicloudsdkantiddos==3.0.89',
    'huaweicloudsdkaom==3.0.89',
    'huaweicloudsdkapig==3.0.89',
    'huaweicloudsdkapm==3.0.89',
    'huaweicloudsdkas==3.0.89',
    'huaweicloudsdkbcs==3.0.89',
    'huaweicloudsdkbms==3.0.89',
    'huaweicloudsdkbss==3.0.89',
    'huaweicloudsdkbssintl==3.0.89',
    'huaweicloudsdkcampusgo==3.0.89',
    'huaweicloudsdkcbh==3.0.89',
    'huaweicloudsdkcbr==3.0.89',
    'huaweicloudsdkcbs==3.0.89',
    'huaweicloudsdkcc==3.0.89',
    'huaweicloudsdkcce==3.0.89',
    'huaweicloudsdkccm==3.0.89',
    'huaweicloudsdkcdm==3.0.89',
    'huaweicloudsdkcdn==3.0.89',
    'huaweicloudsdkces==3.0.89',
    'huaweicloudsdkcgs==3.0.89',
    'huaweicloudsdkclassroom==3.0.89',
    'huaweicloudsdkcloudbuild==3.0.89',
    'huaweicloudsdkclouddeploy==3.0.89',
    'huaweicloudsdkcloudide==3.0.89',
    'huaweicloudsdkcloudpipeline==3.0.89',
    'huaweicloudsdkcloudrtc==3.0.89',
    'huaweicloudsdkcloudtable==3.0.89',
    'huaweicloudsdkcloudtest==3.0.89',
    'huaweicloudsdkcodecheck==3.0.89',
    'huaweicloudsdkcodecraft==3.0.89',
    'huaweicloudsdkcodehub==3.0.89',
    'huaweicloudsdkcpts==3.0.89',
    'huaweicloudsdkcse==3.0.89',
    'huaweicloudsdkcsms==3.0.89',
    'huaweicloudsdkcss==3.0.89',
    'huaweicloudsdkcts==3.0.89',
    'huaweicloudsdkdas==3.0.89',
    'huaweicloudsdkdbss==3.0.89',
    'huaweicloudsdkdcs==3.0.89',
    'huaweicloudsdkddm==3.0.89',
    'huaweicloudsdkdds==3.0.89',
    'huaweicloudsdkdeh==3.0.89',
    'huaweicloudsdkdevstar==3.0.89',
    'huaweicloudsdkdgc==3.0.89',
    'huaweicloudsdkdms==3.0.89',
    'huaweicloudsdkdns==3.0.89',
    'huaweicloudsdkdrs==3.0.89',
    'huaweicloudsdkdsc==3.0.89',
    'huaweicloudsdkdws==3.0.89',
    'huaweicloudsdkecs==3.0.89',
    'huaweicloudsdkeip==3.0.89',
    'huaweicloudsdkelb==3.0.89',
    'huaweicloudsdkeps==3.0.89',
    'huaweicloudsdkevs==3.0.89',
    'huaweicloudsdkfrs==3.0.89',
    'huaweicloudsdkfunctiongraph==3.0.89',
    'huaweicloudsdkgaussdb==3.0.89',
    'huaweicloudsdkgaussdbfornosql==3.0.89',
    'huaweicloudsdkgaussdbforopengauss==3.0.89',
    'huaweicloudsdkges==3.0.89',
    'huaweicloudsdkgsl==3.0.89',
    'huaweicloudsdkhilens==3.0.89',
    'huaweicloudsdkhss==3.0.89',
    'huaweicloudsdkiam==3.0.89',
    'huaweicloudsdkiec==3.0.89',
    'huaweicloudsdkief==3.0.89',
    'huaweicloudsdkies==3.0.89',
    'huaweicloudsdkimage==3.0.89',
    'huaweicloudsdkimagesearch==3.0.89',
    'huaweicloudsdkims==3.0.89',
    'huaweicloudsdkiotanalytics==3.0.89',
    'huaweicloudsdkiotda==3.0.89',
    'huaweicloudsdkiotedge==3.0.89',
    'huaweicloudsdkivs==3.0.89',
    'huaweicloudsdkkafka==3.0.89',
    'huaweicloudsdkkms==3.0.89',
    'huaweicloudsdkkps==3.0.89',
    'huaweicloudsdklive==3.0.89',
    'huaweicloudsdklts==3.0.89',
    'huaweicloudsdkmeeting==3.0.89',
    'huaweicloudsdkmoderation==3.0.89',
    'huaweicloudsdkmpc==3.0.89',
    'huaweicloudsdkmrs==3.0.89',
    'huaweicloudsdknat==3.0.89',
    'huaweicloudsdknlp==3.0.89',
    'huaweicloudsdkocr==3.0.89',
    'huaweicloudsdkoms==3.0.89',
    'huaweicloudsdkosm==3.0.89',
    'huaweicloudsdkprojectman==3.0.89',
    'huaweicloudsdkrabbitmq==3.0.89',
    'huaweicloudsdkrds==3.0.89',
    'huaweicloudsdkres==3.0.89',
    'huaweicloudsdkrms==3.0.89',
    'huaweicloudsdkrocketmq==3.0.89',
    'huaweicloudsdkroma==3.0.89',
    'huaweicloudsdksa==3.0.89',
    'huaweicloudsdkscm==3.0.89',
    'huaweicloudsdksdrs==3.0.89',
    'huaweicloudsdkservicestage==3.0.89',
    'huaweicloudsdksfsturbo==3.0.89',
    'huaweicloudsdksis==3.0.89',
    'huaweicloudsdksmn==3.0.89',
    'huaweicloudsdksms==3.0.89',
    'huaweicloudsdkswr==3.0.89',
    'huaweicloudsdktms==3.0.89',
    'huaweicloudsdkvas==3.0.89',
    'huaweicloudsdkvod==3.0.89',
    'huaweicloudsdkvpc==3.0.89',
    'huaweicloudsdkvpcep==3.0.89',
    'huaweicloudsdkvss==3.0.89',
    'huaweicloudsdkwaf==3.0.89',
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
