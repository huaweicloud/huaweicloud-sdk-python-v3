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
VERSION = "3.1.43"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.43',
    'huaweicloudsdkantiddos==3.1.43',
    'huaweicloudsdkaom==3.1.43',
    'huaweicloudsdkaos==3.1.43',
    'huaweicloudsdkapig==3.1.43',
    'huaweicloudsdkapm==3.1.43',
    'huaweicloudsdkas==3.1.43',
    'huaweicloudsdkbcs==3.1.43',
    'huaweicloudsdkbms==3.1.43',
    'huaweicloudsdkbss==3.1.43',
    'huaweicloudsdkbssintl==3.1.43',
    'huaweicloudsdkcae==3.1.43',
    'huaweicloudsdkcampusgo==3.1.43',
    'huaweicloudsdkcbh==3.1.43',
    'huaweicloudsdkcbr==3.1.43',
    'huaweicloudsdkcbs==3.1.43',
    'huaweicloudsdkcc==3.1.43',
    'huaweicloudsdkcce==3.1.43',
    'huaweicloudsdkccm==3.1.43',
    'huaweicloudsdkcdm==3.1.43',
    'huaweicloudsdkcdn==3.1.43',
    'huaweicloudsdkces==3.1.43',
    'huaweicloudsdkcfw==3.1.43',
    'huaweicloudsdkcgs==3.1.43',
    'huaweicloudsdkclassroom==3.1.43',
    'huaweicloudsdkclouddeploy==3.1.43',
    'huaweicloudsdkcloudide==3.1.43',
    'huaweicloudsdkcloudpipeline==3.1.43',
    'huaweicloudsdkcloudrtc==3.1.43',
    'huaweicloudsdkcloudtable==3.1.43',
    'huaweicloudsdkcloudtest==3.1.43',
    'huaweicloudsdkcodeartsartifact==3.1.43',
    'huaweicloudsdkcodeartsbuild==3.1.43',
    'huaweicloudsdkcodecheck==3.1.43',
    'huaweicloudsdkcodecraft==3.1.43',
    'huaweicloudsdkcodehub==3.1.43',
    'huaweicloudsdkcph==3.1.43',
    'huaweicloudsdkcpts==3.1.43',
    'huaweicloudsdkcse==3.1.43',
    'huaweicloudsdkcsms==3.1.43',
    'huaweicloudsdkcss==3.1.43',
    'huaweicloudsdkcts==3.1.43',
    'huaweicloudsdkdas==3.1.43',
    'huaweicloudsdkdbss==3.1.43',
    'huaweicloudsdkdc==3.1.43',
    'huaweicloudsdkdcs==3.1.43',
    'huaweicloudsdkddm==3.1.43',
    'huaweicloudsdkdds==3.1.43',
    'huaweicloudsdkdeh==3.1.43',
    'huaweicloudsdkdevsecurity==3.1.43',
    'huaweicloudsdkdevstar==3.1.43',
    'huaweicloudsdkdgc==3.1.43',
    'huaweicloudsdkdlf==3.1.43',
    'huaweicloudsdkdli==3.1.43',
    'huaweicloudsdkdns==3.1.43',
    'huaweicloudsdkdris==3.1.43',
    'huaweicloudsdkdrs==3.1.43',
    'huaweicloudsdkdsc==3.1.43',
    'huaweicloudsdkdwr==3.1.43',
    'huaweicloudsdkdws==3.1.43',
    'huaweicloudsdkecs==3.1.43',
    'huaweicloudsdkeg==3.1.43',
    'huaweicloudsdkeihealth==3.1.43',
    'huaweicloudsdkeip==3.1.43',
    'huaweicloudsdkelb==3.1.43',
    'huaweicloudsdkeps==3.1.43',
    'huaweicloudsdker==3.1.43',
    'huaweicloudsdkevs==3.1.43',
    'huaweicloudsdkfrs==3.1.43',
    'huaweicloudsdkfunctiongraph==3.1.43',
    'huaweicloudsdkga==3.1.43',
    'huaweicloudsdkgaussdb==3.1.43',
    'huaweicloudsdkgaussdbfornosql==3.1.43',
    'huaweicloudsdkgaussdbforopengauss==3.1.43',
    'huaweicloudsdkges==3.1.43',
    'huaweicloudsdkgsl==3.1.43',
    'huaweicloudsdkhilens==3.1.43',
    'huaweicloudsdkhss==3.1.43',
    'huaweicloudsdkiam==3.1.43',
    'huaweicloudsdkidme==3.1.43',
    'huaweicloudsdkiec==3.1.43',
    'huaweicloudsdkief==3.1.43',
    'huaweicloudsdkies==3.1.43',
    'huaweicloudsdkimage==3.1.43',
    'huaweicloudsdkimagesearch==3.1.43',
    'huaweicloudsdkims==3.1.43',
    'huaweicloudsdkiotanalytics==3.1.43',
    'huaweicloudsdkiotda==3.1.43',
    'huaweicloudsdkiotedge==3.1.43',
    'huaweicloudsdkivs==3.1.43',
    'huaweicloudsdkkafka==3.1.43',
    'huaweicloudsdkkms==3.1.43',
    'huaweicloudsdkkps==3.1.43',
    'huaweicloudsdklakeformation==3.1.43',
    'huaweicloudsdklive==3.1.43',
    'huaweicloudsdklts==3.1.43',
    'huaweicloudsdkmapds==3.1.43',
    'huaweicloudsdkmas==3.1.43',
    'huaweicloudsdkmeeting==3.1.43',
    'huaweicloudsdkmetastudio==3.1.43',
    'huaweicloudsdkmoderation==3.1.43',
    'huaweicloudsdkmpc==3.1.43',
    'huaweicloudsdkmrs==3.1.43',
    'huaweicloudsdkmsgsms==3.1.43',
    'huaweicloudsdknat==3.1.43',
    'huaweicloudsdknlp==3.1.43',
    'huaweicloudsdkocr==3.1.43',
    'huaweicloudsdkoms==3.1.43',
    'huaweicloudsdkorganizations==3.1.43',
    'huaweicloudsdkosm==3.1.43',
    'huaweicloudsdkprojectman==3.1.43',
    'huaweicloudsdkrabbitmq==3.1.43',
    'huaweicloudsdkram==3.1.43',
    'huaweicloudsdkrds==3.1.43',
    'huaweicloudsdkres==3.1.43',
    'huaweicloudsdkrms==3.1.43',
    'huaweicloudsdkrocketmq==3.1.43',
    'huaweicloudsdkroma==3.1.43',
    'huaweicloudsdksa==3.1.43',
    'huaweicloudsdkscm==3.1.43',
    'huaweicloudsdksdrs==3.1.43',
    'huaweicloudsdksecmaster==3.1.43',
    'huaweicloudsdkservicestage==3.1.43',
    'huaweicloudsdksfsturbo==3.1.43',
    'huaweicloudsdksis==3.1.43',
    'huaweicloudsdksmn==3.1.43',
    'huaweicloudsdksms==3.1.43',
    'huaweicloudsdkswr==3.1.43',
    'huaweicloudsdktms==3.1.43',
    'huaweicloudsdkugo==3.1.43',
    'huaweicloudsdkvas==3.1.43',
    'huaweicloudsdkvcm==3.1.43',
    'huaweicloudsdkvod==3.1.43',
    'huaweicloudsdkvpc==3.1.43',
    'huaweicloudsdkvpcep==3.1.43',
    'huaweicloudsdkvss==3.1.43',
    'huaweicloudsdkwaf==3.1.43',
    'huaweicloudsdkworkspace==3.1.43',
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
