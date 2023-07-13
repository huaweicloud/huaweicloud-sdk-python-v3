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
VERSION = "3.1.48"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.48',
    'huaweicloudsdkantiddos==3.1.48',
    'huaweicloudsdkaom==3.1.48',
    'huaweicloudsdkaos==3.1.48',
    'huaweicloudsdkapig==3.1.48',
    'huaweicloudsdkapm==3.1.48',
    'huaweicloudsdkas==3.1.48',
    'huaweicloudsdkbcs==3.1.48',
    'huaweicloudsdkbms==3.1.48',
    'huaweicloudsdkbss==3.1.48',
    'huaweicloudsdkbssintl==3.1.48',
    'huaweicloudsdkcae==3.1.48',
    'huaweicloudsdkcampusgo==3.1.48',
    'huaweicloudsdkcbh==3.1.48',
    'huaweicloudsdkcbr==3.1.48',
    'huaweicloudsdkcbs==3.1.48',
    'huaweicloudsdkcc==3.1.48',
    'huaweicloudsdkcce==3.1.48',
    'huaweicloudsdkccm==3.1.48',
    'huaweicloudsdkcdm==3.1.48',
    'huaweicloudsdkcdn==3.1.48',
    'huaweicloudsdkces==3.1.48',
    'huaweicloudsdkcfw==3.1.48',
    'huaweicloudsdkcgs==3.1.48',
    'huaweicloudsdkclassroom==3.1.48',
    'huaweicloudsdkcloudide==3.1.48',
    'huaweicloudsdkcloudpipeline==3.1.48',
    'huaweicloudsdkcloudrtc==3.1.48',
    'huaweicloudsdkcloudtable==3.1.48',
    'huaweicloudsdkcloudtest==3.1.48',
    'huaweicloudsdkcodeartsartifact==3.1.48',
    'huaweicloudsdkcodeartsbuild==3.1.48',
    'huaweicloudsdkcodeartscheck==3.1.48',
    'huaweicloudsdkcodeartsdeploy==3.1.48',
    'huaweicloudsdkcodecraft==3.1.48',
    'huaweicloudsdkcodehub==3.1.48',
    'huaweicloudsdkconfig==3.1.48',
    'huaweicloudsdkcph==3.1.48',
    'huaweicloudsdkcpts==3.1.48',
    'huaweicloudsdkcse==3.1.48',
    'huaweicloudsdkcsms==3.1.48',
    'huaweicloudsdkcss==3.1.48',
    'huaweicloudsdkcts==3.1.48',
    'huaweicloudsdkdas==3.1.48',
    'huaweicloudsdkdataartsstudio==3.1.48',
    'huaweicloudsdkdbss==3.1.48',
    'huaweicloudsdkdc==3.1.48',
    'huaweicloudsdkdcs==3.1.48',
    'huaweicloudsdkddm==3.1.48',
    'huaweicloudsdkdds==3.1.48',
    'huaweicloudsdkdeh==3.1.48',
    'huaweicloudsdkdevsecurity==3.1.48',
    'huaweicloudsdkdevstar==3.1.48',
    'huaweicloudsdkdgc==3.1.48',
    'huaweicloudsdkdlf==3.1.48',
    'huaweicloudsdkdli==3.1.48',
    'huaweicloudsdkdns==3.1.48',
    'huaweicloudsdkdris==3.1.48',
    'huaweicloudsdkdrs==3.1.48',
    'huaweicloudsdkdsc==3.1.48',
    'huaweicloudsdkdwr==3.1.48',
    'huaweicloudsdkdws==3.1.48',
    'huaweicloudsdkecs==3.1.48',
    'huaweicloudsdkeg==3.1.48',
    'huaweicloudsdkeihealth==3.1.48',
    'huaweicloudsdkeip==3.1.48',
    'huaweicloudsdkelb==3.1.48',
    'huaweicloudsdkeps==3.1.48',
    'huaweicloudsdker==3.1.48',
    'huaweicloudsdkevs==3.1.48',
    'huaweicloudsdkfrs==3.1.48',
    'huaweicloudsdkfunctiongraph==3.1.48',
    'huaweicloudsdkga==3.1.48',
    'huaweicloudsdkgaussdb==3.1.48',
    'huaweicloudsdkgaussdbfornosql==3.1.48',
    'huaweicloudsdkgaussdbforopengauss==3.1.48',
    'huaweicloudsdkges==3.1.48',
    'huaweicloudsdkgsl==3.1.48',
    'huaweicloudsdkhilens==3.1.48',
    'huaweicloudsdkhss==3.1.48',
    'huaweicloudsdkiam==3.1.48',
    'huaweicloudsdkidentitycenter==3.1.48',
    'huaweicloudsdkidme==3.1.48',
    'huaweicloudsdkiec==3.1.48',
    'huaweicloudsdkief==3.1.48',
    'huaweicloudsdkies==3.1.48',
    'huaweicloudsdkimage==3.1.48',
    'huaweicloudsdkimagesearch==3.1.48',
    'huaweicloudsdkims==3.1.48',
    'huaweicloudsdkiotanalytics==3.1.48',
    'huaweicloudsdkiotda==3.1.48',
    'huaweicloudsdkiotedge==3.1.48',
    'huaweicloudsdkivs==3.1.48',
    'huaweicloudsdkkafka==3.1.48',
    'huaweicloudsdkkms==3.1.48',
    'huaweicloudsdkkoomessage==3.1.48',
    'huaweicloudsdkkps==3.1.48',
    'huaweicloudsdklakeformation==3.1.48',
    'huaweicloudsdklive==3.1.48',
    'huaweicloudsdklts==3.1.48',
    'huaweicloudsdkmapds==3.1.48',
    'huaweicloudsdkmas==3.1.48',
    'huaweicloudsdkmeeting==3.1.48',
    'huaweicloudsdkmetastudio==3.1.48',
    'huaweicloudsdkmoderation==3.1.48',
    'huaweicloudsdkmpc==3.1.48',
    'huaweicloudsdkmrs==3.1.48',
    'huaweicloudsdkmsgsms==3.1.48',
    'huaweicloudsdknat==3.1.48',
    'huaweicloudsdknlp==3.1.48',
    'huaweicloudsdkocr==3.1.48',
    'huaweicloudsdkoms==3.1.48',
    'huaweicloudsdkorganizations==3.1.48',
    'huaweicloudsdkoroas==3.1.48',
    'huaweicloudsdkosm==3.1.48',
    'huaweicloudsdkprojectman==3.1.48',
    'huaweicloudsdkrabbitmq==3.1.48',
    'huaweicloudsdkram==3.1.48',
    'huaweicloudsdkrds==3.1.48',
    'huaweicloudsdkres==3.1.48',
    'huaweicloudsdkrms==3.1.48',
    'huaweicloudsdkrocketmq==3.1.48',
    'huaweicloudsdkroma==3.1.48',
    'huaweicloudsdksa==3.1.48',
    'huaweicloudsdkscm==3.1.48',
    'huaweicloudsdksdrs==3.1.48',
    'huaweicloudsdksecmaster==3.1.48',
    'huaweicloudsdkservicestage==3.1.48',
    'huaweicloudsdksfsturbo==3.1.48',
    'huaweicloudsdksis==3.1.48',
    'huaweicloudsdksmn==3.1.48',
    'huaweicloudsdksms==3.1.48',
    'huaweicloudsdkswr==3.1.48',
    'huaweicloudsdktms==3.1.48',
    'huaweicloudsdkugo==3.1.48',
    'huaweicloudsdkvas==3.1.48',
    'huaweicloudsdkvcm==3.1.48',
    'huaweicloudsdkvod==3.1.48',
    'huaweicloudsdkvpc==3.1.48',
    'huaweicloudsdkvpcep==3.1.48',
    'huaweicloudsdkvss==3.1.48',
    'huaweicloudsdkwaf==3.1.48',
    'huaweicloudsdkworkspace==3.1.48',
    'huaweicloudsdkworkspaceapp==3.1.48',
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
