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
VERSION = "3.1.7"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.7',
    'huaweicloudsdkantiddos==3.1.7',
    'huaweicloudsdkaom==3.1.7',
    'huaweicloudsdkapig==3.1.7',
    'huaweicloudsdkapm==3.1.7',
    'huaweicloudsdkas==3.1.7',
    'huaweicloudsdkbcs==3.1.7',
    'huaweicloudsdkbms==3.1.7',
    'huaweicloudsdkbss==3.1.7',
    'huaweicloudsdkbssintl==3.1.7',
    'huaweicloudsdkcae==3.1.7',
    'huaweicloudsdkcampusgo==3.1.7',
    'huaweicloudsdkcbh==3.1.7',
    'huaweicloudsdkcbr==3.1.7',
    'huaweicloudsdkcbs==3.1.7',
    'huaweicloudsdkcc==3.1.7',
    'huaweicloudsdkcce==3.1.7',
    'huaweicloudsdkccm==3.1.7',
    'huaweicloudsdkcdm==3.1.7',
    'huaweicloudsdkcdn==3.1.7',
    'huaweicloudsdkces==3.1.7',
    'huaweicloudsdkcgs==3.1.7',
    'huaweicloudsdkclassroom==3.1.7',
    'huaweicloudsdkcloudartifact==3.1.7',
    'huaweicloudsdkcloudbuild==3.1.7',
    'huaweicloudsdkclouddeploy==3.1.7',
    'huaweicloudsdkcloudide==3.1.7',
    'huaweicloudsdkcloudpipeline==3.1.7',
    'huaweicloudsdkcloudrtc==3.1.7',
    'huaweicloudsdkcloudtable==3.1.7',
    'huaweicloudsdkcloudtest==3.1.7',
    'huaweicloudsdkcodecheck==3.1.7',
    'huaweicloudsdkcodecraft==3.1.7',
    'huaweicloudsdkcodehub==3.1.7',
    'huaweicloudsdkcph==3.1.7',
    'huaweicloudsdkcpts==3.1.7',
    'huaweicloudsdkcse==3.1.7',
    'huaweicloudsdkcsms==3.1.7',
    'huaweicloudsdkcss==3.1.7',
    'huaweicloudsdkcts==3.1.7',
    'huaweicloudsdkdas==3.1.7',
    'huaweicloudsdkdbss==3.1.7',
    'huaweicloudsdkdcs==3.1.7',
    'huaweicloudsdkddm==3.1.7',
    'huaweicloudsdkdds==3.1.7',
    'huaweicloudsdkdeh==3.1.7',
    'huaweicloudsdkdevstar==3.1.7',
    'huaweicloudsdkdgc==3.1.7',
    'huaweicloudsdkdli==3.1.7',
    'huaweicloudsdkdms==3.1.7',
    'huaweicloudsdkdns==3.1.7',
    'huaweicloudsdkdrs==3.1.7',
    'huaweicloudsdkdsc==3.1.7',
    'huaweicloudsdkdws==3.1.7',
    'huaweicloudsdkecs==3.1.7',
    'huaweicloudsdkeg==3.1.7',
    'huaweicloudsdkeihealth==3.1.7',
    'huaweicloudsdkeip==3.1.7',
    'huaweicloudsdkelb==3.1.7',
    'huaweicloudsdkeps==3.1.7',
    'huaweicloudsdker==3.1.7',
    'huaweicloudsdkevs==3.1.7',
    'huaweicloudsdkfrs==3.1.7',
    'huaweicloudsdkfunctiongraph==3.1.7',
    'huaweicloudsdkgaussdb==3.1.7',
    'huaweicloudsdkgaussdbfornosql==3.1.7',
    'huaweicloudsdkgaussdbforopengauss==3.1.7',
    'huaweicloudsdkges==3.1.7',
    'huaweicloudsdkgsl==3.1.7',
    'huaweicloudsdkhilens==3.1.7',
    'huaweicloudsdkhss==3.1.7',
    'huaweicloudsdkiam==3.1.7',
    'huaweicloudsdkiec==3.1.7',
    'huaweicloudsdkief==3.1.7',
    'huaweicloudsdkies==3.1.7',
    'huaweicloudsdkimage==3.1.7',
    'huaweicloudsdkimagesearch==3.1.7',
    'huaweicloudsdkims==3.1.7',
    'huaweicloudsdkiotanalytics==3.1.7',
    'huaweicloudsdkiotda==3.1.7',
    'huaweicloudsdkiotedge==3.1.7',
    'huaweicloudsdkivs==3.1.7',
    'huaweicloudsdkkafka==3.1.7',
    'huaweicloudsdkkms==3.1.7',
    'huaweicloudsdkkps==3.1.7',
    'huaweicloudsdklive==3.1.7',
    'huaweicloudsdklts==3.1.7',
    'huaweicloudsdkmeeting==3.1.7',
    'huaweicloudsdkmoderation==3.1.7',
    'huaweicloudsdkmpc==3.1.7',
    'huaweicloudsdkmrs==3.1.7',
    'huaweicloudsdknat==3.1.7',
    'huaweicloudsdknlp==3.1.7',
    'huaweicloudsdkocr==3.1.7',
    'huaweicloudsdkoms==3.1.7',
    'huaweicloudsdkosm==3.1.7',
    'huaweicloudsdkprojectman==3.1.7',
    'huaweicloudsdkrabbitmq==3.1.7',
    'huaweicloudsdkrds==3.1.7',
    'huaweicloudsdkres==3.1.7',
    'huaweicloudsdkrms==3.1.7',
    'huaweicloudsdkrocketmq==3.1.7',
    'huaweicloudsdkroma==3.1.7',
    'huaweicloudsdksa==3.1.7',
    'huaweicloudsdkscm==3.1.7',
    'huaweicloudsdksdrs==3.1.7',
    'huaweicloudsdkservicestage==3.1.7',
    'huaweicloudsdksfsturbo==3.1.7',
    'huaweicloudsdksis==3.1.7',
    'huaweicloudsdksmn==3.1.7',
    'huaweicloudsdksms==3.1.7',
    'huaweicloudsdkswr==3.1.7',
    'huaweicloudsdktms==3.1.7',
    'huaweicloudsdkugo==3.1.7',
    'huaweicloudsdkvas==3.1.7',
    'huaweicloudsdkvcm==3.1.7',
    'huaweicloudsdkvod==3.1.7',
    'huaweicloudsdkvpc==3.1.7',
    'huaweicloudsdkvpcep==3.1.7',
    'huaweicloudsdkvss==3.1.7',
    'huaweicloudsdkwaf==3.1.7',
    'huaweicloudsdkworkspace==3.1.7',
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
