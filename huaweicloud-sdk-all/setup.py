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
VERSION = "3.1.18"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.18',
    'huaweicloudsdkantiddos==3.1.18',
    'huaweicloudsdkaom==3.1.18',
    'huaweicloudsdkaos==3.1.18',
    'huaweicloudsdkapig==3.1.18',
    'huaweicloudsdkapm==3.1.18',
    'huaweicloudsdkas==3.1.18',
    'huaweicloudsdkbcs==3.1.18',
    'huaweicloudsdkbms==3.1.18',
    'huaweicloudsdkbss==3.1.18',
    'huaweicloudsdkbssintl==3.1.18',
    'huaweicloudsdkcae==3.1.18',
    'huaweicloudsdkcampusgo==3.1.18',
    'huaweicloudsdkcbh==3.1.18',
    'huaweicloudsdkcbr==3.1.18',
    'huaweicloudsdkcbs==3.1.18',
    'huaweicloudsdkcc==3.1.18',
    'huaweicloudsdkcce==3.1.18',
    'huaweicloudsdkccm==3.1.18',
    'huaweicloudsdkcdm==3.1.18',
    'huaweicloudsdkcdn==3.1.18',
    'huaweicloudsdkces==3.1.18',
    'huaweicloudsdkcfw==3.1.18',
    'huaweicloudsdkcgs==3.1.18',
    'huaweicloudsdkclassroom==3.1.18',
    'huaweicloudsdkcloudartifact==3.1.18',
    'huaweicloudsdkcloudbuild==3.1.18',
    'huaweicloudsdkclouddeploy==3.1.18',
    'huaweicloudsdkcloudide==3.1.18',
    'huaweicloudsdkcloudpipeline==3.1.18',
    'huaweicloudsdkcloudrtc==3.1.18',
    'huaweicloudsdkcloudtable==3.1.18',
    'huaweicloudsdkcloudtest==3.1.18',
    'huaweicloudsdkcodecheck==3.1.18',
    'huaweicloudsdkcodecraft==3.1.18',
    'huaweicloudsdkcodehub==3.1.18',
    'huaweicloudsdkcph==3.1.18',
    'huaweicloudsdkcpts==3.1.18',
    'huaweicloudsdkcse==3.1.18',
    'huaweicloudsdkcsms==3.1.18',
    'huaweicloudsdkcss==3.1.18',
    'huaweicloudsdkcts==3.1.18',
    'huaweicloudsdkdas==3.1.18',
    'huaweicloudsdkdbss==3.1.18',
    'huaweicloudsdkdc==3.1.18',
    'huaweicloudsdkdcs==3.1.18',
    'huaweicloudsdkddm==3.1.18',
    'huaweicloudsdkdds==3.1.18',
    'huaweicloudsdkdeh==3.1.18',
    'huaweicloudsdkdevsecurity==3.1.18',
    'huaweicloudsdkdevstar==3.1.18',
    'huaweicloudsdkdgc==3.1.18',
    'huaweicloudsdkdlf==3.1.18',
    'huaweicloudsdkdli==3.1.18',
    'huaweicloudsdkdms==3.1.18',
    'huaweicloudsdkdns==3.1.18',
    'huaweicloudsdkdris==3.1.18',
    'huaweicloudsdkdrs==3.1.18',
    'huaweicloudsdkdsc==3.1.18',
    'huaweicloudsdkdwr==3.1.18',
    'huaweicloudsdkdws==3.1.18',
    'huaweicloudsdkecs==3.1.18',
    'huaweicloudsdkeg==3.1.18',
    'huaweicloudsdkeihealth==3.1.18',
    'huaweicloudsdkeip==3.1.18',
    'huaweicloudsdkelb==3.1.18',
    'huaweicloudsdkeps==3.1.18',
    'huaweicloudsdker==3.1.18',
    'huaweicloudsdkevs==3.1.18',
    'huaweicloudsdkfrs==3.1.18',
    'huaweicloudsdkfunctiongraph==3.1.18',
    'huaweicloudsdkga==3.1.18',
    'huaweicloudsdkgaussdb==3.1.18',
    'huaweicloudsdkgaussdbfornosql==3.1.18',
    'huaweicloudsdkgaussdbforopengauss==3.1.18',
    'huaweicloudsdkges==3.1.18',
    'huaweicloudsdkgsl==3.1.18',
    'huaweicloudsdkhilens==3.1.18',
    'huaweicloudsdkhss==3.1.18',
    'huaweicloudsdkiam==3.1.18',
    'huaweicloudsdkiec==3.1.18',
    'huaweicloudsdkief==3.1.18',
    'huaweicloudsdkies==3.1.18',
    'huaweicloudsdkimage==3.1.18',
    'huaweicloudsdkimagesearch==3.1.18',
    'huaweicloudsdkims==3.1.18',
    'huaweicloudsdkiotanalytics==3.1.18',
    'huaweicloudsdkiotda==3.1.18',
    'huaweicloudsdkiotedge==3.1.18',
    'huaweicloudsdkivs==3.1.18',
    'huaweicloudsdkkafka==3.1.18',
    'huaweicloudsdkkms==3.1.18',
    'huaweicloudsdkkps==3.1.18',
    'huaweicloudsdklive==3.1.18',
    'huaweicloudsdklts==3.1.18',
    'huaweicloudsdkmapds==3.1.18',
    'huaweicloudsdkmas==3.1.18',
    'huaweicloudsdkmeeting==3.1.18',
    'huaweicloudsdkmoderation==3.1.18',
    'huaweicloudsdkmpc==3.1.18',
    'huaweicloudsdkmrs==3.1.18',
    'huaweicloudsdknat==3.1.18',
    'huaweicloudsdknlp==3.1.18',
    'huaweicloudsdkocr==3.1.18',
    'huaweicloudsdkoms==3.1.18',
    'huaweicloudsdkosm==3.1.18',
    'huaweicloudsdkprojectman==3.1.18',
    'huaweicloudsdkrabbitmq==3.1.18',
    'huaweicloudsdkrds==3.1.18',
    'huaweicloudsdkres==3.1.18',
    'huaweicloudsdkrms==3.1.18',
    'huaweicloudsdkrocketmq==3.1.18',
    'huaweicloudsdkroma==3.1.18',
    'huaweicloudsdksa==3.1.18',
    'huaweicloudsdkscm==3.1.18',
    'huaweicloudsdksdrs==3.1.18',
    'huaweicloudsdkservicestage==3.1.18',
    'huaweicloudsdksfsturbo==3.1.18',
    'huaweicloudsdksis==3.1.18',
    'huaweicloudsdksmn==3.1.18',
    'huaweicloudsdksms==3.1.18',
    'huaweicloudsdkswr==3.1.18',
    'huaweicloudsdktms==3.1.18',
    'huaweicloudsdkugo==3.1.18',
    'huaweicloudsdkvas==3.1.18',
    'huaweicloudsdkvcm==3.1.18',
    'huaweicloudsdkvod==3.1.18',
    'huaweicloudsdkvpc==3.1.18',
    'huaweicloudsdkvpcep==3.1.18',
    'huaweicloudsdkvss==3.1.18',
    'huaweicloudsdkwaf==3.1.18',
    'huaweicloudsdkworkspace==3.1.18',
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
