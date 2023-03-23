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
VERSION = "3.1.33"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.33',
    'huaweicloudsdkantiddos==3.1.33',
    'huaweicloudsdkaom==3.1.33',
    'huaweicloudsdkaos==3.1.33',
    'huaweicloudsdkapig==3.1.33',
    'huaweicloudsdkapm==3.1.33',
    'huaweicloudsdkas==3.1.33',
    'huaweicloudsdkbcs==3.1.33',
    'huaweicloudsdkbms==3.1.33',
    'huaweicloudsdkbss==3.1.33',
    'huaweicloudsdkbssintl==3.1.33',
    'huaweicloudsdkcae==3.1.33',
    'huaweicloudsdkcampusgo==3.1.33',
    'huaweicloudsdkcbh==3.1.33',
    'huaweicloudsdkcbr==3.1.33',
    'huaweicloudsdkcbs==3.1.33',
    'huaweicloudsdkcc==3.1.33',
    'huaweicloudsdkcce==3.1.33',
    'huaweicloudsdkccm==3.1.33',
    'huaweicloudsdkcdm==3.1.33',
    'huaweicloudsdkcdn==3.1.33',
    'huaweicloudsdkces==3.1.33',
    'huaweicloudsdkcfw==3.1.33',
    'huaweicloudsdkcgs==3.1.33',
    'huaweicloudsdkclassroom==3.1.33',
    'huaweicloudsdkclouddeploy==3.1.33',
    'huaweicloudsdkcloudide==3.1.33',
    'huaweicloudsdkcloudpipeline==3.1.33',
    'huaweicloudsdkcloudrtc==3.1.33',
    'huaweicloudsdkcloudtable==3.1.33',
    'huaweicloudsdkcloudtest==3.1.33',
    'huaweicloudsdkcodeartsartifact==3.1.33',
    'huaweicloudsdkcodeartsbuild==3.1.33',
    'huaweicloudsdkcodecheck==3.1.33',
    'huaweicloudsdkcodecraft==3.1.33',
    'huaweicloudsdkcodehub==3.1.33',
    'huaweicloudsdkcph==3.1.33',
    'huaweicloudsdkcpts==3.1.33',
    'huaweicloudsdkcse==3.1.33',
    'huaweicloudsdkcsms==3.1.33',
    'huaweicloudsdkcss==3.1.33',
    'huaweicloudsdkcts==3.1.33',
    'huaweicloudsdkdas==3.1.33',
    'huaweicloudsdkdbss==3.1.33',
    'huaweicloudsdkdc==3.1.33',
    'huaweicloudsdkdcs==3.1.33',
    'huaweicloudsdkddm==3.1.33',
    'huaweicloudsdkdds==3.1.33',
    'huaweicloudsdkdeh==3.1.33',
    'huaweicloudsdkdevsecurity==3.1.33',
    'huaweicloudsdkdevstar==3.1.33',
    'huaweicloudsdkdgc==3.1.33',
    'huaweicloudsdkdlf==3.1.33',
    'huaweicloudsdkdli==3.1.33',
    'huaweicloudsdkdms==3.1.33',
    'huaweicloudsdkdns==3.1.33',
    'huaweicloudsdkdris==3.1.33',
    'huaweicloudsdkdrs==3.1.33',
    'huaweicloudsdkdsc==3.1.33',
    'huaweicloudsdkdwr==3.1.33',
    'huaweicloudsdkdws==3.1.33',
    'huaweicloudsdkecs==3.1.33',
    'huaweicloudsdkeg==3.1.33',
    'huaweicloudsdkeihealth==3.1.33',
    'huaweicloudsdkeip==3.1.33',
    'huaweicloudsdkelb==3.1.33',
    'huaweicloudsdkeps==3.1.33',
    'huaweicloudsdker==3.1.33',
    'huaweicloudsdkevs==3.1.33',
    'huaweicloudsdkfrs==3.1.33',
    'huaweicloudsdkfunctiongraph==3.1.33',
    'huaweicloudsdkga==3.1.33',
    'huaweicloudsdkgaussdb==3.1.33',
    'huaweicloudsdkgaussdbfornosql==3.1.33',
    'huaweicloudsdkgaussdbforopengauss==3.1.33',
    'huaweicloudsdkges==3.1.33',
    'huaweicloudsdkgsl==3.1.33',
    'huaweicloudsdkhilens==3.1.33',
    'huaweicloudsdkhss==3.1.33',
    'huaweicloudsdkiam==3.1.33',
    'huaweicloudsdkiec==3.1.33',
    'huaweicloudsdkief==3.1.33',
    'huaweicloudsdkies==3.1.33',
    'huaweicloudsdkimage==3.1.33',
    'huaweicloudsdkimagesearch==3.1.33',
    'huaweicloudsdkims==3.1.33',
    'huaweicloudsdkiotanalytics==3.1.33',
    'huaweicloudsdkiotda==3.1.33',
    'huaweicloudsdkiotedge==3.1.33',
    'huaweicloudsdkivs==3.1.33',
    'huaweicloudsdkkafka==3.1.33',
    'huaweicloudsdkkms==3.1.33',
    'huaweicloudsdkkps==3.1.33',
    'huaweicloudsdklakeformation==3.1.33',
    'huaweicloudsdklive==3.1.33',
    'huaweicloudsdklts==3.1.33',
    'huaweicloudsdkmapds==3.1.33',
    'huaweicloudsdkmas==3.1.33',
    'huaweicloudsdkmeeting==3.1.33',
    'huaweicloudsdkmoderation==3.1.33',
    'huaweicloudsdkmpc==3.1.33',
    'huaweicloudsdkmrs==3.1.33',
    'huaweicloudsdknat==3.1.33',
    'huaweicloudsdknlp==3.1.33',
    'huaweicloudsdkocr==3.1.33',
    'huaweicloudsdkoms==3.1.33',
    'huaweicloudsdkorganizations==3.1.33',
    'huaweicloudsdkosm==3.1.33',
    'huaweicloudsdkprojectman==3.1.33',
    'huaweicloudsdkrabbitmq==3.1.33',
    'huaweicloudsdkram==3.1.33',
    'huaweicloudsdkrds==3.1.33',
    'huaweicloudsdkres==3.1.33',
    'huaweicloudsdkrms==3.1.33',
    'huaweicloudsdkrocketmq==3.1.33',
    'huaweicloudsdkroma==3.1.33',
    'huaweicloudsdksa==3.1.33',
    'huaweicloudsdkscm==3.1.33',
    'huaweicloudsdksdrs==3.1.33',
    'huaweicloudsdksecmaster==3.1.33',
    'huaweicloudsdkservicestage==3.1.33',
    'huaweicloudsdksfsturbo==3.1.33',
    'huaweicloudsdksis==3.1.33',
    'huaweicloudsdksmn==3.1.33',
    'huaweicloudsdksms==3.1.33',
    'huaweicloudsdkswr==3.1.33',
    'huaweicloudsdktms==3.1.33',
    'huaweicloudsdkugo==3.1.33',
    'huaweicloudsdkvas==3.1.33',
    'huaweicloudsdkvcm==3.1.33',
    'huaweicloudsdkvod==3.1.33',
    'huaweicloudsdkvpc==3.1.33',
    'huaweicloudsdkvpcep==3.1.33',
    'huaweicloudsdkvss==3.1.33',
    'huaweicloudsdkwaf==3.1.33',
    'huaweicloudsdkworkspace==3.1.33',
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
