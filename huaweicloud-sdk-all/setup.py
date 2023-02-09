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
VERSION = "3.1.25"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.25',
    'huaweicloudsdkantiddos==3.1.25',
    'huaweicloudsdkaom==3.1.25',
    'huaweicloudsdkaos==3.1.25',
    'huaweicloudsdkapig==3.1.25',
    'huaweicloudsdkapm==3.1.25',
    'huaweicloudsdkas==3.1.25',
    'huaweicloudsdkbcs==3.1.25',
    'huaweicloudsdkbms==3.1.25',
    'huaweicloudsdkbss==3.1.25',
    'huaweicloudsdkbssintl==3.1.25',
    'huaweicloudsdkcae==3.1.25',
    'huaweicloudsdkcampusgo==3.1.25',
    'huaweicloudsdkcbh==3.1.25',
    'huaweicloudsdkcbr==3.1.25',
    'huaweicloudsdkcbs==3.1.25',
    'huaweicloudsdkcc==3.1.25',
    'huaweicloudsdkcce==3.1.25',
    'huaweicloudsdkccm==3.1.25',
    'huaweicloudsdkcdm==3.1.25',
    'huaweicloudsdkcdn==3.1.25',
    'huaweicloudsdkces==3.1.25',
    'huaweicloudsdkcfw==3.1.25',
    'huaweicloudsdkcgs==3.1.25',
    'huaweicloudsdkclassroom==3.1.25',
    'huaweicloudsdkclouddeploy==3.1.25',
    'huaweicloudsdkcloudide==3.1.25',
    'huaweicloudsdkcloudpipeline==3.1.25',
    'huaweicloudsdkcloudrtc==3.1.25',
    'huaweicloudsdkcloudtable==3.1.25',
    'huaweicloudsdkcloudtest==3.1.25',
    'huaweicloudsdkcodeartsartifact==3.1.25',
    'huaweicloudsdkcodeartsbuild==3.1.25',
    'huaweicloudsdkcodecheck==3.1.25',
    'huaweicloudsdkcodecraft==3.1.25',
    'huaweicloudsdkcodehub==3.1.25',
    'huaweicloudsdkcph==3.1.25',
    'huaweicloudsdkcpts==3.1.25',
    'huaweicloudsdkcse==3.1.25',
    'huaweicloudsdkcsms==3.1.25',
    'huaweicloudsdkcss==3.1.25',
    'huaweicloudsdkcts==3.1.25',
    'huaweicloudsdkdas==3.1.25',
    'huaweicloudsdkdbss==3.1.25',
    'huaweicloudsdkdc==3.1.25',
    'huaweicloudsdkdcs==3.1.25',
    'huaweicloudsdkddm==3.1.25',
    'huaweicloudsdkdds==3.1.25',
    'huaweicloudsdkdeh==3.1.25',
    'huaweicloudsdkdevsecurity==3.1.25',
    'huaweicloudsdkdevstar==3.1.25',
    'huaweicloudsdkdgc==3.1.25',
    'huaweicloudsdkdlf==3.1.25',
    'huaweicloudsdkdli==3.1.25',
    'huaweicloudsdkdms==3.1.25',
    'huaweicloudsdkdns==3.1.25',
    'huaweicloudsdkdris==3.1.25',
    'huaweicloudsdkdrs==3.1.25',
    'huaweicloudsdkdsc==3.1.25',
    'huaweicloudsdkdwr==3.1.25',
    'huaweicloudsdkdws==3.1.25',
    'huaweicloudsdkecs==3.1.25',
    'huaweicloudsdkeg==3.1.25',
    'huaweicloudsdkeihealth==3.1.25',
    'huaweicloudsdkeip==3.1.25',
    'huaweicloudsdkelb==3.1.25',
    'huaweicloudsdkeps==3.1.25',
    'huaweicloudsdker==3.1.25',
    'huaweicloudsdkevs==3.1.25',
    'huaweicloudsdkfrs==3.1.25',
    'huaweicloudsdkfunctiongraph==3.1.25',
    'huaweicloudsdkga==3.1.25',
    'huaweicloudsdkgaussdb==3.1.25',
    'huaweicloudsdkgaussdbfornosql==3.1.25',
    'huaweicloudsdkgaussdbforopengauss==3.1.25',
    'huaweicloudsdkges==3.1.25',
    'huaweicloudsdkgsl==3.1.25',
    'huaweicloudsdkhilens==3.1.25',
    'huaweicloudsdkhss==3.1.25',
    'huaweicloudsdkiam==3.1.25',
    'huaweicloudsdkiec==3.1.25',
    'huaweicloudsdkief==3.1.25',
    'huaweicloudsdkies==3.1.25',
    'huaweicloudsdkimage==3.1.25',
    'huaweicloudsdkimagesearch==3.1.25',
    'huaweicloudsdkims==3.1.25',
    'huaweicloudsdkiotanalytics==3.1.25',
    'huaweicloudsdkiotda==3.1.25',
    'huaweicloudsdkiotedge==3.1.25',
    'huaweicloudsdkivs==3.1.25',
    'huaweicloudsdkkafka==3.1.25',
    'huaweicloudsdkkms==3.1.25',
    'huaweicloudsdkkps==3.1.25',
    'huaweicloudsdklakeformation==3.1.25',
    'huaweicloudsdklive==3.1.25',
    'huaweicloudsdklts==3.1.25',
    'huaweicloudsdkmapds==3.1.25',
    'huaweicloudsdkmas==3.1.25',
    'huaweicloudsdkmeeting==3.1.25',
    'huaweicloudsdkmoderation==3.1.25',
    'huaweicloudsdkmpc==3.1.25',
    'huaweicloudsdkmrs==3.1.25',
    'huaweicloudsdknat==3.1.25',
    'huaweicloudsdknlp==3.1.25',
    'huaweicloudsdkocr==3.1.25',
    'huaweicloudsdkoms==3.1.25',
    'huaweicloudsdkosm==3.1.25',
    'huaweicloudsdkprojectman==3.1.25',
    'huaweicloudsdkrabbitmq==3.1.25',
    'huaweicloudsdkrds==3.1.25',
    'huaweicloudsdkres==3.1.25',
    'huaweicloudsdkrms==3.1.25',
    'huaweicloudsdkrocketmq==3.1.25',
    'huaweicloudsdkroma==3.1.25',
    'huaweicloudsdksa==3.1.25',
    'huaweicloudsdkscm==3.1.25',
    'huaweicloudsdksdrs==3.1.25',
    'huaweicloudsdksecmaster==3.1.25',
    'huaweicloudsdkservicestage==3.1.25',
    'huaweicloudsdksfsturbo==3.1.25',
    'huaweicloudsdksis==3.1.25',
    'huaweicloudsdksmn==3.1.25',
    'huaweicloudsdksms==3.1.25',
    'huaweicloudsdkswr==3.1.25',
    'huaweicloudsdktms==3.1.25',
    'huaweicloudsdkugo==3.1.25',
    'huaweicloudsdkvas==3.1.25',
    'huaweicloudsdkvcm==3.1.25',
    'huaweicloudsdkvod==3.1.25',
    'huaweicloudsdkvpc==3.1.25',
    'huaweicloudsdkvpcep==3.1.25',
    'huaweicloudsdkvss==3.1.25',
    'huaweicloudsdkwaf==3.1.25',
    'huaweicloudsdkworkspace==3.1.25',
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
