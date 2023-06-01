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
VERSION = "3.1.42"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.42',
    'huaweicloudsdkantiddos==3.1.42',
    'huaweicloudsdkaom==3.1.42',
    'huaweicloudsdkaos==3.1.42',
    'huaweicloudsdkapig==3.1.42',
    'huaweicloudsdkapm==3.1.42',
    'huaweicloudsdkas==3.1.42',
    'huaweicloudsdkbcs==3.1.42',
    'huaweicloudsdkbms==3.1.42',
    'huaweicloudsdkbss==3.1.42',
    'huaweicloudsdkbssintl==3.1.42',
    'huaweicloudsdkcae==3.1.42',
    'huaweicloudsdkcampusgo==3.1.42',
    'huaweicloudsdkcbh==3.1.42',
    'huaweicloudsdkcbr==3.1.42',
    'huaweicloudsdkcbs==3.1.42',
    'huaweicloudsdkcc==3.1.42',
    'huaweicloudsdkcce==3.1.42',
    'huaweicloudsdkccm==3.1.42',
    'huaweicloudsdkcdm==3.1.42',
    'huaweicloudsdkcdn==3.1.42',
    'huaweicloudsdkces==3.1.42',
    'huaweicloudsdkcfw==3.1.42',
    'huaweicloudsdkcgs==3.1.42',
    'huaweicloudsdkclassroom==3.1.42',
    'huaweicloudsdkclouddeploy==3.1.42',
    'huaweicloudsdkcloudide==3.1.42',
    'huaweicloudsdkcloudpipeline==3.1.42',
    'huaweicloudsdkcloudrtc==3.1.42',
    'huaweicloudsdkcloudtable==3.1.42',
    'huaweicloudsdkcloudtest==3.1.42',
    'huaweicloudsdkcodeartsartifact==3.1.42',
    'huaweicloudsdkcodeartsbuild==3.1.42',
    'huaweicloudsdkcodecheck==3.1.42',
    'huaweicloudsdkcodecraft==3.1.42',
    'huaweicloudsdkcodehub==3.1.42',
    'huaweicloudsdkcph==3.1.42',
    'huaweicloudsdkcpts==3.1.42',
    'huaweicloudsdkcse==3.1.42',
    'huaweicloudsdkcsms==3.1.42',
    'huaweicloudsdkcss==3.1.42',
    'huaweicloudsdkcts==3.1.42',
    'huaweicloudsdkdas==3.1.42',
    'huaweicloudsdkdbss==3.1.42',
    'huaweicloudsdkdc==3.1.42',
    'huaweicloudsdkdcs==3.1.42',
    'huaweicloudsdkddm==3.1.42',
    'huaweicloudsdkdds==3.1.42',
    'huaweicloudsdkdeh==3.1.42',
    'huaweicloudsdkdevsecurity==3.1.42',
    'huaweicloudsdkdevstar==3.1.42',
    'huaweicloudsdkdgc==3.1.42',
    'huaweicloudsdkdlf==3.1.42',
    'huaweicloudsdkdli==3.1.42',
    'huaweicloudsdkdms==3.1.42',
    'huaweicloudsdkdns==3.1.42',
    'huaweicloudsdkdris==3.1.42',
    'huaweicloudsdkdrs==3.1.42',
    'huaweicloudsdkdsc==3.1.42',
    'huaweicloudsdkdwr==3.1.42',
    'huaweicloudsdkdws==3.1.42',
    'huaweicloudsdkecs==3.1.42',
    'huaweicloudsdkeg==3.1.42',
    'huaweicloudsdkeihealth==3.1.42',
    'huaweicloudsdkeip==3.1.42',
    'huaweicloudsdkelb==3.1.42',
    'huaweicloudsdkeps==3.1.42',
    'huaweicloudsdker==3.1.42',
    'huaweicloudsdkevs==3.1.42',
    'huaweicloudsdkfrs==3.1.42',
    'huaweicloudsdkfunctiongraph==3.1.42',
    'huaweicloudsdkga==3.1.42',
    'huaweicloudsdkgaussdb==3.1.42',
    'huaweicloudsdkgaussdbfornosql==3.1.42',
    'huaweicloudsdkgaussdbforopengauss==3.1.42',
    'huaweicloudsdkges==3.1.42',
    'huaweicloudsdkgsl==3.1.42',
    'huaweicloudsdkhilens==3.1.42',
    'huaweicloudsdkhss==3.1.42',
    'huaweicloudsdkiam==3.1.42',
    'huaweicloudsdkiec==3.1.42',
    'huaweicloudsdkief==3.1.42',
    'huaweicloudsdkies==3.1.42',
    'huaweicloudsdkimage==3.1.42',
    'huaweicloudsdkimagesearch==3.1.42',
    'huaweicloudsdkims==3.1.42',
    'huaweicloudsdkiotanalytics==3.1.42',
    'huaweicloudsdkiotda==3.1.42',
    'huaweicloudsdkiotedge==3.1.42',
    'huaweicloudsdkivs==3.1.42',
    'huaweicloudsdkkafka==3.1.42',
    'huaweicloudsdkkms==3.1.42',
    'huaweicloudsdkkps==3.1.42',
    'huaweicloudsdklakeformation==3.1.42',
    'huaweicloudsdklive==3.1.42',
    'huaweicloudsdklts==3.1.42',
    'huaweicloudsdkmapds==3.1.42',
    'huaweicloudsdkmas==3.1.42',
    'huaweicloudsdkmeeting==3.1.42',
    'huaweicloudsdkmetastudio==3.1.42',
    'huaweicloudsdkmoderation==3.1.42',
    'huaweicloudsdkmpc==3.1.42',
    'huaweicloudsdkmrs==3.1.42',
    'huaweicloudsdkmsgsms==3.1.42',
    'huaweicloudsdknat==3.1.42',
    'huaweicloudsdknlp==3.1.42',
    'huaweicloudsdkocr==3.1.42',
    'huaweicloudsdkoms==3.1.42',
    'huaweicloudsdkorganizations==3.1.42',
    'huaweicloudsdkosm==3.1.42',
    'huaweicloudsdkprojectman==3.1.42',
    'huaweicloudsdkrabbitmq==3.1.42',
    'huaweicloudsdkram==3.1.42',
    'huaweicloudsdkrds==3.1.42',
    'huaweicloudsdkres==3.1.42',
    'huaweicloudsdkrms==3.1.42',
    'huaweicloudsdkrocketmq==3.1.42',
    'huaweicloudsdkroma==3.1.42',
    'huaweicloudsdksa==3.1.42',
    'huaweicloudsdkscm==3.1.42',
    'huaweicloudsdksdrs==3.1.42',
    'huaweicloudsdksecmaster==3.1.42',
    'huaweicloudsdkservicestage==3.1.42',
    'huaweicloudsdksfsturbo==3.1.42',
    'huaweicloudsdksis==3.1.42',
    'huaweicloudsdksmn==3.1.42',
    'huaweicloudsdksms==3.1.42',
    'huaweicloudsdkswr==3.1.42',
    'huaweicloudsdktms==3.1.42',
    'huaweicloudsdkugo==3.1.42',
    'huaweicloudsdkvas==3.1.42',
    'huaweicloudsdkvcm==3.1.42',
    'huaweicloudsdkvod==3.1.42',
    'huaweicloudsdkvpc==3.1.42',
    'huaweicloudsdkvpcep==3.1.42',
    'huaweicloudsdkvss==3.1.42',
    'huaweicloudsdkwaf==3.1.42',
    'huaweicloudsdkworkspace==3.1.42',
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
