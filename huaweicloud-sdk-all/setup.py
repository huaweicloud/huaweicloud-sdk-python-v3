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
VERSION = "3.1.15"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.15',
    'huaweicloudsdkantiddos==3.1.15',
    'huaweicloudsdkaom==3.1.15',
    'huaweicloudsdkaos==3.1.15',
    'huaweicloudsdkapig==3.1.15',
    'huaweicloudsdkapm==3.1.15',
    'huaweicloudsdkas==3.1.15',
    'huaweicloudsdkbcs==3.1.15',
    'huaweicloudsdkbms==3.1.15',
    'huaweicloudsdkbss==3.1.15',
    'huaweicloudsdkbssintl==3.1.15',
    'huaweicloudsdkcae==3.1.15',
    'huaweicloudsdkcampusgo==3.1.15',
    'huaweicloudsdkcbh==3.1.15',
    'huaweicloudsdkcbr==3.1.15',
    'huaweicloudsdkcbs==3.1.15',
    'huaweicloudsdkcc==3.1.15',
    'huaweicloudsdkcce==3.1.15',
    'huaweicloudsdkccm==3.1.15',
    'huaweicloudsdkcdm==3.1.15',
    'huaweicloudsdkcdn==3.1.15',
    'huaweicloudsdkces==3.1.15',
    'huaweicloudsdkcfw==3.1.15',
    'huaweicloudsdkcgs==3.1.15',
    'huaweicloudsdkclassroom==3.1.15',
    'huaweicloudsdkcloudartifact==3.1.15',
    'huaweicloudsdkcloudbuild==3.1.15',
    'huaweicloudsdkclouddeploy==3.1.15',
    'huaweicloudsdkcloudide==3.1.15',
    'huaweicloudsdkcloudpipeline==3.1.15',
    'huaweicloudsdkcloudrtc==3.1.15',
    'huaweicloudsdkcloudtable==3.1.15',
    'huaweicloudsdkcloudtest==3.1.15',
    'huaweicloudsdkcodecheck==3.1.15',
    'huaweicloudsdkcodecraft==3.1.15',
    'huaweicloudsdkcodehub==3.1.15',
    'huaweicloudsdkcph==3.1.15',
    'huaweicloudsdkcpts==3.1.15',
    'huaweicloudsdkcse==3.1.15',
    'huaweicloudsdkcsms==3.1.15',
    'huaweicloudsdkcss==3.1.15',
    'huaweicloudsdkcts==3.1.15',
    'huaweicloudsdkdas==3.1.15',
    'huaweicloudsdkdbss==3.1.15',
    'huaweicloudsdkdc==3.1.15',
    'huaweicloudsdkdcs==3.1.15',
    'huaweicloudsdkddm==3.1.15',
    'huaweicloudsdkdds==3.1.15',
    'huaweicloudsdkdeh==3.1.15',
    'huaweicloudsdkdevsecurity==3.1.15',
    'huaweicloudsdkdevstar==3.1.15',
    'huaweicloudsdkdgc==3.1.15',
    'huaweicloudsdkdli==3.1.15',
    'huaweicloudsdkdms==3.1.15',
    'huaweicloudsdkdns==3.1.15',
    'huaweicloudsdkdrs==3.1.15',
    'huaweicloudsdkdsc==3.1.15',
    'huaweicloudsdkdwr==3.1.15',
    'huaweicloudsdkdws==3.1.15',
    'huaweicloudsdkecs==3.1.15',
    'huaweicloudsdkeg==3.1.15',
    'huaweicloudsdkeihealth==3.1.15',
    'huaweicloudsdkeip==3.1.15',
    'huaweicloudsdkelb==3.1.15',
    'huaweicloudsdkeps==3.1.15',
    'huaweicloudsdker==3.1.15',
    'huaweicloudsdkevs==3.1.15',
    'huaweicloudsdkfrs==3.1.15',
    'huaweicloudsdkfunctiongraph==3.1.15',
    'huaweicloudsdkga==3.1.15',
    'huaweicloudsdkgaussdb==3.1.15',
    'huaweicloudsdkgaussdbfornosql==3.1.15',
    'huaweicloudsdkgaussdbforopengauss==3.1.15',
    'huaweicloudsdkges==3.1.15',
    'huaweicloudsdkgsl==3.1.15',
    'huaweicloudsdkhilens==3.1.15',
    'huaweicloudsdkhss==3.1.15',
    'huaweicloudsdkiam==3.1.15',
    'huaweicloudsdkiec==3.1.15',
    'huaweicloudsdkief==3.1.15',
    'huaweicloudsdkies==3.1.15',
    'huaweicloudsdkimage==3.1.15',
    'huaweicloudsdkimagesearch==3.1.15',
    'huaweicloudsdkims==3.1.15',
    'huaweicloudsdkiotanalytics==3.1.15',
    'huaweicloudsdkiotda==3.1.15',
    'huaweicloudsdkiotedge==3.1.15',
    'huaweicloudsdkivs==3.1.15',
    'huaweicloudsdkkafka==3.1.15',
    'huaweicloudsdkkms==3.1.15',
    'huaweicloudsdkkps==3.1.15',
    'huaweicloudsdklive==3.1.15',
    'huaweicloudsdklts==3.1.15',
    'huaweicloudsdkmapds==3.1.15',
    'huaweicloudsdkmas==3.1.15',
    'huaweicloudsdkmeeting==3.1.15',
    'huaweicloudsdkmoderation==3.1.15',
    'huaweicloudsdkmpc==3.1.15',
    'huaweicloudsdkmrs==3.1.15',
    'huaweicloudsdknat==3.1.15',
    'huaweicloudsdknlp==3.1.15',
    'huaweicloudsdkocr==3.1.15',
    'huaweicloudsdkoms==3.1.15',
    'huaweicloudsdkosm==3.1.15',
    'huaweicloudsdkprojectman==3.1.15',
    'huaweicloudsdkrabbitmq==3.1.15',
    'huaweicloudsdkrds==3.1.15',
    'huaweicloudsdkres==3.1.15',
    'huaweicloudsdkrms==3.1.15',
    'huaweicloudsdkrocketmq==3.1.15',
    'huaweicloudsdkroma==3.1.15',
    'huaweicloudsdksa==3.1.15',
    'huaweicloudsdkscm==3.1.15',
    'huaweicloudsdksdrs==3.1.15',
    'huaweicloudsdkservicestage==3.1.15',
    'huaweicloudsdksfsturbo==3.1.15',
    'huaweicloudsdksis==3.1.15',
    'huaweicloudsdksmn==3.1.15',
    'huaweicloudsdksms==3.1.15',
    'huaweicloudsdkswr==3.1.15',
    'huaweicloudsdktms==3.1.15',
    'huaweicloudsdkugo==3.1.15',
    'huaweicloudsdkvas==3.1.15',
    'huaweicloudsdkvcm==3.1.15',
    'huaweicloudsdkvod==3.1.15',
    'huaweicloudsdkvpc==3.1.15',
    'huaweicloudsdkvpcep==3.1.15',
    'huaweicloudsdkvss==3.1.15',
    'huaweicloudsdkwaf==3.1.15',
    'huaweicloudsdkworkspace==3.1.15',
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
