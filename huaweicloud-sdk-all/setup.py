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
VERSION = "3.1.17"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.17',
    'huaweicloudsdkantiddos==3.1.17',
    'huaweicloudsdkaom==3.1.17',
    'huaweicloudsdkaos==3.1.17',
    'huaweicloudsdkapig==3.1.17',
    'huaweicloudsdkapm==3.1.17',
    'huaweicloudsdkas==3.1.17',
    'huaweicloudsdkbcs==3.1.17',
    'huaweicloudsdkbms==3.1.17',
    'huaweicloudsdkbss==3.1.17',
    'huaweicloudsdkbssintl==3.1.17',
    'huaweicloudsdkcae==3.1.17',
    'huaweicloudsdkcampusgo==3.1.17',
    'huaweicloudsdkcbh==3.1.17',
    'huaweicloudsdkcbr==3.1.17',
    'huaweicloudsdkcbs==3.1.17',
    'huaweicloudsdkcc==3.1.17',
    'huaweicloudsdkcce==3.1.17',
    'huaweicloudsdkccm==3.1.17',
    'huaweicloudsdkcdm==3.1.17',
    'huaweicloudsdkcdn==3.1.17',
    'huaweicloudsdkces==3.1.17',
    'huaweicloudsdkcfw==3.1.17',
    'huaweicloudsdkcgs==3.1.17',
    'huaweicloudsdkclassroom==3.1.17',
    'huaweicloudsdkcloudartifact==3.1.17',
    'huaweicloudsdkcloudbuild==3.1.17',
    'huaweicloudsdkclouddeploy==3.1.17',
    'huaweicloudsdkcloudide==3.1.17',
    'huaweicloudsdkcloudpipeline==3.1.17',
    'huaweicloudsdkcloudrtc==3.1.17',
    'huaweicloudsdkcloudtable==3.1.17',
    'huaweicloudsdkcloudtest==3.1.17',
    'huaweicloudsdkcodecheck==3.1.17',
    'huaweicloudsdkcodecraft==3.1.17',
    'huaweicloudsdkcodehub==3.1.17',
    'huaweicloudsdkcph==3.1.17',
    'huaweicloudsdkcpts==3.1.17',
    'huaweicloudsdkcse==3.1.17',
    'huaweicloudsdkcsms==3.1.17',
    'huaweicloudsdkcss==3.1.17',
    'huaweicloudsdkcts==3.1.17',
    'huaweicloudsdkdas==3.1.17',
    'huaweicloudsdkdbss==3.1.17',
    'huaweicloudsdkdc==3.1.17',
    'huaweicloudsdkdcs==3.1.17',
    'huaweicloudsdkddm==3.1.17',
    'huaweicloudsdkdds==3.1.17',
    'huaweicloudsdkdeh==3.1.17',
    'huaweicloudsdkdevsecurity==3.1.17',
    'huaweicloudsdkdevstar==3.1.17',
    'huaweicloudsdkdgc==3.1.17',
    'huaweicloudsdkdlf==3.1.17',
    'huaweicloudsdkdli==3.1.17',
    'huaweicloudsdkdms==3.1.17',
    'huaweicloudsdkdns==3.1.17',
    'huaweicloudsdkdris==3.1.17',
    'huaweicloudsdkdrs==3.1.17',
    'huaweicloudsdkdsc==3.1.17',
    'huaweicloudsdkdwr==3.1.17',
    'huaweicloudsdkdws==3.1.17',
    'huaweicloudsdkecs==3.1.17',
    'huaweicloudsdkeg==3.1.17',
    'huaweicloudsdkeihealth==3.1.17',
    'huaweicloudsdkeip==3.1.17',
    'huaweicloudsdkelb==3.1.17',
    'huaweicloudsdkeps==3.1.17',
    'huaweicloudsdker==3.1.17',
    'huaweicloudsdkevs==3.1.17',
    'huaweicloudsdkfrs==3.1.17',
    'huaweicloudsdkfunctiongraph==3.1.17',
    'huaweicloudsdkga==3.1.17',
    'huaweicloudsdkgaussdb==3.1.17',
    'huaweicloudsdkgaussdbfornosql==3.1.17',
    'huaweicloudsdkgaussdbforopengauss==3.1.17',
    'huaweicloudsdkges==3.1.17',
    'huaweicloudsdkgsl==3.1.17',
    'huaweicloudsdkhilens==3.1.17',
    'huaweicloudsdkhss==3.1.17',
    'huaweicloudsdkiam==3.1.17',
    'huaweicloudsdkiec==3.1.17',
    'huaweicloudsdkief==3.1.17',
    'huaweicloudsdkies==3.1.17',
    'huaweicloudsdkimage==3.1.17',
    'huaweicloudsdkimagesearch==3.1.17',
    'huaweicloudsdkims==3.1.17',
    'huaweicloudsdkiotanalytics==3.1.17',
    'huaweicloudsdkiotda==3.1.17',
    'huaweicloudsdkiotedge==3.1.17',
    'huaweicloudsdkivs==3.1.17',
    'huaweicloudsdkkafka==3.1.17',
    'huaweicloudsdkkms==3.1.17',
    'huaweicloudsdkkps==3.1.17',
    'huaweicloudsdklive==3.1.17',
    'huaweicloudsdklts==3.1.17',
    'huaweicloudsdkmapds==3.1.17',
    'huaweicloudsdkmas==3.1.17',
    'huaweicloudsdkmeeting==3.1.17',
    'huaweicloudsdkmoderation==3.1.17',
    'huaweicloudsdkmpc==3.1.17',
    'huaweicloudsdkmrs==3.1.17',
    'huaweicloudsdknat==3.1.17',
    'huaweicloudsdknlp==3.1.17',
    'huaweicloudsdkocr==3.1.17',
    'huaweicloudsdkoms==3.1.17',
    'huaweicloudsdkosm==3.1.17',
    'huaweicloudsdkprojectman==3.1.17',
    'huaweicloudsdkrabbitmq==3.1.17',
    'huaweicloudsdkrds==3.1.17',
    'huaweicloudsdkres==3.1.17',
    'huaweicloudsdkrms==3.1.17',
    'huaweicloudsdkrocketmq==3.1.17',
    'huaweicloudsdkroma==3.1.17',
    'huaweicloudsdksa==3.1.17',
    'huaweicloudsdkscm==3.1.17',
    'huaweicloudsdksdrs==3.1.17',
    'huaweicloudsdkservicestage==3.1.17',
    'huaweicloudsdksfsturbo==3.1.17',
    'huaweicloudsdksis==3.1.17',
    'huaweicloudsdksmn==3.1.17',
    'huaweicloudsdksms==3.1.17',
    'huaweicloudsdkswr==3.1.17',
    'huaweicloudsdktms==3.1.17',
    'huaweicloudsdkugo==3.1.17',
    'huaweicloudsdkvas==3.1.17',
    'huaweicloudsdkvcm==3.1.17',
    'huaweicloudsdkvod==3.1.17',
    'huaweicloudsdkvpc==3.1.17',
    'huaweicloudsdkvpcep==3.1.17',
    'huaweicloudsdkvss==3.1.17',
    'huaweicloudsdkwaf==3.1.17',
    'huaweicloudsdkworkspace==3.1.17',
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
