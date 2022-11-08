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
VERSION = "3.1.9"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.9',
    'huaweicloudsdkantiddos==3.1.9',
    'huaweicloudsdkaom==3.1.9',
    'huaweicloudsdkapig==3.1.9',
    'huaweicloudsdkapm==3.1.9',
    'huaweicloudsdkas==3.1.9',
    'huaweicloudsdkbcs==3.1.9',
    'huaweicloudsdkbms==3.1.9',
    'huaweicloudsdkbss==3.1.9',
    'huaweicloudsdkbssintl==3.1.9',
    'huaweicloudsdkcae==3.1.9',
    'huaweicloudsdkcampusgo==3.1.9',
    'huaweicloudsdkcbh==3.1.9',
    'huaweicloudsdkcbr==3.1.9',
    'huaweicloudsdkcbs==3.1.9',
    'huaweicloudsdkcc==3.1.9',
    'huaweicloudsdkcce==3.1.9',
    'huaweicloudsdkccm==3.1.9',
    'huaweicloudsdkcdm==3.1.9',
    'huaweicloudsdkcdn==3.1.9',
    'huaweicloudsdkces==3.1.9',
    'huaweicloudsdkcgs==3.1.9',
    'huaweicloudsdkclassroom==3.1.9',
    'huaweicloudsdkcloudartifact==3.1.9',
    'huaweicloudsdkcloudbuild==3.1.9',
    'huaweicloudsdkclouddeploy==3.1.9',
    'huaweicloudsdkcloudide==3.1.9',
    'huaweicloudsdkcloudpipeline==3.1.9',
    'huaweicloudsdkcloudrtc==3.1.9',
    'huaweicloudsdkcloudtable==3.1.9',
    'huaweicloudsdkcloudtest==3.1.9',
    'huaweicloudsdkcodecheck==3.1.9',
    'huaweicloudsdkcodecraft==3.1.9',
    'huaweicloudsdkcodehub==3.1.9',
    'huaweicloudsdkcph==3.1.9',
    'huaweicloudsdkcpts==3.1.9',
    'huaweicloudsdkcse==3.1.9',
    'huaweicloudsdkcsms==3.1.9',
    'huaweicloudsdkcss==3.1.9',
    'huaweicloudsdkcts==3.1.9',
    'huaweicloudsdkdas==3.1.9',
    'huaweicloudsdkdbss==3.1.9',
    'huaweicloudsdkdcs==3.1.9',
    'huaweicloudsdkddm==3.1.9',
    'huaweicloudsdkdds==3.1.9',
    'huaweicloudsdkdeh==3.1.9',
    'huaweicloudsdkdevsecurity==3.1.9',
    'huaweicloudsdkdevstar==3.1.9',
    'huaweicloudsdkdgc==3.1.9',
    'huaweicloudsdkdli==3.1.9',
    'huaweicloudsdkdms==3.1.9',
    'huaweicloudsdkdns==3.1.9',
    'huaweicloudsdkdrs==3.1.9',
    'huaweicloudsdkdsc==3.1.9',
    'huaweicloudsdkdws==3.1.9',
    'huaweicloudsdkecs==3.1.9',
    'huaweicloudsdkeg==3.1.9',
    'huaweicloudsdkeihealth==3.1.9',
    'huaweicloudsdkeip==3.1.9',
    'huaweicloudsdkelb==3.1.9',
    'huaweicloudsdkeps==3.1.9',
    'huaweicloudsdker==3.1.9',
    'huaweicloudsdkevs==3.1.9',
    'huaweicloudsdkfrs==3.1.9',
    'huaweicloudsdkfunctiongraph==3.1.9',
    'huaweicloudsdkga==3.1.9',
    'huaweicloudsdkgaussdb==3.1.9',
    'huaweicloudsdkgaussdbfornosql==3.1.9',
    'huaweicloudsdkgaussdbforopengauss==3.1.9',
    'huaweicloudsdkges==3.1.9',
    'huaweicloudsdkgsl==3.1.9',
    'huaweicloudsdkhilens==3.1.9',
    'huaweicloudsdkhss==3.1.9',
    'huaweicloudsdkiam==3.1.9',
    'huaweicloudsdkiec==3.1.9',
    'huaweicloudsdkief==3.1.9',
    'huaweicloudsdkies==3.1.9',
    'huaweicloudsdkimage==3.1.9',
    'huaweicloudsdkimagesearch==3.1.9',
    'huaweicloudsdkims==3.1.9',
    'huaweicloudsdkiotanalytics==3.1.9',
    'huaweicloudsdkiotda==3.1.9',
    'huaweicloudsdkiotedge==3.1.9',
    'huaweicloudsdkivs==3.1.9',
    'huaweicloudsdkkafka==3.1.9',
    'huaweicloudsdkkms==3.1.9',
    'huaweicloudsdkkps==3.1.9',
    'huaweicloudsdklive==3.1.9',
    'huaweicloudsdklts==3.1.9',
    'huaweicloudsdkmeeting==3.1.9',
    'huaweicloudsdkmoderation==3.1.9',
    'huaweicloudsdkmpc==3.1.9',
    'huaweicloudsdkmrs==3.1.9',
    'huaweicloudsdknat==3.1.9',
    'huaweicloudsdknlp==3.1.9',
    'huaweicloudsdkocr==3.1.9',
    'huaweicloudsdkoms==3.1.9',
    'huaweicloudsdkosm==3.1.9',
    'huaweicloudsdkprojectman==3.1.9',
    'huaweicloudsdkrabbitmq==3.1.9',
    'huaweicloudsdkrds==3.1.9',
    'huaweicloudsdkres==3.1.9',
    'huaweicloudsdkrms==3.1.9',
    'huaweicloudsdkrocketmq==3.1.9',
    'huaweicloudsdkroma==3.1.9',
    'huaweicloudsdksa==3.1.9',
    'huaweicloudsdkscm==3.1.9',
    'huaweicloudsdksdrs==3.1.9',
    'huaweicloudsdkservicestage==3.1.9',
    'huaweicloudsdksfsturbo==3.1.9',
    'huaweicloudsdksis==3.1.9',
    'huaweicloudsdksmn==3.1.9',
    'huaweicloudsdksms==3.1.9',
    'huaweicloudsdkswr==3.1.9',
    'huaweicloudsdktms==3.1.9',
    'huaweicloudsdkugo==3.1.9',
    'huaweicloudsdkvas==3.1.9',
    'huaweicloudsdkvcm==3.1.9',
    'huaweicloudsdkvod==3.1.9',
    'huaweicloudsdkvpc==3.1.9',
    'huaweicloudsdkvpcep==3.1.9',
    'huaweicloudsdkvss==3.1.9',
    'huaweicloudsdkwaf==3.1.9',
    'huaweicloudsdkworkspace==3.1.9',
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
