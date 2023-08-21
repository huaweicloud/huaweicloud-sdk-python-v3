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
VERSION = "3.1.55"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.55',
    'huaweicloudsdkantiddos==3.1.55',
    'huaweicloudsdkaom==3.1.55',
    'huaweicloudsdkaos==3.1.55',
    'huaweicloudsdkapig==3.1.55',
    'huaweicloudsdkapm==3.1.55',
    'huaweicloudsdkas==3.1.55',
    'huaweicloudsdkbcs==3.1.55',
    'huaweicloudsdkbms==3.1.55',
    'huaweicloudsdkbss==3.1.55',
    'huaweicloudsdkbssintl==3.1.55',
    'huaweicloudsdkcae==3.1.55',
    'huaweicloudsdkcampusgo==3.1.55',
    'huaweicloudsdkcbh==3.1.55',
    'huaweicloudsdkcbr==3.1.55',
    'huaweicloudsdkcbs==3.1.55',
    'huaweicloudsdkcc==3.1.55',
    'huaweicloudsdkcce==3.1.55',
    'huaweicloudsdkccm==3.1.55',
    'huaweicloudsdkcdm==3.1.55',
    'huaweicloudsdkcdn==3.1.55',
    'huaweicloudsdkces==3.1.55',
    'huaweicloudsdkcfw==3.1.55',
    'huaweicloudsdkcgs==3.1.55',
    'huaweicloudsdkclassroom==3.1.55',
    'huaweicloudsdkcloudide==3.1.55',
    'huaweicloudsdkcloudpipeline==3.1.55',
    'huaweicloudsdkcloudrtc==3.1.55',
    'huaweicloudsdkcloudtable==3.1.55',
    'huaweicloudsdkcloudtest==3.1.55',
    'huaweicloudsdkcodeartsartifact==3.1.55',
    'huaweicloudsdkcodeartsbuild==3.1.55',
    'huaweicloudsdkcodeartscheck==3.1.55',
    'huaweicloudsdkcodeartsdeploy==3.1.55',
    'huaweicloudsdkcodecraft==3.1.55',
    'huaweicloudsdkcodehub==3.1.55',
    'huaweicloudsdkconfig==3.1.55',
    'huaweicloudsdkcph==3.1.55',
    'huaweicloudsdkcpts==3.1.55',
    'huaweicloudsdkcse==3.1.55',
    'huaweicloudsdkcsms==3.1.55',
    'huaweicloudsdkcss==3.1.55',
    'huaweicloudsdkcts==3.1.55',
    'huaweicloudsdkdas==3.1.55',
    'huaweicloudsdkdataartsstudio==3.1.55',
    'huaweicloudsdkdbss==3.1.55',
    'huaweicloudsdkdc==3.1.55',
    'huaweicloudsdkdcs==3.1.55',
    'huaweicloudsdkddm==3.1.55',
    'huaweicloudsdkdds==3.1.55',
    'huaweicloudsdkdeh==3.1.55',
    'huaweicloudsdkdevsecurity==3.1.55',
    'huaweicloudsdkdevstar==3.1.55',
    'huaweicloudsdkdgc==3.1.55',
    'huaweicloudsdkdlf==3.1.55',
    'huaweicloudsdkdli==3.1.55',
    'huaweicloudsdkdns==3.1.55',
    'huaweicloudsdkdris==3.1.55',
    'huaweicloudsdkdrs==3.1.55',
    'huaweicloudsdkdsc==3.1.55',
    'huaweicloudsdkdwr==3.1.55',
    'huaweicloudsdkdws==3.1.55',
    'huaweicloudsdkecs==3.1.55',
    'huaweicloudsdkedgesec==3.1.55',
    'huaweicloudsdkeg==3.1.55',
    'huaweicloudsdkeihealth==3.1.55',
    'huaweicloudsdkeip==3.1.55',
    'huaweicloudsdkelb==3.1.55',
    'huaweicloudsdkeps==3.1.55',
    'huaweicloudsdker==3.1.55',
    'huaweicloudsdkevs==3.1.55',
    'huaweicloudsdkfrs==3.1.55',
    'huaweicloudsdkfunctiongraph==3.1.55',
    'huaweicloudsdkga==3.1.55',
    'huaweicloudsdkgaussdb==3.1.55',
    'huaweicloudsdkgaussdbfornosql==3.1.55',
    'huaweicloudsdkgaussdbforopengauss==3.1.55',
    'huaweicloudsdkges==3.1.55',
    'huaweicloudsdkgsl==3.1.55',
    'huaweicloudsdkhilens==3.1.55',
    'huaweicloudsdkhss==3.1.55',
    'huaweicloudsdkiam==3.1.55',
    'huaweicloudsdkidentitycenter==3.1.55',
    'huaweicloudsdkidme==3.1.55',
    'huaweicloudsdkiec==3.1.55',
    'huaweicloudsdkief==3.1.55',
    'huaweicloudsdkies==3.1.55',
    'huaweicloudsdkimage==3.1.55',
    'huaweicloudsdkimagesearch==3.1.55',
    'huaweicloudsdkims==3.1.55',
    'huaweicloudsdkiotanalytics==3.1.55',
    'huaweicloudsdkiotda==3.1.55',
    'huaweicloudsdkiotedge==3.1.55',
    'huaweicloudsdkivs==3.1.55',
    'huaweicloudsdkkafka==3.1.55',
    'huaweicloudsdkkms==3.1.55',
    'huaweicloudsdkkoomessage==3.1.55',
    'huaweicloudsdkkps==3.1.55',
    'huaweicloudsdklakeformation==3.1.55',
    'huaweicloudsdklive==3.1.55',
    'huaweicloudsdklts==3.1.55',
    'huaweicloudsdkmapds==3.1.55',
    'huaweicloudsdkmas==3.1.55',
    'huaweicloudsdkmeeting==3.1.55',
    'huaweicloudsdkmetastudio==3.1.55',
    'huaweicloudsdkmoderation==3.1.55',
    'huaweicloudsdkmpc==3.1.55',
    'huaweicloudsdkmrs==3.1.55',
    'huaweicloudsdkmsgsms==3.1.55',
    'huaweicloudsdknat==3.1.55',
    'huaweicloudsdknlp==3.1.55',
    'huaweicloudsdkocr==3.1.55',
    'huaweicloudsdkoms==3.1.55',
    'huaweicloudsdkorganizations==3.1.55',
    'huaweicloudsdkoroas==3.1.55',
    'huaweicloudsdkosm==3.1.55',
    'huaweicloudsdkpangulargemodels==3.1.55',
    'huaweicloudsdkprojectman==3.1.55',
    'huaweicloudsdkrabbitmq==3.1.55',
    'huaweicloudsdkram==3.1.55',
    'huaweicloudsdkrds==3.1.55',
    'huaweicloudsdkres==3.1.55',
    'huaweicloudsdkrms==3.1.55',
    'huaweicloudsdkrocketmq==3.1.55',
    'huaweicloudsdkroma==3.1.55',
    'huaweicloudsdksa==3.1.55',
    'huaweicloudsdkscm==3.1.55',
    'huaweicloudsdksdrs==3.1.55',
    'huaweicloudsdksecmaster==3.1.55',
    'huaweicloudsdkservicestage==3.1.55',
    'huaweicloudsdksfsturbo==3.1.55',
    'huaweicloudsdksis==3.1.55',
    'huaweicloudsdksmn==3.1.55',
    'huaweicloudsdksms==3.1.55',
    'huaweicloudsdkswr==3.1.55',
    'huaweicloudsdktms==3.1.55',
    'huaweicloudsdkugo==3.1.55',
    'huaweicloudsdkvas==3.1.55',
    'huaweicloudsdkvcm==3.1.55',
    'huaweicloudsdkvod==3.1.55',
    'huaweicloudsdkvpc==3.1.55',
    'huaweicloudsdkvpcep==3.1.55',
    'huaweicloudsdkvss==3.1.55',
    'huaweicloudsdkwaf==3.1.55',
    'huaweicloudsdkworkspace==3.1.55',
    'huaweicloudsdkworkspaceapp==3.1.55',
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
