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
VERSION = "3.1.23"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.23',
    'huaweicloudsdkantiddos==3.1.23',
    'huaweicloudsdkaom==3.1.23',
    'huaweicloudsdkaos==3.1.23',
    'huaweicloudsdkapig==3.1.23',
    'huaweicloudsdkapm==3.1.23',
    'huaweicloudsdkas==3.1.23',
    'huaweicloudsdkbcs==3.1.23',
    'huaweicloudsdkbms==3.1.23',
    'huaweicloudsdkbss==3.1.23',
    'huaweicloudsdkbssintl==3.1.23',
    'huaweicloudsdkcae==3.1.23',
    'huaweicloudsdkcampusgo==3.1.23',
    'huaweicloudsdkcbh==3.1.23',
    'huaweicloudsdkcbr==3.1.23',
    'huaweicloudsdkcbs==3.1.23',
    'huaweicloudsdkcc==3.1.23',
    'huaweicloudsdkcce==3.1.23',
    'huaweicloudsdkccm==3.1.23',
    'huaweicloudsdkcdm==3.1.23',
    'huaweicloudsdkcdn==3.1.23',
    'huaweicloudsdkces==3.1.23',
    'huaweicloudsdkcfw==3.1.23',
    'huaweicloudsdkcgs==3.1.23',
    'huaweicloudsdkclassroom==3.1.23',
    'huaweicloudsdkcloudartifact==3.1.23',
    'huaweicloudsdkcloudbuild==3.1.23',
    'huaweicloudsdkclouddeploy==3.1.23',
    'huaweicloudsdkcloudide==3.1.23',
    'huaweicloudsdkcloudpipeline==3.1.23',
    'huaweicloudsdkcloudrtc==3.1.23',
    'huaweicloudsdkcloudtable==3.1.23',
    'huaweicloudsdkcloudtest==3.1.23',
    'huaweicloudsdkcodecheck==3.1.23',
    'huaweicloudsdkcodecraft==3.1.23',
    'huaweicloudsdkcodehub==3.1.23',
    'huaweicloudsdkcph==3.1.23',
    'huaweicloudsdkcpts==3.1.23',
    'huaweicloudsdkcse==3.1.23',
    'huaweicloudsdkcsms==3.1.23',
    'huaweicloudsdkcss==3.1.23',
    'huaweicloudsdkcts==3.1.23',
    'huaweicloudsdkdas==3.1.23',
    'huaweicloudsdkdbss==3.1.23',
    'huaweicloudsdkdc==3.1.23',
    'huaweicloudsdkdcs==3.1.23',
    'huaweicloudsdkddm==3.1.23',
    'huaweicloudsdkdds==3.1.23',
    'huaweicloudsdkdeh==3.1.23',
    'huaweicloudsdkdevsecurity==3.1.23',
    'huaweicloudsdkdevstar==3.1.23',
    'huaweicloudsdkdgc==3.1.23',
    'huaweicloudsdkdlf==3.1.23',
    'huaweicloudsdkdli==3.1.23',
    'huaweicloudsdkdms==3.1.23',
    'huaweicloudsdkdns==3.1.23',
    'huaweicloudsdkdris==3.1.23',
    'huaweicloudsdkdrs==3.1.23',
    'huaweicloudsdkdsc==3.1.23',
    'huaweicloudsdkdwr==3.1.23',
    'huaweicloudsdkdws==3.1.23',
    'huaweicloudsdkecs==3.1.23',
    'huaweicloudsdkeg==3.1.23',
    'huaweicloudsdkeihealth==3.1.23',
    'huaweicloudsdkeip==3.1.23',
    'huaweicloudsdkelb==3.1.23',
    'huaweicloudsdkeps==3.1.23',
    'huaweicloudsdker==3.1.23',
    'huaweicloudsdkevs==3.1.23',
    'huaweicloudsdkfrs==3.1.23',
    'huaweicloudsdkfunctiongraph==3.1.23',
    'huaweicloudsdkga==3.1.23',
    'huaweicloudsdkgaussdb==3.1.23',
    'huaweicloudsdkgaussdbfornosql==3.1.23',
    'huaweicloudsdkgaussdbforopengauss==3.1.23',
    'huaweicloudsdkges==3.1.23',
    'huaweicloudsdkgsl==3.1.23',
    'huaweicloudsdkhilens==3.1.23',
    'huaweicloudsdkhss==3.1.23',
    'huaweicloudsdkiam==3.1.23',
    'huaweicloudsdkiec==3.1.23',
    'huaweicloudsdkief==3.1.23',
    'huaweicloudsdkies==3.1.23',
    'huaweicloudsdkimage==3.1.23',
    'huaweicloudsdkimagesearch==3.1.23',
    'huaweicloudsdkims==3.1.23',
    'huaweicloudsdkiotanalytics==3.1.23',
    'huaweicloudsdkiotda==3.1.23',
    'huaweicloudsdkiotedge==3.1.23',
    'huaweicloudsdkivs==3.1.23',
    'huaweicloudsdkkafka==3.1.23',
    'huaweicloudsdkkms==3.1.23',
    'huaweicloudsdkkps==3.1.23',
    'huaweicloudsdklive==3.1.23',
    'huaweicloudsdklts==3.1.23',
    'huaweicloudsdkmapds==3.1.23',
    'huaweicloudsdkmas==3.1.23',
    'huaweicloudsdkmeeting==3.1.23',
    'huaweicloudsdkmoderation==3.1.23',
    'huaweicloudsdkmpc==3.1.23',
    'huaweicloudsdkmrs==3.1.23',
    'huaweicloudsdknat==3.1.23',
    'huaweicloudsdknlp==3.1.23',
    'huaweicloudsdkocr==3.1.23',
    'huaweicloudsdkoms==3.1.23',
    'huaweicloudsdkosm==3.1.23',
    'huaweicloudsdkprojectman==3.1.23',
    'huaweicloudsdkrabbitmq==3.1.23',
    'huaweicloudsdkrds==3.1.23',
    'huaweicloudsdkres==3.1.23',
    'huaweicloudsdkrms==3.1.23',
    'huaweicloudsdkrocketmq==3.1.23',
    'huaweicloudsdkroma==3.1.23',
    'huaweicloudsdksa==3.1.23',
    'huaweicloudsdkscm==3.1.23',
    'huaweicloudsdksdrs==3.1.23',
    'huaweicloudsdksecmaster==3.1.23',
    'huaweicloudsdkservicestage==3.1.23',
    'huaweicloudsdksfsturbo==3.1.23',
    'huaweicloudsdksis==3.1.23',
    'huaweicloudsdksmn==3.1.23',
    'huaweicloudsdksms==3.1.23',
    'huaweicloudsdkswr==3.1.23',
    'huaweicloudsdktms==3.1.23',
    'huaweicloudsdkugo==3.1.23',
    'huaweicloudsdkvas==3.1.23',
    'huaweicloudsdkvcm==3.1.23',
    'huaweicloudsdkvod==3.1.23',
    'huaweicloudsdkvpc==3.1.23',
    'huaweicloudsdkvpcep==3.1.23',
    'huaweicloudsdkvss==3.1.23',
    'huaweicloudsdkwaf==3.1.23',
    'huaweicloudsdkworkspace==3.1.23',
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
