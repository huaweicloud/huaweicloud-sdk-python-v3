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
VERSION = "3.0.104"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.0.104',
    'huaweicloudsdkantiddos==3.0.104',
    'huaweicloudsdkaom==3.0.104',
    'huaweicloudsdkapig==3.0.104',
    'huaweicloudsdkapm==3.0.104',
    'huaweicloudsdkas==3.0.104',
    'huaweicloudsdkbcs==3.0.104',
    'huaweicloudsdkbms==3.0.104',
    'huaweicloudsdkbss==3.0.104',
    'huaweicloudsdkbssintl==3.0.104',
    'huaweicloudsdkcampusgo==3.0.104',
    'huaweicloudsdkcbh==3.0.104',
    'huaweicloudsdkcbr==3.0.104',
    'huaweicloudsdkcbs==3.0.104',
    'huaweicloudsdkcc==3.0.104',
    'huaweicloudsdkcce==3.0.104',
    'huaweicloudsdkccm==3.0.104',
    'huaweicloudsdkcdm==3.0.104',
    'huaweicloudsdkcdn==3.0.104',
    'huaweicloudsdkces==3.0.104',
    'huaweicloudsdkcgs==3.0.104',
    'huaweicloudsdkclassroom==3.0.104',
    'huaweicloudsdkcloudbuild==3.0.104',
    'huaweicloudsdkclouddeploy==3.0.104',
    'huaweicloudsdkcloudide==3.0.104',
    'huaweicloudsdkcloudpipeline==3.0.104',
    'huaweicloudsdkcloudrtc==3.0.104',
    'huaweicloudsdkcloudtable==3.0.104',
    'huaweicloudsdkcloudtest==3.0.104',
    'huaweicloudsdkcodecheck==3.0.104',
    'huaweicloudsdkcodecraft==3.0.104',
    'huaweicloudsdkcodehub==3.0.104',
    'huaweicloudsdkcph==3.0.104',
    'huaweicloudsdkcpts==3.0.104',
    'huaweicloudsdkcse==3.0.104',
    'huaweicloudsdkcsms==3.0.104',
    'huaweicloudsdkcss==3.0.104',
    'huaweicloudsdkcts==3.0.104',
    'huaweicloudsdkdas==3.0.104',
    'huaweicloudsdkdbss==3.0.104',
    'huaweicloudsdkdcs==3.0.104',
    'huaweicloudsdkddm==3.0.104',
    'huaweicloudsdkdds==3.0.104',
    'huaweicloudsdkdeh==3.0.104',
    'huaweicloudsdkdevstar==3.0.104',
    'huaweicloudsdkdgc==3.0.104',
    'huaweicloudsdkdli==3.0.104',
    'huaweicloudsdkdms==3.0.104',
    'huaweicloudsdkdns==3.0.104',
    'huaweicloudsdkdrs==3.0.104',
    'huaweicloudsdkdsc==3.0.104',
    'huaweicloudsdkdws==3.0.104',
    'huaweicloudsdkecs==3.0.104',
    'huaweicloudsdkeg==3.0.104',
    'huaweicloudsdkeip==3.0.104',
    'huaweicloudsdkelb==3.0.104',
    'huaweicloudsdkeps==3.0.104',
    'huaweicloudsdkevs==3.0.104',
    'huaweicloudsdkfrs==3.0.104',
    'huaweicloudsdkfunctiongraph==3.0.104',
    'huaweicloudsdkgaussdb==3.0.104',
    'huaweicloudsdkgaussdbfornosql==3.0.104',
    'huaweicloudsdkgaussdbforopengauss==3.0.104',
    'huaweicloudsdkges==3.0.104',
    'huaweicloudsdkgsl==3.0.104',
    'huaweicloudsdkhilens==3.0.104',
    'huaweicloudsdkhss==3.0.104',
    'huaweicloudsdkiam==3.0.104',
    'huaweicloudsdkiec==3.0.104',
    'huaweicloudsdkief==3.0.104',
    'huaweicloudsdkies==3.0.104',
    'huaweicloudsdkimage==3.0.104',
    'huaweicloudsdkimagesearch==3.0.104',
    'huaweicloudsdkims==3.0.104',
    'huaweicloudsdkiotanalytics==3.0.104',
    'huaweicloudsdkiotda==3.0.104',
    'huaweicloudsdkiotedge==3.0.104',
    'huaweicloudsdkivs==3.0.104',
    'huaweicloudsdkkafka==3.0.104',
    'huaweicloudsdkkms==3.0.104',
    'huaweicloudsdkkps==3.0.104',
    'huaweicloudsdklive==3.0.104',
    'huaweicloudsdklts==3.0.104',
    'huaweicloudsdkmeeting==3.0.104',
    'huaweicloudsdkmoderation==3.0.104',
    'huaweicloudsdkmpc==3.0.104',
    'huaweicloudsdkmrs==3.0.104',
    'huaweicloudsdknat==3.0.104',
    'huaweicloudsdknlp==3.0.104',
    'huaweicloudsdkocr==3.0.104',
    'huaweicloudsdkoms==3.0.104',
    'huaweicloudsdkosm==3.0.104',
    'huaweicloudsdkprojectman==3.0.104',
    'huaweicloudsdkrabbitmq==3.0.104',
    'huaweicloudsdkrds==3.0.104',
    'huaweicloudsdkres==3.0.104',
    'huaweicloudsdkrms==3.0.104',
    'huaweicloudsdkrocketmq==3.0.104',
    'huaweicloudsdkroma==3.0.104',
    'huaweicloudsdksa==3.0.104',
    'huaweicloudsdkscm==3.0.104',
    'huaweicloudsdksdrs==3.0.104',
    'huaweicloudsdkservicestage==3.0.104',
    'huaweicloudsdksfsturbo==3.0.104',
    'huaweicloudsdksis==3.0.104',
    'huaweicloudsdksmn==3.0.104',
    'huaweicloudsdksms==3.0.104',
    'huaweicloudsdkswr==3.0.104',
    'huaweicloudsdktms==3.0.104',
    'huaweicloudsdkugo==3.0.104',
    'huaweicloudsdkvas==3.0.104',
    'huaweicloudsdkvcm==3.0.104',
    'huaweicloudsdkvod==3.0.104',
    'huaweicloudsdkvpc==3.0.104',
    'huaweicloudsdkvpcep==3.0.104',
    'huaweicloudsdkvss==3.0.104',
    'huaweicloudsdkwaf==3.0.104',
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
