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
VERSION = "3.1.36"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.36',
    'huaweicloudsdkantiddos==3.1.36',
    'huaweicloudsdkaom==3.1.36',
    'huaweicloudsdkaos==3.1.36',
    'huaweicloudsdkapig==3.1.36',
    'huaweicloudsdkapm==3.1.36',
    'huaweicloudsdkas==3.1.36',
    'huaweicloudsdkbcs==3.1.36',
    'huaweicloudsdkbms==3.1.36',
    'huaweicloudsdkbss==3.1.36',
    'huaweicloudsdkbssintl==3.1.36',
    'huaweicloudsdkcae==3.1.36',
    'huaweicloudsdkcampusgo==3.1.36',
    'huaweicloudsdkcbh==3.1.36',
    'huaweicloudsdkcbr==3.1.36',
    'huaweicloudsdkcbs==3.1.36',
    'huaweicloudsdkcc==3.1.36',
    'huaweicloudsdkcce==3.1.36',
    'huaweicloudsdkccm==3.1.36',
    'huaweicloudsdkcdm==3.1.36',
    'huaweicloudsdkcdn==3.1.36',
    'huaweicloudsdkces==3.1.36',
    'huaweicloudsdkcfw==3.1.36',
    'huaweicloudsdkcgs==3.1.36',
    'huaweicloudsdkclassroom==3.1.36',
    'huaweicloudsdkclouddeploy==3.1.36',
    'huaweicloudsdkcloudide==3.1.36',
    'huaweicloudsdkcloudpipeline==3.1.36',
    'huaweicloudsdkcloudrtc==3.1.36',
    'huaweicloudsdkcloudtable==3.1.36',
    'huaweicloudsdkcloudtest==3.1.36',
    'huaweicloudsdkcodeartsartifact==3.1.36',
    'huaweicloudsdkcodeartsbuild==3.1.36',
    'huaweicloudsdkcodecheck==3.1.36',
    'huaweicloudsdkcodecraft==3.1.36',
    'huaweicloudsdkcodehub==3.1.36',
    'huaweicloudsdkcph==3.1.36',
    'huaweicloudsdkcpts==3.1.36',
    'huaweicloudsdkcse==3.1.36',
    'huaweicloudsdkcsms==3.1.36',
    'huaweicloudsdkcss==3.1.36',
    'huaweicloudsdkcts==3.1.36',
    'huaweicloudsdkdas==3.1.36',
    'huaweicloudsdkdbss==3.1.36',
    'huaweicloudsdkdc==3.1.36',
    'huaweicloudsdkdcs==3.1.36',
    'huaweicloudsdkddm==3.1.36',
    'huaweicloudsdkdds==3.1.36',
    'huaweicloudsdkdeh==3.1.36',
    'huaweicloudsdkdevsecurity==3.1.36',
    'huaweicloudsdkdevstar==3.1.36',
    'huaweicloudsdkdgc==3.1.36',
    'huaweicloudsdkdlf==3.1.36',
    'huaweicloudsdkdli==3.1.36',
    'huaweicloudsdkdms==3.1.36',
    'huaweicloudsdkdns==3.1.36',
    'huaweicloudsdkdris==3.1.36',
    'huaweicloudsdkdrs==3.1.36',
    'huaweicloudsdkdsc==3.1.36',
    'huaweicloudsdkdwr==3.1.36',
    'huaweicloudsdkdws==3.1.36',
    'huaweicloudsdkecs==3.1.36',
    'huaweicloudsdkeg==3.1.36',
    'huaweicloudsdkeihealth==3.1.36',
    'huaweicloudsdkeip==3.1.36',
    'huaweicloudsdkelb==3.1.36',
    'huaweicloudsdkeps==3.1.36',
    'huaweicloudsdker==3.1.36',
    'huaweicloudsdkevs==3.1.36',
    'huaweicloudsdkfrs==3.1.36',
    'huaweicloudsdkfunctiongraph==3.1.36',
    'huaweicloudsdkga==3.1.36',
    'huaweicloudsdkgaussdb==3.1.36',
    'huaweicloudsdkgaussdbfornosql==3.1.36',
    'huaweicloudsdkgaussdbforopengauss==3.1.36',
    'huaweicloudsdkges==3.1.36',
    'huaweicloudsdkgsl==3.1.36',
    'huaweicloudsdkhilens==3.1.36',
    'huaweicloudsdkhss==3.1.36',
    'huaweicloudsdkiam==3.1.36',
    'huaweicloudsdkiec==3.1.36',
    'huaweicloudsdkief==3.1.36',
    'huaweicloudsdkies==3.1.36',
    'huaweicloudsdkimage==3.1.36',
    'huaweicloudsdkimagesearch==3.1.36',
    'huaweicloudsdkims==3.1.36',
    'huaweicloudsdkiotanalytics==3.1.36',
    'huaweicloudsdkiotda==3.1.36',
    'huaweicloudsdkiotedge==3.1.36',
    'huaweicloudsdkivs==3.1.36',
    'huaweicloudsdkkafka==3.1.36',
    'huaweicloudsdkkms==3.1.36',
    'huaweicloudsdkkps==3.1.36',
    'huaweicloudsdklakeformation==3.1.36',
    'huaweicloudsdklive==3.1.36',
    'huaweicloudsdklts==3.1.36',
    'huaweicloudsdkmapds==3.1.36',
    'huaweicloudsdkmas==3.1.36',
    'huaweicloudsdkmeeting==3.1.36',
    'huaweicloudsdkmetastudio==3.1.36',
    'huaweicloudsdkmoderation==3.1.36',
    'huaweicloudsdkmpc==3.1.36',
    'huaweicloudsdkmrs==3.1.36',
    'huaweicloudsdknat==3.1.36',
    'huaweicloudsdknlp==3.1.36',
    'huaweicloudsdkocr==3.1.36',
    'huaweicloudsdkoms==3.1.36',
    'huaweicloudsdkorganizations==3.1.36',
    'huaweicloudsdkosm==3.1.36',
    'huaweicloudsdkprojectman==3.1.36',
    'huaweicloudsdkrabbitmq==3.1.36',
    'huaweicloudsdkram==3.1.36',
    'huaweicloudsdkrds==3.1.36',
    'huaweicloudsdkres==3.1.36',
    'huaweicloudsdkrms==3.1.36',
    'huaweicloudsdkrocketmq==3.1.36',
    'huaweicloudsdkroma==3.1.36',
    'huaweicloudsdksa==3.1.36',
    'huaweicloudsdkscm==3.1.36',
    'huaweicloudsdksdrs==3.1.36',
    'huaweicloudsdksecmaster==3.1.36',
    'huaweicloudsdkservicestage==3.1.36',
    'huaweicloudsdksfsturbo==3.1.36',
    'huaweicloudsdksis==3.1.36',
    'huaweicloudsdksmn==3.1.36',
    'huaweicloudsdksms==3.1.36',
    'huaweicloudsdkswr==3.1.36',
    'huaweicloudsdktms==3.1.36',
    'huaweicloudsdkugo==3.1.36',
    'huaweicloudsdkvas==3.1.36',
    'huaweicloudsdkvcm==3.1.36',
    'huaweicloudsdkvod==3.1.36',
    'huaweicloudsdkvpc==3.1.36',
    'huaweicloudsdkvpcep==3.1.36',
    'huaweicloudsdkvss==3.1.36',
    'huaweicloudsdkwaf==3.1.36',
    'huaweicloudsdkworkspace==3.1.36',
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
