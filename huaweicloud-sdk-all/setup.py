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
VERSION = "3.1.39"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.39',
    'huaweicloudsdkantiddos==3.1.39',
    'huaweicloudsdkaom==3.1.39',
    'huaweicloudsdkaos==3.1.39',
    'huaweicloudsdkapig==3.1.39',
    'huaweicloudsdkapm==3.1.39',
    'huaweicloudsdkas==3.1.39',
    'huaweicloudsdkbcs==3.1.39',
    'huaweicloudsdkbms==3.1.39',
    'huaweicloudsdkbss==3.1.39',
    'huaweicloudsdkbssintl==3.1.39',
    'huaweicloudsdkcae==3.1.39',
    'huaweicloudsdkcampusgo==3.1.39',
    'huaweicloudsdkcbh==3.1.39',
    'huaweicloudsdkcbr==3.1.39',
    'huaweicloudsdkcbs==3.1.39',
    'huaweicloudsdkcc==3.1.39',
    'huaweicloudsdkcce==3.1.39',
    'huaweicloudsdkccm==3.1.39',
    'huaweicloudsdkcdm==3.1.39',
    'huaweicloudsdkcdn==3.1.39',
    'huaweicloudsdkces==3.1.39',
    'huaweicloudsdkcfw==3.1.39',
    'huaweicloudsdkcgs==3.1.39',
    'huaweicloudsdkclassroom==3.1.39',
    'huaweicloudsdkclouddeploy==3.1.39',
    'huaweicloudsdkcloudide==3.1.39',
    'huaweicloudsdkcloudpipeline==3.1.39',
    'huaweicloudsdkcloudrtc==3.1.39',
    'huaweicloudsdkcloudtable==3.1.39',
    'huaweicloudsdkcloudtest==3.1.39',
    'huaweicloudsdkcodeartsartifact==3.1.39',
    'huaweicloudsdkcodeartsbuild==3.1.39',
    'huaweicloudsdkcodecheck==3.1.39',
    'huaweicloudsdkcodecraft==3.1.39',
    'huaweicloudsdkcodehub==3.1.39',
    'huaweicloudsdkcph==3.1.39',
    'huaweicloudsdkcpts==3.1.39',
    'huaweicloudsdkcse==3.1.39',
    'huaweicloudsdkcsms==3.1.39',
    'huaweicloudsdkcss==3.1.39',
    'huaweicloudsdkcts==3.1.39',
    'huaweicloudsdkdas==3.1.39',
    'huaweicloudsdkdbss==3.1.39',
    'huaweicloudsdkdc==3.1.39',
    'huaweicloudsdkdcs==3.1.39',
    'huaweicloudsdkddm==3.1.39',
    'huaweicloudsdkdds==3.1.39',
    'huaweicloudsdkdeh==3.1.39',
    'huaweicloudsdkdevsecurity==3.1.39',
    'huaweicloudsdkdevstar==3.1.39',
    'huaweicloudsdkdgc==3.1.39',
    'huaweicloudsdkdlf==3.1.39',
    'huaweicloudsdkdli==3.1.39',
    'huaweicloudsdkdms==3.1.39',
    'huaweicloudsdkdns==3.1.39',
    'huaweicloudsdkdris==3.1.39',
    'huaweicloudsdkdrs==3.1.39',
    'huaweicloudsdkdsc==3.1.39',
    'huaweicloudsdkdwr==3.1.39',
    'huaweicloudsdkdws==3.1.39',
    'huaweicloudsdkecs==3.1.39',
    'huaweicloudsdkeg==3.1.39',
    'huaweicloudsdkeihealth==3.1.39',
    'huaweicloudsdkeip==3.1.39',
    'huaweicloudsdkelb==3.1.39',
    'huaweicloudsdkeps==3.1.39',
    'huaweicloudsdker==3.1.39',
    'huaweicloudsdkevs==3.1.39',
    'huaweicloudsdkfrs==3.1.39',
    'huaweicloudsdkfunctiongraph==3.1.39',
    'huaweicloudsdkga==3.1.39',
    'huaweicloudsdkgaussdb==3.1.39',
    'huaweicloudsdkgaussdbfornosql==3.1.39',
    'huaweicloudsdkgaussdbforopengauss==3.1.39',
    'huaweicloudsdkges==3.1.39',
    'huaweicloudsdkgsl==3.1.39',
    'huaweicloudsdkhilens==3.1.39',
    'huaweicloudsdkhss==3.1.39',
    'huaweicloudsdkiam==3.1.39',
    'huaweicloudsdkiec==3.1.39',
    'huaweicloudsdkief==3.1.39',
    'huaweicloudsdkies==3.1.39',
    'huaweicloudsdkimage==3.1.39',
    'huaweicloudsdkimagesearch==3.1.39',
    'huaweicloudsdkims==3.1.39',
    'huaweicloudsdkiotanalytics==3.1.39',
    'huaweicloudsdkiotda==3.1.39',
    'huaweicloudsdkiotedge==3.1.39',
    'huaweicloudsdkivs==3.1.39',
    'huaweicloudsdkkafka==3.1.39',
    'huaweicloudsdkkms==3.1.39',
    'huaweicloudsdkkps==3.1.39',
    'huaweicloudsdklakeformation==3.1.39',
    'huaweicloudsdklive==3.1.39',
    'huaweicloudsdklts==3.1.39',
    'huaweicloudsdkmapds==3.1.39',
    'huaweicloudsdkmas==3.1.39',
    'huaweicloudsdkmeeting==3.1.39',
    'huaweicloudsdkmetastudio==3.1.39',
    'huaweicloudsdkmoderation==3.1.39',
    'huaweicloudsdkmpc==3.1.39',
    'huaweicloudsdkmrs==3.1.39',
    'huaweicloudsdkmsgsms==3.1.39',
    'huaweicloudsdknat==3.1.39',
    'huaweicloudsdknlp==3.1.39',
    'huaweicloudsdkocr==3.1.39',
    'huaweicloudsdkoms==3.1.39',
    'huaweicloudsdkorganizations==3.1.39',
    'huaweicloudsdkosm==3.1.39',
    'huaweicloudsdkprojectman==3.1.39',
    'huaweicloudsdkrabbitmq==3.1.39',
    'huaweicloudsdkram==3.1.39',
    'huaweicloudsdkrds==3.1.39',
    'huaweicloudsdkres==3.1.39',
    'huaweicloudsdkrms==3.1.39',
    'huaweicloudsdkrocketmq==3.1.39',
    'huaweicloudsdkroma==3.1.39',
    'huaweicloudsdksa==3.1.39',
    'huaweicloudsdkscm==3.1.39',
    'huaweicloudsdksdrs==3.1.39',
    'huaweicloudsdksecmaster==3.1.39',
    'huaweicloudsdkservicestage==3.1.39',
    'huaweicloudsdksfsturbo==3.1.39',
    'huaweicloudsdksis==3.1.39',
    'huaweicloudsdksmn==3.1.39',
    'huaweicloudsdksms==3.1.39',
    'huaweicloudsdkswr==3.1.39',
    'huaweicloudsdktms==3.1.39',
    'huaweicloudsdkugo==3.1.39',
    'huaweicloudsdkvas==3.1.39',
    'huaweicloudsdkvcm==3.1.39',
    'huaweicloudsdkvod==3.1.39',
    'huaweicloudsdkvpc==3.1.39',
    'huaweicloudsdkvpcep==3.1.39',
    'huaweicloudsdkvss==3.1.39',
    'huaweicloudsdkwaf==3.1.39',
    'huaweicloudsdkworkspace==3.1.39',
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
