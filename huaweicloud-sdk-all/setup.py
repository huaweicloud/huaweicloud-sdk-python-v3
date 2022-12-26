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
VERSION = "3.1.19"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.19',
    'huaweicloudsdkantiddos==3.1.19',
    'huaweicloudsdkaom==3.1.19',
    'huaweicloudsdkaos==3.1.19',
    'huaweicloudsdkapig==3.1.19',
    'huaweicloudsdkapm==3.1.19',
    'huaweicloudsdkas==3.1.19',
    'huaweicloudsdkbcs==3.1.19',
    'huaweicloudsdkbms==3.1.19',
    'huaweicloudsdkbss==3.1.19',
    'huaweicloudsdkbssintl==3.1.19',
    'huaweicloudsdkcae==3.1.19',
    'huaweicloudsdkcampusgo==3.1.19',
    'huaweicloudsdkcbh==3.1.19',
    'huaweicloudsdkcbr==3.1.19',
    'huaweicloudsdkcbs==3.1.19',
    'huaweicloudsdkcc==3.1.19',
    'huaweicloudsdkcce==3.1.19',
    'huaweicloudsdkccm==3.1.19',
    'huaweicloudsdkcdm==3.1.19',
    'huaweicloudsdkcdn==3.1.19',
    'huaweicloudsdkces==3.1.19',
    'huaweicloudsdkcfw==3.1.19',
    'huaweicloudsdkcgs==3.1.19',
    'huaweicloudsdkclassroom==3.1.19',
    'huaweicloudsdkcloudartifact==3.1.19',
    'huaweicloudsdkcloudbuild==3.1.19',
    'huaweicloudsdkclouddeploy==3.1.19',
    'huaweicloudsdkcloudide==3.1.19',
    'huaweicloudsdkcloudpipeline==3.1.19',
    'huaweicloudsdkcloudrtc==3.1.19',
    'huaweicloudsdkcloudtable==3.1.19',
    'huaweicloudsdkcloudtest==3.1.19',
    'huaweicloudsdkcodecheck==3.1.19',
    'huaweicloudsdkcodecraft==3.1.19',
    'huaweicloudsdkcodehub==3.1.19',
    'huaweicloudsdkcph==3.1.19',
    'huaweicloudsdkcpts==3.1.19',
    'huaweicloudsdkcse==3.1.19',
    'huaweicloudsdkcsms==3.1.19',
    'huaweicloudsdkcss==3.1.19',
    'huaweicloudsdkcts==3.1.19',
    'huaweicloudsdkdas==3.1.19',
    'huaweicloudsdkdbss==3.1.19',
    'huaweicloudsdkdc==3.1.19',
    'huaweicloudsdkdcs==3.1.19',
    'huaweicloudsdkddm==3.1.19',
    'huaweicloudsdkdds==3.1.19',
    'huaweicloudsdkdeh==3.1.19',
    'huaweicloudsdkdevsecurity==3.1.19',
    'huaweicloudsdkdevstar==3.1.19',
    'huaweicloudsdkdgc==3.1.19',
    'huaweicloudsdkdlf==3.1.19',
    'huaweicloudsdkdli==3.1.19',
    'huaweicloudsdkdms==3.1.19',
    'huaweicloudsdkdns==3.1.19',
    'huaweicloudsdkdris==3.1.19',
    'huaweicloudsdkdrs==3.1.19',
    'huaweicloudsdkdsc==3.1.19',
    'huaweicloudsdkdwr==3.1.19',
    'huaweicloudsdkdws==3.1.19',
    'huaweicloudsdkecs==3.1.19',
    'huaweicloudsdkeg==3.1.19',
    'huaweicloudsdkeihealth==3.1.19',
    'huaweicloudsdkeip==3.1.19',
    'huaweicloudsdkelb==3.1.19',
    'huaweicloudsdkeps==3.1.19',
    'huaweicloudsdker==3.1.19',
    'huaweicloudsdkevs==3.1.19',
    'huaweicloudsdkfrs==3.1.19',
    'huaweicloudsdkfunctiongraph==3.1.19',
    'huaweicloudsdkga==3.1.19',
    'huaweicloudsdkgaussdb==3.1.19',
    'huaweicloudsdkgaussdbfornosql==3.1.19',
    'huaweicloudsdkgaussdbforopengauss==3.1.19',
    'huaweicloudsdkges==3.1.19',
    'huaweicloudsdkgsl==3.1.19',
    'huaweicloudsdkhilens==3.1.19',
    'huaweicloudsdkhss==3.1.19',
    'huaweicloudsdkiam==3.1.19',
    'huaweicloudsdkiec==3.1.19',
    'huaweicloudsdkief==3.1.19',
    'huaweicloudsdkies==3.1.19',
    'huaweicloudsdkimage==3.1.19',
    'huaweicloudsdkimagesearch==3.1.19',
    'huaweicloudsdkims==3.1.19',
    'huaweicloudsdkiotanalytics==3.1.19',
    'huaweicloudsdkiotda==3.1.19',
    'huaweicloudsdkiotedge==3.1.19',
    'huaweicloudsdkivs==3.1.19',
    'huaweicloudsdkkafka==3.1.19',
    'huaweicloudsdkkms==3.1.19',
    'huaweicloudsdkkps==3.1.19',
    'huaweicloudsdklive==3.1.19',
    'huaweicloudsdklts==3.1.19',
    'huaweicloudsdkmapds==3.1.19',
    'huaweicloudsdkmas==3.1.19',
    'huaweicloudsdkmeeting==3.1.19',
    'huaweicloudsdkmoderation==3.1.19',
    'huaweicloudsdkmpc==3.1.19',
    'huaweicloudsdkmrs==3.1.19',
    'huaweicloudsdknat==3.1.19',
    'huaweicloudsdknlp==3.1.19',
    'huaweicloudsdkocr==3.1.19',
    'huaweicloudsdkoms==3.1.19',
    'huaweicloudsdkosm==3.1.19',
    'huaweicloudsdkprojectman==3.1.19',
    'huaweicloudsdkrabbitmq==3.1.19',
    'huaweicloudsdkrds==3.1.19',
    'huaweicloudsdkres==3.1.19',
    'huaweicloudsdkrms==3.1.19',
    'huaweicloudsdkrocketmq==3.1.19',
    'huaweicloudsdkroma==3.1.19',
    'huaweicloudsdksa==3.1.19',
    'huaweicloudsdkscm==3.1.19',
    'huaweicloudsdksdrs==3.1.19',
    'huaweicloudsdkservicestage==3.1.19',
    'huaweicloudsdksfsturbo==3.1.19',
    'huaweicloudsdksis==3.1.19',
    'huaweicloudsdksmn==3.1.19',
    'huaweicloudsdksms==3.1.19',
    'huaweicloudsdkswr==3.1.19',
    'huaweicloudsdktms==3.1.19',
    'huaweicloudsdkugo==3.1.19',
    'huaweicloudsdkvas==3.1.19',
    'huaweicloudsdkvcm==3.1.19',
    'huaweicloudsdkvod==3.1.19',
    'huaweicloudsdkvpc==3.1.19',
    'huaweicloudsdkvpcep==3.1.19',
    'huaweicloudsdkvss==3.1.19',
    'huaweicloudsdkwaf==3.1.19',
    'huaweicloudsdkworkspace==3.1.19',
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
