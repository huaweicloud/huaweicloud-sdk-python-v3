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
VERSION = "3.0.90"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.90',
    'huaweicloudsdkantiddos==3.0.90',
    'huaweicloudsdkaom==3.0.90',
    'huaweicloudsdkapig==3.0.90',
    'huaweicloudsdkapm==3.0.90',
    'huaweicloudsdkas==3.0.90',
    'huaweicloudsdkbcs==3.0.90',
    'huaweicloudsdkbms==3.0.90',
    'huaweicloudsdkbss==3.0.90',
    'huaweicloudsdkbssintl==3.0.90',
    'huaweicloudsdkcampusgo==3.0.90',
    'huaweicloudsdkcbh==3.0.90',
    'huaweicloudsdkcbr==3.0.90',
    'huaweicloudsdkcbs==3.0.90',
    'huaweicloudsdkcc==3.0.90',
    'huaweicloudsdkcce==3.0.90',
    'huaweicloudsdkccm==3.0.90',
    'huaweicloudsdkcdm==3.0.90',
    'huaweicloudsdkcdn==3.0.90',
    'huaweicloudsdkces==3.0.90',
    'huaweicloudsdkcgs==3.0.90',
    'huaweicloudsdkclassroom==3.0.90',
    'huaweicloudsdkcloudbuild==3.0.90',
    'huaweicloudsdkclouddeploy==3.0.90',
    'huaweicloudsdkcloudide==3.0.90',
    'huaweicloudsdkcloudpipeline==3.0.90',
    'huaweicloudsdkcloudrtc==3.0.90',
    'huaweicloudsdkcloudtable==3.0.90',
    'huaweicloudsdkcloudtest==3.0.90',
    'huaweicloudsdkcodecheck==3.0.90',
    'huaweicloudsdkcodecraft==3.0.90',
    'huaweicloudsdkcodehub==3.0.90',
    'huaweicloudsdkcpts==3.0.90',
    'huaweicloudsdkcse==3.0.90',
    'huaweicloudsdkcsms==3.0.90',
    'huaweicloudsdkcss==3.0.90',
    'huaweicloudsdkcts==3.0.90',
    'huaweicloudsdkdas==3.0.90',
    'huaweicloudsdkdbss==3.0.90',
    'huaweicloudsdkdcs==3.0.90',
    'huaweicloudsdkddm==3.0.90',
    'huaweicloudsdkdds==3.0.90',
    'huaweicloudsdkdeh==3.0.90',
    'huaweicloudsdkdevstar==3.0.90',
    'huaweicloudsdkdgc==3.0.90',
    'huaweicloudsdkdms==3.0.90',
    'huaweicloudsdkdns==3.0.90',
    'huaweicloudsdkdrs==3.0.90',
    'huaweicloudsdkdsc==3.0.90',
    'huaweicloudsdkdws==3.0.90',
    'huaweicloudsdkecs==3.0.90',
    'huaweicloudsdkeip==3.0.90',
    'huaweicloudsdkelb==3.0.90',
    'huaweicloudsdkeps==3.0.90',
    'huaweicloudsdkevs==3.0.90',
    'huaweicloudsdkfrs==3.0.90',
    'huaweicloudsdkfunctiongraph==3.0.90',
    'huaweicloudsdkgaussdb==3.0.90',
    'huaweicloudsdkgaussdbfornosql==3.0.90',
    'huaweicloudsdkgaussdbforopengauss==3.0.90',
    'huaweicloudsdkges==3.0.90',
    'huaweicloudsdkgsl==3.0.90',
    'huaweicloudsdkhilens==3.0.90',
    'huaweicloudsdkhss==3.0.90',
    'huaweicloudsdkiam==3.0.90',
    'huaweicloudsdkiec==3.0.90',
    'huaweicloudsdkief==3.0.90',
    'huaweicloudsdkies==3.0.90',
    'huaweicloudsdkimage==3.0.90',
    'huaweicloudsdkimagesearch==3.0.90',
    'huaweicloudsdkims==3.0.90',
    'huaweicloudsdkiotanalytics==3.0.90',
    'huaweicloudsdkiotda==3.0.90',
    'huaweicloudsdkiotedge==3.0.90',
    'huaweicloudsdkivs==3.0.90',
    'huaweicloudsdkkafka==3.0.90',
    'huaweicloudsdkkms==3.0.90',
    'huaweicloudsdkkps==3.0.90',
    'huaweicloudsdklive==3.0.90',
    'huaweicloudsdklts==3.0.90',
    'huaweicloudsdkmeeting==3.0.90',
    'huaweicloudsdkmoderation==3.0.90',
    'huaweicloudsdkmpc==3.0.90',
    'huaweicloudsdkmrs==3.0.90',
    'huaweicloudsdknat==3.0.90',
    'huaweicloudsdknlp==3.0.90',
    'huaweicloudsdkocr==3.0.90',
    'huaweicloudsdkoms==3.0.90',
    'huaweicloudsdkosm==3.0.90',
    'huaweicloudsdkprojectman==3.0.90',
    'huaweicloudsdkrabbitmq==3.0.90',
    'huaweicloudsdkrds==3.0.90',
    'huaweicloudsdkres==3.0.90',
    'huaweicloudsdkrms==3.0.90',
    'huaweicloudsdkrocketmq==3.0.90',
    'huaweicloudsdkroma==3.0.90',
    'huaweicloudsdksa==3.0.90',
    'huaweicloudsdkscm==3.0.90',
    'huaweicloudsdksdrs==3.0.90',
    'huaweicloudsdkservicestage==3.0.90',
    'huaweicloudsdksfsturbo==3.0.90',
    'huaweicloudsdksis==3.0.90',
    'huaweicloudsdksmn==3.0.90',
    'huaweicloudsdksms==3.0.90',
    'huaweicloudsdkswr==3.0.90',
    'huaweicloudsdktms==3.0.90',
    'huaweicloudsdkvas==3.0.90',
    'huaweicloudsdkvod==3.0.90',
    'huaweicloudsdkvpc==3.0.90',
    'huaweicloudsdkvpcep==3.0.90',
    'huaweicloudsdkvss==3.0.90',
    'huaweicloudsdkwaf==3.0.90',
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
