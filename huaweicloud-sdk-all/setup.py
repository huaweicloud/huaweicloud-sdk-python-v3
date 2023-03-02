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
VERSION = "3.1.28"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.28',
    'huaweicloudsdkantiddos==3.1.28',
    'huaweicloudsdkaom==3.1.28',
    'huaweicloudsdkaos==3.1.28',
    'huaweicloudsdkapig==3.1.28',
    'huaweicloudsdkapm==3.1.28',
    'huaweicloudsdkas==3.1.28',
    'huaweicloudsdkbcs==3.1.28',
    'huaweicloudsdkbms==3.1.28',
    'huaweicloudsdkbss==3.1.28',
    'huaweicloudsdkbssintl==3.1.28',
    'huaweicloudsdkcae==3.1.28',
    'huaweicloudsdkcampusgo==3.1.28',
    'huaweicloudsdkcbh==3.1.28',
    'huaweicloudsdkcbr==3.1.28',
    'huaweicloudsdkcbs==3.1.28',
    'huaweicloudsdkcc==3.1.28',
    'huaweicloudsdkcce==3.1.28',
    'huaweicloudsdkccm==3.1.28',
    'huaweicloudsdkcdm==3.1.28',
    'huaweicloudsdkcdn==3.1.28',
    'huaweicloudsdkces==3.1.28',
    'huaweicloudsdkcfw==3.1.28',
    'huaweicloudsdkcgs==3.1.28',
    'huaweicloudsdkclassroom==3.1.28',
    'huaweicloudsdkclouddeploy==3.1.28',
    'huaweicloudsdkcloudide==3.1.28',
    'huaweicloudsdkcloudpipeline==3.1.28',
    'huaweicloudsdkcloudrtc==3.1.28',
    'huaweicloudsdkcloudtable==3.1.28',
    'huaweicloudsdkcloudtest==3.1.28',
    'huaweicloudsdkcodeartsartifact==3.1.28',
    'huaweicloudsdkcodeartsbuild==3.1.28',
    'huaweicloudsdkcodecheck==3.1.28',
    'huaweicloudsdkcodecraft==3.1.28',
    'huaweicloudsdkcodehub==3.1.28',
    'huaweicloudsdkcph==3.1.28',
    'huaweicloudsdkcpts==3.1.28',
    'huaweicloudsdkcse==3.1.28',
    'huaweicloudsdkcsms==3.1.28',
    'huaweicloudsdkcss==3.1.28',
    'huaweicloudsdkcts==3.1.28',
    'huaweicloudsdkdas==3.1.28',
    'huaweicloudsdkdbss==3.1.28',
    'huaweicloudsdkdc==3.1.28',
    'huaweicloudsdkdcs==3.1.28',
    'huaweicloudsdkddm==3.1.28',
    'huaweicloudsdkdds==3.1.28',
    'huaweicloudsdkdeh==3.1.28',
    'huaweicloudsdkdevsecurity==3.1.28',
    'huaweicloudsdkdevstar==3.1.28',
    'huaweicloudsdkdgc==3.1.28',
    'huaweicloudsdkdlf==3.1.28',
    'huaweicloudsdkdli==3.1.28',
    'huaweicloudsdkdms==3.1.28',
    'huaweicloudsdkdns==3.1.28',
    'huaweicloudsdkdris==3.1.28',
    'huaweicloudsdkdrs==3.1.28',
    'huaweicloudsdkdsc==3.1.28',
    'huaweicloudsdkdwr==3.1.28',
    'huaweicloudsdkdws==3.1.28',
    'huaweicloudsdkecs==3.1.28',
    'huaweicloudsdkeg==3.1.28',
    'huaweicloudsdkeihealth==3.1.28',
    'huaweicloudsdkeip==3.1.28',
    'huaweicloudsdkelb==3.1.28',
    'huaweicloudsdkeps==3.1.28',
    'huaweicloudsdker==3.1.28',
    'huaweicloudsdkevs==3.1.28',
    'huaweicloudsdkfrs==3.1.28',
    'huaweicloudsdkfunctiongraph==3.1.28',
    'huaweicloudsdkga==3.1.28',
    'huaweicloudsdkgaussdb==3.1.28',
    'huaweicloudsdkgaussdbfornosql==3.1.28',
    'huaweicloudsdkgaussdbforopengauss==3.1.28',
    'huaweicloudsdkges==3.1.28',
    'huaweicloudsdkgsl==3.1.28',
    'huaweicloudsdkhilens==3.1.28',
    'huaweicloudsdkhss==3.1.28',
    'huaweicloudsdkiam==3.1.28',
    'huaweicloudsdkiec==3.1.28',
    'huaweicloudsdkief==3.1.28',
    'huaweicloudsdkies==3.1.28',
    'huaweicloudsdkimage==3.1.28',
    'huaweicloudsdkimagesearch==3.1.28',
    'huaweicloudsdkims==3.1.28',
    'huaweicloudsdkiotanalytics==3.1.28',
    'huaweicloudsdkiotda==3.1.28',
    'huaweicloudsdkiotedge==3.1.28',
    'huaweicloudsdkivs==3.1.28',
    'huaweicloudsdkkafka==3.1.28',
    'huaweicloudsdkkms==3.1.28',
    'huaweicloudsdkkps==3.1.28',
    'huaweicloudsdklakeformation==3.1.28',
    'huaweicloudsdklive==3.1.28',
    'huaweicloudsdklts==3.1.28',
    'huaweicloudsdkmapds==3.1.28',
    'huaweicloudsdkmas==3.1.28',
    'huaweicloudsdkmeeting==3.1.28',
    'huaweicloudsdkmoderation==3.1.28',
    'huaweicloudsdkmpc==3.1.28',
    'huaweicloudsdkmrs==3.1.28',
    'huaweicloudsdknat==3.1.28',
    'huaweicloudsdknlp==3.1.28',
    'huaweicloudsdkocr==3.1.28',
    'huaweicloudsdkoms==3.1.28',
    'huaweicloudsdkosm==3.1.28',
    'huaweicloudsdkprojectman==3.1.28',
    'huaweicloudsdkrabbitmq==3.1.28',
    'huaweicloudsdkrds==3.1.28',
    'huaweicloudsdkres==3.1.28',
    'huaweicloudsdkrms==3.1.28',
    'huaweicloudsdkrocketmq==3.1.28',
    'huaweicloudsdkroma==3.1.28',
    'huaweicloudsdksa==3.1.28',
    'huaweicloudsdkscm==3.1.28',
    'huaweicloudsdksdrs==3.1.28',
    'huaweicloudsdksecmaster==3.1.28',
    'huaweicloudsdkservicestage==3.1.28',
    'huaweicloudsdksfsturbo==3.1.28',
    'huaweicloudsdksis==3.1.28',
    'huaweicloudsdksmn==3.1.28',
    'huaweicloudsdksms==3.1.28',
    'huaweicloudsdkswr==3.1.28',
    'huaweicloudsdktms==3.1.28',
    'huaweicloudsdkugo==3.1.28',
    'huaweicloudsdkvas==3.1.28',
    'huaweicloudsdkvcm==3.1.28',
    'huaweicloudsdkvod==3.1.28',
    'huaweicloudsdkvpc==3.1.28',
    'huaweicloudsdkvpcep==3.1.28',
    'huaweicloudsdkvss==3.1.28',
    'huaweicloudsdkwaf==3.1.28',
    'huaweicloudsdkworkspace==3.1.28',
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
