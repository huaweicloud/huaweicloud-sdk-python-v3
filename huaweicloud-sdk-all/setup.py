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
VERSION = "3.1.12"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.12',
    'huaweicloudsdkantiddos==3.1.12',
    'huaweicloudsdkaom==3.1.12',
    'huaweicloudsdkaos==3.1.12',
    'huaweicloudsdkapig==3.1.12',
    'huaweicloudsdkapm==3.1.12',
    'huaweicloudsdkas==3.1.12',
    'huaweicloudsdkbcs==3.1.12',
    'huaweicloudsdkbms==3.1.12',
    'huaweicloudsdkbss==3.1.12',
    'huaweicloudsdkbssintl==3.1.12',
    'huaweicloudsdkcae==3.1.12',
    'huaweicloudsdkcampusgo==3.1.12',
    'huaweicloudsdkcbh==3.1.12',
    'huaweicloudsdkcbr==3.1.12',
    'huaweicloudsdkcbs==3.1.12',
    'huaweicloudsdkcc==3.1.12',
    'huaweicloudsdkcce==3.1.12',
    'huaweicloudsdkccm==3.1.12',
    'huaweicloudsdkcdm==3.1.12',
    'huaweicloudsdkcdn==3.1.12',
    'huaweicloudsdkces==3.1.12',
    'huaweicloudsdkcfw==3.1.12',
    'huaweicloudsdkcgs==3.1.12',
    'huaweicloudsdkclassroom==3.1.12',
    'huaweicloudsdkcloudartifact==3.1.12',
    'huaweicloudsdkcloudbuild==3.1.12',
    'huaweicloudsdkclouddeploy==3.1.12',
    'huaweicloudsdkcloudide==3.1.12',
    'huaweicloudsdkcloudpipeline==3.1.12',
    'huaweicloudsdkcloudrtc==3.1.12',
    'huaweicloudsdkcloudtable==3.1.12',
    'huaweicloudsdkcloudtest==3.1.12',
    'huaweicloudsdkcodecheck==3.1.12',
    'huaweicloudsdkcodecraft==3.1.12',
    'huaweicloudsdkcodehub==3.1.12',
    'huaweicloudsdkcph==3.1.12',
    'huaweicloudsdkcpts==3.1.12',
    'huaweicloudsdkcse==3.1.12',
    'huaweicloudsdkcsms==3.1.12',
    'huaweicloudsdkcss==3.1.12',
    'huaweicloudsdkcts==3.1.12',
    'huaweicloudsdkdas==3.1.12',
    'huaweicloudsdkdbss==3.1.12',
    'huaweicloudsdkdc==3.1.12',
    'huaweicloudsdkdcs==3.1.12',
    'huaweicloudsdkddm==3.1.12',
    'huaweicloudsdkdds==3.1.12',
    'huaweicloudsdkdeh==3.1.12',
    'huaweicloudsdkdevsecurity==3.1.12',
    'huaweicloudsdkdevstar==3.1.12',
    'huaweicloudsdkdgc==3.1.12',
    'huaweicloudsdkdli==3.1.12',
    'huaweicloudsdkdms==3.1.12',
    'huaweicloudsdkdns==3.1.12',
    'huaweicloudsdkdrs==3.1.12',
    'huaweicloudsdkdsc==3.1.12',
    'huaweicloudsdkdwr==3.1.12',
    'huaweicloudsdkdws==3.1.12',
    'huaweicloudsdkecs==3.1.12',
    'huaweicloudsdkeg==3.1.12',
    'huaweicloudsdkeihealth==3.1.12',
    'huaweicloudsdkeip==3.1.12',
    'huaweicloudsdkelb==3.1.12',
    'huaweicloudsdkeps==3.1.12',
    'huaweicloudsdker==3.1.12',
    'huaweicloudsdkevs==3.1.12',
    'huaweicloudsdkfrs==3.1.12',
    'huaweicloudsdkfunctiongraph==3.1.12',
    'huaweicloudsdkga==3.1.12',
    'huaweicloudsdkgaussdb==3.1.12',
    'huaweicloudsdkgaussdbfornosql==3.1.12',
    'huaweicloudsdkgaussdbforopengauss==3.1.12',
    'huaweicloudsdkges==3.1.12',
    'huaweicloudsdkgsl==3.1.12',
    'huaweicloudsdkhilens==3.1.12',
    'huaweicloudsdkhss==3.1.12',
    'huaweicloudsdkiam==3.1.12',
    'huaweicloudsdkiec==3.1.12',
    'huaweicloudsdkief==3.1.12',
    'huaweicloudsdkies==3.1.12',
    'huaweicloudsdkimage==3.1.12',
    'huaweicloudsdkimagesearch==3.1.12',
    'huaweicloudsdkims==3.1.12',
    'huaweicloudsdkiotanalytics==3.1.12',
    'huaweicloudsdkiotda==3.1.12',
    'huaweicloudsdkiotedge==3.1.12',
    'huaweicloudsdkivs==3.1.12',
    'huaweicloudsdkkafka==3.1.12',
    'huaweicloudsdkkms==3.1.12',
    'huaweicloudsdkkps==3.1.12',
    'huaweicloudsdklive==3.1.12',
    'huaweicloudsdklts==3.1.12',
    'huaweicloudsdkmeeting==3.1.12',
    'huaweicloudsdkmoderation==3.1.12',
    'huaweicloudsdkmpc==3.1.12',
    'huaweicloudsdkmrs==3.1.12',
    'huaweicloudsdknat==3.1.12',
    'huaweicloudsdknlp==3.1.12',
    'huaweicloudsdkocr==3.1.12',
    'huaweicloudsdkoms==3.1.12',
    'huaweicloudsdkosm==3.1.12',
    'huaweicloudsdkprojectman==3.1.12',
    'huaweicloudsdkrabbitmq==3.1.12',
    'huaweicloudsdkrds==3.1.12',
    'huaweicloudsdkres==3.1.12',
    'huaweicloudsdkrms==3.1.12',
    'huaweicloudsdkrocketmq==3.1.12',
    'huaweicloudsdkroma==3.1.12',
    'huaweicloudsdksa==3.1.12',
    'huaweicloudsdkscm==3.1.12',
    'huaweicloudsdksdrs==3.1.12',
    'huaweicloudsdkservicestage==3.1.12',
    'huaweicloudsdksfsturbo==3.1.12',
    'huaweicloudsdksis==3.1.12',
    'huaweicloudsdksmn==3.1.12',
    'huaweicloudsdksms==3.1.12',
    'huaweicloudsdkswr==3.1.12',
    'huaweicloudsdktms==3.1.12',
    'huaweicloudsdkugo==3.1.12',
    'huaweicloudsdkvas==3.1.12',
    'huaweicloudsdkvcm==3.1.12',
    'huaweicloudsdkvod==3.1.12',
    'huaweicloudsdkvpc==3.1.12',
    'huaweicloudsdkvpcep==3.1.12',
    'huaweicloudsdkvss==3.1.12',
    'huaweicloudsdkwaf==3.1.12',
    'huaweicloudsdkworkspace==3.1.12',
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
