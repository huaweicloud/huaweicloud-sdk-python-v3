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
VERSION = "3.0.93"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.93',
    'huaweicloudsdkantiddos==3.0.93',
    'huaweicloudsdkaom==3.0.93',
    'huaweicloudsdkapig==3.0.93',
    'huaweicloudsdkapm==3.0.93',
    'huaweicloudsdkas==3.0.93',
    'huaweicloudsdkbcs==3.0.93',
    'huaweicloudsdkbms==3.0.93',
    'huaweicloudsdkbss==3.0.93',
    'huaweicloudsdkbssintl==3.0.93',
    'huaweicloudsdkcampusgo==3.0.93',
    'huaweicloudsdkcbh==3.0.93',
    'huaweicloudsdkcbr==3.0.93',
    'huaweicloudsdkcbs==3.0.93',
    'huaweicloudsdkcc==3.0.93',
    'huaweicloudsdkcce==3.0.93',
    'huaweicloudsdkccm==3.0.93',
    'huaweicloudsdkcdm==3.0.93',
    'huaweicloudsdkcdn==3.0.93',
    'huaweicloudsdkces==3.0.93',
    'huaweicloudsdkcgs==3.0.93',
    'huaweicloudsdkclassroom==3.0.93',
    'huaweicloudsdkcloudbuild==3.0.93',
    'huaweicloudsdkclouddeploy==3.0.93',
    'huaweicloudsdkcloudide==3.0.93',
    'huaweicloudsdkcloudpipeline==3.0.93',
    'huaweicloudsdkcloudrtc==3.0.93',
    'huaweicloudsdkcloudtable==3.0.93',
    'huaweicloudsdkcloudtest==3.0.93',
    'huaweicloudsdkcodecheck==3.0.93',
    'huaweicloudsdkcodecraft==3.0.93',
    'huaweicloudsdkcodehub==3.0.93',
    'huaweicloudsdkcpts==3.0.93',
    'huaweicloudsdkcse==3.0.93',
    'huaweicloudsdkcsms==3.0.93',
    'huaweicloudsdkcss==3.0.93',
    'huaweicloudsdkcts==3.0.93',
    'huaweicloudsdkdas==3.0.93',
    'huaweicloudsdkdbss==3.0.93',
    'huaweicloudsdkdcs==3.0.93',
    'huaweicloudsdkddm==3.0.93',
    'huaweicloudsdkdds==3.0.93',
    'huaweicloudsdkdeh==3.0.93',
    'huaweicloudsdkdevstar==3.0.93',
    'huaweicloudsdkdgc==3.0.93',
    'huaweicloudsdkdms==3.0.93',
    'huaweicloudsdkdns==3.0.93',
    'huaweicloudsdkdrs==3.0.93',
    'huaweicloudsdkdsc==3.0.93',
    'huaweicloudsdkdws==3.0.93',
    'huaweicloudsdkecs==3.0.93',
    'huaweicloudsdkeip==3.0.93',
    'huaweicloudsdkelb==3.0.93',
    'huaweicloudsdkeps==3.0.93',
    'huaweicloudsdkevs==3.0.93',
    'huaweicloudsdkfrs==3.0.93',
    'huaweicloudsdkfunctiongraph==3.0.93',
    'huaweicloudsdkgaussdb==3.0.93',
    'huaweicloudsdkgaussdbfornosql==3.0.93',
    'huaweicloudsdkgaussdbforopengauss==3.0.93',
    'huaweicloudsdkges==3.0.93',
    'huaweicloudsdkgsl==3.0.93',
    'huaweicloudsdkhilens==3.0.93',
    'huaweicloudsdkhss==3.0.93',
    'huaweicloudsdkiam==3.0.93',
    'huaweicloudsdkiec==3.0.93',
    'huaweicloudsdkief==3.0.93',
    'huaweicloudsdkies==3.0.93',
    'huaweicloudsdkimage==3.0.93',
    'huaweicloudsdkimagesearch==3.0.93',
    'huaweicloudsdkims==3.0.93',
    'huaweicloudsdkiotanalytics==3.0.93',
    'huaweicloudsdkiotda==3.0.93',
    'huaweicloudsdkiotedge==3.0.93',
    'huaweicloudsdkivs==3.0.93',
    'huaweicloudsdkkafka==3.0.93',
    'huaweicloudsdkkms==3.0.93',
    'huaweicloudsdkkps==3.0.93',
    'huaweicloudsdklive==3.0.93',
    'huaweicloudsdklts==3.0.93',
    'huaweicloudsdkmeeting==3.0.93',
    'huaweicloudsdkmoderation==3.0.93',
    'huaweicloudsdkmpc==3.0.93',
    'huaweicloudsdkmrs==3.0.93',
    'huaweicloudsdknat==3.0.93',
    'huaweicloudsdknlp==3.0.93',
    'huaweicloudsdkocr==3.0.93',
    'huaweicloudsdkoms==3.0.93',
    'huaweicloudsdkosm==3.0.93',
    'huaweicloudsdkprojectman==3.0.93',
    'huaweicloudsdkrabbitmq==3.0.93',
    'huaweicloudsdkrds==3.0.93',
    'huaweicloudsdkres==3.0.93',
    'huaweicloudsdkrms==3.0.93',
    'huaweicloudsdkrocketmq==3.0.93',
    'huaweicloudsdkroma==3.0.93',
    'huaweicloudsdksa==3.0.93',
    'huaweicloudsdkscm==3.0.93',
    'huaweicloudsdksdrs==3.0.93',
    'huaweicloudsdkservicestage==3.0.93',
    'huaweicloudsdksfsturbo==3.0.93',
    'huaweicloudsdksis==3.0.93',
    'huaweicloudsdksmn==3.0.93',
    'huaweicloudsdksms==3.0.93',
    'huaweicloudsdkswr==3.0.93',
    'huaweicloudsdktms==3.0.93',
    'huaweicloudsdkvas==3.0.93',
    'huaweicloudsdkvod==3.0.93',
    'huaweicloudsdkvpc==3.0.93',
    'huaweicloudsdkvpcep==3.0.93',
    'huaweicloudsdkvss==3.0.93',
    'huaweicloudsdkwaf==3.0.93',
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
