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
VERSION = "3.1.47"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.47',
    'huaweicloudsdkantiddos==3.1.47',
    'huaweicloudsdkaom==3.1.47',
    'huaweicloudsdkaos==3.1.47',
    'huaweicloudsdkapig==3.1.47',
    'huaweicloudsdkapm==3.1.47',
    'huaweicloudsdkas==3.1.47',
    'huaweicloudsdkbcs==3.1.47',
    'huaweicloudsdkbms==3.1.47',
    'huaweicloudsdkbss==3.1.47',
    'huaweicloudsdkbssintl==3.1.47',
    'huaweicloudsdkcae==3.1.47',
    'huaweicloudsdkcampusgo==3.1.47',
    'huaweicloudsdkcbh==3.1.47',
    'huaweicloudsdkcbr==3.1.47',
    'huaweicloudsdkcbs==3.1.47',
    'huaweicloudsdkcc==3.1.47',
    'huaweicloudsdkcce==3.1.47',
    'huaweicloudsdkccm==3.1.47',
    'huaweicloudsdkcdm==3.1.47',
    'huaweicloudsdkcdn==3.1.47',
    'huaweicloudsdkces==3.1.47',
    'huaweicloudsdkcfw==3.1.47',
    'huaweicloudsdkcgs==3.1.47',
    'huaweicloudsdkclassroom==3.1.47',
    'huaweicloudsdkcloudide==3.1.47',
    'huaweicloudsdkcloudpipeline==3.1.47',
    'huaweicloudsdkcloudrtc==3.1.47',
    'huaweicloudsdkcloudtable==3.1.47',
    'huaweicloudsdkcloudtest==3.1.47',
    'huaweicloudsdkcodeartsartifact==3.1.47',
    'huaweicloudsdkcodeartsbuild==3.1.47',
    'huaweicloudsdkcodeartscheck==3.1.47',
    'huaweicloudsdkcodeartsdeploy==3.1.47',
    'huaweicloudsdkcodecraft==3.1.47',
    'huaweicloudsdkcodehub==3.1.47',
    'huaweicloudsdkconfig==3.1.47',
    'huaweicloudsdkcph==3.1.47',
    'huaweicloudsdkcpts==3.1.47',
    'huaweicloudsdkcse==3.1.47',
    'huaweicloudsdkcsms==3.1.47',
    'huaweicloudsdkcss==3.1.47',
    'huaweicloudsdkcts==3.1.47',
    'huaweicloudsdkdas==3.1.47',
    'huaweicloudsdkdataartsstudio==3.1.47',
    'huaweicloudsdkdbss==3.1.47',
    'huaweicloudsdkdc==3.1.47',
    'huaweicloudsdkdcs==3.1.47',
    'huaweicloudsdkddm==3.1.47',
    'huaweicloudsdkdds==3.1.47',
    'huaweicloudsdkdeh==3.1.47',
    'huaweicloudsdkdevsecurity==3.1.47',
    'huaweicloudsdkdevstar==3.1.47',
    'huaweicloudsdkdgc==3.1.47',
    'huaweicloudsdkdlf==3.1.47',
    'huaweicloudsdkdli==3.1.47',
    'huaweicloudsdkdns==3.1.47',
    'huaweicloudsdkdris==3.1.47',
    'huaweicloudsdkdrs==3.1.47',
    'huaweicloudsdkdsc==3.1.47',
    'huaweicloudsdkdwr==3.1.47',
    'huaweicloudsdkdws==3.1.47',
    'huaweicloudsdkecs==3.1.47',
    'huaweicloudsdkeg==3.1.47',
    'huaweicloudsdkeihealth==3.1.47',
    'huaweicloudsdkeip==3.1.47',
    'huaweicloudsdkelb==3.1.47',
    'huaweicloudsdkeps==3.1.47',
    'huaweicloudsdker==3.1.47',
    'huaweicloudsdkevs==3.1.47',
    'huaweicloudsdkfrs==3.1.47',
    'huaweicloudsdkfunctiongraph==3.1.47',
    'huaweicloudsdkga==3.1.47',
    'huaweicloudsdkgaussdb==3.1.47',
    'huaweicloudsdkgaussdbfornosql==3.1.47',
    'huaweicloudsdkgaussdbforopengauss==3.1.47',
    'huaweicloudsdkges==3.1.47',
    'huaweicloudsdkgsl==3.1.47',
    'huaweicloudsdkhilens==3.1.47',
    'huaweicloudsdkhss==3.1.47',
    'huaweicloudsdkiam==3.1.47',
    'huaweicloudsdkidentitycenter==3.1.47',
    'huaweicloudsdkidme==3.1.47',
    'huaweicloudsdkiec==3.1.47',
    'huaweicloudsdkief==3.1.47',
    'huaweicloudsdkies==3.1.47',
    'huaweicloudsdkimage==3.1.47',
    'huaweicloudsdkimagesearch==3.1.47',
    'huaweicloudsdkims==3.1.47',
    'huaweicloudsdkiotanalytics==3.1.47',
    'huaweicloudsdkiotda==3.1.47',
    'huaweicloudsdkiotedge==3.1.47',
    'huaweicloudsdkivs==3.1.47',
    'huaweicloudsdkkafka==3.1.47',
    'huaweicloudsdkkms==3.1.47',
    'huaweicloudsdkkoomessage==3.1.47',
    'huaweicloudsdkkps==3.1.47',
    'huaweicloudsdklakeformation==3.1.47',
    'huaweicloudsdklive==3.1.47',
    'huaweicloudsdklts==3.1.47',
    'huaweicloudsdkmapds==3.1.47',
    'huaweicloudsdkmas==3.1.47',
    'huaweicloudsdkmeeting==3.1.47',
    'huaweicloudsdkmetastudio==3.1.47',
    'huaweicloudsdkmoderation==3.1.47',
    'huaweicloudsdkmpc==3.1.47',
    'huaweicloudsdkmrs==3.1.47',
    'huaweicloudsdkmsgsms==3.1.47',
    'huaweicloudsdknat==3.1.47',
    'huaweicloudsdknlp==3.1.47',
    'huaweicloudsdkocr==3.1.47',
    'huaweicloudsdkoms==3.1.47',
    'huaweicloudsdkorganizations==3.1.47',
    'huaweicloudsdkosm==3.1.47',
    'huaweicloudsdkprojectman==3.1.47',
    'huaweicloudsdkrabbitmq==3.1.47',
    'huaweicloudsdkram==3.1.47',
    'huaweicloudsdkrds==3.1.47',
    'huaweicloudsdkres==3.1.47',
    'huaweicloudsdkrms==3.1.47',
    'huaweicloudsdkrocketmq==3.1.47',
    'huaweicloudsdkroma==3.1.47',
    'huaweicloudsdksa==3.1.47',
    'huaweicloudsdkscm==3.1.47',
    'huaweicloudsdksdrs==3.1.47',
    'huaweicloudsdksecmaster==3.1.47',
    'huaweicloudsdkservicestage==3.1.47',
    'huaweicloudsdksfsturbo==3.1.47',
    'huaweicloudsdksis==3.1.47',
    'huaweicloudsdksmn==3.1.47',
    'huaweicloudsdksms==3.1.47',
    'huaweicloudsdkswr==3.1.47',
    'huaweicloudsdktms==3.1.47',
    'huaweicloudsdkugo==3.1.47',
    'huaweicloudsdkvas==3.1.47',
    'huaweicloudsdkvcm==3.1.47',
    'huaweicloudsdkvod==3.1.47',
    'huaweicloudsdkvpc==3.1.47',
    'huaweicloudsdkvpcep==3.1.47',
    'huaweicloudsdkvss==3.1.47',
    'huaweicloudsdkwaf==3.1.47',
    'huaweicloudsdkworkspace==3.1.47',
    'huaweicloudsdkworkspaceapp==3.1.47',
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
