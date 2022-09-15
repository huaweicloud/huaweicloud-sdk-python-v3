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
VERSION = "3.1.2"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.2',
    'huaweicloudsdkantiddos==3.1.2',
    'huaweicloudsdkaom==3.1.2',
    'huaweicloudsdkapig==3.1.2',
    'huaweicloudsdkapm==3.1.2',
    'huaweicloudsdkas==3.1.2',
    'huaweicloudsdkbcs==3.1.2',
    'huaweicloudsdkbms==3.1.2',
    'huaweicloudsdkbss==3.1.2',
    'huaweicloudsdkbssintl==3.1.2',
    'huaweicloudsdkcampusgo==3.1.2',
    'huaweicloudsdkcbh==3.1.2',
    'huaweicloudsdkcbr==3.1.2',
    'huaweicloudsdkcbs==3.1.2',
    'huaweicloudsdkcc==3.1.2',
    'huaweicloudsdkcce==3.1.2',
    'huaweicloudsdkccm==3.1.2',
    'huaweicloudsdkcdm==3.1.2',
    'huaweicloudsdkcdn==3.1.2',
    'huaweicloudsdkces==3.1.2',
    'huaweicloudsdkcgs==3.1.2',
    'huaweicloudsdkclassroom==3.1.2',
    'huaweicloudsdkcloudbuild==3.1.2',
    'huaweicloudsdkclouddeploy==3.1.2',
    'huaweicloudsdkcloudide==3.1.2',
    'huaweicloudsdkcloudpipeline==3.1.2',
    'huaweicloudsdkcloudrtc==3.1.2',
    'huaweicloudsdkcloudtable==3.1.2',
    'huaweicloudsdkcloudtest==3.1.2',
    'huaweicloudsdkcodecheck==3.1.2',
    'huaweicloudsdkcodecraft==3.1.2',
    'huaweicloudsdkcodehub==3.1.2',
    'huaweicloudsdkcph==3.1.2',
    'huaweicloudsdkcpts==3.1.2',
    'huaweicloudsdkcse==3.1.2',
    'huaweicloudsdkcsms==3.1.2',
    'huaweicloudsdkcss==3.1.2',
    'huaweicloudsdkcts==3.1.2',
    'huaweicloudsdkdas==3.1.2',
    'huaweicloudsdkdbss==3.1.2',
    'huaweicloudsdkdcs==3.1.2',
    'huaweicloudsdkddm==3.1.2',
    'huaweicloudsdkdds==3.1.2',
    'huaweicloudsdkdeh==3.1.2',
    'huaweicloudsdkdevstar==3.1.2',
    'huaweicloudsdkdgc==3.1.2',
    'huaweicloudsdkdli==3.1.2',
    'huaweicloudsdkdms==3.1.2',
    'huaweicloudsdkdns==3.1.2',
    'huaweicloudsdkdrs==3.1.2',
    'huaweicloudsdkdsc==3.1.2',
    'huaweicloudsdkdws==3.1.2',
    'huaweicloudsdkecs==3.1.2',
    'huaweicloudsdkeg==3.1.2',
    'huaweicloudsdkeip==3.1.2',
    'huaweicloudsdkelb==3.1.2',
    'huaweicloudsdkeps==3.1.2',
    'huaweicloudsdker==3.1.2',
    'huaweicloudsdkevs==3.1.2',
    'huaweicloudsdkfrs==3.1.2',
    'huaweicloudsdkfunctiongraph==3.1.2',
    'huaweicloudsdkgaussdb==3.1.2',
    'huaweicloudsdkgaussdbfornosql==3.1.2',
    'huaweicloudsdkgaussdbforopengauss==3.1.2',
    'huaweicloudsdkges==3.1.2',
    'huaweicloudsdkgsl==3.1.2',
    'huaweicloudsdkhilens==3.1.2',
    'huaweicloudsdkhss==3.1.2',
    'huaweicloudsdkiam==3.1.2',
    'huaweicloudsdkiec==3.1.2',
    'huaweicloudsdkief==3.1.2',
    'huaweicloudsdkies==3.1.2',
    'huaweicloudsdkimage==3.1.2',
    'huaweicloudsdkimagesearch==3.1.2',
    'huaweicloudsdkims==3.1.2',
    'huaweicloudsdkiotanalytics==3.1.2',
    'huaweicloudsdkiotda==3.1.2',
    'huaweicloudsdkiotedge==3.1.2',
    'huaweicloudsdkivs==3.1.2',
    'huaweicloudsdkkafka==3.1.2',
    'huaweicloudsdkkms==3.1.2',
    'huaweicloudsdkkps==3.1.2',
    'huaweicloudsdklive==3.1.2',
    'huaweicloudsdklts==3.1.2',
    'huaweicloudsdkmeeting==3.1.2',
    'huaweicloudsdkmoderation==3.1.2',
    'huaweicloudsdkmpc==3.1.2',
    'huaweicloudsdkmrs==3.1.2',
    'huaweicloudsdknat==3.1.2',
    'huaweicloudsdknlp==3.1.2',
    'huaweicloudsdkocr==3.1.2',
    'huaweicloudsdkoms==3.1.2',
    'huaweicloudsdkosm==3.1.2',
    'huaweicloudsdkprojectman==3.1.2',
    'huaweicloudsdkrabbitmq==3.1.2',
    'huaweicloudsdkrds==3.1.2',
    'huaweicloudsdkres==3.1.2',
    'huaweicloudsdkrms==3.1.2',
    'huaweicloudsdkrocketmq==3.1.2',
    'huaweicloudsdkroma==3.1.2',
    'huaweicloudsdksa==3.1.2',
    'huaweicloudsdkscm==3.1.2',
    'huaweicloudsdksdrs==3.1.2',
    'huaweicloudsdkservicestage==3.1.2',
    'huaweicloudsdksfsturbo==3.1.2',
    'huaweicloudsdksis==3.1.2',
    'huaweicloudsdksmn==3.1.2',
    'huaweicloudsdksms==3.1.2',
    'huaweicloudsdkswr==3.1.2',
    'huaweicloudsdktms==3.1.2',
    'huaweicloudsdkugo==3.1.2',
    'huaweicloudsdkvas==3.1.2',
    'huaweicloudsdkvcm==3.1.2',
    'huaweicloudsdkvod==3.1.2',
    'huaweicloudsdkvpc==3.1.2',
    'huaweicloudsdkvpcep==3.1.2',
    'huaweicloudsdkvss==3.1.2',
    'huaweicloudsdkwaf==3.1.2',
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
