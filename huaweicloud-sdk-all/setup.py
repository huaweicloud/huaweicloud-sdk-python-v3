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
VERSION = "3.1.26"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.26',
    'huaweicloudsdkantiddos==3.1.26',
    'huaweicloudsdkaom==3.1.26',
    'huaweicloudsdkaos==3.1.26',
    'huaweicloudsdkapig==3.1.26',
    'huaweicloudsdkapm==3.1.26',
    'huaweicloudsdkas==3.1.26',
    'huaweicloudsdkbcs==3.1.26',
    'huaweicloudsdkbms==3.1.26',
    'huaweicloudsdkbss==3.1.26',
    'huaweicloudsdkbssintl==3.1.26',
    'huaweicloudsdkcae==3.1.26',
    'huaweicloudsdkcampusgo==3.1.26',
    'huaweicloudsdkcbh==3.1.26',
    'huaweicloudsdkcbr==3.1.26',
    'huaweicloudsdkcbs==3.1.26',
    'huaweicloudsdkcc==3.1.26',
    'huaweicloudsdkcce==3.1.26',
    'huaweicloudsdkccm==3.1.26',
    'huaweicloudsdkcdm==3.1.26',
    'huaweicloudsdkcdn==3.1.26',
    'huaweicloudsdkces==3.1.26',
    'huaweicloudsdkcfw==3.1.26',
    'huaweicloudsdkcgs==3.1.26',
    'huaweicloudsdkclassroom==3.1.26',
    'huaweicloudsdkclouddeploy==3.1.26',
    'huaweicloudsdkcloudide==3.1.26',
    'huaweicloudsdkcloudpipeline==3.1.26',
    'huaweicloudsdkcloudrtc==3.1.26',
    'huaweicloudsdkcloudtable==3.1.26',
    'huaweicloudsdkcloudtest==3.1.26',
    'huaweicloudsdkcodeartsartifact==3.1.26',
    'huaweicloudsdkcodeartsbuild==3.1.26',
    'huaweicloudsdkcodecheck==3.1.26',
    'huaweicloudsdkcodecraft==3.1.26',
    'huaweicloudsdkcodehub==3.1.26',
    'huaweicloudsdkcph==3.1.26',
    'huaweicloudsdkcpts==3.1.26',
    'huaweicloudsdkcse==3.1.26',
    'huaweicloudsdkcsms==3.1.26',
    'huaweicloudsdkcss==3.1.26',
    'huaweicloudsdkcts==3.1.26',
    'huaweicloudsdkdas==3.1.26',
    'huaweicloudsdkdbss==3.1.26',
    'huaweicloudsdkdc==3.1.26',
    'huaweicloudsdkdcs==3.1.26',
    'huaweicloudsdkddm==3.1.26',
    'huaweicloudsdkdds==3.1.26',
    'huaweicloudsdkdeh==3.1.26',
    'huaweicloudsdkdevsecurity==3.1.26',
    'huaweicloudsdkdevstar==3.1.26',
    'huaweicloudsdkdgc==3.1.26',
    'huaweicloudsdkdlf==3.1.26',
    'huaweicloudsdkdli==3.1.26',
    'huaweicloudsdkdms==3.1.26',
    'huaweicloudsdkdns==3.1.26',
    'huaweicloudsdkdris==3.1.26',
    'huaweicloudsdkdrs==3.1.26',
    'huaweicloudsdkdsc==3.1.26',
    'huaweicloudsdkdwr==3.1.26',
    'huaweicloudsdkdws==3.1.26',
    'huaweicloudsdkecs==3.1.26',
    'huaweicloudsdkeg==3.1.26',
    'huaweicloudsdkeihealth==3.1.26',
    'huaweicloudsdkeip==3.1.26',
    'huaweicloudsdkelb==3.1.26',
    'huaweicloudsdkeps==3.1.26',
    'huaweicloudsdker==3.1.26',
    'huaweicloudsdkevs==3.1.26',
    'huaweicloudsdkfrs==3.1.26',
    'huaweicloudsdkfunctiongraph==3.1.26',
    'huaweicloudsdkga==3.1.26',
    'huaweicloudsdkgaussdb==3.1.26',
    'huaweicloudsdkgaussdbfornosql==3.1.26',
    'huaweicloudsdkgaussdbforopengauss==3.1.26',
    'huaweicloudsdkges==3.1.26',
    'huaweicloudsdkgsl==3.1.26',
    'huaweicloudsdkhilens==3.1.26',
    'huaweicloudsdkhss==3.1.26',
    'huaweicloudsdkiam==3.1.26',
    'huaweicloudsdkiec==3.1.26',
    'huaweicloudsdkief==3.1.26',
    'huaweicloudsdkies==3.1.26',
    'huaweicloudsdkimage==3.1.26',
    'huaweicloudsdkimagesearch==3.1.26',
    'huaweicloudsdkims==3.1.26',
    'huaweicloudsdkiotanalytics==3.1.26',
    'huaweicloudsdkiotda==3.1.26',
    'huaweicloudsdkiotedge==3.1.26',
    'huaweicloudsdkivs==3.1.26',
    'huaweicloudsdkkafka==3.1.26',
    'huaweicloudsdkkms==3.1.26',
    'huaweicloudsdkkps==3.1.26',
    'huaweicloudsdklakeformation==3.1.26',
    'huaweicloudsdklive==3.1.26',
    'huaweicloudsdklts==3.1.26',
    'huaweicloudsdkmapds==3.1.26',
    'huaweicloudsdkmas==3.1.26',
    'huaweicloudsdkmeeting==3.1.26',
    'huaweicloudsdkmoderation==3.1.26',
    'huaweicloudsdkmpc==3.1.26',
    'huaweicloudsdkmrs==3.1.26',
    'huaweicloudsdknat==3.1.26',
    'huaweicloudsdknlp==3.1.26',
    'huaweicloudsdkocr==3.1.26',
    'huaweicloudsdkoms==3.1.26',
    'huaweicloudsdkosm==3.1.26',
    'huaweicloudsdkprojectman==3.1.26',
    'huaweicloudsdkrabbitmq==3.1.26',
    'huaweicloudsdkrds==3.1.26',
    'huaweicloudsdkres==3.1.26',
    'huaweicloudsdkrms==3.1.26',
    'huaweicloudsdkrocketmq==3.1.26',
    'huaweicloudsdkroma==3.1.26',
    'huaweicloudsdksa==3.1.26',
    'huaweicloudsdkscm==3.1.26',
    'huaweicloudsdksdrs==3.1.26',
    'huaweicloudsdksecmaster==3.1.26',
    'huaweicloudsdkservicestage==3.1.26',
    'huaweicloudsdksfsturbo==3.1.26',
    'huaweicloudsdksis==3.1.26',
    'huaweicloudsdksmn==3.1.26',
    'huaweicloudsdksms==3.1.26',
    'huaweicloudsdkswr==3.1.26',
    'huaweicloudsdktms==3.1.26',
    'huaweicloudsdkugo==3.1.26',
    'huaweicloudsdkvas==3.1.26',
    'huaweicloudsdkvcm==3.1.26',
    'huaweicloudsdkvod==3.1.26',
    'huaweicloudsdkvpc==3.1.26',
    'huaweicloudsdkvpcep==3.1.26',
    'huaweicloudsdkvss==3.1.26',
    'huaweicloudsdkwaf==3.1.26',
    'huaweicloudsdkworkspace==3.1.26',
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
