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
VERSION = "3.1.38"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.38',
    'huaweicloudsdkantiddos==3.1.38',
    'huaweicloudsdkaom==3.1.38',
    'huaweicloudsdkaos==3.1.38',
    'huaweicloudsdkapig==3.1.38',
    'huaweicloudsdkapm==3.1.38',
    'huaweicloudsdkas==3.1.38',
    'huaweicloudsdkbcs==3.1.38',
    'huaweicloudsdkbms==3.1.38',
    'huaweicloudsdkbss==3.1.38',
    'huaweicloudsdkbssintl==3.1.38',
    'huaweicloudsdkcae==3.1.38',
    'huaweicloudsdkcampusgo==3.1.38',
    'huaweicloudsdkcbh==3.1.38',
    'huaweicloudsdkcbr==3.1.38',
    'huaweicloudsdkcbs==3.1.38',
    'huaweicloudsdkcc==3.1.38',
    'huaweicloudsdkcce==3.1.38',
    'huaweicloudsdkccm==3.1.38',
    'huaweicloudsdkcdm==3.1.38',
    'huaweicloudsdkcdn==3.1.38',
    'huaweicloudsdkces==3.1.38',
    'huaweicloudsdkcfw==3.1.38',
    'huaweicloudsdkcgs==3.1.38',
    'huaweicloudsdkclassroom==3.1.38',
    'huaweicloudsdkclouddeploy==3.1.38',
    'huaweicloudsdkcloudide==3.1.38',
    'huaweicloudsdkcloudpipeline==3.1.38',
    'huaweicloudsdkcloudrtc==3.1.38',
    'huaweicloudsdkcloudtable==3.1.38',
    'huaweicloudsdkcloudtest==3.1.38',
    'huaweicloudsdkcodeartsartifact==3.1.38',
    'huaweicloudsdkcodeartsbuild==3.1.38',
    'huaweicloudsdkcodecheck==3.1.38',
    'huaweicloudsdkcodecraft==3.1.38',
    'huaweicloudsdkcodehub==3.1.38',
    'huaweicloudsdkcph==3.1.38',
    'huaweicloudsdkcpts==3.1.38',
    'huaweicloudsdkcse==3.1.38',
    'huaweicloudsdkcsms==3.1.38',
    'huaweicloudsdkcss==3.1.38',
    'huaweicloudsdkcts==3.1.38',
    'huaweicloudsdkdas==3.1.38',
    'huaweicloudsdkdbss==3.1.38',
    'huaweicloudsdkdc==3.1.38',
    'huaweicloudsdkdcs==3.1.38',
    'huaweicloudsdkddm==3.1.38',
    'huaweicloudsdkdds==3.1.38',
    'huaweicloudsdkdeh==3.1.38',
    'huaweicloudsdkdevsecurity==3.1.38',
    'huaweicloudsdkdevstar==3.1.38',
    'huaweicloudsdkdgc==3.1.38',
    'huaweicloudsdkdlf==3.1.38',
    'huaweicloudsdkdli==3.1.38',
    'huaweicloudsdkdms==3.1.38',
    'huaweicloudsdkdns==3.1.38',
    'huaweicloudsdkdris==3.1.38',
    'huaweicloudsdkdrs==3.1.38',
    'huaweicloudsdkdsc==3.1.38',
    'huaweicloudsdkdwr==3.1.38',
    'huaweicloudsdkdws==3.1.38',
    'huaweicloudsdkecs==3.1.38',
    'huaweicloudsdkeg==3.1.38',
    'huaweicloudsdkeihealth==3.1.38',
    'huaweicloudsdkeip==3.1.38',
    'huaweicloudsdkelb==3.1.38',
    'huaweicloudsdkeps==3.1.38',
    'huaweicloudsdker==3.1.38',
    'huaweicloudsdkevs==3.1.38',
    'huaweicloudsdkfrs==3.1.38',
    'huaweicloudsdkfunctiongraph==3.1.38',
    'huaweicloudsdkga==3.1.38',
    'huaweicloudsdkgaussdb==3.1.38',
    'huaweicloudsdkgaussdbfornosql==3.1.38',
    'huaweicloudsdkgaussdbforopengauss==3.1.38',
    'huaweicloudsdkges==3.1.38',
    'huaweicloudsdkgsl==3.1.38',
    'huaweicloudsdkhilens==3.1.38',
    'huaweicloudsdkhss==3.1.38',
    'huaweicloudsdkiam==3.1.38',
    'huaweicloudsdkiec==3.1.38',
    'huaweicloudsdkief==3.1.38',
    'huaweicloudsdkies==3.1.38',
    'huaweicloudsdkimage==3.1.38',
    'huaweicloudsdkimagesearch==3.1.38',
    'huaweicloudsdkims==3.1.38',
    'huaweicloudsdkiotanalytics==3.1.38',
    'huaweicloudsdkiotda==3.1.38',
    'huaweicloudsdkiotedge==3.1.38',
    'huaweicloudsdkivs==3.1.38',
    'huaweicloudsdkkafka==3.1.38',
    'huaweicloudsdkkms==3.1.38',
    'huaweicloudsdkkps==3.1.38',
    'huaweicloudsdklakeformation==3.1.38',
    'huaweicloudsdklive==3.1.38',
    'huaweicloudsdklts==3.1.38',
    'huaweicloudsdkmapds==3.1.38',
    'huaweicloudsdkmas==3.1.38',
    'huaweicloudsdkmeeting==3.1.38',
    'huaweicloudsdkmetastudio==3.1.38',
    'huaweicloudsdkmoderation==3.1.38',
    'huaweicloudsdkmpc==3.1.38',
    'huaweicloudsdkmrs==3.1.38',
    'huaweicloudsdkmsgsms==3.1.38',
    'huaweicloudsdknat==3.1.38',
    'huaweicloudsdknlp==3.1.38',
    'huaweicloudsdkocr==3.1.38',
    'huaweicloudsdkoms==3.1.38',
    'huaweicloudsdkorganizations==3.1.38',
    'huaweicloudsdkosm==3.1.38',
    'huaweicloudsdkprojectman==3.1.38',
    'huaweicloudsdkrabbitmq==3.1.38',
    'huaweicloudsdkram==3.1.38',
    'huaweicloudsdkrds==3.1.38',
    'huaweicloudsdkres==3.1.38',
    'huaweicloudsdkrms==3.1.38',
    'huaweicloudsdkrocketmq==3.1.38',
    'huaweicloudsdkroma==3.1.38',
    'huaweicloudsdksa==3.1.38',
    'huaweicloudsdkscm==3.1.38',
    'huaweicloudsdksdrs==3.1.38',
    'huaweicloudsdksecmaster==3.1.38',
    'huaweicloudsdkservicestage==3.1.38',
    'huaweicloudsdksfsturbo==3.1.38',
    'huaweicloudsdksis==3.1.38',
    'huaweicloudsdksmn==3.1.38',
    'huaweicloudsdksms==3.1.38',
    'huaweicloudsdkswr==3.1.38',
    'huaweicloudsdktms==3.1.38',
    'huaweicloudsdkugo==3.1.38',
    'huaweicloudsdkvas==3.1.38',
    'huaweicloudsdkvcm==3.1.38',
    'huaweicloudsdkvod==3.1.38',
    'huaweicloudsdkvpc==3.1.38',
    'huaweicloudsdkvpcep==3.1.38',
    'huaweicloudsdkvss==3.1.38',
    'huaweicloudsdkwaf==3.1.38',
    'huaweicloudsdkworkspace==3.1.38',
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
