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
VERSION = "3.1.32"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.32',
    'huaweicloudsdkantiddos==3.1.32',
    'huaweicloudsdkaom==3.1.32',
    'huaweicloudsdkaos==3.1.32',
    'huaweicloudsdkapig==3.1.32',
    'huaweicloudsdkapm==3.1.32',
    'huaweicloudsdkas==3.1.32',
    'huaweicloudsdkbcs==3.1.32',
    'huaweicloudsdkbms==3.1.32',
    'huaweicloudsdkbss==3.1.32',
    'huaweicloudsdkbssintl==3.1.32',
    'huaweicloudsdkcae==3.1.32',
    'huaweicloudsdkcampusgo==3.1.32',
    'huaweicloudsdkcbh==3.1.32',
    'huaweicloudsdkcbr==3.1.32',
    'huaweicloudsdkcbs==3.1.32',
    'huaweicloudsdkcc==3.1.32',
    'huaweicloudsdkcce==3.1.32',
    'huaweicloudsdkccm==3.1.32',
    'huaweicloudsdkcdm==3.1.32',
    'huaweicloudsdkcdn==3.1.32',
    'huaweicloudsdkces==3.1.32',
    'huaweicloudsdkcfw==3.1.32',
    'huaweicloudsdkcgs==3.1.32',
    'huaweicloudsdkclassroom==3.1.32',
    'huaweicloudsdkclouddeploy==3.1.32',
    'huaweicloudsdkcloudide==3.1.32',
    'huaweicloudsdkcloudpipeline==3.1.32',
    'huaweicloudsdkcloudrtc==3.1.32',
    'huaweicloudsdkcloudtable==3.1.32',
    'huaweicloudsdkcloudtest==3.1.32',
    'huaweicloudsdkcodeartsartifact==3.1.32',
    'huaweicloudsdkcodeartsbuild==3.1.32',
    'huaweicloudsdkcodecheck==3.1.32',
    'huaweicloudsdkcodecraft==3.1.32',
    'huaweicloudsdkcodehub==3.1.32',
    'huaweicloudsdkcph==3.1.32',
    'huaweicloudsdkcpts==3.1.32',
    'huaweicloudsdkcse==3.1.32',
    'huaweicloudsdkcsms==3.1.32',
    'huaweicloudsdkcss==3.1.32',
    'huaweicloudsdkcts==3.1.32',
    'huaweicloudsdkdas==3.1.32',
    'huaweicloudsdkdbss==3.1.32',
    'huaweicloudsdkdc==3.1.32',
    'huaweicloudsdkdcs==3.1.32',
    'huaweicloudsdkddm==3.1.32',
    'huaweicloudsdkdds==3.1.32',
    'huaweicloudsdkdeh==3.1.32',
    'huaweicloudsdkdevsecurity==3.1.32',
    'huaweicloudsdkdevstar==3.1.32',
    'huaweicloudsdkdgc==3.1.32',
    'huaweicloudsdkdlf==3.1.32',
    'huaweicloudsdkdli==3.1.32',
    'huaweicloudsdkdms==3.1.32',
    'huaweicloudsdkdns==3.1.32',
    'huaweicloudsdkdris==3.1.32',
    'huaweicloudsdkdrs==3.1.32',
    'huaweicloudsdkdsc==3.1.32',
    'huaweicloudsdkdwr==3.1.32',
    'huaweicloudsdkdws==3.1.32',
    'huaweicloudsdkecs==3.1.32',
    'huaweicloudsdkeg==3.1.32',
    'huaweicloudsdkeihealth==3.1.32',
    'huaweicloudsdkeip==3.1.32',
    'huaweicloudsdkelb==3.1.32',
    'huaweicloudsdkeps==3.1.32',
    'huaweicloudsdker==3.1.32',
    'huaweicloudsdkevs==3.1.32',
    'huaweicloudsdkfrs==3.1.32',
    'huaweicloudsdkfunctiongraph==3.1.32',
    'huaweicloudsdkga==3.1.32',
    'huaweicloudsdkgaussdb==3.1.32',
    'huaweicloudsdkgaussdbfornosql==3.1.32',
    'huaweicloudsdkgaussdbforopengauss==3.1.32',
    'huaweicloudsdkges==3.1.32',
    'huaweicloudsdkgsl==3.1.32',
    'huaweicloudsdkhilens==3.1.32',
    'huaweicloudsdkhss==3.1.32',
    'huaweicloudsdkiam==3.1.32',
    'huaweicloudsdkiec==3.1.32',
    'huaweicloudsdkief==3.1.32',
    'huaweicloudsdkies==3.1.32',
    'huaweicloudsdkimage==3.1.32',
    'huaweicloudsdkimagesearch==3.1.32',
    'huaweicloudsdkims==3.1.32',
    'huaweicloudsdkiotanalytics==3.1.32',
    'huaweicloudsdkiotda==3.1.32',
    'huaweicloudsdkiotedge==3.1.32',
    'huaweicloudsdkivs==3.1.32',
    'huaweicloudsdkkafka==3.1.32',
    'huaweicloudsdkkms==3.1.32',
    'huaweicloudsdkkps==3.1.32',
    'huaweicloudsdklakeformation==3.1.32',
    'huaweicloudsdklive==3.1.32',
    'huaweicloudsdklts==3.1.32',
    'huaweicloudsdkmapds==3.1.32',
    'huaweicloudsdkmas==3.1.32',
    'huaweicloudsdkmeeting==3.1.32',
    'huaweicloudsdkmoderation==3.1.32',
    'huaweicloudsdkmpc==3.1.32',
    'huaweicloudsdkmrs==3.1.32',
    'huaweicloudsdknat==3.1.32',
    'huaweicloudsdknlp==3.1.32',
    'huaweicloudsdkocr==3.1.32',
    'huaweicloudsdkoms==3.1.32',
    'huaweicloudsdkorganizations==3.1.32',
    'huaweicloudsdkosm==3.1.32',
    'huaweicloudsdkprojectman==3.1.32',
    'huaweicloudsdkrabbitmq==3.1.32',
    'huaweicloudsdkrds==3.1.32',
    'huaweicloudsdkres==3.1.32',
    'huaweicloudsdkrms==3.1.32',
    'huaweicloudsdkrocketmq==3.1.32',
    'huaweicloudsdkroma==3.1.32',
    'huaweicloudsdksa==3.1.32',
    'huaweicloudsdkscm==3.1.32',
    'huaweicloudsdksdrs==3.1.32',
    'huaweicloudsdksecmaster==3.1.32',
    'huaweicloudsdkservicestage==3.1.32',
    'huaweicloudsdksfsturbo==3.1.32',
    'huaweicloudsdksis==3.1.32',
    'huaweicloudsdksmn==3.1.32',
    'huaweicloudsdksms==3.1.32',
    'huaweicloudsdkswr==3.1.32',
    'huaweicloudsdktms==3.1.32',
    'huaweicloudsdkugo==3.1.32',
    'huaweicloudsdkvas==3.1.32',
    'huaweicloudsdkvcm==3.1.32',
    'huaweicloudsdkvod==3.1.32',
    'huaweicloudsdkvpc==3.1.32',
    'huaweicloudsdkvpcep==3.1.32',
    'huaweicloudsdkvss==3.1.32',
    'huaweicloudsdkwaf==3.1.32',
    'huaweicloudsdkworkspace==3.1.32',
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
