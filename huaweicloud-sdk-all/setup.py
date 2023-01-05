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
VERSION = "3.1.21"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.21',
    'huaweicloudsdkantiddos==3.1.21',
    'huaweicloudsdkaom==3.1.21',
    'huaweicloudsdkaos==3.1.21',
    'huaweicloudsdkapig==3.1.21',
    'huaweicloudsdkapm==3.1.21',
    'huaweicloudsdkas==3.1.21',
    'huaweicloudsdkbcs==3.1.21',
    'huaweicloudsdkbms==3.1.21',
    'huaweicloudsdkbss==3.1.21',
    'huaweicloudsdkbssintl==3.1.21',
    'huaweicloudsdkcae==3.1.21',
    'huaweicloudsdkcampusgo==3.1.21',
    'huaweicloudsdkcbh==3.1.21',
    'huaweicloudsdkcbr==3.1.21',
    'huaweicloudsdkcbs==3.1.21',
    'huaweicloudsdkcc==3.1.21',
    'huaweicloudsdkcce==3.1.21',
    'huaweicloudsdkccm==3.1.21',
    'huaweicloudsdkcdm==3.1.21',
    'huaweicloudsdkcdn==3.1.21',
    'huaweicloudsdkces==3.1.21',
    'huaweicloudsdkcfw==3.1.21',
    'huaweicloudsdkcgs==3.1.21',
    'huaweicloudsdkclassroom==3.1.21',
    'huaweicloudsdkcloudartifact==3.1.21',
    'huaweicloudsdkcloudbuild==3.1.21',
    'huaweicloudsdkclouddeploy==3.1.21',
    'huaweicloudsdkcloudide==3.1.21',
    'huaweicloudsdkcloudpipeline==3.1.21',
    'huaweicloudsdkcloudrtc==3.1.21',
    'huaweicloudsdkcloudtable==3.1.21',
    'huaweicloudsdkcloudtest==3.1.21',
    'huaweicloudsdkcodecheck==3.1.21',
    'huaweicloudsdkcodecraft==3.1.21',
    'huaweicloudsdkcodehub==3.1.21',
    'huaweicloudsdkcph==3.1.21',
    'huaweicloudsdkcpts==3.1.21',
    'huaweicloudsdkcse==3.1.21',
    'huaweicloudsdkcsms==3.1.21',
    'huaweicloudsdkcss==3.1.21',
    'huaweicloudsdkcts==3.1.21',
    'huaweicloudsdkdas==3.1.21',
    'huaweicloudsdkdbss==3.1.21',
    'huaweicloudsdkdc==3.1.21',
    'huaweicloudsdkdcs==3.1.21',
    'huaweicloudsdkddm==3.1.21',
    'huaweicloudsdkdds==3.1.21',
    'huaweicloudsdkdeh==3.1.21',
    'huaweicloudsdkdevsecurity==3.1.21',
    'huaweicloudsdkdevstar==3.1.21',
    'huaweicloudsdkdgc==3.1.21',
    'huaweicloudsdkdlf==3.1.21',
    'huaweicloudsdkdli==3.1.21',
    'huaweicloudsdkdms==3.1.21',
    'huaweicloudsdkdns==3.1.21',
    'huaweicloudsdkdris==3.1.21',
    'huaweicloudsdkdrs==3.1.21',
    'huaweicloudsdkdsc==3.1.21',
    'huaweicloudsdkdwr==3.1.21',
    'huaweicloudsdkdws==3.1.21',
    'huaweicloudsdkecs==3.1.21',
    'huaweicloudsdkeg==3.1.21',
    'huaweicloudsdkeihealth==3.1.21',
    'huaweicloudsdkeip==3.1.21',
    'huaweicloudsdkelb==3.1.21',
    'huaweicloudsdkeps==3.1.21',
    'huaweicloudsdker==3.1.21',
    'huaweicloudsdkevs==3.1.21',
    'huaweicloudsdkfrs==3.1.21',
    'huaweicloudsdkfunctiongraph==3.1.21',
    'huaweicloudsdkga==3.1.21',
    'huaweicloudsdkgaussdb==3.1.21',
    'huaweicloudsdkgaussdbfornosql==3.1.21',
    'huaweicloudsdkgaussdbforopengauss==3.1.21',
    'huaweicloudsdkges==3.1.21',
    'huaweicloudsdkgsl==3.1.21',
    'huaweicloudsdkhilens==3.1.21',
    'huaweicloudsdkhss==3.1.21',
    'huaweicloudsdkiam==3.1.21',
    'huaweicloudsdkiec==3.1.21',
    'huaweicloudsdkief==3.1.21',
    'huaweicloudsdkies==3.1.21',
    'huaweicloudsdkimage==3.1.21',
    'huaweicloudsdkimagesearch==3.1.21',
    'huaweicloudsdkims==3.1.21',
    'huaweicloudsdkiotanalytics==3.1.21',
    'huaweicloudsdkiotda==3.1.21',
    'huaweicloudsdkiotedge==3.1.21',
    'huaweicloudsdkivs==3.1.21',
    'huaweicloudsdkkafka==3.1.21',
    'huaweicloudsdkkms==3.1.21',
    'huaweicloudsdkkps==3.1.21',
    'huaweicloudsdklive==3.1.21',
    'huaweicloudsdklts==3.1.21',
    'huaweicloudsdkmapds==3.1.21',
    'huaweicloudsdkmas==3.1.21',
    'huaweicloudsdkmeeting==3.1.21',
    'huaweicloudsdkmoderation==3.1.21',
    'huaweicloudsdkmpc==3.1.21',
    'huaweicloudsdkmrs==3.1.21',
    'huaweicloudsdknat==3.1.21',
    'huaweicloudsdknlp==3.1.21',
    'huaweicloudsdkocr==3.1.21',
    'huaweicloudsdkoms==3.1.21',
    'huaweicloudsdkosm==3.1.21',
    'huaweicloudsdkprojectman==3.1.21',
    'huaweicloudsdkrabbitmq==3.1.21',
    'huaweicloudsdkrds==3.1.21',
    'huaweicloudsdkres==3.1.21',
    'huaweicloudsdkrms==3.1.21',
    'huaweicloudsdkrocketmq==3.1.21',
    'huaweicloudsdkroma==3.1.21',
    'huaweicloudsdksa==3.1.21',
    'huaweicloudsdkscm==3.1.21',
    'huaweicloudsdksdrs==3.1.21',
    'huaweicloudsdkservicestage==3.1.21',
    'huaweicloudsdksfsturbo==3.1.21',
    'huaweicloudsdksis==3.1.21',
    'huaweicloudsdksmn==3.1.21',
    'huaweicloudsdksms==3.1.21',
    'huaweicloudsdkswr==3.1.21',
    'huaweicloudsdktms==3.1.21',
    'huaweicloudsdkugo==3.1.21',
    'huaweicloudsdkvas==3.1.21',
    'huaweicloudsdkvcm==3.1.21',
    'huaweicloudsdkvod==3.1.21',
    'huaweicloudsdkvpc==3.1.21',
    'huaweicloudsdkvpcep==3.1.21',
    'huaweicloudsdkvss==3.1.21',
    'huaweicloudsdkwaf==3.1.21',
    'huaweicloudsdkworkspace==3.1.21',
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
