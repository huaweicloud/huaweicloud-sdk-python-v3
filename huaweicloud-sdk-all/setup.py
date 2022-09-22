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
VERSION = "3.1.3"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.3',
    'huaweicloudsdkantiddos==3.1.3',
    'huaweicloudsdkaom==3.1.3',
    'huaweicloudsdkapig==3.1.3',
    'huaweicloudsdkapm==3.1.3',
    'huaweicloudsdkas==3.1.3',
    'huaweicloudsdkbcs==3.1.3',
    'huaweicloudsdkbms==3.1.3',
    'huaweicloudsdkbss==3.1.3',
    'huaweicloudsdkbssintl==3.1.3',
    'huaweicloudsdkcampusgo==3.1.3',
    'huaweicloudsdkcbh==3.1.3',
    'huaweicloudsdkcbr==3.1.3',
    'huaweicloudsdkcbs==3.1.3',
    'huaweicloudsdkcc==3.1.3',
    'huaweicloudsdkcce==3.1.3',
    'huaweicloudsdkccm==3.1.3',
    'huaweicloudsdkcdm==3.1.3',
    'huaweicloudsdkcdn==3.1.3',
    'huaweicloudsdkces==3.1.3',
    'huaweicloudsdkcgs==3.1.3',
    'huaweicloudsdkclassroom==3.1.3',
    'huaweicloudsdkcloudbuild==3.1.3',
    'huaweicloudsdkclouddeploy==3.1.3',
    'huaweicloudsdkcloudide==3.1.3',
    'huaweicloudsdkcloudpipeline==3.1.3',
    'huaweicloudsdkcloudrtc==3.1.3',
    'huaweicloudsdkcloudtable==3.1.3',
    'huaweicloudsdkcloudtest==3.1.3',
    'huaweicloudsdkcodecheck==3.1.3',
    'huaweicloudsdkcodecraft==3.1.3',
    'huaweicloudsdkcodehub==3.1.3',
    'huaweicloudsdkcph==3.1.3',
    'huaweicloudsdkcpts==3.1.3',
    'huaweicloudsdkcse==3.1.3',
    'huaweicloudsdkcsms==3.1.3',
    'huaweicloudsdkcss==3.1.3',
    'huaweicloudsdkcts==3.1.3',
    'huaweicloudsdkdas==3.1.3',
    'huaweicloudsdkdbss==3.1.3',
    'huaweicloudsdkdcs==3.1.3',
    'huaweicloudsdkddm==3.1.3',
    'huaweicloudsdkdds==3.1.3',
    'huaweicloudsdkdeh==3.1.3',
    'huaweicloudsdkdevstar==3.1.3',
    'huaweicloudsdkdgc==3.1.3',
    'huaweicloudsdkdli==3.1.3',
    'huaweicloudsdkdms==3.1.3',
    'huaweicloudsdkdns==3.1.3',
    'huaweicloudsdkdrs==3.1.3',
    'huaweicloudsdkdsc==3.1.3',
    'huaweicloudsdkdws==3.1.3',
    'huaweicloudsdkecs==3.1.3',
    'huaweicloudsdkeg==3.1.3',
    'huaweicloudsdkeip==3.1.3',
    'huaweicloudsdkelb==3.1.3',
    'huaweicloudsdkeps==3.1.3',
    'huaweicloudsdker==3.1.3',
    'huaweicloudsdkevs==3.1.3',
    'huaweicloudsdkfrs==3.1.3',
    'huaweicloudsdkfunctiongraph==3.1.3',
    'huaweicloudsdkgaussdb==3.1.3',
    'huaweicloudsdkgaussdbfornosql==3.1.3',
    'huaweicloudsdkgaussdbforopengauss==3.1.3',
    'huaweicloudsdkges==3.1.3',
    'huaweicloudsdkgsl==3.1.3',
    'huaweicloudsdkhilens==3.1.3',
    'huaweicloudsdkhss==3.1.3',
    'huaweicloudsdkiam==3.1.3',
    'huaweicloudsdkiec==3.1.3',
    'huaweicloudsdkief==3.1.3',
    'huaweicloudsdkies==3.1.3',
    'huaweicloudsdkimage==3.1.3',
    'huaweicloudsdkimagesearch==3.1.3',
    'huaweicloudsdkims==3.1.3',
    'huaweicloudsdkiotanalytics==3.1.3',
    'huaweicloudsdkiotda==3.1.3',
    'huaweicloudsdkiotedge==3.1.3',
    'huaweicloudsdkivs==3.1.3',
    'huaweicloudsdkkafka==3.1.3',
    'huaweicloudsdkkms==3.1.3',
    'huaweicloudsdkkps==3.1.3',
    'huaweicloudsdklive==3.1.3',
    'huaweicloudsdklts==3.1.3',
    'huaweicloudsdkmeeting==3.1.3',
    'huaweicloudsdkmoderation==3.1.3',
    'huaweicloudsdkmpc==3.1.3',
    'huaweicloudsdkmrs==3.1.3',
    'huaweicloudsdknat==3.1.3',
    'huaweicloudsdknlp==3.1.3',
    'huaweicloudsdkocr==3.1.3',
    'huaweicloudsdkoms==3.1.3',
    'huaweicloudsdkosm==3.1.3',
    'huaweicloudsdkprojectman==3.1.3',
    'huaweicloudsdkrabbitmq==3.1.3',
    'huaweicloudsdkrds==3.1.3',
    'huaweicloudsdkres==3.1.3',
    'huaweicloudsdkrms==3.1.3',
    'huaweicloudsdkrocketmq==3.1.3',
    'huaweicloudsdkroma==3.1.3',
    'huaweicloudsdksa==3.1.3',
    'huaweicloudsdkscm==3.1.3',
    'huaweicloudsdksdrs==3.1.3',
    'huaweicloudsdkservicestage==3.1.3',
    'huaweicloudsdksfsturbo==3.1.3',
    'huaweicloudsdksis==3.1.3',
    'huaweicloudsdksmn==3.1.3',
    'huaweicloudsdksms==3.1.3',
    'huaweicloudsdkswr==3.1.3',
    'huaweicloudsdktms==3.1.3',
    'huaweicloudsdkugo==3.1.3',
    'huaweicloudsdkvas==3.1.3',
    'huaweicloudsdkvcm==3.1.3',
    'huaweicloudsdkvod==3.1.3',
    'huaweicloudsdkvpc==3.1.3',
    'huaweicloudsdkvpcep==3.1.3',
    'huaweicloudsdkvss==3.1.3',
    'huaweicloudsdkwaf==3.1.3',
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
