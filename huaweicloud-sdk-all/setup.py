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
VERSION = "3.1.34"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.34',
    'huaweicloudsdkantiddos==3.1.34',
    'huaweicloudsdkaom==3.1.34',
    'huaweicloudsdkaos==3.1.34',
    'huaweicloudsdkapig==3.1.34',
    'huaweicloudsdkapm==3.1.34',
    'huaweicloudsdkas==3.1.34',
    'huaweicloudsdkbcs==3.1.34',
    'huaweicloudsdkbms==3.1.34',
    'huaweicloudsdkbss==3.1.34',
    'huaweicloudsdkbssintl==3.1.34',
    'huaweicloudsdkcae==3.1.34',
    'huaweicloudsdkcampusgo==3.1.34',
    'huaweicloudsdkcbh==3.1.34',
    'huaweicloudsdkcbr==3.1.34',
    'huaweicloudsdkcbs==3.1.34',
    'huaweicloudsdkcc==3.1.34',
    'huaweicloudsdkcce==3.1.34',
    'huaweicloudsdkccm==3.1.34',
    'huaweicloudsdkcdm==3.1.34',
    'huaweicloudsdkcdn==3.1.34',
    'huaweicloudsdkces==3.1.34',
    'huaweicloudsdkcfw==3.1.34',
    'huaweicloudsdkcgs==3.1.34',
    'huaweicloudsdkclassroom==3.1.34',
    'huaweicloudsdkclouddeploy==3.1.34',
    'huaweicloudsdkcloudide==3.1.34',
    'huaweicloudsdkcloudpipeline==3.1.34',
    'huaweicloudsdkcloudrtc==3.1.34',
    'huaweicloudsdkcloudtable==3.1.34',
    'huaweicloudsdkcloudtest==3.1.34',
    'huaweicloudsdkcodeartsartifact==3.1.34',
    'huaweicloudsdkcodeartsbuild==3.1.34',
    'huaweicloudsdkcodecheck==3.1.34',
    'huaweicloudsdkcodecraft==3.1.34',
    'huaweicloudsdkcodehub==3.1.34',
    'huaweicloudsdkcph==3.1.34',
    'huaweicloudsdkcpts==3.1.34',
    'huaweicloudsdkcse==3.1.34',
    'huaweicloudsdkcsms==3.1.34',
    'huaweicloudsdkcss==3.1.34',
    'huaweicloudsdkcts==3.1.34',
    'huaweicloudsdkdas==3.1.34',
    'huaweicloudsdkdbss==3.1.34',
    'huaweicloudsdkdc==3.1.34',
    'huaweicloudsdkdcs==3.1.34',
    'huaweicloudsdkddm==3.1.34',
    'huaweicloudsdkdds==3.1.34',
    'huaweicloudsdkdeh==3.1.34',
    'huaweicloudsdkdevsecurity==3.1.34',
    'huaweicloudsdkdevstar==3.1.34',
    'huaweicloudsdkdgc==3.1.34',
    'huaweicloudsdkdlf==3.1.34',
    'huaweicloudsdkdli==3.1.34',
    'huaweicloudsdkdms==3.1.34',
    'huaweicloudsdkdns==3.1.34',
    'huaweicloudsdkdris==3.1.34',
    'huaweicloudsdkdrs==3.1.34',
    'huaweicloudsdkdsc==3.1.34',
    'huaweicloudsdkdwr==3.1.34',
    'huaweicloudsdkdws==3.1.34',
    'huaweicloudsdkecs==3.1.34',
    'huaweicloudsdkeg==3.1.34',
    'huaweicloudsdkeihealth==3.1.34',
    'huaweicloudsdkeip==3.1.34',
    'huaweicloudsdkelb==3.1.34',
    'huaweicloudsdkeps==3.1.34',
    'huaweicloudsdker==3.1.34',
    'huaweicloudsdkevs==3.1.34',
    'huaweicloudsdkfrs==3.1.34',
    'huaweicloudsdkfunctiongraph==3.1.34',
    'huaweicloudsdkga==3.1.34',
    'huaweicloudsdkgaussdb==3.1.34',
    'huaweicloudsdkgaussdbfornosql==3.1.34',
    'huaweicloudsdkgaussdbforopengauss==3.1.34',
    'huaweicloudsdkges==3.1.34',
    'huaweicloudsdkgsl==3.1.34',
    'huaweicloudsdkhilens==3.1.34',
    'huaweicloudsdkhss==3.1.34',
    'huaweicloudsdkiam==3.1.34',
    'huaweicloudsdkiec==3.1.34',
    'huaweicloudsdkief==3.1.34',
    'huaweicloudsdkies==3.1.34',
    'huaweicloudsdkimage==3.1.34',
    'huaweicloudsdkimagesearch==3.1.34',
    'huaweicloudsdkims==3.1.34',
    'huaweicloudsdkiotanalytics==3.1.34',
    'huaweicloudsdkiotda==3.1.34',
    'huaweicloudsdkiotedge==3.1.34',
    'huaweicloudsdkivs==3.1.34',
    'huaweicloudsdkkafka==3.1.34',
    'huaweicloudsdkkms==3.1.34',
    'huaweicloudsdkkps==3.1.34',
    'huaweicloudsdklakeformation==3.1.34',
    'huaweicloudsdklive==3.1.34',
    'huaweicloudsdklts==3.1.34',
    'huaweicloudsdkmapds==3.1.34',
    'huaweicloudsdkmas==3.1.34',
    'huaweicloudsdkmeeting==3.1.34',
    'huaweicloudsdkmoderation==3.1.34',
    'huaweicloudsdkmpc==3.1.34',
    'huaweicloudsdkmrs==3.1.34',
    'huaweicloudsdknat==3.1.34',
    'huaweicloudsdknlp==3.1.34',
    'huaweicloudsdkocr==3.1.34',
    'huaweicloudsdkoms==3.1.34',
    'huaweicloudsdkorganizations==3.1.34',
    'huaweicloudsdkosm==3.1.34',
    'huaweicloudsdkprojectman==3.1.34',
    'huaweicloudsdkrabbitmq==3.1.34',
    'huaweicloudsdkram==3.1.34',
    'huaweicloudsdkrds==3.1.34',
    'huaweicloudsdkres==3.1.34',
    'huaweicloudsdkrms==3.1.34',
    'huaweicloudsdkrocketmq==3.1.34',
    'huaweicloudsdkroma==3.1.34',
    'huaweicloudsdksa==3.1.34',
    'huaweicloudsdkscm==3.1.34',
    'huaweicloudsdksdrs==3.1.34',
    'huaweicloudsdksecmaster==3.1.34',
    'huaweicloudsdkservicestage==3.1.34',
    'huaweicloudsdksfsturbo==3.1.34',
    'huaweicloudsdksis==3.1.34',
    'huaweicloudsdksmn==3.1.34',
    'huaweicloudsdksms==3.1.34',
    'huaweicloudsdkswr==3.1.34',
    'huaweicloudsdktms==3.1.34',
    'huaweicloudsdkugo==3.1.34',
    'huaweicloudsdkvas==3.1.34',
    'huaweicloudsdkvcm==3.1.34',
    'huaweicloudsdkvod==3.1.34',
    'huaweicloudsdkvpc==3.1.34',
    'huaweicloudsdkvpcep==3.1.34',
    'huaweicloudsdkvss==3.1.34',
    'huaweicloudsdkwaf==3.1.34',
    'huaweicloudsdkworkspace==3.1.34',
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
