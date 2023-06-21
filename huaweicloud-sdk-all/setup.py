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
VERSION = "3.1.45"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.45',
    'huaweicloudsdkantiddos==3.1.45',
    'huaweicloudsdkaom==3.1.45',
    'huaweicloudsdkaos==3.1.45',
    'huaweicloudsdkapig==3.1.45',
    'huaweicloudsdkapm==3.1.45',
    'huaweicloudsdkas==3.1.45',
    'huaweicloudsdkbcs==3.1.45',
    'huaweicloudsdkbms==3.1.45',
    'huaweicloudsdkbss==3.1.45',
    'huaweicloudsdkbssintl==3.1.45',
    'huaweicloudsdkcae==3.1.45',
    'huaweicloudsdkcampusgo==3.1.45',
    'huaweicloudsdkcbh==3.1.45',
    'huaweicloudsdkcbr==3.1.45',
    'huaweicloudsdkcbs==3.1.45',
    'huaweicloudsdkcc==3.1.45',
    'huaweicloudsdkcce==3.1.45',
    'huaweicloudsdkccm==3.1.45',
    'huaweicloudsdkcdm==3.1.45',
    'huaweicloudsdkcdn==3.1.45',
    'huaweicloudsdkces==3.1.45',
    'huaweicloudsdkcfw==3.1.45',
    'huaweicloudsdkcgs==3.1.45',
    'huaweicloudsdkclassroom==3.1.45',
    'huaweicloudsdkcloudide==3.1.45',
    'huaweicloudsdkcloudpipeline==3.1.45',
    'huaweicloudsdkcloudrtc==3.1.45',
    'huaweicloudsdkcloudtable==3.1.45',
    'huaweicloudsdkcloudtest==3.1.45',
    'huaweicloudsdkcodeartsartifact==3.1.45',
    'huaweicloudsdkcodeartsbuild==3.1.45',
    'huaweicloudsdkcodeartsdeploy==3.1.45',
    'huaweicloudsdkcodecheck==3.1.45',
    'huaweicloudsdkcodecraft==3.1.45',
    'huaweicloudsdkcodehub==3.1.45',
    'huaweicloudsdkcph==3.1.45',
    'huaweicloudsdkcpts==3.1.45',
    'huaweicloudsdkcse==3.1.45',
    'huaweicloudsdkcsms==3.1.45',
    'huaweicloudsdkcss==3.1.45',
    'huaweicloudsdkcts==3.1.45',
    'huaweicloudsdkdas==3.1.45',
    'huaweicloudsdkdataartsstudio==3.1.45',
    'huaweicloudsdkdbss==3.1.45',
    'huaweicloudsdkdc==3.1.45',
    'huaweicloudsdkdcs==3.1.45',
    'huaweicloudsdkddm==3.1.45',
    'huaweicloudsdkdds==3.1.45',
    'huaweicloudsdkdeh==3.1.45',
    'huaweicloudsdkdevsecurity==3.1.45',
    'huaweicloudsdkdevstar==3.1.45',
    'huaweicloudsdkdgc==3.1.45',
    'huaweicloudsdkdlf==3.1.45',
    'huaweicloudsdkdli==3.1.45',
    'huaweicloudsdkdns==3.1.45',
    'huaweicloudsdkdris==3.1.45',
    'huaweicloudsdkdrs==3.1.45',
    'huaweicloudsdkdsc==3.1.45',
    'huaweicloudsdkdwr==3.1.45',
    'huaweicloudsdkdws==3.1.45',
    'huaweicloudsdkecs==3.1.45',
    'huaweicloudsdkeg==3.1.45',
    'huaweicloudsdkeihealth==3.1.45',
    'huaweicloudsdkeip==3.1.45',
    'huaweicloudsdkelb==3.1.45',
    'huaweicloudsdkeps==3.1.45',
    'huaweicloudsdker==3.1.45',
    'huaweicloudsdkevs==3.1.45',
    'huaweicloudsdkfrs==3.1.45',
    'huaweicloudsdkfunctiongraph==3.1.45',
    'huaweicloudsdkga==3.1.45',
    'huaweicloudsdkgaussdb==3.1.45',
    'huaweicloudsdkgaussdbfornosql==3.1.45',
    'huaweicloudsdkgaussdbforopengauss==3.1.45',
    'huaweicloudsdkges==3.1.45',
    'huaweicloudsdkgsl==3.1.45',
    'huaweicloudsdkhilens==3.1.45',
    'huaweicloudsdkhss==3.1.45',
    'huaweicloudsdkiam==3.1.45',
    'huaweicloudsdkidme==3.1.45',
    'huaweicloudsdkiec==3.1.45',
    'huaweicloudsdkief==3.1.45',
    'huaweicloudsdkies==3.1.45',
    'huaweicloudsdkimage==3.1.45',
    'huaweicloudsdkimagesearch==3.1.45',
    'huaweicloudsdkims==3.1.45',
    'huaweicloudsdkiotanalytics==3.1.45',
    'huaweicloudsdkiotda==3.1.45',
    'huaweicloudsdkiotedge==3.1.45',
    'huaweicloudsdkivs==3.1.45',
    'huaweicloudsdkkafka==3.1.45',
    'huaweicloudsdkkms==3.1.45',
    'huaweicloudsdkkoomessage==3.1.45',
    'huaweicloudsdkkps==3.1.45',
    'huaweicloudsdklakeformation==3.1.45',
    'huaweicloudsdklive==3.1.45',
    'huaweicloudsdklts==3.1.45',
    'huaweicloudsdkmapds==3.1.45',
    'huaweicloudsdkmas==3.1.45',
    'huaweicloudsdkmeeting==3.1.45',
    'huaweicloudsdkmetastudio==3.1.45',
    'huaweicloudsdkmoderation==3.1.45',
    'huaweicloudsdkmpc==3.1.45',
    'huaweicloudsdkmrs==3.1.45',
    'huaweicloudsdkmsgsms==3.1.45',
    'huaweicloudsdknat==3.1.45',
    'huaweicloudsdknlp==3.1.45',
    'huaweicloudsdkocr==3.1.45',
    'huaweicloudsdkoms==3.1.45',
    'huaweicloudsdkorganizations==3.1.45',
    'huaweicloudsdkosm==3.1.45',
    'huaweicloudsdkprojectman==3.1.45',
    'huaweicloudsdkrabbitmq==3.1.45',
    'huaweicloudsdkram==3.1.45',
    'huaweicloudsdkrds==3.1.45',
    'huaweicloudsdkres==3.1.45',
    'huaweicloudsdkrms==3.1.45',
    'huaweicloudsdkrocketmq==3.1.45',
    'huaweicloudsdkroma==3.1.45',
    'huaweicloudsdksa==3.1.45',
    'huaweicloudsdkscm==3.1.45',
    'huaweicloudsdksdrs==3.1.45',
    'huaweicloudsdksecmaster==3.1.45',
    'huaweicloudsdkservicestage==3.1.45',
    'huaweicloudsdksfsturbo==3.1.45',
    'huaweicloudsdksis==3.1.45',
    'huaweicloudsdksmn==3.1.45',
    'huaweicloudsdksms==3.1.45',
    'huaweicloudsdkswr==3.1.45',
    'huaweicloudsdktms==3.1.45',
    'huaweicloudsdkugo==3.1.45',
    'huaweicloudsdkvas==3.1.45',
    'huaweicloudsdkvcm==3.1.45',
    'huaweicloudsdkvod==3.1.45',
    'huaweicloudsdkvpc==3.1.45',
    'huaweicloudsdkvpcep==3.1.45',
    'huaweicloudsdkvss==3.1.45',
    'huaweicloudsdkwaf==3.1.45',
    'huaweicloudsdkworkspace==3.1.45',
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
