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
VERSION = "3.1.49"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.49',
    'huaweicloudsdkantiddos==3.1.49',
    'huaweicloudsdkaom==3.1.49',
    'huaweicloudsdkaos==3.1.49',
    'huaweicloudsdkapig==3.1.49',
    'huaweicloudsdkapm==3.1.49',
    'huaweicloudsdkas==3.1.49',
    'huaweicloudsdkbcs==3.1.49',
    'huaweicloudsdkbms==3.1.49',
    'huaweicloudsdkbss==3.1.49',
    'huaweicloudsdkbssintl==3.1.49',
    'huaweicloudsdkcae==3.1.49',
    'huaweicloudsdkcampusgo==3.1.49',
    'huaweicloudsdkcbh==3.1.49',
    'huaweicloudsdkcbr==3.1.49',
    'huaweicloudsdkcbs==3.1.49',
    'huaweicloudsdkcc==3.1.49',
    'huaweicloudsdkcce==3.1.49',
    'huaweicloudsdkccm==3.1.49',
    'huaweicloudsdkcdm==3.1.49',
    'huaweicloudsdkcdn==3.1.49',
    'huaweicloudsdkces==3.1.49',
    'huaweicloudsdkcfw==3.1.49',
    'huaweicloudsdkcgs==3.1.49',
    'huaweicloudsdkclassroom==3.1.49',
    'huaweicloudsdkcloudide==3.1.49',
    'huaweicloudsdkcloudpipeline==3.1.49',
    'huaweicloudsdkcloudrtc==3.1.49',
    'huaweicloudsdkcloudtable==3.1.49',
    'huaweicloudsdkcloudtest==3.1.49',
    'huaweicloudsdkcodeartsartifact==3.1.49',
    'huaweicloudsdkcodeartsbuild==3.1.49',
    'huaweicloudsdkcodeartscheck==3.1.49',
    'huaweicloudsdkcodeartsdeploy==3.1.49',
    'huaweicloudsdkcodecraft==3.1.49',
    'huaweicloudsdkcodehub==3.1.49',
    'huaweicloudsdkconfig==3.1.49',
    'huaweicloudsdkcph==3.1.49',
    'huaweicloudsdkcpts==3.1.49',
    'huaweicloudsdkcse==3.1.49',
    'huaweicloudsdkcsms==3.1.49',
    'huaweicloudsdkcss==3.1.49',
    'huaweicloudsdkcts==3.1.49',
    'huaweicloudsdkdas==3.1.49',
    'huaweicloudsdkdataartsstudio==3.1.49',
    'huaweicloudsdkdbss==3.1.49',
    'huaweicloudsdkdc==3.1.49',
    'huaweicloudsdkdcs==3.1.49',
    'huaweicloudsdkddm==3.1.49',
    'huaweicloudsdkdds==3.1.49',
    'huaweicloudsdkdeh==3.1.49',
    'huaweicloudsdkdevsecurity==3.1.49',
    'huaweicloudsdkdevstar==3.1.49',
    'huaweicloudsdkdgc==3.1.49',
    'huaweicloudsdkdlf==3.1.49',
    'huaweicloudsdkdli==3.1.49',
    'huaweicloudsdkdns==3.1.49',
    'huaweicloudsdkdris==3.1.49',
    'huaweicloudsdkdrs==3.1.49',
    'huaweicloudsdkdsc==3.1.49',
    'huaweicloudsdkdwr==3.1.49',
    'huaweicloudsdkdws==3.1.49',
    'huaweicloudsdkecs==3.1.49',
    'huaweicloudsdkeg==3.1.49',
    'huaweicloudsdkeihealth==3.1.49',
    'huaweicloudsdkeip==3.1.49',
    'huaweicloudsdkelb==3.1.49',
    'huaweicloudsdkeps==3.1.49',
    'huaweicloudsdker==3.1.49',
    'huaweicloudsdkevs==3.1.49',
    'huaweicloudsdkfrs==3.1.49',
    'huaweicloudsdkfunctiongraph==3.1.49',
    'huaweicloudsdkga==3.1.49',
    'huaweicloudsdkgaussdb==3.1.49',
    'huaweicloudsdkgaussdbfornosql==3.1.49',
    'huaweicloudsdkgaussdbforopengauss==3.1.49',
    'huaweicloudsdkges==3.1.49',
    'huaweicloudsdkgsl==3.1.49',
    'huaweicloudsdkhilens==3.1.49',
    'huaweicloudsdkhss==3.1.49',
    'huaweicloudsdkiam==3.1.49',
    'huaweicloudsdkidentitycenter==3.1.49',
    'huaweicloudsdkidme==3.1.49',
    'huaweicloudsdkiec==3.1.49',
    'huaweicloudsdkief==3.1.49',
    'huaweicloudsdkies==3.1.49',
    'huaweicloudsdkimage==3.1.49',
    'huaweicloudsdkimagesearch==3.1.49',
    'huaweicloudsdkims==3.1.49',
    'huaweicloudsdkiotanalytics==3.1.49',
    'huaweicloudsdkiotda==3.1.49',
    'huaweicloudsdkiotedge==3.1.49',
    'huaweicloudsdkivs==3.1.49',
    'huaweicloudsdkkafka==3.1.49',
    'huaweicloudsdkkms==3.1.49',
    'huaweicloudsdkkoomessage==3.1.49',
    'huaweicloudsdkkps==3.1.49',
    'huaweicloudsdklakeformation==3.1.49',
    'huaweicloudsdklive==3.1.49',
    'huaweicloudsdklts==3.1.49',
    'huaweicloudsdkmapds==3.1.49',
    'huaweicloudsdkmas==3.1.49',
    'huaweicloudsdkmeeting==3.1.49',
    'huaweicloudsdkmetastudio==3.1.49',
    'huaweicloudsdkmoderation==3.1.49',
    'huaweicloudsdkmpc==3.1.49',
    'huaweicloudsdkmrs==3.1.49',
    'huaweicloudsdkmsgsms==3.1.49',
    'huaweicloudsdknat==3.1.49',
    'huaweicloudsdknlp==3.1.49',
    'huaweicloudsdkocr==3.1.49',
    'huaweicloudsdkoms==3.1.49',
    'huaweicloudsdkorganizations==3.1.49',
    'huaweicloudsdkoroas==3.1.49',
    'huaweicloudsdkosm==3.1.49',
    'huaweicloudsdkprojectman==3.1.49',
    'huaweicloudsdkrabbitmq==3.1.49',
    'huaweicloudsdkram==3.1.49',
    'huaweicloudsdkrds==3.1.49',
    'huaweicloudsdkres==3.1.49',
    'huaweicloudsdkrms==3.1.49',
    'huaweicloudsdkrocketmq==3.1.49',
    'huaweicloudsdkroma==3.1.49',
    'huaweicloudsdksa==3.1.49',
    'huaweicloudsdkscm==3.1.49',
    'huaweicloudsdksdrs==3.1.49',
    'huaweicloudsdksecmaster==3.1.49',
    'huaweicloudsdkservicestage==3.1.49',
    'huaweicloudsdksfsturbo==3.1.49',
    'huaweicloudsdksis==3.1.49',
    'huaweicloudsdksmn==3.1.49',
    'huaweicloudsdksms==3.1.49',
    'huaweicloudsdkswr==3.1.49',
    'huaweicloudsdktms==3.1.49',
    'huaweicloudsdkugo==3.1.49',
    'huaweicloudsdkvas==3.1.49',
    'huaweicloudsdkvcm==3.1.49',
    'huaweicloudsdkvod==3.1.49',
    'huaweicloudsdkvpc==3.1.49',
    'huaweicloudsdkvpcep==3.1.49',
    'huaweicloudsdkvss==3.1.49',
    'huaweicloudsdkwaf==3.1.49',
    'huaweicloudsdkworkspace==3.1.49',
    'huaweicloudsdkworkspaceapp==3.1.49',
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
