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
VERSION = "3.1.20"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.20',
    'huaweicloudsdkantiddos==3.1.20',
    'huaweicloudsdkaom==3.1.20',
    'huaweicloudsdkaos==3.1.20',
    'huaweicloudsdkapig==3.1.20',
    'huaweicloudsdkapm==3.1.20',
    'huaweicloudsdkas==3.1.20',
    'huaweicloudsdkbcs==3.1.20',
    'huaweicloudsdkbms==3.1.20',
    'huaweicloudsdkbss==3.1.20',
    'huaweicloudsdkbssintl==3.1.20',
    'huaweicloudsdkcae==3.1.20',
    'huaweicloudsdkcampusgo==3.1.20',
    'huaweicloudsdkcbh==3.1.20',
    'huaweicloudsdkcbr==3.1.20',
    'huaweicloudsdkcbs==3.1.20',
    'huaweicloudsdkcc==3.1.20',
    'huaweicloudsdkcce==3.1.20',
    'huaweicloudsdkccm==3.1.20',
    'huaweicloudsdkcdm==3.1.20',
    'huaweicloudsdkcdn==3.1.20',
    'huaweicloudsdkces==3.1.20',
    'huaweicloudsdkcfw==3.1.20',
    'huaweicloudsdkcgs==3.1.20',
    'huaweicloudsdkclassroom==3.1.20',
    'huaweicloudsdkcloudartifact==3.1.20',
    'huaweicloudsdkcloudbuild==3.1.20',
    'huaweicloudsdkclouddeploy==3.1.20',
    'huaweicloudsdkcloudide==3.1.20',
    'huaweicloudsdkcloudpipeline==3.1.20',
    'huaweicloudsdkcloudrtc==3.1.20',
    'huaweicloudsdkcloudtable==3.1.20',
    'huaweicloudsdkcloudtest==3.1.20',
    'huaweicloudsdkcodecheck==3.1.20',
    'huaweicloudsdkcodecraft==3.1.20',
    'huaweicloudsdkcodehub==3.1.20',
    'huaweicloudsdkcph==3.1.20',
    'huaweicloudsdkcpts==3.1.20',
    'huaweicloudsdkcse==3.1.20',
    'huaweicloudsdkcsms==3.1.20',
    'huaweicloudsdkcss==3.1.20',
    'huaweicloudsdkcts==3.1.20',
    'huaweicloudsdkdas==3.1.20',
    'huaweicloudsdkdbss==3.1.20',
    'huaweicloudsdkdc==3.1.20',
    'huaweicloudsdkdcs==3.1.20',
    'huaweicloudsdkddm==3.1.20',
    'huaweicloudsdkdds==3.1.20',
    'huaweicloudsdkdeh==3.1.20',
    'huaweicloudsdkdevsecurity==3.1.20',
    'huaweicloudsdkdevstar==3.1.20',
    'huaweicloudsdkdgc==3.1.20',
    'huaweicloudsdkdlf==3.1.20',
    'huaweicloudsdkdli==3.1.20',
    'huaweicloudsdkdms==3.1.20',
    'huaweicloudsdkdns==3.1.20',
    'huaweicloudsdkdris==3.1.20',
    'huaweicloudsdkdrs==3.1.20',
    'huaweicloudsdkdsc==3.1.20',
    'huaweicloudsdkdwr==3.1.20',
    'huaweicloudsdkdws==3.1.20',
    'huaweicloudsdkecs==3.1.20',
    'huaweicloudsdkeg==3.1.20',
    'huaweicloudsdkeihealth==3.1.20',
    'huaweicloudsdkeip==3.1.20',
    'huaweicloudsdkelb==3.1.20',
    'huaweicloudsdkeps==3.1.20',
    'huaweicloudsdker==3.1.20',
    'huaweicloudsdkevs==3.1.20',
    'huaweicloudsdkfrs==3.1.20',
    'huaweicloudsdkfunctiongraph==3.1.20',
    'huaweicloudsdkga==3.1.20',
    'huaweicloudsdkgaussdb==3.1.20',
    'huaweicloudsdkgaussdbfornosql==3.1.20',
    'huaweicloudsdkgaussdbforopengauss==3.1.20',
    'huaweicloudsdkges==3.1.20',
    'huaweicloudsdkgsl==3.1.20',
    'huaweicloudsdkhilens==3.1.20',
    'huaweicloudsdkhss==3.1.20',
    'huaweicloudsdkiam==3.1.20',
    'huaweicloudsdkiec==3.1.20',
    'huaweicloudsdkief==3.1.20',
    'huaweicloudsdkies==3.1.20',
    'huaweicloudsdkimage==3.1.20',
    'huaweicloudsdkimagesearch==3.1.20',
    'huaweicloudsdkims==3.1.20',
    'huaweicloudsdkiotanalytics==3.1.20',
    'huaweicloudsdkiotda==3.1.20',
    'huaweicloudsdkiotedge==3.1.20',
    'huaweicloudsdkivs==3.1.20',
    'huaweicloudsdkkafka==3.1.20',
    'huaweicloudsdkkms==3.1.20',
    'huaweicloudsdkkps==3.1.20',
    'huaweicloudsdklive==3.1.20',
    'huaweicloudsdklts==3.1.20',
    'huaweicloudsdkmapds==3.1.20',
    'huaweicloudsdkmas==3.1.20',
    'huaweicloudsdkmeeting==3.1.20',
    'huaweicloudsdkmoderation==3.1.20',
    'huaweicloudsdkmpc==3.1.20',
    'huaweicloudsdkmrs==3.1.20',
    'huaweicloudsdknat==3.1.20',
    'huaweicloudsdknlp==3.1.20',
    'huaweicloudsdkocr==3.1.20',
    'huaweicloudsdkoms==3.1.20',
    'huaweicloudsdkosm==3.1.20',
    'huaweicloudsdkprojectman==3.1.20',
    'huaweicloudsdkrabbitmq==3.1.20',
    'huaweicloudsdkrds==3.1.20',
    'huaweicloudsdkres==3.1.20',
    'huaweicloudsdkrms==3.1.20',
    'huaweicloudsdkrocketmq==3.1.20',
    'huaweicloudsdkroma==3.1.20',
    'huaweicloudsdksa==3.1.20',
    'huaweicloudsdkscm==3.1.20',
    'huaweicloudsdksdrs==3.1.20',
    'huaweicloudsdkservicestage==3.1.20',
    'huaweicloudsdksfsturbo==3.1.20',
    'huaweicloudsdksis==3.1.20',
    'huaweicloudsdksmn==3.1.20',
    'huaweicloudsdksms==3.1.20',
    'huaweicloudsdkswr==3.1.20',
    'huaweicloudsdktms==3.1.20',
    'huaweicloudsdkugo==3.1.20',
    'huaweicloudsdkvas==3.1.20',
    'huaweicloudsdkvcm==3.1.20',
    'huaweicloudsdkvod==3.1.20',
    'huaweicloudsdkvpc==3.1.20',
    'huaweicloudsdkvpcep==3.1.20',
    'huaweicloudsdkvss==3.1.20',
    'huaweicloudsdkwaf==3.1.20',
    'huaweicloudsdkworkspace==3.1.20',
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
