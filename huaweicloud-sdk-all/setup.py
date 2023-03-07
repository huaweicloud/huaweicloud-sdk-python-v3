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
VERSION = "3.1.29"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.29',
    'huaweicloudsdkantiddos==3.1.29',
    'huaweicloudsdkaom==3.1.29',
    'huaweicloudsdkaos==3.1.29',
    'huaweicloudsdkapig==3.1.29',
    'huaweicloudsdkapm==3.1.29',
    'huaweicloudsdkas==3.1.29',
    'huaweicloudsdkbcs==3.1.29',
    'huaweicloudsdkbms==3.1.29',
    'huaweicloudsdkbss==3.1.29',
    'huaweicloudsdkbssintl==3.1.29',
    'huaweicloudsdkcae==3.1.29',
    'huaweicloudsdkcampusgo==3.1.29',
    'huaweicloudsdkcbh==3.1.29',
    'huaweicloudsdkcbr==3.1.29',
    'huaweicloudsdkcbs==3.1.29',
    'huaweicloudsdkcc==3.1.29',
    'huaweicloudsdkcce==3.1.29',
    'huaweicloudsdkccm==3.1.29',
    'huaweicloudsdkcdm==3.1.29',
    'huaweicloudsdkcdn==3.1.29',
    'huaweicloudsdkces==3.1.29',
    'huaweicloudsdkcfw==3.1.29',
    'huaweicloudsdkcgs==3.1.29',
    'huaweicloudsdkclassroom==3.1.29',
    'huaweicloudsdkclouddeploy==3.1.29',
    'huaweicloudsdkcloudide==3.1.29',
    'huaweicloudsdkcloudpipeline==3.1.29',
    'huaweicloudsdkcloudrtc==3.1.29',
    'huaweicloudsdkcloudtable==3.1.29',
    'huaweicloudsdkcloudtest==3.1.29',
    'huaweicloudsdkcodeartsartifact==3.1.29',
    'huaweicloudsdkcodeartsbuild==3.1.29',
    'huaweicloudsdkcodecheck==3.1.29',
    'huaweicloudsdkcodecraft==3.1.29',
    'huaweicloudsdkcodehub==3.1.29',
    'huaweicloudsdkcph==3.1.29',
    'huaweicloudsdkcpts==3.1.29',
    'huaweicloudsdkcse==3.1.29',
    'huaweicloudsdkcsms==3.1.29',
    'huaweicloudsdkcss==3.1.29',
    'huaweicloudsdkcts==3.1.29',
    'huaweicloudsdkdas==3.1.29',
    'huaweicloudsdkdbss==3.1.29',
    'huaweicloudsdkdc==3.1.29',
    'huaweicloudsdkdcs==3.1.29',
    'huaweicloudsdkddm==3.1.29',
    'huaweicloudsdkdds==3.1.29',
    'huaweicloudsdkdeh==3.1.29',
    'huaweicloudsdkdevsecurity==3.1.29',
    'huaweicloudsdkdevstar==3.1.29',
    'huaweicloudsdkdgc==3.1.29',
    'huaweicloudsdkdlf==3.1.29',
    'huaweicloudsdkdli==3.1.29',
    'huaweicloudsdkdms==3.1.29',
    'huaweicloudsdkdns==3.1.29',
    'huaweicloudsdkdris==3.1.29',
    'huaweicloudsdkdrs==3.1.29',
    'huaweicloudsdkdsc==3.1.29',
    'huaweicloudsdkdwr==3.1.29',
    'huaweicloudsdkdws==3.1.29',
    'huaweicloudsdkecs==3.1.29',
    'huaweicloudsdkeg==3.1.29',
    'huaweicloudsdkeihealth==3.1.29',
    'huaweicloudsdkeip==3.1.29',
    'huaweicloudsdkelb==3.1.29',
    'huaweicloudsdkeps==3.1.29',
    'huaweicloudsdker==3.1.29',
    'huaweicloudsdkevs==3.1.29',
    'huaweicloudsdkfrs==3.1.29',
    'huaweicloudsdkfunctiongraph==3.1.29',
    'huaweicloudsdkga==3.1.29',
    'huaweicloudsdkgaussdb==3.1.29',
    'huaweicloudsdkgaussdbfornosql==3.1.29',
    'huaweicloudsdkgaussdbforopengauss==3.1.29',
    'huaweicloudsdkges==3.1.29',
    'huaweicloudsdkgsl==3.1.29',
    'huaweicloudsdkhilens==3.1.29',
    'huaweicloudsdkhss==3.1.29',
    'huaweicloudsdkiam==3.1.29',
    'huaweicloudsdkiec==3.1.29',
    'huaweicloudsdkief==3.1.29',
    'huaweicloudsdkies==3.1.29',
    'huaweicloudsdkimage==3.1.29',
    'huaweicloudsdkimagesearch==3.1.29',
    'huaweicloudsdkims==3.1.29',
    'huaweicloudsdkiotanalytics==3.1.29',
    'huaweicloudsdkiotda==3.1.29',
    'huaweicloudsdkiotedge==3.1.29',
    'huaweicloudsdkivs==3.1.29',
    'huaweicloudsdkkafka==3.1.29',
    'huaweicloudsdkkms==3.1.29',
    'huaweicloudsdkkps==3.1.29',
    'huaweicloudsdklakeformation==3.1.29',
    'huaweicloudsdklive==3.1.29',
    'huaweicloudsdklts==3.1.29',
    'huaweicloudsdkmapds==3.1.29',
    'huaweicloudsdkmas==3.1.29',
    'huaweicloudsdkmeeting==3.1.29',
    'huaweicloudsdkmoderation==3.1.29',
    'huaweicloudsdkmpc==3.1.29',
    'huaweicloudsdkmrs==3.1.29',
    'huaweicloudsdknat==3.1.29',
    'huaweicloudsdknlp==3.1.29',
    'huaweicloudsdkocr==3.1.29',
    'huaweicloudsdkoms==3.1.29',
    'huaweicloudsdkosm==3.1.29',
    'huaweicloudsdkprojectman==3.1.29',
    'huaweicloudsdkrabbitmq==3.1.29',
    'huaweicloudsdkrds==3.1.29',
    'huaweicloudsdkres==3.1.29',
    'huaweicloudsdkrms==3.1.29',
    'huaweicloudsdkrocketmq==3.1.29',
    'huaweicloudsdkroma==3.1.29',
    'huaweicloudsdksa==3.1.29',
    'huaweicloudsdkscm==3.1.29',
    'huaweicloudsdksdrs==3.1.29',
    'huaweicloudsdksecmaster==3.1.29',
    'huaweicloudsdkservicestage==3.1.29',
    'huaweicloudsdksfsturbo==3.1.29',
    'huaweicloudsdksis==3.1.29',
    'huaweicloudsdksmn==3.1.29',
    'huaweicloudsdksms==3.1.29',
    'huaweicloudsdkswr==3.1.29',
    'huaweicloudsdktms==3.1.29',
    'huaweicloudsdkugo==3.1.29',
    'huaweicloudsdkvas==3.1.29',
    'huaweicloudsdkvcm==3.1.29',
    'huaweicloudsdkvod==3.1.29',
    'huaweicloudsdkvpc==3.1.29',
    'huaweicloudsdkvpcep==3.1.29',
    'huaweicloudsdkvss==3.1.29',
    'huaweicloudsdkwaf==3.1.29',
    'huaweicloudsdkworkspace==3.1.29',
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
