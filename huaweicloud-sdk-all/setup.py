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
VERSION = "3.1.46"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.46',
    'huaweicloudsdkantiddos==3.1.46',
    'huaweicloudsdkaom==3.1.46',
    'huaweicloudsdkaos==3.1.46',
    'huaweicloudsdkapig==3.1.46',
    'huaweicloudsdkapm==3.1.46',
    'huaweicloudsdkas==3.1.46',
    'huaweicloudsdkbcs==3.1.46',
    'huaweicloudsdkbms==3.1.46',
    'huaweicloudsdkbss==3.1.46',
    'huaweicloudsdkbssintl==3.1.46',
    'huaweicloudsdkcae==3.1.46',
    'huaweicloudsdkcampusgo==3.1.46',
    'huaweicloudsdkcbh==3.1.46',
    'huaweicloudsdkcbr==3.1.46',
    'huaweicloudsdkcbs==3.1.46',
    'huaweicloudsdkcc==3.1.46',
    'huaweicloudsdkcce==3.1.46',
    'huaweicloudsdkccm==3.1.46',
    'huaweicloudsdkcdm==3.1.46',
    'huaweicloudsdkcdn==3.1.46',
    'huaweicloudsdkces==3.1.46',
    'huaweicloudsdkcfw==3.1.46',
    'huaweicloudsdkcgs==3.1.46',
    'huaweicloudsdkclassroom==3.1.46',
    'huaweicloudsdkcloudide==3.1.46',
    'huaweicloudsdkcloudpipeline==3.1.46',
    'huaweicloudsdkcloudrtc==3.1.46',
    'huaweicloudsdkcloudtable==3.1.46',
    'huaweicloudsdkcloudtest==3.1.46',
    'huaweicloudsdkcodeartsartifact==3.1.46',
    'huaweicloudsdkcodeartsbuild==3.1.46',
    'huaweicloudsdkcodeartsdeploy==3.1.46',
    'huaweicloudsdkcodecheck==3.1.46',
    'huaweicloudsdkcodecraft==3.1.46',
    'huaweicloudsdkcodehub==3.1.46',
    'huaweicloudsdkconfig==3.1.46',
    'huaweicloudsdkcph==3.1.46',
    'huaweicloudsdkcpts==3.1.46',
    'huaweicloudsdkcse==3.1.46',
    'huaweicloudsdkcsms==3.1.46',
    'huaweicloudsdkcss==3.1.46',
    'huaweicloudsdkcts==3.1.46',
    'huaweicloudsdkdas==3.1.46',
    'huaweicloudsdkdataartsstudio==3.1.46',
    'huaweicloudsdkdbss==3.1.46',
    'huaweicloudsdkdc==3.1.46',
    'huaweicloudsdkdcs==3.1.46',
    'huaweicloudsdkddm==3.1.46',
    'huaweicloudsdkdds==3.1.46',
    'huaweicloudsdkdeh==3.1.46',
    'huaweicloudsdkdevsecurity==3.1.46',
    'huaweicloudsdkdevstar==3.1.46',
    'huaweicloudsdkdgc==3.1.46',
    'huaweicloudsdkdlf==3.1.46',
    'huaweicloudsdkdli==3.1.46',
    'huaweicloudsdkdns==3.1.46',
    'huaweicloudsdkdris==3.1.46',
    'huaweicloudsdkdrs==3.1.46',
    'huaweicloudsdkdsc==3.1.46',
    'huaweicloudsdkdwr==3.1.46',
    'huaweicloudsdkdws==3.1.46',
    'huaweicloudsdkecs==3.1.46',
    'huaweicloudsdkeg==3.1.46',
    'huaweicloudsdkeihealth==3.1.46',
    'huaweicloudsdkeip==3.1.46',
    'huaweicloudsdkelb==3.1.46',
    'huaweicloudsdkeps==3.1.46',
    'huaweicloudsdker==3.1.46',
    'huaweicloudsdkevs==3.1.46',
    'huaweicloudsdkfrs==3.1.46',
    'huaweicloudsdkfunctiongraph==3.1.46',
    'huaweicloudsdkga==3.1.46',
    'huaweicloudsdkgaussdb==3.1.46',
    'huaweicloudsdkgaussdbfornosql==3.1.46',
    'huaweicloudsdkgaussdbforopengauss==3.1.46',
    'huaweicloudsdkges==3.1.46',
    'huaweicloudsdkgsl==3.1.46',
    'huaweicloudsdkhilens==3.1.46',
    'huaweicloudsdkhss==3.1.46',
    'huaweicloudsdkiam==3.1.46',
    'huaweicloudsdkidentitycenter==3.1.46',
    'huaweicloudsdkidme==3.1.46',
    'huaweicloudsdkiec==3.1.46',
    'huaweicloudsdkief==3.1.46',
    'huaweicloudsdkies==3.1.46',
    'huaweicloudsdkimage==3.1.46',
    'huaweicloudsdkimagesearch==3.1.46',
    'huaweicloudsdkims==3.1.46',
    'huaweicloudsdkiotanalytics==3.1.46',
    'huaweicloudsdkiotda==3.1.46',
    'huaweicloudsdkiotedge==3.1.46',
    'huaweicloudsdkivs==3.1.46',
    'huaweicloudsdkkafka==3.1.46',
    'huaweicloudsdkkms==3.1.46',
    'huaweicloudsdkkoomessage==3.1.46',
    'huaweicloudsdkkps==3.1.46',
    'huaweicloudsdklakeformation==3.1.46',
    'huaweicloudsdklive==3.1.46',
    'huaweicloudsdklts==3.1.46',
    'huaweicloudsdkmapds==3.1.46',
    'huaweicloudsdkmas==3.1.46',
    'huaweicloudsdkmeeting==3.1.46',
    'huaweicloudsdkmetastudio==3.1.46',
    'huaweicloudsdkmoderation==3.1.46',
    'huaweicloudsdkmpc==3.1.46',
    'huaweicloudsdkmrs==3.1.46',
    'huaweicloudsdkmsgsms==3.1.46',
    'huaweicloudsdknat==3.1.46',
    'huaweicloudsdknlp==3.1.46',
    'huaweicloudsdkocr==3.1.46',
    'huaweicloudsdkoms==3.1.46',
    'huaweicloudsdkorganizations==3.1.46',
    'huaweicloudsdkosm==3.1.46',
    'huaweicloudsdkprojectman==3.1.46',
    'huaweicloudsdkrabbitmq==3.1.46',
    'huaweicloudsdkram==3.1.46',
    'huaweicloudsdkrds==3.1.46',
    'huaweicloudsdkres==3.1.46',
    'huaweicloudsdkrms==3.1.46',
    'huaweicloudsdkrocketmq==3.1.46',
    'huaweicloudsdkroma==3.1.46',
    'huaweicloudsdksa==3.1.46',
    'huaweicloudsdkscm==3.1.46',
    'huaweicloudsdksdrs==3.1.46',
    'huaweicloudsdksecmaster==3.1.46',
    'huaweicloudsdkservicestage==3.1.46',
    'huaweicloudsdksfsturbo==3.1.46',
    'huaweicloudsdksis==3.1.46',
    'huaweicloudsdksmn==3.1.46',
    'huaweicloudsdksms==3.1.46',
    'huaweicloudsdkswr==3.1.46',
    'huaweicloudsdktms==3.1.46',
    'huaweicloudsdkugo==3.1.46',
    'huaweicloudsdkvas==3.1.46',
    'huaweicloudsdkvcm==3.1.46',
    'huaweicloudsdkvod==3.1.46',
    'huaweicloudsdkvpc==3.1.46',
    'huaweicloudsdkvpcep==3.1.46',
    'huaweicloudsdkvss==3.1.46',
    'huaweicloudsdkwaf==3.1.46',
    'huaweicloudsdkworkspace==3.1.46',
    'huaweicloudsdkworkspaceapp==3.1.46',
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
