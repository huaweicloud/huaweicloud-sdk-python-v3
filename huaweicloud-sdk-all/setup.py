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
VERSION = "3.1.41"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.41',
    'huaweicloudsdkantiddos==3.1.41',
    'huaweicloudsdkaom==3.1.41',
    'huaweicloudsdkaos==3.1.41',
    'huaweicloudsdkapig==3.1.41',
    'huaweicloudsdkapm==3.1.41',
    'huaweicloudsdkas==3.1.41',
    'huaweicloudsdkbcs==3.1.41',
    'huaweicloudsdkbms==3.1.41',
    'huaweicloudsdkbss==3.1.41',
    'huaweicloudsdkbssintl==3.1.41',
    'huaweicloudsdkcae==3.1.41',
    'huaweicloudsdkcampusgo==3.1.41',
    'huaweicloudsdkcbh==3.1.41',
    'huaweicloudsdkcbr==3.1.41',
    'huaweicloudsdkcbs==3.1.41',
    'huaweicloudsdkcc==3.1.41',
    'huaweicloudsdkcce==3.1.41',
    'huaweicloudsdkccm==3.1.41',
    'huaweicloudsdkcdm==3.1.41',
    'huaweicloudsdkcdn==3.1.41',
    'huaweicloudsdkces==3.1.41',
    'huaweicloudsdkcfw==3.1.41',
    'huaweicloudsdkcgs==3.1.41',
    'huaweicloudsdkclassroom==3.1.41',
    'huaweicloudsdkclouddeploy==3.1.41',
    'huaweicloudsdkcloudide==3.1.41',
    'huaweicloudsdkcloudpipeline==3.1.41',
    'huaweicloudsdkcloudrtc==3.1.41',
    'huaweicloudsdkcloudtable==3.1.41',
    'huaweicloudsdkcloudtest==3.1.41',
    'huaweicloudsdkcodeartsartifact==3.1.41',
    'huaweicloudsdkcodeartsbuild==3.1.41',
    'huaweicloudsdkcodecheck==3.1.41',
    'huaweicloudsdkcodecraft==3.1.41',
    'huaweicloudsdkcodehub==3.1.41',
    'huaweicloudsdkcph==3.1.41',
    'huaweicloudsdkcpts==3.1.41',
    'huaweicloudsdkcse==3.1.41',
    'huaweicloudsdkcsms==3.1.41',
    'huaweicloudsdkcss==3.1.41',
    'huaweicloudsdkcts==3.1.41',
    'huaweicloudsdkdas==3.1.41',
    'huaweicloudsdkdbss==3.1.41',
    'huaweicloudsdkdc==3.1.41',
    'huaweicloudsdkdcs==3.1.41',
    'huaweicloudsdkddm==3.1.41',
    'huaweicloudsdkdds==3.1.41',
    'huaweicloudsdkdeh==3.1.41',
    'huaweicloudsdkdevsecurity==3.1.41',
    'huaweicloudsdkdevstar==3.1.41',
    'huaweicloudsdkdgc==3.1.41',
    'huaweicloudsdkdlf==3.1.41',
    'huaweicloudsdkdli==3.1.41',
    'huaweicloudsdkdms==3.1.41',
    'huaweicloudsdkdns==3.1.41',
    'huaweicloudsdkdris==3.1.41',
    'huaweicloudsdkdrs==3.1.41',
    'huaweicloudsdkdsc==3.1.41',
    'huaweicloudsdkdwr==3.1.41',
    'huaweicloudsdkdws==3.1.41',
    'huaweicloudsdkecs==3.1.41',
    'huaweicloudsdkeg==3.1.41',
    'huaweicloudsdkeihealth==3.1.41',
    'huaweicloudsdkeip==3.1.41',
    'huaweicloudsdkelb==3.1.41',
    'huaweicloudsdkeps==3.1.41',
    'huaweicloudsdker==3.1.41',
    'huaweicloudsdkevs==3.1.41',
    'huaweicloudsdkfrs==3.1.41',
    'huaweicloudsdkfunctiongraph==3.1.41',
    'huaweicloudsdkga==3.1.41',
    'huaweicloudsdkgaussdb==3.1.41',
    'huaweicloudsdkgaussdbfornosql==3.1.41',
    'huaweicloudsdkgaussdbforopengauss==3.1.41',
    'huaweicloudsdkges==3.1.41',
    'huaweicloudsdkgsl==3.1.41',
    'huaweicloudsdkhilens==3.1.41',
    'huaweicloudsdkhss==3.1.41',
    'huaweicloudsdkiam==3.1.41',
    'huaweicloudsdkiec==3.1.41',
    'huaweicloudsdkief==3.1.41',
    'huaweicloudsdkies==3.1.41',
    'huaweicloudsdkimage==3.1.41',
    'huaweicloudsdkimagesearch==3.1.41',
    'huaweicloudsdkims==3.1.41',
    'huaweicloudsdkiotanalytics==3.1.41',
    'huaweicloudsdkiotda==3.1.41',
    'huaweicloudsdkiotedge==3.1.41',
    'huaweicloudsdkivs==3.1.41',
    'huaweicloudsdkkafka==3.1.41',
    'huaweicloudsdkkms==3.1.41',
    'huaweicloudsdkkps==3.1.41',
    'huaweicloudsdklakeformation==3.1.41',
    'huaweicloudsdklive==3.1.41',
    'huaweicloudsdklts==3.1.41',
    'huaweicloudsdkmapds==3.1.41',
    'huaweicloudsdkmas==3.1.41',
    'huaweicloudsdkmeeting==3.1.41',
    'huaweicloudsdkmetastudio==3.1.41',
    'huaweicloudsdkmoderation==3.1.41',
    'huaweicloudsdkmpc==3.1.41',
    'huaweicloudsdkmrs==3.1.41',
    'huaweicloudsdkmsgsms==3.1.41',
    'huaweicloudsdknat==3.1.41',
    'huaweicloudsdknlp==3.1.41',
    'huaweicloudsdkocr==3.1.41',
    'huaweicloudsdkoms==3.1.41',
    'huaweicloudsdkorganizations==3.1.41',
    'huaweicloudsdkosm==3.1.41',
    'huaweicloudsdkprojectman==3.1.41',
    'huaweicloudsdkrabbitmq==3.1.41',
    'huaweicloudsdkram==3.1.41',
    'huaweicloudsdkrds==3.1.41',
    'huaweicloudsdkres==3.1.41',
    'huaweicloudsdkrms==3.1.41',
    'huaweicloudsdkrocketmq==3.1.41',
    'huaweicloudsdkroma==3.1.41',
    'huaweicloudsdksa==3.1.41',
    'huaweicloudsdkscm==3.1.41',
    'huaweicloudsdksdrs==3.1.41',
    'huaweicloudsdksecmaster==3.1.41',
    'huaweicloudsdkservicestage==3.1.41',
    'huaweicloudsdksfsturbo==3.1.41',
    'huaweicloudsdksis==3.1.41',
    'huaweicloudsdksmn==3.1.41',
    'huaweicloudsdksms==3.1.41',
    'huaweicloudsdkswr==3.1.41',
    'huaweicloudsdktms==3.1.41',
    'huaweicloudsdkugo==3.1.41',
    'huaweicloudsdkvas==3.1.41',
    'huaweicloudsdkvcm==3.1.41',
    'huaweicloudsdkvod==3.1.41',
    'huaweicloudsdkvpc==3.1.41',
    'huaweicloudsdkvpcep==3.1.41',
    'huaweicloudsdkvss==3.1.41',
    'huaweicloudsdkwaf==3.1.41',
    'huaweicloudsdkworkspace==3.1.41',
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
