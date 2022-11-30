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
VERSION = "3.1.13"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.13',
    'huaweicloudsdkantiddos==3.1.13',
    'huaweicloudsdkaom==3.1.13',
    'huaweicloudsdkaos==3.1.13',
    'huaweicloudsdkapig==3.1.13',
    'huaweicloudsdkapm==3.1.13',
    'huaweicloudsdkas==3.1.13',
    'huaweicloudsdkbcs==3.1.13',
    'huaweicloudsdkbms==3.1.13',
    'huaweicloudsdkbss==3.1.13',
    'huaweicloudsdkbssintl==3.1.13',
    'huaweicloudsdkcae==3.1.13',
    'huaweicloudsdkcampusgo==3.1.13',
    'huaweicloudsdkcbh==3.1.13',
    'huaweicloudsdkcbr==3.1.13',
    'huaweicloudsdkcbs==3.1.13',
    'huaweicloudsdkcc==3.1.13',
    'huaweicloudsdkcce==3.1.13',
    'huaweicloudsdkccm==3.1.13',
    'huaweicloudsdkcdm==3.1.13',
    'huaweicloudsdkcdn==3.1.13',
    'huaweicloudsdkces==3.1.13',
    'huaweicloudsdkcfw==3.1.13',
    'huaweicloudsdkcgs==3.1.13',
    'huaweicloudsdkclassroom==3.1.13',
    'huaweicloudsdkcloudartifact==3.1.13',
    'huaweicloudsdkcloudbuild==3.1.13',
    'huaweicloudsdkclouddeploy==3.1.13',
    'huaweicloudsdkcloudide==3.1.13',
    'huaweicloudsdkcloudpipeline==3.1.13',
    'huaweicloudsdkcloudrtc==3.1.13',
    'huaweicloudsdkcloudtable==3.1.13',
    'huaweicloudsdkcloudtest==3.1.13',
    'huaweicloudsdkcodecheck==3.1.13',
    'huaweicloudsdkcodecraft==3.1.13',
    'huaweicloudsdkcodehub==3.1.13',
    'huaweicloudsdkcph==3.1.13',
    'huaweicloudsdkcpts==3.1.13',
    'huaweicloudsdkcse==3.1.13',
    'huaweicloudsdkcsms==3.1.13',
    'huaweicloudsdkcss==3.1.13',
    'huaweicloudsdkcts==3.1.13',
    'huaweicloudsdkdas==3.1.13',
    'huaweicloudsdkdbss==3.1.13',
    'huaweicloudsdkdc==3.1.13',
    'huaweicloudsdkdcs==3.1.13',
    'huaweicloudsdkddm==3.1.13',
    'huaweicloudsdkdds==3.1.13',
    'huaweicloudsdkdeh==3.1.13',
    'huaweicloudsdkdevsecurity==3.1.13',
    'huaweicloudsdkdevstar==3.1.13',
    'huaweicloudsdkdgc==3.1.13',
    'huaweicloudsdkdli==3.1.13',
    'huaweicloudsdkdms==3.1.13',
    'huaweicloudsdkdns==3.1.13',
    'huaweicloudsdkdrs==3.1.13',
    'huaweicloudsdkdsc==3.1.13',
    'huaweicloudsdkdwr==3.1.13',
    'huaweicloudsdkdws==3.1.13',
    'huaweicloudsdkecs==3.1.13',
    'huaweicloudsdkeg==3.1.13',
    'huaweicloudsdkeihealth==3.1.13',
    'huaweicloudsdkeip==3.1.13',
    'huaweicloudsdkelb==3.1.13',
    'huaweicloudsdkeps==3.1.13',
    'huaweicloudsdker==3.1.13',
    'huaweicloudsdkevs==3.1.13',
    'huaweicloudsdkfrs==3.1.13',
    'huaweicloudsdkfunctiongraph==3.1.13',
    'huaweicloudsdkga==3.1.13',
    'huaweicloudsdkgaussdb==3.1.13',
    'huaweicloudsdkgaussdbfornosql==3.1.13',
    'huaweicloudsdkgaussdbforopengauss==3.1.13',
    'huaweicloudsdkges==3.1.13',
    'huaweicloudsdkgsl==3.1.13',
    'huaweicloudsdkhilens==3.1.13',
    'huaweicloudsdkhss==3.1.13',
    'huaweicloudsdkiam==3.1.13',
    'huaweicloudsdkiec==3.1.13',
    'huaweicloudsdkief==3.1.13',
    'huaweicloudsdkies==3.1.13',
    'huaweicloudsdkimage==3.1.13',
    'huaweicloudsdkimagesearch==3.1.13',
    'huaweicloudsdkims==3.1.13',
    'huaweicloudsdkiotanalytics==3.1.13',
    'huaweicloudsdkiotda==3.1.13',
    'huaweicloudsdkiotedge==3.1.13',
    'huaweicloudsdkivs==3.1.13',
    'huaweicloudsdkkafka==3.1.13',
    'huaweicloudsdkkms==3.1.13',
    'huaweicloudsdkkps==3.1.13',
    'huaweicloudsdklive==3.1.13',
    'huaweicloudsdklts==3.1.13',
    'huaweicloudsdkmas==3.1.13',
    'huaweicloudsdkmeeting==3.1.13',
    'huaweicloudsdkmoderation==3.1.13',
    'huaweicloudsdkmpc==3.1.13',
    'huaweicloudsdkmrs==3.1.13',
    'huaweicloudsdknat==3.1.13',
    'huaweicloudsdknlp==3.1.13',
    'huaweicloudsdkocr==3.1.13',
    'huaweicloudsdkoms==3.1.13',
    'huaweicloudsdkosm==3.1.13',
    'huaweicloudsdkprojectman==3.1.13',
    'huaweicloudsdkrabbitmq==3.1.13',
    'huaweicloudsdkrds==3.1.13',
    'huaweicloudsdkres==3.1.13',
    'huaweicloudsdkrms==3.1.13',
    'huaweicloudsdkrocketmq==3.1.13',
    'huaweicloudsdkroma==3.1.13',
    'huaweicloudsdksa==3.1.13',
    'huaweicloudsdkscm==3.1.13',
    'huaweicloudsdksdrs==3.1.13',
    'huaweicloudsdkservicestage==3.1.13',
    'huaweicloudsdksfsturbo==3.1.13',
    'huaweicloudsdksis==3.1.13',
    'huaweicloudsdksmn==3.1.13',
    'huaweicloudsdksms==3.1.13',
    'huaweicloudsdkswr==3.1.13',
    'huaweicloudsdktms==3.1.13',
    'huaweicloudsdkugo==3.1.13',
    'huaweicloudsdkvas==3.1.13',
    'huaweicloudsdkvcm==3.1.13',
    'huaweicloudsdkvod==3.1.13',
    'huaweicloudsdkvpc==3.1.13',
    'huaweicloudsdkvpcep==3.1.13',
    'huaweicloudsdkvss==3.1.13',
    'huaweicloudsdkwaf==3.1.13',
    'huaweicloudsdkworkspace==3.1.13',
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
