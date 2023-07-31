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
VERSION = "3.1.51"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.51',
    'huaweicloudsdkantiddos==3.1.51',
    'huaweicloudsdkaom==3.1.51',
    'huaweicloudsdkaos==3.1.51',
    'huaweicloudsdkapig==3.1.51',
    'huaweicloudsdkapm==3.1.51',
    'huaweicloudsdkas==3.1.51',
    'huaweicloudsdkbcs==3.1.51',
    'huaweicloudsdkbms==3.1.51',
    'huaweicloudsdkbss==3.1.51',
    'huaweicloudsdkbssintl==3.1.51',
    'huaweicloudsdkcae==3.1.51',
    'huaweicloudsdkcampusgo==3.1.51',
    'huaweicloudsdkcbh==3.1.51',
    'huaweicloudsdkcbr==3.1.51',
    'huaweicloudsdkcbs==3.1.51',
    'huaweicloudsdkcc==3.1.51',
    'huaweicloudsdkcce==3.1.51',
    'huaweicloudsdkccm==3.1.51',
    'huaweicloudsdkcdm==3.1.51',
    'huaweicloudsdkcdn==3.1.51',
    'huaweicloudsdkces==3.1.51',
    'huaweicloudsdkcfw==3.1.51',
    'huaweicloudsdkcgs==3.1.51',
    'huaweicloudsdkclassroom==3.1.51',
    'huaweicloudsdkcloudide==3.1.51',
    'huaweicloudsdkcloudpipeline==3.1.51',
    'huaweicloudsdkcloudrtc==3.1.51',
    'huaweicloudsdkcloudtable==3.1.51',
    'huaweicloudsdkcloudtest==3.1.51',
    'huaweicloudsdkcodeartsartifact==3.1.51',
    'huaweicloudsdkcodeartsbuild==3.1.51',
    'huaweicloudsdkcodeartscheck==3.1.51',
    'huaweicloudsdkcodeartsdeploy==3.1.51',
    'huaweicloudsdkcodecraft==3.1.51',
    'huaweicloudsdkcodehub==3.1.51',
    'huaweicloudsdkconfig==3.1.51',
    'huaweicloudsdkcph==3.1.51',
    'huaweicloudsdkcpts==3.1.51',
    'huaweicloudsdkcse==3.1.51',
    'huaweicloudsdkcsms==3.1.51',
    'huaweicloudsdkcss==3.1.51',
    'huaweicloudsdkcts==3.1.51',
    'huaweicloudsdkdas==3.1.51',
    'huaweicloudsdkdataartsstudio==3.1.51',
    'huaweicloudsdkdbss==3.1.51',
    'huaweicloudsdkdc==3.1.51',
    'huaweicloudsdkdcs==3.1.51',
    'huaweicloudsdkddm==3.1.51',
    'huaweicloudsdkdds==3.1.51',
    'huaweicloudsdkdeh==3.1.51',
    'huaweicloudsdkdevsecurity==3.1.51',
    'huaweicloudsdkdevstar==3.1.51',
    'huaweicloudsdkdgc==3.1.51',
    'huaweicloudsdkdlf==3.1.51',
    'huaweicloudsdkdli==3.1.51',
    'huaweicloudsdkdns==3.1.51',
    'huaweicloudsdkdris==3.1.51',
    'huaweicloudsdkdrs==3.1.51',
    'huaweicloudsdkdsc==3.1.51',
    'huaweicloudsdkdwr==3.1.51',
    'huaweicloudsdkdws==3.1.51',
    'huaweicloudsdkecs==3.1.51',
    'huaweicloudsdkeg==3.1.51',
    'huaweicloudsdkeihealth==3.1.51',
    'huaweicloudsdkeip==3.1.51',
    'huaweicloudsdkelb==3.1.51',
    'huaweicloudsdkeps==3.1.51',
    'huaweicloudsdker==3.1.51',
    'huaweicloudsdkevs==3.1.51',
    'huaweicloudsdkfrs==3.1.51',
    'huaweicloudsdkfunctiongraph==3.1.51',
    'huaweicloudsdkga==3.1.51',
    'huaweicloudsdkgaussdb==3.1.51',
    'huaweicloudsdkgaussdbfornosql==3.1.51',
    'huaweicloudsdkgaussdbforopengauss==3.1.51',
    'huaweicloudsdkges==3.1.51',
    'huaweicloudsdkgsl==3.1.51',
    'huaweicloudsdkhilens==3.1.51',
    'huaweicloudsdkhss==3.1.51',
    'huaweicloudsdkiam==3.1.51',
    'huaweicloudsdkidentitycenter==3.1.51',
    'huaweicloudsdkidme==3.1.51',
    'huaweicloudsdkiec==3.1.51',
    'huaweicloudsdkief==3.1.51',
    'huaweicloudsdkies==3.1.51',
    'huaweicloudsdkimage==3.1.51',
    'huaweicloudsdkimagesearch==3.1.51',
    'huaweicloudsdkims==3.1.51',
    'huaweicloudsdkiotanalytics==3.1.51',
    'huaweicloudsdkiotda==3.1.51',
    'huaweicloudsdkiotedge==3.1.51',
    'huaweicloudsdkivs==3.1.51',
    'huaweicloudsdkkafka==3.1.51',
    'huaweicloudsdkkms==3.1.51',
    'huaweicloudsdkkoomessage==3.1.51',
    'huaweicloudsdkkps==3.1.51',
    'huaweicloudsdklakeformation==3.1.51',
    'huaweicloudsdklive==3.1.51',
    'huaweicloudsdklts==3.1.51',
    'huaweicloudsdkmapds==3.1.51',
    'huaweicloudsdkmas==3.1.51',
    'huaweicloudsdkmeeting==3.1.51',
    'huaweicloudsdkmetastudio==3.1.51',
    'huaweicloudsdkmoderation==3.1.51',
    'huaweicloudsdkmpc==3.1.51',
    'huaweicloudsdkmrs==3.1.51',
    'huaweicloudsdkmsgsms==3.1.51',
    'huaweicloudsdknat==3.1.51',
    'huaweicloudsdknlp==3.1.51',
    'huaweicloudsdkocr==3.1.51',
    'huaweicloudsdkoms==3.1.51',
    'huaweicloudsdkorganizations==3.1.51',
    'huaweicloudsdkoroas==3.1.51',
    'huaweicloudsdkosm==3.1.51',
    'huaweicloudsdkpangulargemodels==3.1.51',
    'huaweicloudsdkprojectman==3.1.51',
    'huaweicloudsdkrabbitmq==3.1.51',
    'huaweicloudsdkram==3.1.51',
    'huaweicloudsdkrds==3.1.51',
    'huaweicloudsdkres==3.1.51',
    'huaweicloudsdkrms==3.1.51',
    'huaweicloudsdkrocketmq==3.1.51',
    'huaweicloudsdkroma==3.1.51',
    'huaweicloudsdksa==3.1.51',
    'huaweicloudsdkscm==3.1.51',
    'huaweicloudsdksdrs==3.1.51',
    'huaweicloudsdksecmaster==3.1.51',
    'huaweicloudsdkservicestage==3.1.51',
    'huaweicloudsdksfsturbo==3.1.51',
    'huaweicloudsdksis==3.1.51',
    'huaweicloudsdksmn==3.1.51',
    'huaweicloudsdksms==3.1.51',
    'huaweicloudsdkswr==3.1.51',
    'huaweicloudsdktms==3.1.51',
    'huaweicloudsdkugo==3.1.51',
    'huaweicloudsdkvas==3.1.51',
    'huaweicloudsdkvcm==3.1.51',
    'huaweicloudsdkvod==3.1.51',
    'huaweicloudsdkvpc==3.1.51',
    'huaweicloudsdkvpcep==3.1.51',
    'huaweicloudsdkvss==3.1.51',
    'huaweicloudsdkwaf==3.1.51',
    'huaweicloudsdkworkspace==3.1.51',
    'huaweicloudsdkworkspaceapp==3.1.51',
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
