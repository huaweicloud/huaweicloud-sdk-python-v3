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
VERSION = "3.1.8"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.8',
    'huaweicloudsdkantiddos==3.1.8',
    'huaweicloudsdkaom==3.1.8',
    'huaweicloudsdkapig==3.1.8',
    'huaweicloudsdkapm==3.1.8',
    'huaweicloudsdkas==3.1.8',
    'huaweicloudsdkbcs==3.1.8',
    'huaweicloudsdkbms==3.1.8',
    'huaweicloudsdkbss==3.1.8',
    'huaweicloudsdkbssintl==3.1.8',
    'huaweicloudsdkcae==3.1.8',
    'huaweicloudsdkcampusgo==3.1.8',
    'huaweicloudsdkcbh==3.1.8',
    'huaweicloudsdkcbr==3.1.8',
    'huaweicloudsdkcbs==3.1.8',
    'huaweicloudsdkcc==3.1.8',
    'huaweicloudsdkcce==3.1.8',
    'huaweicloudsdkccm==3.1.8',
    'huaweicloudsdkcdm==3.1.8',
    'huaweicloudsdkcdn==3.1.8',
    'huaweicloudsdkces==3.1.8',
    'huaweicloudsdkcgs==3.1.8',
    'huaweicloudsdkclassroom==3.1.8',
    'huaweicloudsdkcloudartifact==3.1.8',
    'huaweicloudsdkcloudbuild==3.1.8',
    'huaweicloudsdkclouddeploy==3.1.8',
    'huaweicloudsdkcloudide==3.1.8',
    'huaweicloudsdkcloudpipeline==3.1.8',
    'huaweicloudsdkcloudrtc==3.1.8',
    'huaweicloudsdkcloudtable==3.1.8',
    'huaweicloudsdkcloudtest==3.1.8',
    'huaweicloudsdkcodecheck==3.1.8',
    'huaweicloudsdkcodecraft==3.1.8',
    'huaweicloudsdkcodehub==3.1.8',
    'huaweicloudsdkcph==3.1.8',
    'huaweicloudsdkcpts==3.1.8',
    'huaweicloudsdkcse==3.1.8',
    'huaweicloudsdkcsms==3.1.8',
    'huaweicloudsdkcss==3.1.8',
    'huaweicloudsdkcts==3.1.8',
    'huaweicloudsdkdas==3.1.8',
    'huaweicloudsdkdbss==3.1.8',
    'huaweicloudsdkdcs==3.1.8',
    'huaweicloudsdkddm==3.1.8',
    'huaweicloudsdkdds==3.1.8',
    'huaweicloudsdkdeh==3.1.8',
    'huaweicloudsdkdevsecurity==3.1.8',
    'huaweicloudsdkdevstar==3.1.8',
    'huaweicloudsdkdgc==3.1.8',
    'huaweicloudsdkdli==3.1.8',
    'huaweicloudsdkdms==3.1.8',
    'huaweicloudsdkdns==3.1.8',
    'huaweicloudsdkdrs==3.1.8',
    'huaweicloudsdkdsc==3.1.8',
    'huaweicloudsdkdws==3.1.8',
    'huaweicloudsdkecs==3.1.8',
    'huaweicloudsdkeg==3.1.8',
    'huaweicloudsdkeihealth==3.1.8',
    'huaweicloudsdkeip==3.1.8',
    'huaweicloudsdkelb==3.1.8',
    'huaweicloudsdkeps==3.1.8',
    'huaweicloudsdker==3.1.8',
    'huaweicloudsdkevs==3.1.8',
    'huaweicloudsdkfrs==3.1.8',
    'huaweicloudsdkfunctiongraph==3.1.8',
    'huaweicloudsdkga==3.1.8',
    'huaweicloudsdkgaussdb==3.1.8',
    'huaweicloudsdkgaussdbfornosql==3.1.8',
    'huaweicloudsdkgaussdbforopengauss==3.1.8',
    'huaweicloudsdkges==3.1.8',
    'huaweicloudsdkgsl==3.1.8',
    'huaweicloudsdkhilens==3.1.8',
    'huaweicloudsdkhss==3.1.8',
    'huaweicloudsdkiam==3.1.8',
    'huaweicloudsdkiec==3.1.8',
    'huaweicloudsdkief==3.1.8',
    'huaweicloudsdkies==3.1.8',
    'huaweicloudsdkimage==3.1.8',
    'huaweicloudsdkimagesearch==3.1.8',
    'huaweicloudsdkims==3.1.8',
    'huaweicloudsdkiotanalytics==3.1.8',
    'huaweicloudsdkiotda==3.1.8',
    'huaweicloudsdkiotedge==3.1.8',
    'huaweicloudsdkivs==3.1.8',
    'huaweicloudsdkkafka==3.1.8',
    'huaweicloudsdkkms==3.1.8',
    'huaweicloudsdkkps==3.1.8',
    'huaweicloudsdklive==3.1.8',
    'huaweicloudsdklts==3.1.8',
    'huaweicloudsdkmeeting==3.1.8',
    'huaweicloudsdkmoderation==3.1.8',
    'huaweicloudsdkmpc==3.1.8',
    'huaweicloudsdkmrs==3.1.8',
    'huaweicloudsdknat==3.1.8',
    'huaweicloudsdknlp==3.1.8',
    'huaweicloudsdkocr==3.1.8',
    'huaweicloudsdkoms==3.1.8',
    'huaweicloudsdkosm==3.1.8',
    'huaweicloudsdkprojectman==3.1.8',
    'huaweicloudsdkrabbitmq==3.1.8',
    'huaweicloudsdkrds==3.1.8',
    'huaweicloudsdkres==3.1.8',
    'huaweicloudsdkrms==3.1.8',
    'huaweicloudsdkrocketmq==3.1.8',
    'huaweicloudsdkroma==3.1.8',
    'huaweicloudsdksa==3.1.8',
    'huaweicloudsdkscm==3.1.8',
    'huaweicloudsdksdrs==3.1.8',
    'huaweicloudsdkservicestage==3.1.8',
    'huaweicloudsdksfsturbo==3.1.8',
    'huaweicloudsdksis==3.1.8',
    'huaweicloudsdksmn==3.1.8',
    'huaweicloudsdksms==3.1.8',
    'huaweicloudsdkswr==3.1.8',
    'huaweicloudsdktms==3.1.8',
    'huaweicloudsdkugo==3.1.8',
    'huaweicloudsdkvas==3.1.8',
    'huaweicloudsdkvcm==3.1.8',
    'huaweicloudsdkvod==3.1.8',
    'huaweicloudsdkvpc==3.1.8',
    'huaweicloudsdkvpcep==3.1.8',
    'huaweicloudsdkvss==3.1.8',
    'huaweicloudsdkwaf==3.1.8',
    'huaweicloudsdkworkspace==3.1.8',
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
