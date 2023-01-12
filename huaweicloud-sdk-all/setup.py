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
VERSION = "3.1.22"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.22',
    'huaweicloudsdkantiddos==3.1.22',
    'huaweicloudsdkaom==3.1.22',
    'huaweicloudsdkaos==3.1.22',
    'huaweicloudsdkapig==3.1.22',
    'huaweicloudsdkapm==3.1.22',
    'huaweicloudsdkas==3.1.22',
    'huaweicloudsdkbcs==3.1.22',
    'huaweicloudsdkbms==3.1.22',
    'huaweicloudsdkbss==3.1.22',
    'huaweicloudsdkbssintl==3.1.22',
    'huaweicloudsdkcae==3.1.22',
    'huaweicloudsdkcampusgo==3.1.22',
    'huaweicloudsdkcbh==3.1.22',
    'huaweicloudsdkcbr==3.1.22',
    'huaweicloudsdkcbs==3.1.22',
    'huaweicloudsdkcc==3.1.22',
    'huaweicloudsdkcce==3.1.22',
    'huaweicloudsdkccm==3.1.22',
    'huaweicloudsdkcdm==3.1.22',
    'huaweicloudsdkcdn==3.1.22',
    'huaweicloudsdkces==3.1.22',
    'huaweicloudsdkcfw==3.1.22',
    'huaweicloudsdkcgs==3.1.22',
    'huaweicloudsdkclassroom==3.1.22',
    'huaweicloudsdkcloudartifact==3.1.22',
    'huaweicloudsdkcloudbuild==3.1.22',
    'huaweicloudsdkclouddeploy==3.1.22',
    'huaweicloudsdkcloudide==3.1.22',
    'huaweicloudsdkcloudpipeline==3.1.22',
    'huaweicloudsdkcloudrtc==3.1.22',
    'huaweicloudsdkcloudtable==3.1.22',
    'huaweicloudsdkcloudtest==3.1.22',
    'huaweicloudsdkcodecheck==3.1.22',
    'huaweicloudsdkcodecraft==3.1.22',
    'huaweicloudsdkcodehub==3.1.22',
    'huaweicloudsdkcph==3.1.22',
    'huaweicloudsdkcpts==3.1.22',
    'huaweicloudsdkcse==3.1.22',
    'huaweicloudsdkcsms==3.1.22',
    'huaweicloudsdkcss==3.1.22',
    'huaweicloudsdkcts==3.1.22',
    'huaweicloudsdkdas==3.1.22',
    'huaweicloudsdkdbss==3.1.22',
    'huaweicloudsdkdc==3.1.22',
    'huaweicloudsdkdcs==3.1.22',
    'huaweicloudsdkddm==3.1.22',
    'huaweicloudsdkdds==3.1.22',
    'huaweicloudsdkdeh==3.1.22',
    'huaweicloudsdkdevsecurity==3.1.22',
    'huaweicloudsdkdevstar==3.1.22',
    'huaweicloudsdkdgc==3.1.22',
    'huaweicloudsdkdlf==3.1.22',
    'huaweicloudsdkdli==3.1.22',
    'huaweicloudsdkdms==3.1.22',
    'huaweicloudsdkdns==3.1.22',
    'huaweicloudsdkdris==3.1.22',
    'huaweicloudsdkdrs==3.1.22',
    'huaweicloudsdkdsc==3.1.22',
    'huaweicloudsdkdwr==3.1.22',
    'huaweicloudsdkdws==3.1.22',
    'huaweicloudsdkecs==3.1.22',
    'huaweicloudsdkeg==3.1.22',
    'huaweicloudsdkeihealth==3.1.22',
    'huaweicloudsdkeip==3.1.22',
    'huaweicloudsdkelb==3.1.22',
    'huaweicloudsdkeps==3.1.22',
    'huaweicloudsdker==3.1.22',
    'huaweicloudsdkevs==3.1.22',
    'huaweicloudsdkfrs==3.1.22',
    'huaweicloudsdkfunctiongraph==3.1.22',
    'huaweicloudsdkga==3.1.22',
    'huaweicloudsdkgaussdb==3.1.22',
    'huaweicloudsdkgaussdbfornosql==3.1.22',
    'huaweicloudsdkgaussdbforopengauss==3.1.22',
    'huaweicloudsdkges==3.1.22',
    'huaweicloudsdkgsl==3.1.22',
    'huaweicloudsdkhilens==3.1.22',
    'huaweicloudsdkhss==3.1.22',
    'huaweicloudsdkiam==3.1.22',
    'huaweicloudsdkiec==3.1.22',
    'huaweicloudsdkief==3.1.22',
    'huaweicloudsdkies==3.1.22',
    'huaweicloudsdkimage==3.1.22',
    'huaweicloudsdkimagesearch==3.1.22',
    'huaweicloudsdkims==3.1.22',
    'huaweicloudsdkiotanalytics==3.1.22',
    'huaweicloudsdkiotda==3.1.22',
    'huaweicloudsdkiotedge==3.1.22',
    'huaweicloudsdkivs==3.1.22',
    'huaweicloudsdkkafka==3.1.22',
    'huaweicloudsdkkms==3.1.22',
    'huaweicloudsdkkps==3.1.22',
    'huaweicloudsdklive==3.1.22',
    'huaweicloudsdklts==3.1.22',
    'huaweicloudsdkmapds==3.1.22',
    'huaweicloudsdkmas==3.1.22',
    'huaweicloudsdkmeeting==3.1.22',
    'huaweicloudsdkmoderation==3.1.22',
    'huaweicloudsdkmpc==3.1.22',
    'huaweicloudsdkmrs==3.1.22',
    'huaweicloudsdknat==3.1.22',
    'huaweicloudsdknlp==3.1.22',
    'huaweicloudsdkocr==3.1.22',
    'huaweicloudsdkoms==3.1.22',
    'huaweicloudsdkosm==3.1.22',
    'huaweicloudsdkprojectman==3.1.22',
    'huaweicloudsdkrabbitmq==3.1.22',
    'huaweicloudsdkrds==3.1.22',
    'huaweicloudsdkres==3.1.22',
    'huaweicloudsdkrms==3.1.22',
    'huaweicloudsdkrocketmq==3.1.22',
    'huaweicloudsdkroma==3.1.22',
    'huaweicloudsdksa==3.1.22',
    'huaweicloudsdkscm==3.1.22',
    'huaweicloudsdksdrs==3.1.22',
    'huaweicloudsdksecmaster==3.1.22',
    'huaweicloudsdkservicestage==3.1.22',
    'huaweicloudsdksfsturbo==3.1.22',
    'huaweicloudsdksis==3.1.22',
    'huaweicloudsdksmn==3.1.22',
    'huaweicloudsdksms==3.1.22',
    'huaweicloudsdkswr==3.1.22',
    'huaweicloudsdktms==3.1.22',
    'huaweicloudsdkugo==3.1.22',
    'huaweicloudsdkvas==3.1.22',
    'huaweicloudsdkvcm==3.1.22',
    'huaweicloudsdkvod==3.1.22',
    'huaweicloudsdkvpc==3.1.22',
    'huaweicloudsdkvpcep==3.1.22',
    'huaweicloudsdkvss==3.1.22',
    'huaweicloudsdkwaf==3.1.22',
    'huaweicloudsdkworkspace==3.1.22',
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
