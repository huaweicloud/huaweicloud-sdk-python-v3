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
VERSION = "3.1.27"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.27',
    'huaweicloudsdkantiddos==3.1.27',
    'huaweicloudsdkaom==3.1.27',
    'huaweicloudsdkaos==3.1.27',
    'huaweicloudsdkapig==3.1.27',
    'huaweicloudsdkapm==3.1.27',
    'huaweicloudsdkas==3.1.27',
    'huaweicloudsdkbcs==3.1.27',
    'huaweicloudsdkbms==3.1.27',
    'huaweicloudsdkbss==3.1.27',
    'huaweicloudsdkbssintl==3.1.27',
    'huaweicloudsdkcae==3.1.27',
    'huaweicloudsdkcampusgo==3.1.27',
    'huaweicloudsdkcbh==3.1.27',
    'huaweicloudsdkcbr==3.1.27',
    'huaweicloudsdkcbs==3.1.27',
    'huaweicloudsdkcc==3.1.27',
    'huaweicloudsdkcce==3.1.27',
    'huaweicloudsdkccm==3.1.27',
    'huaweicloudsdkcdm==3.1.27',
    'huaweicloudsdkcdn==3.1.27',
    'huaweicloudsdkces==3.1.27',
    'huaweicloudsdkcfw==3.1.27',
    'huaweicloudsdkcgs==3.1.27',
    'huaweicloudsdkclassroom==3.1.27',
    'huaweicloudsdkclouddeploy==3.1.27',
    'huaweicloudsdkcloudide==3.1.27',
    'huaweicloudsdkcloudpipeline==3.1.27',
    'huaweicloudsdkcloudrtc==3.1.27',
    'huaweicloudsdkcloudtable==3.1.27',
    'huaweicloudsdkcloudtest==3.1.27',
    'huaweicloudsdkcodeartsartifact==3.1.27',
    'huaweicloudsdkcodeartsbuild==3.1.27',
    'huaweicloudsdkcodecheck==3.1.27',
    'huaweicloudsdkcodecraft==3.1.27',
    'huaweicloudsdkcodehub==3.1.27',
    'huaweicloudsdkcph==3.1.27',
    'huaweicloudsdkcpts==3.1.27',
    'huaweicloudsdkcse==3.1.27',
    'huaweicloudsdkcsms==3.1.27',
    'huaweicloudsdkcss==3.1.27',
    'huaweicloudsdkcts==3.1.27',
    'huaweicloudsdkdas==3.1.27',
    'huaweicloudsdkdbss==3.1.27',
    'huaweicloudsdkdc==3.1.27',
    'huaweicloudsdkdcs==3.1.27',
    'huaweicloudsdkddm==3.1.27',
    'huaweicloudsdkdds==3.1.27',
    'huaweicloudsdkdeh==3.1.27',
    'huaweicloudsdkdevsecurity==3.1.27',
    'huaweicloudsdkdevstar==3.1.27',
    'huaweicloudsdkdgc==3.1.27',
    'huaweicloudsdkdlf==3.1.27',
    'huaweicloudsdkdli==3.1.27',
    'huaweicloudsdkdms==3.1.27',
    'huaweicloudsdkdns==3.1.27',
    'huaweicloudsdkdris==3.1.27',
    'huaweicloudsdkdrs==3.1.27',
    'huaweicloudsdkdsc==3.1.27',
    'huaweicloudsdkdwr==3.1.27',
    'huaweicloudsdkdws==3.1.27',
    'huaweicloudsdkecs==3.1.27',
    'huaweicloudsdkeg==3.1.27',
    'huaweicloudsdkeihealth==3.1.27',
    'huaweicloudsdkeip==3.1.27',
    'huaweicloudsdkelb==3.1.27',
    'huaweicloudsdkeps==3.1.27',
    'huaweicloudsdker==3.1.27',
    'huaweicloudsdkevs==3.1.27',
    'huaweicloudsdkfrs==3.1.27',
    'huaweicloudsdkfunctiongraph==3.1.27',
    'huaweicloudsdkga==3.1.27',
    'huaweicloudsdkgaussdb==3.1.27',
    'huaweicloudsdkgaussdbfornosql==3.1.27',
    'huaweicloudsdkgaussdbforopengauss==3.1.27',
    'huaweicloudsdkges==3.1.27',
    'huaweicloudsdkgsl==3.1.27',
    'huaweicloudsdkhilens==3.1.27',
    'huaweicloudsdkhss==3.1.27',
    'huaweicloudsdkiam==3.1.27',
    'huaweicloudsdkiec==3.1.27',
    'huaweicloudsdkief==3.1.27',
    'huaweicloudsdkies==3.1.27',
    'huaweicloudsdkimage==3.1.27',
    'huaweicloudsdkimagesearch==3.1.27',
    'huaweicloudsdkims==3.1.27',
    'huaweicloudsdkiotanalytics==3.1.27',
    'huaweicloudsdkiotda==3.1.27',
    'huaweicloudsdkiotedge==3.1.27',
    'huaweicloudsdkivs==3.1.27',
    'huaweicloudsdkkafka==3.1.27',
    'huaweicloudsdkkms==3.1.27',
    'huaweicloudsdkkps==3.1.27',
    'huaweicloudsdklakeformation==3.1.27',
    'huaweicloudsdklive==3.1.27',
    'huaweicloudsdklts==3.1.27',
    'huaweicloudsdkmapds==3.1.27',
    'huaweicloudsdkmas==3.1.27',
    'huaweicloudsdkmeeting==3.1.27',
    'huaweicloudsdkmoderation==3.1.27',
    'huaweicloudsdkmpc==3.1.27',
    'huaweicloudsdkmrs==3.1.27',
    'huaweicloudsdknat==3.1.27',
    'huaweicloudsdknlp==3.1.27',
    'huaweicloudsdkocr==3.1.27',
    'huaweicloudsdkoms==3.1.27',
    'huaweicloudsdkosm==3.1.27',
    'huaweicloudsdkprojectman==3.1.27',
    'huaweicloudsdkrabbitmq==3.1.27',
    'huaweicloudsdkrds==3.1.27',
    'huaweicloudsdkres==3.1.27',
    'huaweicloudsdkrms==3.1.27',
    'huaweicloudsdkrocketmq==3.1.27',
    'huaweicloudsdkroma==3.1.27',
    'huaweicloudsdksa==3.1.27',
    'huaweicloudsdkscm==3.1.27',
    'huaweicloudsdksdrs==3.1.27',
    'huaweicloudsdksecmaster==3.1.27',
    'huaweicloudsdkservicestage==3.1.27',
    'huaweicloudsdksfsturbo==3.1.27',
    'huaweicloudsdksis==3.1.27',
    'huaweicloudsdksmn==3.1.27',
    'huaweicloudsdksms==3.1.27',
    'huaweicloudsdkswr==3.1.27',
    'huaweicloudsdktms==3.1.27',
    'huaweicloudsdkugo==3.1.27',
    'huaweicloudsdkvas==3.1.27',
    'huaweicloudsdkvcm==3.1.27',
    'huaweicloudsdkvod==3.1.27',
    'huaweicloudsdkvpc==3.1.27',
    'huaweicloudsdkvpcep==3.1.27',
    'huaweicloudsdkvss==3.1.27',
    'huaweicloudsdkwaf==3.1.27',
    'huaweicloudsdkworkspace==3.1.27',
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
