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
VERSION = "3.0.95"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.95',
    'huaweicloudsdkantiddos==3.0.95',
    'huaweicloudsdkaom==3.0.95',
    'huaweicloudsdkapig==3.0.95',
    'huaweicloudsdkapm==3.0.95',
    'huaweicloudsdkas==3.0.95',
    'huaweicloudsdkbcs==3.0.95',
    'huaweicloudsdkbms==3.0.95',
    'huaweicloudsdkbss==3.0.95',
    'huaweicloudsdkbssintl==3.0.95',
    'huaweicloudsdkcampusgo==3.0.95',
    'huaweicloudsdkcbh==3.0.95',
    'huaweicloudsdkcbr==3.0.95',
    'huaweicloudsdkcbs==3.0.95',
    'huaweicloudsdkcc==3.0.95',
    'huaweicloudsdkcce==3.0.95',
    'huaweicloudsdkccm==3.0.95',
    'huaweicloudsdkcdm==3.0.95',
    'huaweicloudsdkcdn==3.0.95',
    'huaweicloudsdkces==3.0.95',
    'huaweicloudsdkcgs==3.0.95',
    'huaweicloudsdkclassroom==3.0.95',
    'huaweicloudsdkcloudbuild==3.0.95',
    'huaweicloudsdkclouddeploy==3.0.95',
    'huaweicloudsdkcloudide==3.0.95',
    'huaweicloudsdkcloudpipeline==3.0.95',
    'huaweicloudsdkcloudrtc==3.0.95',
    'huaweicloudsdkcloudtable==3.0.95',
    'huaweicloudsdkcloudtest==3.0.95',
    'huaweicloudsdkcodecheck==3.0.95',
    'huaweicloudsdkcodecraft==3.0.95',
    'huaweicloudsdkcodehub==3.0.95',
    'huaweicloudsdkcpts==3.0.95',
    'huaweicloudsdkcse==3.0.95',
    'huaweicloudsdkcsms==3.0.95',
    'huaweicloudsdkcss==3.0.95',
    'huaweicloudsdkcts==3.0.95',
    'huaweicloudsdkdas==3.0.95',
    'huaweicloudsdkdbss==3.0.95',
    'huaweicloudsdkdcs==3.0.95',
    'huaweicloudsdkddm==3.0.95',
    'huaweicloudsdkdds==3.0.95',
    'huaweicloudsdkdeh==3.0.95',
    'huaweicloudsdkdevstar==3.0.95',
    'huaweicloudsdkdgc==3.0.95',
    'huaweicloudsdkdli==3.0.95',
    'huaweicloudsdkdms==3.0.95',
    'huaweicloudsdkdns==3.0.95',
    'huaweicloudsdkdrs==3.0.95',
    'huaweicloudsdkdsc==3.0.95',
    'huaweicloudsdkdws==3.0.95',
    'huaweicloudsdkecs==3.0.95',
    'huaweicloudsdkeip==3.0.95',
    'huaweicloudsdkelb==3.0.95',
    'huaweicloudsdkeps==3.0.95',
    'huaweicloudsdkevs==3.0.95',
    'huaweicloudsdkfrs==3.0.95',
    'huaweicloudsdkfunctiongraph==3.0.95',
    'huaweicloudsdkgaussdb==3.0.95',
    'huaweicloudsdkgaussdbfornosql==3.0.95',
    'huaweicloudsdkgaussdbforopengauss==3.0.95',
    'huaweicloudsdkges==3.0.95',
    'huaweicloudsdkgsl==3.0.95',
    'huaweicloudsdkhilens==3.0.95',
    'huaweicloudsdkhss==3.0.95',
    'huaweicloudsdkiam==3.0.95',
    'huaweicloudsdkiec==3.0.95',
    'huaweicloudsdkief==3.0.95',
    'huaweicloudsdkies==3.0.95',
    'huaweicloudsdkimage==3.0.95',
    'huaweicloudsdkimagesearch==3.0.95',
    'huaweicloudsdkims==3.0.95',
    'huaweicloudsdkiotanalytics==3.0.95',
    'huaweicloudsdkiotda==3.0.95',
    'huaweicloudsdkiotedge==3.0.95',
    'huaweicloudsdkivs==3.0.95',
    'huaweicloudsdkkafka==3.0.95',
    'huaweicloudsdkkms==3.0.95',
    'huaweicloudsdkkps==3.0.95',
    'huaweicloudsdklive==3.0.95',
    'huaweicloudsdklts==3.0.95',
    'huaweicloudsdkmeeting==3.0.95',
    'huaweicloudsdkmoderation==3.0.95',
    'huaweicloudsdkmpc==3.0.95',
    'huaweicloudsdkmrs==3.0.95',
    'huaweicloudsdknat==3.0.95',
    'huaweicloudsdknlp==3.0.95',
    'huaweicloudsdkocr==3.0.95',
    'huaweicloudsdkoms==3.0.95',
    'huaweicloudsdkosm==3.0.95',
    'huaweicloudsdkprojectman==3.0.95',
    'huaweicloudsdkrabbitmq==3.0.95',
    'huaweicloudsdkrds==3.0.95',
    'huaweicloudsdkres==3.0.95',
    'huaweicloudsdkrms==3.0.95',
    'huaweicloudsdkrocketmq==3.0.95',
    'huaweicloudsdkroma==3.0.95',
    'huaweicloudsdksa==3.0.95',
    'huaweicloudsdkscm==3.0.95',
    'huaweicloudsdksdrs==3.0.95',
    'huaweicloudsdkservicestage==3.0.95',
    'huaweicloudsdksfsturbo==3.0.95',
    'huaweicloudsdksis==3.0.95',
    'huaweicloudsdksmn==3.0.95',
    'huaweicloudsdksms==3.0.95',
    'huaweicloudsdkswr==3.0.95',
    'huaweicloudsdktms==3.0.95',
    'huaweicloudsdkvas==3.0.95',
    'huaweicloudsdkvod==3.0.95',
    'huaweicloudsdkvpc==3.0.95',
    'huaweicloudsdkvpcep==3.0.95',
    'huaweicloudsdkvss==3.0.95',
    'huaweicloudsdkwaf==3.0.95',
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
