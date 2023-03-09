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
VERSION = "3.1.30"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.30',
    'huaweicloudsdkantiddos==3.1.30',
    'huaweicloudsdkaom==3.1.30',
    'huaweicloudsdkaos==3.1.30',
    'huaweicloudsdkapig==3.1.30',
    'huaweicloudsdkapm==3.1.30',
    'huaweicloudsdkas==3.1.30',
    'huaweicloudsdkbcs==3.1.30',
    'huaweicloudsdkbms==3.1.30',
    'huaweicloudsdkbss==3.1.30',
    'huaweicloudsdkbssintl==3.1.30',
    'huaweicloudsdkcae==3.1.30',
    'huaweicloudsdkcampusgo==3.1.30',
    'huaweicloudsdkcbh==3.1.30',
    'huaweicloudsdkcbr==3.1.30',
    'huaweicloudsdkcbs==3.1.30',
    'huaweicloudsdkcc==3.1.30',
    'huaweicloudsdkcce==3.1.30',
    'huaweicloudsdkccm==3.1.30',
    'huaweicloudsdkcdm==3.1.30',
    'huaweicloudsdkcdn==3.1.30',
    'huaweicloudsdkces==3.1.30',
    'huaweicloudsdkcfw==3.1.30',
    'huaweicloudsdkcgs==3.1.30',
    'huaweicloudsdkclassroom==3.1.30',
    'huaweicloudsdkclouddeploy==3.1.30',
    'huaweicloudsdkcloudide==3.1.30',
    'huaweicloudsdkcloudpipeline==3.1.30',
    'huaweicloudsdkcloudrtc==3.1.30',
    'huaweicloudsdkcloudtable==3.1.30',
    'huaweicloudsdkcloudtest==3.1.30',
    'huaweicloudsdkcodeartsartifact==3.1.30',
    'huaweicloudsdkcodeartsbuild==3.1.30',
    'huaweicloudsdkcodecheck==3.1.30',
    'huaweicloudsdkcodecraft==3.1.30',
    'huaweicloudsdkcodehub==3.1.30',
    'huaweicloudsdkcph==3.1.30',
    'huaweicloudsdkcpts==3.1.30',
    'huaweicloudsdkcse==3.1.30',
    'huaweicloudsdkcsms==3.1.30',
    'huaweicloudsdkcss==3.1.30',
    'huaweicloudsdkcts==3.1.30',
    'huaweicloudsdkdas==3.1.30',
    'huaweicloudsdkdbss==3.1.30',
    'huaweicloudsdkdc==3.1.30',
    'huaweicloudsdkdcs==3.1.30',
    'huaweicloudsdkddm==3.1.30',
    'huaweicloudsdkdds==3.1.30',
    'huaweicloudsdkdeh==3.1.30',
    'huaweicloudsdkdevsecurity==3.1.30',
    'huaweicloudsdkdevstar==3.1.30',
    'huaweicloudsdkdgc==3.1.30',
    'huaweicloudsdkdlf==3.1.30',
    'huaweicloudsdkdli==3.1.30',
    'huaweicloudsdkdms==3.1.30',
    'huaweicloudsdkdns==3.1.30',
    'huaweicloudsdkdris==3.1.30',
    'huaweicloudsdkdrs==3.1.30',
    'huaweicloudsdkdsc==3.1.30',
    'huaweicloudsdkdwr==3.1.30',
    'huaweicloudsdkdws==3.1.30',
    'huaweicloudsdkecs==3.1.30',
    'huaweicloudsdkeg==3.1.30',
    'huaweicloudsdkeihealth==3.1.30',
    'huaweicloudsdkeip==3.1.30',
    'huaweicloudsdkelb==3.1.30',
    'huaweicloudsdkeps==3.1.30',
    'huaweicloudsdker==3.1.30',
    'huaweicloudsdkevs==3.1.30',
    'huaweicloudsdkfrs==3.1.30',
    'huaweicloudsdkfunctiongraph==3.1.30',
    'huaweicloudsdkga==3.1.30',
    'huaweicloudsdkgaussdb==3.1.30',
    'huaweicloudsdkgaussdbfornosql==3.1.30',
    'huaweicloudsdkgaussdbforopengauss==3.1.30',
    'huaweicloudsdkges==3.1.30',
    'huaweicloudsdkgsl==3.1.30',
    'huaweicloudsdkhilens==3.1.30',
    'huaweicloudsdkhss==3.1.30',
    'huaweicloudsdkiam==3.1.30',
    'huaweicloudsdkiec==3.1.30',
    'huaweicloudsdkief==3.1.30',
    'huaweicloudsdkies==3.1.30',
    'huaweicloudsdkimage==3.1.30',
    'huaweicloudsdkimagesearch==3.1.30',
    'huaweicloudsdkims==3.1.30',
    'huaweicloudsdkiotanalytics==3.1.30',
    'huaweicloudsdkiotda==3.1.30',
    'huaweicloudsdkiotedge==3.1.30',
    'huaweicloudsdkivs==3.1.30',
    'huaweicloudsdkkafka==3.1.30',
    'huaweicloudsdkkms==3.1.30',
    'huaweicloudsdkkps==3.1.30',
    'huaweicloudsdklakeformation==3.1.30',
    'huaweicloudsdklive==3.1.30',
    'huaweicloudsdklts==3.1.30',
    'huaweicloudsdkmapds==3.1.30',
    'huaweicloudsdkmas==3.1.30',
    'huaweicloudsdkmeeting==3.1.30',
    'huaweicloudsdkmoderation==3.1.30',
    'huaweicloudsdkmpc==3.1.30',
    'huaweicloudsdkmrs==3.1.30',
    'huaweicloudsdknat==3.1.30',
    'huaweicloudsdknlp==3.1.30',
    'huaweicloudsdkocr==3.1.30',
    'huaweicloudsdkoms==3.1.30',
    'huaweicloudsdkosm==3.1.30',
    'huaweicloudsdkprojectman==3.1.30',
    'huaweicloudsdkrabbitmq==3.1.30',
    'huaweicloudsdkrds==3.1.30',
    'huaweicloudsdkres==3.1.30',
    'huaweicloudsdkrms==3.1.30',
    'huaweicloudsdkrocketmq==3.1.30',
    'huaweicloudsdkroma==3.1.30',
    'huaweicloudsdksa==3.1.30',
    'huaweicloudsdkscm==3.1.30',
    'huaweicloudsdksdrs==3.1.30',
    'huaweicloudsdksecmaster==3.1.30',
    'huaweicloudsdkservicestage==3.1.30',
    'huaweicloudsdksfsturbo==3.1.30',
    'huaweicloudsdksis==3.1.30',
    'huaweicloudsdksmn==3.1.30',
    'huaweicloudsdksms==3.1.30',
    'huaweicloudsdkswr==3.1.30',
    'huaweicloudsdktms==3.1.30',
    'huaweicloudsdkugo==3.1.30',
    'huaweicloudsdkvas==3.1.30',
    'huaweicloudsdkvcm==3.1.30',
    'huaweicloudsdkvod==3.1.30',
    'huaweicloudsdkvpc==3.1.30',
    'huaweicloudsdkvpcep==3.1.30',
    'huaweicloudsdkvss==3.1.30',
    'huaweicloudsdkwaf==3.1.30',
    'huaweicloudsdkworkspace==3.1.30',
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
