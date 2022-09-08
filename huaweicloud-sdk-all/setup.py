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
VERSION = "3.1.1"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.1',
    'huaweicloudsdkantiddos==3.1.1',
    'huaweicloudsdkaom==3.1.1',
    'huaweicloudsdkapig==3.1.1',
    'huaweicloudsdkapm==3.1.1',
    'huaweicloudsdkas==3.1.1',
    'huaweicloudsdkbcs==3.1.1',
    'huaweicloudsdkbms==3.1.1',
    'huaweicloudsdkbss==3.1.1',
    'huaweicloudsdkbssintl==3.1.1',
    'huaweicloudsdkcampusgo==3.1.1',
    'huaweicloudsdkcbh==3.1.1',
    'huaweicloudsdkcbr==3.1.1',
    'huaweicloudsdkcbs==3.1.1',
    'huaweicloudsdkcc==3.1.1',
    'huaweicloudsdkcce==3.1.1',
    'huaweicloudsdkccm==3.1.1',
    'huaweicloudsdkcdm==3.1.1',
    'huaweicloudsdkcdn==3.1.1',
    'huaweicloudsdkces==3.1.1',
    'huaweicloudsdkcgs==3.1.1',
    'huaweicloudsdkclassroom==3.1.1',
    'huaweicloudsdkcloudbuild==3.1.1',
    'huaweicloudsdkclouddeploy==3.1.1',
    'huaweicloudsdkcloudide==3.1.1',
    'huaweicloudsdkcloudpipeline==3.1.1',
    'huaweicloudsdkcloudrtc==3.1.1',
    'huaweicloudsdkcloudtable==3.1.1',
    'huaweicloudsdkcloudtest==3.1.1',
    'huaweicloudsdkcodecheck==3.1.1',
    'huaweicloudsdkcodecraft==3.1.1',
    'huaweicloudsdkcodehub==3.1.1',
    'huaweicloudsdkcph==3.1.1',
    'huaweicloudsdkcpts==3.1.1',
    'huaweicloudsdkcse==3.1.1',
    'huaweicloudsdkcsms==3.1.1',
    'huaweicloudsdkcss==3.1.1',
    'huaweicloudsdkcts==3.1.1',
    'huaweicloudsdkdas==3.1.1',
    'huaweicloudsdkdbss==3.1.1',
    'huaweicloudsdkdcs==3.1.1',
    'huaweicloudsdkddm==3.1.1',
    'huaweicloudsdkdds==3.1.1',
    'huaweicloudsdkdeh==3.1.1',
    'huaweicloudsdkdevstar==3.1.1',
    'huaweicloudsdkdgc==3.1.1',
    'huaweicloudsdkdli==3.1.1',
    'huaweicloudsdkdms==3.1.1',
    'huaweicloudsdkdns==3.1.1',
    'huaweicloudsdkdrs==3.1.1',
    'huaweicloudsdkdsc==3.1.1',
    'huaweicloudsdkdws==3.1.1',
    'huaweicloudsdkecs==3.1.1',
    'huaweicloudsdkeg==3.1.1',
    'huaweicloudsdkeip==3.1.1',
    'huaweicloudsdkelb==3.1.1',
    'huaweicloudsdkeps==3.1.1',
    'huaweicloudsdker==3.1.1',
    'huaweicloudsdkevs==3.1.1',
    'huaweicloudsdkfrs==3.1.1',
    'huaweicloudsdkfunctiongraph==3.1.1',
    'huaweicloudsdkgaussdb==3.1.1',
    'huaweicloudsdkgaussdbfornosql==3.1.1',
    'huaweicloudsdkgaussdbforopengauss==3.1.1',
    'huaweicloudsdkges==3.1.1',
    'huaweicloudsdkgsl==3.1.1',
    'huaweicloudsdkhilens==3.1.1',
    'huaweicloudsdkhss==3.1.1',
    'huaweicloudsdkiam==3.1.1',
    'huaweicloudsdkiec==3.1.1',
    'huaweicloudsdkief==3.1.1',
    'huaweicloudsdkies==3.1.1',
    'huaweicloudsdkimage==3.1.1',
    'huaweicloudsdkimagesearch==3.1.1',
    'huaweicloudsdkims==3.1.1',
    'huaweicloudsdkiotanalytics==3.1.1',
    'huaweicloudsdkiotda==3.1.1',
    'huaweicloudsdkiotedge==3.1.1',
    'huaweicloudsdkivs==3.1.1',
    'huaweicloudsdkkafka==3.1.1',
    'huaweicloudsdkkms==3.1.1',
    'huaweicloudsdkkps==3.1.1',
    'huaweicloudsdklive==3.1.1',
    'huaweicloudsdklts==3.1.1',
    'huaweicloudsdkmeeting==3.1.1',
    'huaweicloudsdkmoderation==3.1.1',
    'huaweicloudsdkmpc==3.1.1',
    'huaweicloudsdkmrs==3.1.1',
    'huaweicloudsdknat==3.1.1',
    'huaweicloudsdknlp==3.1.1',
    'huaweicloudsdkocr==3.1.1',
    'huaweicloudsdkoms==3.1.1',
    'huaweicloudsdkosm==3.1.1',
    'huaweicloudsdkprojectman==3.1.1',
    'huaweicloudsdkrabbitmq==3.1.1',
    'huaweicloudsdkrds==3.1.1',
    'huaweicloudsdkres==3.1.1',
    'huaweicloudsdkrms==3.1.1',
    'huaweicloudsdkrocketmq==3.1.1',
    'huaweicloudsdkroma==3.1.1',
    'huaweicloudsdksa==3.1.1',
    'huaweicloudsdkscm==3.1.1',
    'huaweicloudsdksdrs==3.1.1',
    'huaweicloudsdkservicestage==3.1.1',
    'huaweicloudsdksfsturbo==3.1.1',
    'huaweicloudsdksis==3.1.1',
    'huaweicloudsdksmn==3.1.1',
    'huaweicloudsdksms==3.1.1',
    'huaweicloudsdkswr==3.1.1',
    'huaweicloudsdktms==3.1.1',
    'huaweicloudsdkugo==3.1.1',
    'huaweicloudsdkvas==3.1.1',
    'huaweicloudsdkvcm==3.1.1',
    'huaweicloudsdkvod==3.1.1',
    'huaweicloudsdkvpc==3.1.1',
    'huaweicloudsdkvpcep==3.1.1',
    'huaweicloudsdkvss==3.1.1',
    'huaweicloudsdkwaf==3.1.1',
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
