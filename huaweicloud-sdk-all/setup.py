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
VERSION = "3.1.35"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.35',
    'huaweicloudsdkantiddos==3.1.35',
    'huaweicloudsdkaom==3.1.35',
    'huaweicloudsdkaos==3.1.35',
    'huaweicloudsdkapig==3.1.35',
    'huaweicloudsdkapm==3.1.35',
    'huaweicloudsdkas==3.1.35',
    'huaweicloudsdkbcs==3.1.35',
    'huaweicloudsdkbms==3.1.35',
    'huaweicloudsdkbss==3.1.35',
    'huaweicloudsdkbssintl==3.1.35',
    'huaweicloudsdkcae==3.1.35',
    'huaweicloudsdkcampusgo==3.1.35',
    'huaweicloudsdkcbh==3.1.35',
    'huaweicloudsdkcbr==3.1.35',
    'huaweicloudsdkcbs==3.1.35',
    'huaweicloudsdkcc==3.1.35',
    'huaweicloudsdkcce==3.1.35',
    'huaweicloudsdkccm==3.1.35',
    'huaweicloudsdkcdm==3.1.35',
    'huaweicloudsdkcdn==3.1.35',
    'huaweicloudsdkces==3.1.35',
    'huaweicloudsdkcfw==3.1.35',
    'huaweicloudsdkcgs==3.1.35',
    'huaweicloudsdkclassroom==3.1.35',
    'huaweicloudsdkclouddeploy==3.1.35',
    'huaweicloudsdkcloudide==3.1.35',
    'huaweicloudsdkcloudpipeline==3.1.35',
    'huaweicloudsdkcloudrtc==3.1.35',
    'huaweicloudsdkcloudtable==3.1.35',
    'huaweicloudsdkcloudtest==3.1.35',
    'huaweicloudsdkcodeartsartifact==3.1.35',
    'huaweicloudsdkcodeartsbuild==3.1.35',
    'huaweicloudsdkcodecheck==3.1.35',
    'huaweicloudsdkcodecraft==3.1.35',
    'huaweicloudsdkcodehub==3.1.35',
    'huaweicloudsdkcph==3.1.35',
    'huaweicloudsdkcpts==3.1.35',
    'huaweicloudsdkcse==3.1.35',
    'huaweicloudsdkcsms==3.1.35',
    'huaweicloudsdkcss==3.1.35',
    'huaweicloudsdkcts==3.1.35',
    'huaweicloudsdkdas==3.1.35',
    'huaweicloudsdkdbss==3.1.35',
    'huaweicloudsdkdc==3.1.35',
    'huaweicloudsdkdcs==3.1.35',
    'huaweicloudsdkddm==3.1.35',
    'huaweicloudsdkdds==3.1.35',
    'huaweicloudsdkdeh==3.1.35',
    'huaweicloudsdkdevsecurity==3.1.35',
    'huaweicloudsdkdevstar==3.1.35',
    'huaweicloudsdkdgc==3.1.35',
    'huaweicloudsdkdlf==3.1.35',
    'huaweicloudsdkdli==3.1.35',
    'huaweicloudsdkdms==3.1.35',
    'huaweicloudsdkdns==3.1.35',
    'huaweicloudsdkdris==3.1.35',
    'huaweicloudsdkdrs==3.1.35',
    'huaweicloudsdkdsc==3.1.35',
    'huaweicloudsdkdwr==3.1.35',
    'huaweicloudsdkdws==3.1.35',
    'huaweicloudsdkecs==3.1.35',
    'huaweicloudsdkeg==3.1.35',
    'huaweicloudsdkeihealth==3.1.35',
    'huaweicloudsdkeip==3.1.35',
    'huaweicloudsdkelb==3.1.35',
    'huaweicloudsdkeps==3.1.35',
    'huaweicloudsdker==3.1.35',
    'huaweicloudsdkevs==3.1.35',
    'huaweicloudsdkfrs==3.1.35',
    'huaweicloudsdkfunctiongraph==3.1.35',
    'huaweicloudsdkga==3.1.35',
    'huaweicloudsdkgaussdb==3.1.35',
    'huaweicloudsdkgaussdbfornosql==3.1.35',
    'huaweicloudsdkgaussdbforopengauss==3.1.35',
    'huaweicloudsdkges==3.1.35',
    'huaweicloudsdkgsl==3.1.35',
    'huaweicloudsdkhilens==3.1.35',
    'huaweicloudsdkhss==3.1.35',
    'huaweicloudsdkiam==3.1.35',
    'huaweicloudsdkiec==3.1.35',
    'huaweicloudsdkief==3.1.35',
    'huaweicloudsdkies==3.1.35',
    'huaweicloudsdkimage==3.1.35',
    'huaweicloudsdkimagesearch==3.1.35',
    'huaweicloudsdkims==3.1.35',
    'huaweicloudsdkiotanalytics==3.1.35',
    'huaweicloudsdkiotda==3.1.35',
    'huaweicloudsdkiotedge==3.1.35',
    'huaweicloudsdkivs==3.1.35',
    'huaweicloudsdkkafka==3.1.35',
    'huaweicloudsdkkms==3.1.35',
    'huaweicloudsdkkps==3.1.35',
    'huaweicloudsdklakeformation==3.1.35',
    'huaweicloudsdklive==3.1.35',
    'huaweicloudsdklts==3.1.35',
    'huaweicloudsdkmapds==3.1.35',
    'huaweicloudsdkmas==3.1.35',
    'huaweicloudsdkmeeting==3.1.35',
    'huaweicloudsdkmoderation==3.1.35',
    'huaweicloudsdkmpc==3.1.35',
    'huaweicloudsdkmrs==3.1.35',
    'huaweicloudsdknat==3.1.35',
    'huaweicloudsdknlp==3.1.35',
    'huaweicloudsdkocr==3.1.35',
    'huaweicloudsdkoms==3.1.35',
    'huaweicloudsdkorganizations==3.1.35',
    'huaweicloudsdkosm==3.1.35',
    'huaweicloudsdkprojectman==3.1.35',
    'huaweicloudsdkrabbitmq==3.1.35',
    'huaweicloudsdkram==3.1.35',
    'huaweicloudsdkrds==3.1.35',
    'huaweicloudsdkres==3.1.35',
    'huaweicloudsdkrms==3.1.35',
    'huaweicloudsdkrocketmq==3.1.35',
    'huaweicloudsdkroma==3.1.35',
    'huaweicloudsdksa==3.1.35',
    'huaweicloudsdkscm==3.1.35',
    'huaweicloudsdksdrs==3.1.35',
    'huaweicloudsdksecmaster==3.1.35',
    'huaweicloudsdkservicestage==3.1.35',
    'huaweicloudsdksfsturbo==3.1.35',
    'huaweicloudsdksis==3.1.35',
    'huaweicloudsdksmn==3.1.35',
    'huaweicloudsdksms==3.1.35',
    'huaweicloudsdkswr==3.1.35',
    'huaweicloudsdktms==3.1.35',
    'huaweicloudsdkugo==3.1.35',
    'huaweicloudsdkvas==3.1.35',
    'huaweicloudsdkvcm==3.1.35',
    'huaweicloudsdkvod==3.1.35',
    'huaweicloudsdkvpc==3.1.35',
    'huaweicloudsdkvpcep==3.1.35',
    'huaweicloudsdkvss==3.1.35',
    'huaweicloudsdkwaf==3.1.35',
    'huaweicloudsdkworkspace==3.1.35',
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
