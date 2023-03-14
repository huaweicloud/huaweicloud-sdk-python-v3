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
VERSION = "3.1.31"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.31',
    'huaweicloudsdkantiddos==3.1.31',
    'huaweicloudsdkaom==3.1.31',
    'huaweicloudsdkaos==3.1.31',
    'huaweicloudsdkapig==3.1.31',
    'huaweicloudsdkapm==3.1.31',
    'huaweicloudsdkas==3.1.31',
    'huaweicloudsdkbcs==3.1.31',
    'huaweicloudsdkbms==3.1.31',
    'huaweicloudsdkbss==3.1.31',
    'huaweicloudsdkbssintl==3.1.31',
    'huaweicloudsdkcae==3.1.31',
    'huaweicloudsdkcampusgo==3.1.31',
    'huaweicloudsdkcbh==3.1.31',
    'huaweicloudsdkcbr==3.1.31',
    'huaweicloudsdkcbs==3.1.31',
    'huaweicloudsdkcc==3.1.31',
    'huaweicloudsdkcce==3.1.31',
    'huaweicloudsdkccm==3.1.31',
    'huaweicloudsdkcdm==3.1.31',
    'huaweicloudsdkcdn==3.1.31',
    'huaweicloudsdkces==3.1.31',
    'huaweicloudsdkcfw==3.1.31',
    'huaweicloudsdkcgs==3.1.31',
    'huaweicloudsdkclassroom==3.1.31',
    'huaweicloudsdkclouddeploy==3.1.31',
    'huaweicloudsdkcloudide==3.1.31',
    'huaweicloudsdkcloudpipeline==3.1.31',
    'huaweicloudsdkcloudrtc==3.1.31',
    'huaweicloudsdkcloudtable==3.1.31',
    'huaweicloudsdkcloudtest==3.1.31',
    'huaweicloudsdkcodeartsartifact==3.1.31',
    'huaweicloudsdkcodeartsbuild==3.1.31',
    'huaweicloudsdkcodecheck==3.1.31',
    'huaweicloudsdkcodecraft==3.1.31',
    'huaweicloudsdkcodehub==3.1.31',
    'huaweicloudsdkcph==3.1.31',
    'huaweicloudsdkcpts==3.1.31',
    'huaweicloudsdkcse==3.1.31',
    'huaweicloudsdkcsms==3.1.31',
    'huaweicloudsdkcss==3.1.31',
    'huaweicloudsdkcts==3.1.31',
    'huaweicloudsdkdas==3.1.31',
    'huaweicloudsdkdbss==3.1.31',
    'huaweicloudsdkdc==3.1.31',
    'huaweicloudsdkdcs==3.1.31',
    'huaweicloudsdkddm==3.1.31',
    'huaweicloudsdkdds==3.1.31',
    'huaweicloudsdkdeh==3.1.31',
    'huaweicloudsdkdevsecurity==3.1.31',
    'huaweicloudsdkdevstar==3.1.31',
    'huaweicloudsdkdgc==3.1.31',
    'huaweicloudsdkdlf==3.1.31',
    'huaweicloudsdkdli==3.1.31',
    'huaweicloudsdkdms==3.1.31',
    'huaweicloudsdkdns==3.1.31',
    'huaweicloudsdkdris==3.1.31',
    'huaweicloudsdkdrs==3.1.31',
    'huaweicloudsdkdsc==3.1.31',
    'huaweicloudsdkdwr==3.1.31',
    'huaweicloudsdkdws==3.1.31',
    'huaweicloudsdkecs==3.1.31',
    'huaweicloudsdkeg==3.1.31',
    'huaweicloudsdkeihealth==3.1.31',
    'huaweicloudsdkeip==3.1.31',
    'huaweicloudsdkelb==3.1.31',
    'huaweicloudsdkeps==3.1.31',
    'huaweicloudsdker==3.1.31',
    'huaweicloudsdkevs==3.1.31',
    'huaweicloudsdkfrs==3.1.31',
    'huaweicloudsdkfunctiongraph==3.1.31',
    'huaweicloudsdkga==3.1.31',
    'huaweicloudsdkgaussdb==3.1.31',
    'huaweicloudsdkgaussdbfornosql==3.1.31',
    'huaweicloudsdkgaussdbforopengauss==3.1.31',
    'huaweicloudsdkges==3.1.31',
    'huaweicloudsdkgsl==3.1.31',
    'huaweicloudsdkhilens==3.1.31',
    'huaweicloudsdkhss==3.1.31',
    'huaweicloudsdkiam==3.1.31',
    'huaweicloudsdkiec==3.1.31',
    'huaweicloudsdkief==3.1.31',
    'huaweicloudsdkies==3.1.31',
    'huaweicloudsdkimage==3.1.31',
    'huaweicloudsdkimagesearch==3.1.31',
    'huaweicloudsdkims==3.1.31',
    'huaweicloudsdkiotanalytics==3.1.31',
    'huaweicloudsdkiotda==3.1.31',
    'huaweicloudsdkiotedge==3.1.31',
    'huaweicloudsdkivs==3.1.31',
    'huaweicloudsdkkafka==3.1.31',
    'huaweicloudsdkkms==3.1.31',
    'huaweicloudsdkkps==3.1.31',
    'huaweicloudsdklakeformation==3.1.31',
    'huaweicloudsdklive==3.1.31',
    'huaweicloudsdklts==3.1.31',
    'huaweicloudsdkmapds==3.1.31',
    'huaweicloudsdkmas==3.1.31',
    'huaweicloudsdkmeeting==3.1.31',
    'huaweicloudsdkmoderation==3.1.31',
    'huaweicloudsdkmpc==3.1.31',
    'huaweicloudsdkmrs==3.1.31',
    'huaweicloudsdknat==3.1.31',
    'huaweicloudsdknlp==3.1.31',
    'huaweicloudsdkocr==3.1.31',
    'huaweicloudsdkoms==3.1.31',
    'huaweicloudsdkosm==3.1.31',
    'huaweicloudsdkprojectman==3.1.31',
    'huaweicloudsdkrabbitmq==3.1.31',
    'huaweicloudsdkrds==3.1.31',
    'huaweicloudsdkres==3.1.31',
    'huaweicloudsdkrms==3.1.31',
    'huaweicloudsdkrocketmq==3.1.31',
    'huaweicloudsdkroma==3.1.31',
    'huaweicloudsdksa==3.1.31',
    'huaweicloudsdkscm==3.1.31',
    'huaweicloudsdksdrs==3.1.31',
    'huaweicloudsdksecmaster==3.1.31',
    'huaweicloudsdkservicestage==3.1.31',
    'huaweicloudsdksfsturbo==3.1.31',
    'huaweicloudsdksis==3.1.31',
    'huaweicloudsdksmn==3.1.31',
    'huaweicloudsdksms==3.1.31',
    'huaweicloudsdkswr==3.1.31',
    'huaweicloudsdktms==3.1.31',
    'huaweicloudsdkugo==3.1.31',
    'huaweicloudsdkvas==3.1.31',
    'huaweicloudsdkvcm==3.1.31',
    'huaweicloudsdkvod==3.1.31',
    'huaweicloudsdkvpc==3.1.31',
    'huaweicloudsdkvpcep==3.1.31',
    'huaweicloudsdkvss==3.1.31',
    'huaweicloudsdkwaf==3.1.31',
    'huaweicloudsdkworkspace==3.1.31',
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
