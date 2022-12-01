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
VERSION = "3.1.14"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.14',
    'huaweicloudsdkantiddos==3.1.14',
    'huaweicloudsdkaom==3.1.14',
    'huaweicloudsdkaos==3.1.14',
    'huaweicloudsdkapig==3.1.14',
    'huaweicloudsdkapm==3.1.14',
    'huaweicloudsdkas==3.1.14',
    'huaweicloudsdkbcs==3.1.14',
    'huaweicloudsdkbms==3.1.14',
    'huaweicloudsdkbss==3.1.14',
    'huaweicloudsdkbssintl==3.1.14',
    'huaweicloudsdkcae==3.1.14',
    'huaweicloudsdkcampusgo==3.1.14',
    'huaweicloudsdkcbh==3.1.14',
    'huaweicloudsdkcbr==3.1.14',
    'huaweicloudsdkcbs==3.1.14',
    'huaweicloudsdkcc==3.1.14',
    'huaweicloudsdkcce==3.1.14',
    'huaweicloudsdkccm==3.1.14',
    'huaweicloudsdkcdm==3.1.14',
    'huaweicloudsdkcdn==3.1.14',
    'huaweicloudsdkces==3.1.14',
    'huaweicloudsdkcfw==3.1.14',
    'huaweicloudsdkcgs==3.1.14',
    'huaweicloudsdkclassroom==3.1.14',
    'huaweicloudsdkcloudartifact==3.1.14',
    'huaweicloudsdkcloudbuild==3.1.14',
    'huaweicloudsdkclouddeploy==3.1.14',
    'huaweicloudsdkcloudide==3.1.14',
    'huaweicloudsdkcloudpipeline==3.1.14',
    'huaweicloudsdkcloudrtc==3.1.14',
    'huaweicloudsdkcloudtable==3.1.14',
    'huaweicloudsdkcloudtest==3.1.14',
    'huaweicloudsdkcodecheck==3.1.14',
    'huaweicloudsdkcodecraft==3.1.14',
    'huaweicloudsdkcodehub==3.1.14',
    'huaweicloudsdkcph==3.1.14',
    'huaweicloudsdkcpts==3.1.14',
    'huaweicloudsdkcse==3.1.14',
    'huaweicloudsdkcsms==3.1.14',
    'huaweicloudsdkcss==3.1.14',
    'huaweicloudsdkcts==3.1.14',
    'huaweicloudsdkdas==3.1.14',
    'huaweicloudsdkdbss==3.1.14',
    'huaweicloudsdkdc==3.1.14',
    'huaweicloudsdkdcs==3.1.14',
    'huaweicloudsdkddm==3.1.14',
    'huaweicloudsdkdds==3.1.14',
    'huaweicloudsdkdeh==3.1.14',
    'huaweicloudsdkdevsecurity==3.1.14',
    'huaweicloudsdkdevstar==3.1.14',
    'huaweicloudsdkdgc==3.1.14',
    'huaweicloudsdkdli==3.1.14',
    'huaweicloudsdkdms==3.1.14',
    'huaweicloudsdkdns==3.1.14',
    'huaweicloudsdkdrs==3.1.14',
    'huaweicloudsdkdsc==3.1.14',
    'huaweicloudsdkdwr==3.1.14',
    'huaweicloudsdkdws==3.1.14',
    'huaweicloudsdkecs==3.1.14',
    'huaweicloudsdkeg==3.1.14',
    'huaweicloudsdkeihealth==3.1.14',
    'huaweicloudsdkeip==3.1.14',
    'huaweicloudsdkelb==3.1.14',
    'huaweicloudsdkeps==3.1.14',
    'huaweicloudsdker==3.1.14',
    'huaweicloudsdkevs==3.1.14',
    'huaweicloudsdkfrs==3.1.14',
    'huaweicloudsdkfunctiongraph==3.1.14',
    'huaweicloudsdkga==3.1.14',
    'huaweicloudsdkgaussdb==3.1.14',
    'huaweicloudsdkgaussdbfornosql==3.1.14',
    'huaweicloudsdkgaussdbforopengauss==3.1.14',
    'huaweicloudsdkges==3.1.14',
    'huaweicloudsdkgsl==3.1.14',
    'huaweicloudsdkhilens==3.1.14',
    'huaweicloudsdkhss==3.1.14',
    'huaweicloudsdkiam==3.1.14',
    'huaweicloudsdkiec==3.1.14',
    'huaweicloudsdkief==3.1.14',
    'huaweicloudsdkies==3.1.14',
    'huaweicloudsdkimage==3.1.14',
    'huaweicloudsdkimagesearch==3.1.14',
    'huaweicloudsdkims==3.1.14',
    'huaweicloudsdkiotanalytics==3.1.14',
    'huaweicloudsdkiotda==3.1.14',
    'huaweicloudsdkiotedge==3.1.14',
    'huaweicloudsdkivs==3.1.14',
    'huaweicloudsdkkafka==3.1.14',
    'huaweicloudsdkkms==3.1.14',
    'huaweicloudsdkkps==3.1.14',
    'huaweicloudsdklive==3.1.14',
    'huaweicloudsdklts==3.1.14',
    'huaweicloudsdkmas==3.1.14',
    'huaweicloudsdkmeeting==3.1.14',
    'huaweicloudsdkmoderation==3.1.14',
    'huaweicloudsdkmpc==3.1.14',
    'huaweicloudsdkmrs==3.1.14',
    'huaweicloudsdknat==3.1.14',
    'huaweicloudsdknlp==3.1.14',
    'huaweicloudsdkocr==3.1.14',
    'huaweicloudsdkoms==3.1.14',
    'huaweicloudsdkosm==3.1.14',
    'huaweicloudsdkprojectman==3.1.14',
    'huaweicloudsdkrabbitmq==3.1.14',
    'huaweicloudsdkrds==3.1.14',
    'huaweicloudsdkres==3.1.14',
    'huaweicloudsdkrms==3.1.14',
    'huaweicloudsdkrocketmq==3.1.14',
    'huaweicloudsdkroma==3.1.14',
    'huaweicloudsdksa==3.1.14',
    'huaweicloudsdkscm==3.1.14',
    'huaweicloudsdksdrs==3.1.14',
    'huaweicloudsdkservicestage==3.1.14',
    'huaweicloudsdksfsturbo==3.1.14',
    'huaweicloudsdksis==3.1.14',
    'huaweicloudsdksmn==3.1.14',
    'huaweicloudsdksms==3.1.14',
    'huaweicloudsdkswr==3.1.14',
    'huaweicloudsdktms==3.1.14',
    'huaweicloudsdkugo==3.1.14',
    'huaweicloudsdkvas==3.1.14',
    'huaweicloudsdkvcm==3.1.14',
    'huaweicloudsdkvod==3.1.14',
    'huaweicloudsdkvpc==3.1.14',
    'huaweicloudsdkvpcep==3.1.14',
    'huaweicloudsdkvss==3.1.14',
    'huaweicloudsdkwaf==3.1.14',
    'huaweicloudsdkworkspace==3.1.14',
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
