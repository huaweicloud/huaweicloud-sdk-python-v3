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
VERSION = "3.1.16"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.16',
    'huaweicloudsdkantiddos==3.1.16',
    'huaweicloudsdkaom==3.1.16',
    'huaweicloudsdkaos==3.1.16',
    'huaweicloudsdkapig==3.1.16',
    'huaweicloudsdkapm==3.1.16',
    'huaweicloudsdkas==3.1.16',
    'huaweicloudsdkbcs==3.1.16',
    'huaweicloudsdkbms==3.1.16',
    'huaweicloudsdkbss==3.1.16',
    'huaweicloudsdkbssintl==3.1.16',
    'huaweicloudsdkcae==3.1.16',
    'huaweicloudsdkcampusgo==3.1.16',
    'huaweicloudsdkcbh==3.1.16',
    'huaweicloudsdkcbr==3.1.16',
    'huaweicloudsdkcbs==3.1.16',
    'huaweicloudsdkcc==3.1.16',
    'huaweicloudsdkcce==3.1.16',
    'huaweicloudsdkccm==3.1.16',
    'huaweicloudsdkcdm==3.1.16',
    'huaweicloudsdkcdn==3.1.16',
    'huaweicloudsdkces==3.1.16',
    'huaweicloudsdkcfw==3.1.16',
    'huaweicloudsdkcgs==3.1.16',
    'huaweicloudsdkclassroom==3.1.16',
    'huaweicloudsdkcloudartifact==3.1.16',
    'huaweicloudsdkcloudbuild==3.1.16',
    'huaweicloudsdkclouddeploy==3.1.16',
    'huaweicloudsdkcloudide==3.1.16',
    'huaweicloudsdkcloudpipeline==3.1.16',
    'huaweicloudsdkcloudrtc==3.1.16',
    'huaweicloudsdkcloudtable==3.1.16',
    'huaweicloudsdkcloudtest==3.1.16',
    'huaweicloudsdkcodecheck==3.1.16',
    'huaweicloudsdkcodecraft==3.1.16',
    'huaweicloudsdkcodehub==3.1.16',
    'huaweicloudsdkcph==3.1.16',
    'huaweicloudsdkcpts==3.1.16',
    'huaweicloudsdkcse==3.1.16',
    'huaweicloudsdkcsms==3.1.16',
    'huaweicloudsdkcss==3.1.16',
    'huaweicloudsdkcts==3.1.16',
    'huaweicloudsdkdas==3.1.16',
    'huaweicloudsdkdbss==3.1.16',
    'huaweicloudsdkdc==3.1.16',
    'huaweicloudsdkdcs==3.1.16',
    'huaweicloudsdkddm==3.1.16',
    'huaweicloudsdkdds==3.1.16',
    'huaweicloudsdkdeh==3.1.16',
    'huaweicloudsdkdevsecurity==3.1.16',
    'huaweicloudsdkdevstar==3.1.16',
    'huaweicloudsdkdgc==3.1.16',
    'huaweicloudsdkdlf==3.1.16',
    'huaweicloudsdkdli==3.1.16',
    'huaweicloudsdkdms==3.1.16',
    'huaweicloudsdkdns==3.1.16',
    'huaweicloudsdkdrs==3.1.16',
    'huaweicloudsdkdsc==3.1.16',
    'huaweicloudsdkdwr==3.1.16',
    'huaweicloudsdkdws==3.1.16',
    'huaweicloudsdkecs==3.1.16',
    'huaweicloudsdkeg==3.1.16',
    'huaweicloudsdkeihealth==3.1.16',
    'huaweicloudsdkeip==3.1.16',
    'huaweicloudsdkelb==3.1.16',
    'huaweicloudsdkeps==3.1.16',
    'huaweicloudsdker==3.1.16',
    'huaweicloudsdkevs==3.1.16',
    'huaweicloudsdkfrs==3.1.16',
    'huaweicloudsdkfunctiongraph==3.1.16',
    'huaweicloudsdkga==3.1.16',
    'huaweicloudsdkgaussdb==3.1.16',
    'huaweicloudsdkgaussdbfornosql==3.1.16',
    'huaweicloudsdkgaussdbforopengauss==3.1.16',
    'huaweicloudsdkges==3.1.16',
    'huaweicloudsdkgsl==3.1.16',
    'huaweicloudsdkhilens==3.1.16',
    'huaweicloudsdkhss==3.1.16',
    'huaweicloudsdkiam==3.1.16',
    'huaweicloudsdkiec==3.1.16',
    'huaweicloudsdkief==3.1.16',
    'huaweicloudsdkies==3.1.16',
    'huaweicloudsdkimage==3.1.16',
    'huaweicloudsdkimagesearch==3.1.16',
    'huaweicloudsdkims==3.1.16',
    'huaweicloudsdkiotanalytics==3.1.16',
    'huaweicloudsdkiotda==3.1.16',
    'huaweicloudsdkiotedge==3.1.16',
    'huaweicloudsdkivs==3.1.16',
    'huaweicloudsdkkafka==3.1.16',
    'huaweicloudsdkkms==3.1.16',
    'huaweicloudsdkkps==3.1.16',
    'huaweicloudsdklive==3.1.16',
    'huaweicloudsdklts==3.1.16',
    'huaweicloudsdkmapds==3.1.16',
    'huaweicloudsdkmas==3.1.16',
    'huaweicloudsdkmeeting==3.1.16',
    'huaweicloudsdkmoderation==3.1.16',
    'huaweicloudsdkmpc==3.1.16',
    'huaweicloudsdkmrs==3.1.16',
    'huaweicloudsdknat==3.1.16',
    'huaweicloudsdknlp==3.1.16',
    'huaweicloudsdkocr==3.1.16',
    'huaweicloudsdkoms==3.1.16',
    'huaweicloudsdkosm==3.1.16',
    'huaweicloudsdkprojectman==3.1.16',
    'huaweicloudsdkrabbitmq==3.1.16',
    'huaweicloudsdkrds==3.1.16',
    'huaweicloudsdkres==3.1.16',
    'huaweicloudsdkrms==3.1.16',
    'huaweicloudsdkrocketmq==3.1.16',
    'huaweicloudsdkroma==3.1.16',
    'huaweicloudsdksa==3.1.16',
    'huaweicloudsdkscm==3.1.16',
    'huaweicloudsdksdrs==3.1.16',
    'huaweicloudsdkservicestage==3.1.16',
    'huaweicloudsdksfsturbo==3.1.16',
    'huaweicloudsdksis==3.1.16',
    'huaweicloudsdksmn==3.1.16',
    'huaweicloudsdksms==3.1.16',
    'huaweicloudsdkswr==3.1.16',
    'huaweicloudsdktms==3.1.16',
    'huaweicloudsdkugo==3.1.16',
    'huaweicloudsdkvas==3.1.16',
    'huaweicloudsdkvcm==3.1.16',
    'huaweicloudsdkvod==3.1.16',
    'huaweicloudsdkvpc==3.1.16',
    'huaweicloudsdkvpcep==3.1.16',
    'huaweicloudsdkvss==3.1.16',
    'huaweicloudsdkwaf==3.1.16',
    'huaweicloudsdkworkspace==3.1.16',
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
