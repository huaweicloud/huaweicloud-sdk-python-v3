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
VERSION = "3.1.57"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.57',
    'huaweicloudsdkantiddos==3.1.57',
    'huaweicloudsdkaom==3.1.57',
    'huaweicloudsdkaos==3.1.57',
    'huaweicloudsdkapig==3.1.57',
    'huaweicloudsdkapm==3.1.57',
    'huaweicloudsdkas==3.1.57',
    'huaweicloudsdkbcs==3.1.57',
    'huaweicloudsdkbms==3.1.57',
    'huaweicloudsdkbss==3.1.57',
    'huaweicloudsdkbssintl==3.1.57',
    'huaweicloudsdkcae==3.1.57',
    'huaweicloudsdkcampusgo==3.1.57',
    'huaweicloudsdkcbh==3.1.57',
    'huaweicloudsdkcbr==3.1.57',
    'huaweicloudsdkcbs==3.1.57',
    'huaweicloudsdkcc==3.1.57',
    'huaweicloudsdkcce==3.1.57',
    'huaweicloudsdkccm==3.1.57',
    'huaweicloudsdkcdm==3.1.57',
    'huaweicloudsdkcdn==3.1.57',
    'huaweicloudsdkces==3.1.57',
    'huaweicloudsdkcfw==3.1.57',
    'huaweicloudsdkcgs==3.1.57',
    'huaweicloudsdkclassroom==3.1.57',
    'huaweicloudsdkcloudide==3.1.57',
    'huaweicloudsdkcloudpipeline==3.1.57',
    'huaweicloudsdkcloudrtc==3.1.57',
    'huaweicloudsdkcloudtable==3.1.57',
    'huaweicloudsdkcloudtest==3.1.57',
    'huaweicloudsdkcodeartsartifact==3.1.57',
    'huaweicloudsdkcodeartsbuild==3.1.57',
    'huaweicloudsdkcodeartscheck==3.1.57',
    'huaweicloudsdkcodeartsdeploy==3.1.57',
    'huaweicloudsdkcodecraft==3.1.57',
    'huaweicloudsdkcodehub==3.1.57',
    'huaweicloudsdkconfig==3.1.57',
    'huaweicloudsdkcph==3.1.57',
    'huaweicloudsdkcpts==3.1.57',
    'huaweicloudsdkcse==3.1.57',
    'huaweicloudsdkcsms==3.1.57',
    'huaweicloudsdkcss==3.1.57',
    'huaweicloudsdkcts==3.1.57',
    'huaweicloudsdkdas==3.1.57',
    'huaweicloudsdkdataartsstudio==3.1.57',
    'huaweicloudsdkdbss==3.1.57',
    'huaweicloudsdkdc==3.1.57',
    'huaweicloudsdkdcs==3.1.57',
    'huaweicloudsdkddm==3.1.57',
    'huaweicloudsdkdds==3.1.57',
    'huaweicloudsdkdeh==3.1.57',
    'huaweicloudsdkdevsecurity==3.1.57',
    'huaweicloudsdkdevstar==3.1.57',
    'huaweicloudsdkdgc==3.1.57',
    'huaweicloudsdkdlf==3.1.57',
    'huaweicloudsdkdli==3.1.57',
    'huaweicloudsdkdns==3.1.57',
    'huaweicloudsdkdris==3.1.57',
    'huaweicloudsdkdrs==3.1.57',
    'huaweicloudsdkdsc==3.1.57',
    'huaweicloudsdkdwr==3.1.57',
    'huaweicloudsdkdws==3.1.57',
    'huaweicloudsdkec==3.1.57',
    'huaweicloudsdkecs==3.1.57',
    'huaweicloudsdkedgesec==3.1.57',
    'huaweicloudsdkeg==3.1.57',
    'huaweicloudsdkeihealth==3.1.57',
    'huaweicloudsdkeip==3.1.57',
    'huaweicloudsdkelb==3.1.57',
    'huaweicloudsdkeps==3.1.57',
    'huaweicloudsdker==3.1.57',
    'huaweicloudsdkevs==3.1.57',
    'huaweicloudsdkfrs==3.1.57',
    'huaweicloudsdkfunctiongraph==3.1.57',
    'huaweicloudsdkga==3.1.57',
    'huaweicloudsdkgaussdb==3.1.57',
    'huaweicloudsdkgaussdbfornosql==3.1.57',
    'huaweicloudsdkgaussdbforopengauss==3.1.57',
    'huaweicloudsdkges==3.1.57',
    'huaweicloudsdkgsl==3.1.57',
    'huaweicloudsdkhilens==3.1.57',
    'huaweicloudsdkhss==3.1.57',
    'huaweicloudsdkiam==3.1.57',
    'huaweicloudsdkidentitycenter==3.1.57',
    'huaweicloudsdkidme==3.1.57',
    'huaweicloudsdkiec==3.1.57',
    'huaweicloudsdkief==3.1.57',
    'huaweicloudsdkies==3.1.57',
    'huaweicloudsdkimage==3.1.57',
    'huaweicloudsdkimagesearch==3.1.57',
    'huaweicloudsdkims==3.1.57',
    'huaweicloudsdkiotanalytics==3.1.57',
    'huaweicloudsdkiotda==3.1.57',
    'huaweicloudsdkiotedge==3.1.57',
    'huaweicloudsdkivs==3.1.57',
    'huaweicloudsdkkafka==3.1.57',
    'huaweicloudsdkkms==3.1.57',
    'huaweicloudsdkkoomessage==3.1.57',
    'huaweicloudsdkkps==3.1.57',
    'huaweicloudsdklakeformation==3.1.57',
    'huaweicloudsdklive==3.1.57',
    'huaweicloudsdklts==3.1.57',
    'huaweicloudsdkmapds==3.1.57',
    'huaweicloudsdkmas==3.1.57',
    'huaweicloudsdkmeeting==3.1.57',
    'huaweicloudsdkmetastudio==3.1.57',
    'huaweicloudsdkmoderation==3.1.57',
    'huaweicloudsdkmpc==3.1.57',
    'huaweicloudsdkmrs==3.1.57',
    'huaweicloudsdkmsgsms==3.1.57',
    'huaweicloudsdknat==3.1.57',
    'huaweicloudsdknlp==3.1.57',
    'huaweicloudsdkocr==3.1.57',
    'huaweicloudsdkoms==3.1.57',
    'huaweicloudsdkoptverse==3.1.57',
    'huaweicloudsdkorganizations==3.1.57',
    'huaweicloudsdkoroas==3.1.57',
    'huaweicloudsdkosm==3.1.57',
    'huaweicloudsdkpangulargemodels==3.1.57',
    'huaweicloudsdkprojectman==3.1.57',
    'huaweicloudsdkrabbitmq==3.1.57',
    'huaweicloudsdkram==3.1.57',
    'huaweicloudsdkrds==3.1.57',
    'huaweicloudsdkres==3.1.57',
    'huaweicloudsdkrms==3.1.57',
    'huaweicloudsdkrocketmq==3.1.57',
    'huaweicloudsdkroma==3.1.57',
    'huaweicloudsdksa==3.1.57',
    'huaweicloudsdkscm==3.1.57',
    'huaweicloudsdksdrs==3.1.57',
    'huaweicloudsdksecmaster==3.1.57',
    'huaweicloudsdkservicestage==3.1.57',
    'huaweicloudsdksfsturbo==3.1.57',
    'huaweicloudsdksis==3.1.57',
    'huaweicloudsdksmn==3.1.57',
    'huaweicloudsdksms==3.1.57',
    'huaweicloudsdkswr==3.1.57',
    'huaweicloudsdktms==3.1.57',
    'huaweicloudsdkugo==3.1.57',
    'huaweicloudsdkvas==3.1.57',
    'huaweicloudsdkvcm==3.1.57',
    'huaweicloudsdkvod==3.1.57',
    'huaweicloudsdkvpc==3.1.57',
    'huaweicloudsdkvpcep==3.1.57',
    'huaweicloudsdkvss==3.1.57',
    'huaweicloudsdkwaf==3.1.57',
    'huaweicloudsdkworkspace==3.1.57',
    'huaweicloudsdkworkspaceapp==3.1.57',
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
