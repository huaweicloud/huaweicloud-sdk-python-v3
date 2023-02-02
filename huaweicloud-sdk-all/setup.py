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
VERSION = "3.1.24"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.24',
    'huaweicloudsdkantiddos==3.1.24',
    'huaweicloudsdkaom==3.1.24',
    'huaweicloudsdkaos==3.1.24',
    'huaweicloudsdkapig==3.1.24',
    'huaweicloudsdkapm==3.1.24',
    'huaweicloudsdkas==3.1.24',
    'huaweicloudsdkbcs==3.1.24',
    'huaweicloudsdkbms==3.1.24',
    'huaweicloudsdkbss==3.1.24',
    'huaweicloudsdkbssintl==3.1.24',
    'huaweicloudsdkcae==3.1.24',
    'huaweicloudsdkcampusgo==3.1.24',
    'huaweicloudsdkcbh==3.1.24',
    'huaweicloudsdkcbr==3.1.24',
    'huaweicloudsdkcbs==3.1.24',
    'huaweicloudsdkcc==3.1.24',
    'huaweicloudsdkcce==3.1.24',
    'huaweicloudsdkccm==3.1.24',
    'huaweicloudsdkcdm==3.1.24',
    'huaweicloudsdkcdn==3.1.24',
    'huaweicloudsdkces==3.1.24',
    'huaweicloudsdkcfw==3.1.24',
    'huaweicloudsdkcgs==3.1.24',
    'huaweicloudsdkclassroom==3.1.24',
    'huaweicloudsdkcloudartifact==3.1.24',
    'huaweicloudsdkcloudbuild==3.1.24',
    'huaweicloudsdkclouddeploy==3.1.24',
    'huaweicloudsdkcloudide==3.1.24',
    'huaweicloudsdkcloudpipeline==3.1.24',
    'huaweicloudsdkcloudrtc==3.1.24',
    'huaweicloudsdkcloudtable==3.1.24',
    'huaweicloudsdkcloudtest==3.1.24',
    'huaweicloudsdkcodecheck==3.1.24',
    'huaweicloudsdkcodecraft==3.1.24',
    'huaweicloudsdkcodehub==3.1.24',
    'huaweicloudsdkcph==3.1.24',
    'huaweicloudsdkcpts==3.1.24',
    'huaweicloudsdkcse==3.1.24',
    'huaweicloudsdkcsms==3.1.24',
    'huaweicloudsdkcss==3.1.24',
    'huaweicloudsdkcts==3.1.24',
    'huaweicloudsdkdas==3.1.24',
    'huaweicloudsdkdbss==3.1.24',
    'huaweicloudsdkdc==3.1.24',
    'huaweicloudsdkdcs==3.1.24',
    'huaweicloudsdkddm==3.1.24',
    'huaweicloudsdkdds==3.1.24',
    'huaweicloudsdkdeh==3.1.24',
    'huaweicloudsdkdevsecurity==3.1.24',
    'huaweicloudsdkdevstar==3.1.24',
    'huaweicloudsdkdgc==3.1.24',
    'huaweicloudsdkdlf==3.1.24',
    'huaweicloudsdkdli==3.1.24',
    'huaweicloudsdkdms==3.1.24',
    'huaweicloudsdkdns==3.1.24',
    'huaweicloudsdkdris==3.1.24',
    'huaweicloudsdkdrs==3.1.24',
    'huaweicloudsdkdsc==3.1.24',
    'huaweicloudsdkdwr==3.1.24',
    'huaweicloudsdkdws==3.1.24',
    'huaweicloudsdkecs==3.1.24',
    'huaweicloudsdkeg==3.1.24',
    'huaweicloudsdkeihealth==3.1.24',
    'huaweicloudsdkeip==3.1.24',
    'huaweicloudsdkelb==3.1.24',
    'huaweicloudsdkeps==3.1.24',
    'huaweicloudsdker==3.1.24',
    'huaweicloudsdkevs==3.1.24',
    'huaweicloudsdkfrs==3.1.24',
    'huaweicloudsdkfunctiongraph==3.1.24',
    'huaweicloudsdkga==3.1.24',
    'huaweicloudsdkgaussdb==3.1.24',
    'huaweicloudsdkgaussdbfornosql==3.1.24',
    'huaweicloudsdkgaussdbforopengauss==3.1.24',
    'huaweicloudsdkges==3.1.24',
    'huaweicloudsdkgsl==3.1.24',
    'huaweicloudsdkhilens==3.1.24',
    'huaweicloudsdkhss==3.1.24',
    'huaweicloudsdkiam==3.1.24',
    'huaweicloudsdkiec==3.1.24',
    'huaweicloudsdkief==3.1.24',
    'huaweicloudsdkies==3.1.24',
    'huaweicloudsdkimage==3.1.24',
    'huaweicloudsdkimagesearch==3.1.24',
    'huaweicloudsdkims==3.1.24',
    'huaweicloudsdkiotanalytics==3.1.24',
    'huaweicloudsdkiotda==3.1.24',
    'huaweicloudsdkiotedge==3.1.24',
    'huaweicloudsdkivs==3.1.24',
    'huaweicloudsdkkafka==3.1.24',
    'huaweicloudsdkkms==3.1.24',
    'huaweicloudsdkkps==3.1.24',
    'huaweicloudsdklive==3.1.24',
    'huaweicloudsdklts==3.1.24',
    'huaweicloudsdkmapds==3.1.24',
    'huaweicloudsdkmas==3.1.24',
    'huaweicloudsdkmeeting==3.1.24',
    'huaweicloudsdkmoderation==3.1.24',
    'huaweicloudsdkmpc==3.1.24',
    'huaweicloudsdkmrs==3.1.24',
    'huaweicloudsdknat==3.1.24',
    'huaweicloudsdknlp==3.1.24',
    'huaweicloudsdkocr==3.1.24',
    'huaweicloudsdkoms==3.1.24',
    'huaweicloudsdkosm==3.1.24',
    'huaweicloudsdkprojectman==3.1.24',
    'huaweicloudsdkrabbitmq==3.1.24',
    'huaweicloudsdkrds==3.1.24',
    'huaweicloudsdkres==3.1.24',
    'huaweicloudsdkrms==3.1.24',
    'huaweicloudsdkrocketmq==3.1.24',
    'huaweicloudsdkroma==3.1.24',
    'huaweicloudsdksa==3.1.24',
    'huaweicloudsdkscm==3.1.24',
    'huaweicloudsdksdrs==3.1.24',
    'huaweicloudsdksecmaster==3.1.24',
    'huaweicloudsdkservicestage==3.1.24',
    'huaweicloudsdksfsturbo==3.1.24',
    'huaweicloudsdksis==3.1.24',
    'huaweicloudsdksmn==3.1.24',
    'huaweicloudsdksms==3.1.24',
    'huaweicloudsdkswr==3.1.24',
    'huaweicloudsdktms==3.1.24',
    'huaweicloudsdkugo==3.1.24',
    'huaweicloudsdkvas==3.1.24',
    'huaweicloudsdkvcm==3.1.24',
    'huaweicloudsdkvod==3.1.24',
    'huaweicloudsdkvpc==3.1.24',
    'huaweicloudsdkvpcep==3.1.24',
    'huaweicloudsdkvss==3.1.24',
    'huaweicloudsdkwaf==3.1.24',
    'huaweicloudsdkworkspace==3.1.24',
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
