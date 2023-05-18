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
VERSION = "3.1.40"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.40',
    'huaweicloudsdkantiddos==3.1.40',
    'huaweicloudsdkaom==3.1.40',
    'huaweicloudsdkaos==3.1.40',
    'huaweicloudsdkapig==3.1.40',
    'huaweicloudsdkapm==3.1.40',
    'huaweicloudsdkas==3.1.40',
    'huaweicloudsdkbcs==3.1.40',
    'huaweicloudsdkbms==3.1.40',
    'huaweicloudsdkbss==3.1.40',
    'huaweicloudsdkbssintl==3.1.40',
    'huaweicloudsdkcae==3.1.40',
    'huaweicloudsdkcampusgo==3.1.40',
    'huaweicloudsdkcbh==3.1.40',
    'huaweicloudsdkcbr==3.1.40',
    'huaweicloudsdkcbs==3.1.40',
    'huaweicloudsdkcc==3.1.40',
    'huaweicloudsdkcce==3.1.40',
    'huaweicloudsdkccm==3.1.40',
    'huaweicloudsdkcdm==3.1.40',
    'huaweicloudsdkcdn==3.1.40',
    'huaweicloudsdkces==3.1.40',
    'huaweicloudsdkcfw==3.1.40',
    'huaweicloudsdkcgs==3.1.40',
    'huaweicloudsdkclassroom==3.1.40',
    'huaweicloudsdkclouddeploy==3.1.40',
    'huaweicloudsdkcloudide==3.1.40',
    'huaweicloudsdkcloudpipeline==3.1.40',
    'huaweicloudsdkcloudrtc==3.1.40',
    'huaweicloudsdkcloudtable==3.1.40',
    'huaweicloudsdkcloudtest==3.1.40',
    'huaweicloudsdkcodeartsartifact==3.1.40',
    'huaweicloudsdkcodeartsbuild==3.1.40',
    'huaweicloudsdkcodecheck==3.1.40',
    'huaweicloudsdkcodecraft==3.1.40',
    'huaweicloudsdkcodehub==3.1.40',
    'huaweicloudsdkcph==3.1.40',
    'huaweicloudsdkcpts==3.1.40',
    'huaweicloudsdkcse==3.1.40',
    'huaweicloudsdkcsms==3.1.40',
    'huaweicloudsdkcss==3.1.40',
    'huaweicloudsdkcts==3.1.40',
    'huaweicloudsdkdas==3.1.40',
    'huaweicloudsdkdbss==3.1.40',
    'huaweicloudsdkdc==3.1.40',
    'huaweicloudsdkdcs==3.1.40',
    'huaweicloudsdkddm==3.1.40',
    'huaweicloudsdkdds==3.1.40',
    'huaweicloudsdkdeh==3.1.40',
    'huaweicloudsdkdevsecurity==3.1.40',
    'huaweicloudsdkdevstar==3.1.40',
    'huaweicloudsdkdgc==3.1.40',
    'huaweicloudsdkdlf==3.1.40',
    'huaweicloudsdkdli==3.1.40',
    'huaweicloudsdkdms==3.1.40',
    'huaweicloudsdkdns==3.1.40',
    'huaweicloudsdkdris==3.1.40',
    'huaweicloudsdkdrs==3.1.40',
    'huaweicloudsdkdsc==3.1.40',
    'huaweicloudsdkdwr==3.1.40',
    'huaweicloudsdkdws==3.1.40',
    'huaweicloudsdkecs==3.1.40',
    'huaweicloudsdkeg==3.1.40',
    'huaweicloudsdkeihealth==3.1.40',
    'huaweicloudsdkeip==3.1.40',
    'huaweicloudsdkelb==3.1.40',
    'huaweicloudsdkeps==3.1.40',
    'huaweicloudsdker==3.1.40',
    'huaweicloudsdkevs==3.1.40',
    'huaweicloudsdkfrs==3.1.40',
    'huaweicloudsdkfunctiongraph==3.1.40',
    'huaweicloudsdkga==3.1.40',
    'huaweicloudsdkgaussdb==3.1.40',
    'huaweicloudsdkgaussdbfornosql==3.1.40',
    'huaweicloudsdkgaussdbforopengauss==3.1.40',
    'huaweicloudsdkges==3.1.40',
    'huaweicloudsdkgsl==3.1.40',
    'huaweicloudsdkhilens==3.1.40',
    'huaweicloudsdkhss==3.1.40',
    'huaweicloudsdkiam==3.1.40',
    'huaweicloudsdkiec==3.1.40',
    'huaweicloudsdkief==3.1.40',
    'huaweicloudsdkies==3.1.40',
    'huaweicloudsdkimage==3.1.40',
    'huaweicloudsdkimagesearch==3.1.40',
    'huaweicloudsdkims==3.1.40',
    'huaweicloudsdkiotanalytics==3.1.40',
    'huaweicloudsdkiotda==3.1.40',
    'huaweicloudsdkiotedge==3.1.40',
    'huaweicloudsdkivs==3.1.40',
    'huaweicloudsdkkafka==3.1.40',
    'huaweicloudsdkkms==3.1.40',
    'huaweicloudsdkkps==3.1.40',
    'huaweicloudsdklakeformation==3.1.40',
    'huaweicloudsdklive==3.1.40',
    'huaweicloudsdklts==3.1.40',
    'huaweicloudsdkmapds==3.1.40',
    'huaweicloudsdkmas==3.1.40',
    'huaweicloudsdkmeeting==3.1.40',
    'huaweicloudsdkmetastudio==3.1.40',
    'huaweicloudsdkmoderation==3.1.40',
    'huaweicloudsdkmpc==3.1.40',
    'huaweicloudsdkmrs==3.1.40',
    'huaweicloudsdkmsgsms==3.1.40',
    'huaweicloudsdknat==3.1.40',
    'huaweicloudsdknlp==3.1.40',
    'huaweicloudsdkocr==3.1.40',
    'huaweicloudsdkoms==3.1.40',
    'huaweicloudsdkorganizations==3.1.40',
    'huaweicloudsdkosm==3.1.40',
    'huaweicloudsdkprojectman==3.1.40',
    'huaweicloudsdkrabbitmq==3.1.40',
    'huaweicloudsdkram==3.1.40',
    'huaweicloudsdkrds==3.1.40',
    'huaweicloudsdkres==3.1.40',
    'huaweicloudsdkrms==3.1.40',
    'huaweicloudsdkrocketmq==3.1.40',
    'huaweicloudsdkroma==3.1.40',
    'huaweicloudsdksa==3.1.40',
    'huaweicloudsdkscm==3.1.40',
    'huaweicloudsdksdrs==3.1.40',
    'huaweicloudsdksecmaster==3.1.40',
    'huaweicloudsdkservicestage==3.1.40',
    'huaweicloudsdksfsturbo==3.1.40',
    'huaweicloudsdksis==3.1.40',
    'huaweicloudsdksmn==3.1.40',
    'huaweicloudsdksms==3.1.40',
    'huaweicloudsdkswr==3.1.40',
    'huaweicloudsdktms==3.1.40',
    'huaweicloudsdkugo==3.1.40',
    'huaweicloudsdkvas==3.1.40',
    'huaweicloudsdkvcm==3.1.40',
    'huaweicloudsdkvod==3.1.40',
    'huaweicloudsdkvpc==3.1.40',
    'huaweicloudsdkvpcep==3.1.40',
    'huaweicloudsdkvss==3.1.40',
    'huaweicloudsdkwaf==3.1.40',
    'huaweicloudsdkworkspace==3.1.40',
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
