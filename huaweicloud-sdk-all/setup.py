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
VERSION = "3.1.4"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.4',
    'huaweicloudsdkantiddos==3.1.4',
    'huaweicloudsdkaom==3.1.4',
    'huaweicloudsdkapig==3.1.4',
    'huaweicloudsdkapm==3.1.4',
    'huaweicloudsdkas==3.1.4',
    'huaweicloudsdkbcs==3.1.4',
    'huaweicloudsdkbms==3.1.4',
    'huaweicloudsdkbss==3.1.4',
    'huaweicloudsdkbssintl==3.1.4',
    'huaweicloudsdkcampusgo==3.1.4',
    'huaweicloudsdkcbh==3.1.4',
    'huaweicloudsdkcbr==3.1.4',
    'huaweicloudsdkcbs==3.1.4',
    'huaweicloudsdkcc==3.1.4',
    'huaweicloudsdkcce==3.1.4',
    'huaweicloudsdkccm==3.1.4',
    'huaweicloudsdkcdm==3.1.4',
    'huaweicloudsdkcdn==3.1.4',
    'huaweicloudsdkces==3.1.4',
    'huaweicloudsdkcgs==3.1.4',
    'huaweicloudsdkclassroom==3.1.4',
    'huaweicloudsdkcloudbuild==3.1.4',
    'huaweicloudsdkclouddeploy==3.1.4',
    'huaweicloudsdkcloudide==3.1.4',
    'huaweicloudsdkcloudpipeline==3.1.4',
    'huaweicloudsdkcloudrtc==3.1.4',
    'huaweicloudsdkcloudtable==3.1.4',
    'huaweicloudsdkcloudtest==3.1.4',
    'huaweicloudsdkcodecheck==3.1.4',
    'huaweicloudsdkcodecraft==3.1.4',
    'huaweicloudsdkcodehub==3.1.4',
    'huaweicloudsdkcph==3.1.4',
    'huaweicloudsdkcpts==3.1.4',
    'huaweicloudsdkcse==3.1.4',
    'huaweicloudsdkcsms==3.1.4',
    'huaweicloudsdkcss==3.1.4',
    'huaweicloudsdkcts==3.1.4',
    'huaweicloudsdkdas==3.1.4',
    'huaweicloudsdkdbss==3.1.4',
    'huaweicloudsdkdcs==3.1.4',
    'huaweicloudsdkddm==3.1.4',
    'huaweicloudsdkdds==3.1.4',
    'huaweicloudsdkdeh==3.1.4',
    'huaweicloudsdkdevstar==3.1.4',
    'huaweicloudsdkdgc==3.1.4',
    'huaweicloudsdkdli==3.1.4',
    'huaweicloudsdkdms==3.1.4',
    'huaweicloudsdkdns==3.1.4',
    'huaweicloudsdkdrs==3.1.4',
    'huaweicloudsdkdsc==3.1.4',
    'huaweicloudsdkdws==3.1.4',
    'huaweicloudsdkecs==3.1.4',
    'huaweicloudsdkeg==3.1.4',
    'huaweicloudsdkeip==3.1.4',
    'huaweicloudsdkelb==3.1.4',
    'huaweicloudsdkeps==3.1.4',
    'huaweicloudsdker==3.1.4',
    'huaweicloudsdkevs==3.1.4',
    'huaweicloudsdkfrs==3.1.4',
    'huaweicloudsdkfunctiongraph==3.1.4',
    'huaweicloudsdkgaussdb==3.1.4',
    'huaweicloudsdkgaussdbfornosql==3.1.4',
    'huaweicloudsdkgaussdbforopengauss==3.1.4',
    'huaweicloudsdkges==3.1.4',
    'huaweicloudsdkgsl==3.1.4',
    'huaweicloudsdkhilens==3.1.4',
    'huaweicloudsdkhss==3.1.4',
    'huaweicloudsdkiam==3.1.4',
    'huaweicloudsdkiec==3.1.4',
    'huaweicloudsdkief==3.1.4',
    'huaweicloudsdkies==3.1.4',
    'huaweicloudsdkimage==3.1.4',
    'huaweicloudsdkimagesearch==3.1.4',
    'huaweicloudsdkims==3.1.4',
    'huaweicloudsdkiotanalytics==3.1.4',
    'huaweicloudsdkiotda==3.1.4',
    'huaweicloudsdkiotedge==3.1.4',
    'huaweicloudsdkivs==3.1.4',
    'huaweicloudsdkkafka==3.1.4',
    'huaweicloudsdkkms==3.1.4',
    'huaweicloudsdkkps==3.1.4',
    'huaweicloudsdklive==3.1.4',
    'huaweicloudsdklts==3.1.4',
    'huaweicloudsdkmeeting==3.1.4',
    'huaweicloudsdkmoderation==3.1.4',
    'huaweicloudsdkmpc==3.1.4',
    'huaweicloudsdkmrs==3.1.4',
    'huaweicloudsdknat==3.1.4',
    'huaweicloudsdknlp==3.1.4',
    'huaweicloudsdkocr==3.1.4',
    'huaweicloudsdkoms==3.1.4',
    'huaweicloudsdkosm==3.1.4',
    'huaweicloudsdkprojectman==3.1.4',
    'huaweicloudsdkrabbitmq==3.1.4',
    'huaweicloudsdkrds==3.1.4',
    'huaweicloudsdkres==3.1.4',
    'huaweicloudsdkrms==3.1.4',
    'huaweicloudsdkrocketmq==3.1.4',
    'huaweicloudsdkroma==3.1.4',
    'huaweicloudsdksa==3.1.4',
    'huaweicloudsdkscm==3.1.4',
    'huaweicloudsdksdrs==3.1.4',
    'huaweicloudsdkservicestage==3.1.4',
    'huaweicloudsdksfsturbo==3.1.4',
    'huaweicloudsdksis==3.1.4',
    'huaweicloudsdksmn==3.1.4',
    'huaweicloudsdksms==3.1.4',
    'huaweicloudsdkswr==3.1.4',
    'huaweicloudsdktms==3.1.4',
    'huaweicloudsdkugo==3.1.4',
    'huaweicloudsdkvas==3.1.4',
    'huaweicloudsdkvcm==3.1.4',
    'huaweicloudsdkvod==3.1.4',
    'huaweicloudsdkvpc==3.1.4',
    'huaweicloudsdkvpcep==3.1.4',
    'huaweicloudsdkvss==3.1.4',
    'huaweicloudsdkwaf==3.1.4',
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
