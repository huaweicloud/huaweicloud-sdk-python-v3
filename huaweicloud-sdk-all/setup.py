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
VERSION = "3.1.5"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.5',
    'huaweicloudsdkantiddos==3.1.5',
    'huaweicloudsdkaom==3.1.5',
    'huaweicloudsdkapig==3.1.5',
    'huaweicloudsdkapm==3.1.5',
    'huaweicloudsdkas==3.1.5',
    'huaweicloudsdkbcs==3.1.5',
    'huaweicloudsdkbms==3.1.5',
    'huaweicloudsdkbss==3.1.5',
    'huaweicloudsdkbssintl==3.1.5',
    'huaweicloudsdkcampusgo==3.1.5',
    'huaweicloudsdkcbh==3.1.5',
    'huaweicloudsdkcbr==3.1.5',
    'huaweicloudsdkcbs==3.1.5',
    'huaweicloudsdkcc==3.1.5',
    'huaweicloudsdkcce==3.1.5',
    'huaweicloudsdkccm==3.1.5',
    'huaweicloudsdkcdm==3.1.5',
    'huaweicloudsdkcdn==3.1.5',
    'huaweicloudsdkces==3.1.5',
    'huaweicloudsdkcgs==3.1.5',
    'huaweicloudsdkclassroom==3.1.5',
    'huaweicloudsdkcloudartifact==3.1.5',
    'huaweicloudsdkcloudbuild==3.1.5',
    'huaweicloudsdkclouddeploy==3.1.5',
    'huaweicloudsdkcloudide==3.1.5',
    'huaweicloudsdkcloudpipeline==3.1.5',
    'huaweicloudsdkcloudrtc==3.1.5',
    'huaweicloudsdkcloudtable==3.1.5',
    'huaweicloudsdkcloudtest==3.1.5',
    'huaweicloudsdkcodecheck==3.1.5',
    'huaweicloudsdkcodecraft==3.1.5',
    'huaweicloudsdkcodehub==3.1.5',
    'huaweicloudsdkcph==3.1.5',
    'huaweicloudsdkcpts==3.1.5',
    'huaweicloudsdkcse==3.1.5',
    'huaweicloudsdkcsms==3.1.5',
    'huaweicloudsdkcss==3.1.5',
    'huaweicloudsdkcts==3.1.5',
    'huaweicloudsdkdas==3.1.5',
    'huaweicloudsdkdbss==3.1.5',
    'huaweicloudsdkdcs==3.1.5',
    'huaweicloudsdkddm==3.1.5',
    'huaweicloudsdkdds==3.1.5',
    'huaweicloudsdkdeh==3.1.5',
    'huaweicloudsdkdevstar==3.1.5',
    'huaweicloudsdkdgc==3.1.5',
    'huaweicloudsdkdli==3.1.5',
    'huaweicloudsdkdms==3.1.5',
    'huaweicloudsdkdns==3.1.5',
    'huaweicloudsdkdrs==3.1.5',
    'huaweicloudsdkdsc==3.1.5',
    'huaweicloudsdkdws==3.1.5',
    'huaweicloudsdkecs==3.1.5',
    'huaweicloudsdkeg==3.1.5',
    'huaweicloudsdkeihealth==3.1.5',
    'huaweicloudsdkeip==3.1.5',
    'huaweicloudsdkelb==3.1.5',
    'huaweicloudsdkeps==3.1.5',
    'huaweicloudsdker==3.1.5',
    'huaweicloudsdkevs==3.1.5',
    'huaweicloudsdkfrs==3.1.5',
    'huaweicloudsdkfunctiongraph==3.1.5',
    'huaweicloudsdkgaussdb==3.1.5',
    'huaweicloudsdkgaussdbfornosql==3.1.5',
    'huaweicloudsdkgaussdbforopengauss==3.1.5',
    'huaweicloudsdkges==3.1.5',
    'huaweicloudsdkgsl==3.1.5',
    'huaweicloudsdkhilens==3.1.5',
    'huaweicloudsdkhss==3.1.5',
    'huaweicloudsdkiam==3.1.5',
    'huaweicloudsdkiec==3.1.5',
    'huaweicloudsdkief==3.1.5',
    'huaweicloudsdkies==3.1.5',
    'huaweicloudsdkimage==3.1.5',
    'huaweicloudsdkimagesearch==3.1.5',
    'huaweicloudsdkims==3.1.5',
    'huaweicloudsdkiotanalytics==3.1.5',
    'huaweicloudsdkiotda==3.1.5',
    'huaweicloudsdkiotedge==3.1.5',
    'huaweicloudsdkivs==3.1.5',
    'huaweicloudsdkkafka==3.1.5',
    'huaweicloudsdkkms==3.1.5',
    'huaweicloudsdkkps==3.1.5',
    'huaweicloudsdklive==3.1.5',
    'huaweicloudsdklts==3.1.5',
    'huaweicloudsdkmeeting==3.1.5',
    'huaweicloudsdkmoderation==3.1.5',
    'huaweicloudsdkmpc==3.1.5',
    'huaweicloudsdkmrs==3.1.5',
    'huaweicloudsdknat==3.1.5',
    'huaweicloudsdknlp==3.1.5',
    'huaweicloudsdkocr==3.1.5',
    'huaweicloudsdkoms==3.1.5',
    'huaweicloudsdkosm==3.1.5',
    'huaweicloudsdkprojectman==3.1.5',
    'huaweicloudsdkrabbitmq==3.1.5',
    'huaweicloudsdkrds==3.1.5',
    'huaweicloudsdkres==3.1.5',
    'huaweicloudsdkrms==3.1.5',
    'huaweicloudsdkrocketmq==3.1.5',
    'huaweicloudsdkroma==3.1.5',
    'huaweicloudsdksa==3.1.5',
    'huaweicloudsdkscm==3.1.5',
    'huaweicloudsdksdrs==3.1.5',
    'huaweicloudsdkservicestage==3.1.5',
    'huaweicloudsdksfsturbo==3.1.5',
    'huaweicloudsdksis==3.1.5',
    'huaweicloudsdksmn==3.1.5',
    'huaweicloudsdksms==3.1.5',
    'huaweicloudsdkswr==3.1.5',
    'huaweicloudsdktms==3.1.5',
    'huaweicloudsdkugo==3.1.5',
    'huaweicloudsdkvas==3.1.5',
    'huaweicloudsdkvcm==3.1.5',
    'huaweicloudsdkvod==3.1.5',
    'huaweicloudsdkvpc==3.1.5',
    'huaweicloudsdkvpcep==3.1.5',
    'huaweicloudsdkvss==3.1.5',
    'huaweicloudsdkwaf==3.1.5',
    'huaweicloudsdkworkspace==3.1.5',
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
