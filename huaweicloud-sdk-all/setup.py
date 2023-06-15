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
VERSION = "3.1.44"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.44',
    'huaweicloudsdkantiddos==3.1.44',
    'huaweicloudsdkaom==3.1.44',
    'huaweicloudsdkaos==3.1.44',
    'huaweicloudsdkapig==3.1.44',
    'huaweicloudsdkapm==3.1.44',
    'huaweicloudsdkas==3.1.44',
    'huaweicloudsdkbcs==3.1.44',
    'huaweicloudsdkbms==3.1.44',
    'huaweicloudsdkbss==3.1.44',
    'huaweicloudsdkbssintl==3.1.44',
    'huaweicloudsdkcae==3.1.44',
    'huaweicloudsdkcampusgo==3.1.44',
    'huaweicloudsdkcbh==3.1.44',
    'huaweicloudsdkcbr==3.1.44',
    'huaweicloudsdkcbs==3.1.44',
    'huaweicloudsdkcc==3.1.44',
    'huaweicloudsdkcce==3.1.44',
    'huaweicloudsdkccm==3.1.44',
    'huaweicloudsdkcdm==3.1.44',
    'huaweicloudsdkcdn==3.1.44',
    'huaweicloudsdkces==3.1.44',
    'huaweicloudsdkcfw==3.1.44',
    'huaweicloudsdkcgs==3.1.44',
    'huaweicloudsdkclassroom==3.1.44',
    'huaweicloudsdkcloudide==3.1.44',
    'huaweicloudsdkcloudpipeline==3.1.44',
    'huaweicloudsdkcloudrtc==3.1.44',
    'huaweicloudsdkcloudtable==3.1.44',
    'huaweicloudsdkcloudtest==3.1.44',
    'huaweicloudsdkcodeartsartifact==3.1.44',
    'huaweicloudsdkcodeartsbuild==3.1.44',
    'huaweicloudsdkcodeartsdeploy==3.1.44',
    'huaweicloudsdkcodecheck==3.1.44',
    'huaweicloudsdkcodecraft==3.1.44',
    'huaweicloudsdkcodehub==3.1.44',
    'huaweicloudsdkcph==3.1.44',
    'huaweicloudsdkcpts==3.1.44',
    'huaweicloudsdkcse==3.1.44',
    'huaweicloudsdkcsms==3.1.44',
    'huaweicloudsdkcss==3.1.44',
    'huaweicloudsdkcts==3.1.44',
    'huaweicloudsdkdas==3.1.44',
    'huaweicloudsdkdbss==3.1.44',
    'huaweicloudsdkdc==3.1.44',
    'huaweicloudsdkdcs==3.1.44',
    'huaweicloudsdkddm==3.1.44',
    'huaweicloudsdkdds==3.1.44',
    'huaweicloudsdkdeh==3.1.44',
    'huaweicloudsdkdevsecurity==3.1.44',
    'huaweicloudsdkdevstar==3.1.44',
    'huaweicloudsdkdgc==3.1.44',
    'huaweicloudsdkdlf==3.1.44',
    'huaweicloudsdkdli==3.1.44',
    'huaweicloudsdkdns==3.1.44',
    'huaweicloudsdkdris==3.1.44',
    'huaweicloudsdkdrs==3.1.44',
    'huaweicloudsdkdsc==3.1.44',
    'huaweicloudsdkdwr==3.1.44',
    'huaweicloudsdkdws==3.1.44',
    'huaweicloudsdkecs==3.1.44',
    'huaweicloudsdkeg==3.1.44',
    'huaweicloudsdkeihealth==3.1.44',
    'huaweicloudsdkeip==3.1.44',
    'huaweicloudsdkelb==3.1.44',
    'huaweicloudsdkeps==3.1.44',
    'huaweicloudsdker==3.1.44',
    'huaweicloudsdkevs==3.1.44',
    'huaweicloudsdkfrs==3.1.44',
    'huaweicloudsdkfunctiongraph==3.1.44',
    'huaweicloudsdkga==3.1.44',
    'huaweicloudsdkgaussdb==3.1.44',
    'huaweicloudsdkgaussdbfornosql==3.1.44',
    'huaweicloudsdkgaussdbforopengauss==3.1.44',
    'huaweicloudsdkges==3.1.44',
    'huaweicloudsdkgsl==3.1.44',
    'huaweicloudsdkhilens==3.1.44',
    'huaweicloudsdkhss==3.1.44',
    'huaweicloudsdkiam==3.1.44',
    'huaweicloudsdkidme==3.1.44',
    'huaweicloudsdkiec==3.1.44',
    'huaweicloudsdkief==3.1.44',
    'huaweicloudsdkies==3.1.44',
    'huaweicloudsdkimage==3.1.44',
    'huaweicloudsdkimagesearch==3.1.44',
    'huaweicloudsdkims==3.1.44',
    'huaweicloudsdkiotanalytics==3.1.44',
    'huaweicloudsdkiotda==3.1.44',
    'huaweicloudsdkiotedge==3.1.44',
    'huaweicloudsdkivs==3.1.44',
    'huaweicloudsdkkafka==3.1.44',
    'huaweicloudsdkkms==3.1.44',
    'huaweicloudsdkkps==3.1.44',
    'huaweicloudsdklakeformation==3.1.44',
    'huaweicloudsdklive==3.1.44',
    'huaweicloudsdklts==3.1.44',
    'huaweicloudsdkmapds==3.1.44',
    'huaweicloudsdkmas==3.1.44',
    'huaweicloudsdkmeeting==3.1.44',
    'huaweicloudsdkmetastudio==3.1.44',
    'huaweicloudsdkmoderation==3.1.44',
    'huaweicloudsdkmpc==3.1.44',
    'huaweicloudsdkmrs==3.1.44',
    'huaweicloudsdkmsgsms==3.1.44',
    'huaweicloudsdknat==3.1.44',
    'huaweicloudsdknlp==3.1.44',
    'huaweicloudsdkocr==3.1.44',
    'huaweicloudsdkoms==3.1.44',
    'huaweicloudsdkorganizations==3.1.44',
    'huaweicloudsdkosm==3.1.44',
    'huaweicloudsdkprojectman==3.1.44',
    'huaweicloudsdkrabbitmq==3.1.44',
    'huaweicloudsdkram==3.1.44',
    'huaweicloudsdkrds==3.1.44',
    'huaweicloudsdkres==3.1.44',
    'huaweicloudsdkrms==3.1.44',
    'huaweicloudsdkrocketmq==3.1.44',
    'huaweicloudsdkroma==3.1.44',
    'huaweicloudsdksa==3.1.44',
    'huaweicloudsdkscm==3.1.44',
    'huaweicloudsdksdrs==3.1.44',
    'huaweicloudsdksecmaster==3.1.44',
    'huaweicloudsdkservicestage==3.1.44',
    'huaweicloudsdksfsturbo==3.1.44',
    'huaweicloudsdksis==3.1.44',
    'huaweicloudsdksmn==3.1.44',
    'huaweicloudsdksms==3.1.44',
    'huaweicloudsdkswr==3.1.44',
    'huaweicloudsdktms==3.1.44',
    'huaweicloudsdkugo==3.1.44',
    'huaweicloudsdkvas==3.1.44',
    'huaweicloudsdkvcm==3.1.44',
    'huaweicloudsdkvod==3.1.44',
    'huaweicloudsdkvpc==3.1.44',
    'huaweicloudsdkvpcep==3.1.44',
    'huaweicloudsdkvss==3.1.44',
    'huaweicloudsdkwaf==3.1.44',
    'huaweicloudsdkworkspace==3.1.44',
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
