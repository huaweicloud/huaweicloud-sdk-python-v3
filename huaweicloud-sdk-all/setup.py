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
VERSION = "3.1.37"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.37',
    'huaweicloudsdkantiddos==3.1.37',
    'huaweicloudsdkaom==3.1.37',
    'huaweicloudsdkaos==3.1.37',
    'huaweicloudsdkapig==3.1.37',
    'huaweicloudsdkapm==3.1.37',
    'huaweicloudsdkas==3.1.37',
    'huaweicloudsdkbcs==3.1.37',
    'huaweicloudsdkbms==3.1.37',
    'huaweicloudsdkbss==3.1.37',
    'huaweicloudsdkbssintl==3.1.37',
    'huaweicloudsdkcae==3.1.37',
    'huaweicloudsdkcampusgo==3.1.37',
    'huaweicloudsdkcbh==3.1.37',
    'huaweicloudsdkcbr==3.1.37',
    'huaweicloudsdkcbs==3.1.37',
    'huaweicloudsdkcc==3.1.37',
    'huaweicloudsdkcce==3.1.37',
    'huaweicloudsdkccm==3.1.37',
    'huaweicloudsdkcdm==3.1.37',
    'huaweicloudsdkcdn==3.1.37',
    'huaweicloudsdkces==3.1.37',
    'huaweicloudsdkcfw==3.1.37',
    'huaweicloudsdkcgs==3.1.37',
    'huaweicloudsdkclassroom==3.1.37',
    'huaweicloudsdkclouddeploy==3.1.37',
    'huaweicloudsdkcloudide==3.1.37',
    'huaweicloudsdkcloudpipeline==3.1.37',
    'huaweicloudsdkcloudrtc==3.1.37',
    'huaweicloudsdkcloudtable==3.1.37',
    'huaweicloudsdkcloudtest==3.1.37',
    'huaweicloudsdkcodeartsartifact==3.1.37',
    'huaweicloudsdkcodeartsbuild==3.1.37',
    'huaweicloudsdkcodecheck==3.1.37',
    'huaweicloudsdkcodecraft==3.1.37',
    'huaweicloudsdkcodehub==3.1.37',
    'huaweicloudsdkcph==3.1.37',
    'huaweicloudsdkcpts==3.1.37',
    'huaweicloudsdkcse==3.1.37',
    'huaweicloudsdkcsms==3.1.37',
    'huaweicloudsdkcss==3.1.37',
    'huaweicloudsdkcts==3.1.37',
    'huaweicloudsdkdas==3.1.37',
    'huaweicloudsdkdbss==3.1.37',
    'huaweicloudsdkdc==3.1.37',
    'huaweicloudsdkdcs==3.1.37',
    'huaweicloudsdkddm==3.1.37',
    'huaweicloudsdkdds==3.1.37',
    'huaweicloudsdkdeh==3.1.37',
    'huaweicloudsdkdevsecurity==3.1.37',
    'huaweicloudsdkdevstar==3.1.37',
    'huaweicloudsdkdgc==3.1.37',
    'huaweicloudsdkdlf==3.1.37',
    'huaweicloudsdkdli==3.1.37',
    'huaweicloudsdkdms==3.1.37',
    'huaweicloudsdkdns==3.1.37',
    'huaweicloudsdkdris==3.1.37',
    'huaweicloudsdkdrs==3.1.37',
    'huaweicloudsdkdsc==3.1.37',
    'huaweicloudsdkdwr==3.1.37',
    'huaweicloudsdkdws==3.1.37',
    'huaweicloudsdkecs==3.1.37',
    'huaweicloudsdkeg==3.1.37',
    'huaweicloudsdkeihealth==3.1.37',
    'huaweicloudsdkeip==3.1.37',
    'huaweicloudsdkelb==3.1.37',
    'huaweicloudsdkeps==3.1.37',
    'huaweicloudsdker==3.1.37',
    'huaweicloudsdkevs==3.1.37',
    'huaweicloudsdkfrs==3.1.37',
    'huaweicloudsdkfunctiongraph==3.1.37',
    'huaweicloudsdkga==3.1.37',
    'huaweicloudsdkgaussdb==3.1.37',
    'huaweicloudsdkgaussdbfornosql==3.1.37',
    'huaweicloudsdkgaussdbforopengauss==3.1.37',
    'huaweicloudsdkges==3.1.37',
    'huaweicloudsdkgsl==3.1.37',
    'huaweicloudsdkhilens==3.1.37',
    'huaweicloudsdkhss==3.1.37',
    'huaweicloudsdkiam==3.1.37',
    'huaweicloudsdkiec==3.1.37',
    'huaweicloudsdkief==3.1.37',
    'huaweicloudsdkies==3.1.37',
    'huaweicloudsdkimage==3.1.37',
    'huaweicloudsdkimagesearch==3.1.37',
    'huaweicloudsdkims==3.1.37',
    'huaweicloudsdkiotanalytics==3.1.37',
    'huaweicloudsdkiotda==3.1.37',
    'huaweicloudsdkiotedge==3.1.37',
    'huaweicloudsdkivs==3.1.37',
    'huaweicloudsdkkafka==3.1.37',
    'huaweicloudsdkkms==3.1.37',
    'huaweicloudsdkkps==3.1.37',
    'huaweicloudsdklakeformation==3.1.37',
    'huaweicloudsdklive==3.1.37',
    'huaweicloudsdklts==3.1.37',
    'huaweicloudsdkmapds==3.1.37',
    'huaweicloudsdkmas==3.1.37',
    'huaweicloudsdkmeeting==3.1.37',
    'huaweicloudsdkmetastudio==3.1.37',
    'huaweicloudsdkmoderation==3.1.37',
    'huaweicloudsdkmpc==3.1.37',
    'huaweicloudsdkmrs==3.1.37',
    'huaweicloudsdknat==3.1.37',
    'huaweicloudsdknlp==3.1.37',
    'huaweicloudsdkocr==3.1.37',
    'huaweicloudsdkoms==3.1.37',
    'huaweicloudsdkorganizations==3.1.37',
    'huaweicloudsdkosm==3.1.37',
    'huaweicloudsdkprojectman==3.1.37',
    'huaweicloudsdkrabbitmq==3.1.37',
    'huaweicloudsdkram==3.1.37',
    'huaweicloudsdkrds==3.1.37',
    'huaweicloudsdkres==3.1.37',
    'huaweicloudsdkrms==3.1.37',
    'huaweicloudsdkrocketmq==3.1.37',
    'huaweicloudsdkroma==3.1.37',
    'huaweicloudsdksa==3.1.37',
    'huaweicloudsdkscm==3.1.37',
    'huaweicloudsdksdrs==3.1.37',
    'huaweicloudsdksecmaster==3.1.37',
    'huaweicloudsdkservicestage==3.1.37',
    'huaweicloudsdksfsturbo==3.1.37',
    'huaweicloudsdksis==3.1.37',
    'huaweicloudsdksmn==3.1.37',
    'huaweicloudsdksms==3.1.37',
    'huaweicloudsdkswr==3.1.37',
    'huaweicloudsdktms==3.1.37',
    'huaweicloudsdkugo==3.1.37',
    'huaweicloudsdkvas==3.1.37',
    'huaweicloudsdkvcm==3.1.37',
    'huaweicloudsdkvod==3.1.37',
    'huaweicloudsdkvpc==3.1.37',
    'huaweicloudsdkvpcep==3.1.37',
    'huaweicloudsdkvss==3.1.37',
    'huaweicloudsdkwaf==3.1.37',
    'huaweicloudsdkworkspace==3.1.37',
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
