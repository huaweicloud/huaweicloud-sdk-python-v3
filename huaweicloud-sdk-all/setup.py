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
VERSION = "3.1.64"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.64',
    'huaweicloudsdkantiddos==3.1.64',
    'huaweicloudsdkaom==3.1.64',
    'huaweicloudsdkaos==3.1.64',
    'huaweicloudsdkapig==3.1.64',
    'huaweicloudsdkapm==3.1.64',
    'huaweicloudsdkas==3.1.64',
    'huaweicloudsdkasm==3.1.64',
    'huaweicloudsdkbcs==3.1.64',
    'huaweicloudsdkbms==3.1.64',
    'huaweicloudsdkbss==3.1.64',
    'huaweicloudsdkbssintl==3.1.64',
    'huaweicloudsdkcae==3.1.64',
    'huaweicloudsdkcampusgo==3.1.64',
    'huaweicloudsdkcbh==3.1.64',
    'huaweicloudsdkcbr==3.1.64',
    'huaweicloudsdkcbs==3.1.64',
    'huaweicloudsdkcc==3.1.64',
    'huaweicloudsdkcce==3.1.64',
    'huaweicloudsdkccm==3.1.64',
    'huaweicloudsdkcdm==3.1.64',
    'huaweicloudsdkcdn==3.1.64',
    'huaweicloudsdkces==3.1.64',
    'huaweicloudsdkcfw==3.1.64',
    'huaweicloudsdkcgs==3.1.64',
    'huaweicloudsdkclassroom==3.1.64',
    'huaweicloudsdkcloudide==3.1.64',
    'huaweicloudsdkcloudpond==3.1.64',
    'huaweicloudsdkcloudrtc==3.1.64',
    'huaweicloudsdkcloudtable==3.1.64',
    'huaweicloudsdkcloudtest==3.1.64',
    'huaweicloudsdkcodeartsartifact==3.1.64',
    'huaweicloudsdkcodeartsbuild==3.1.64',
    'huaweicloudsdkcodeartscheck==3.1.64',
    'huaweicloudsdkcodeartsdeploy==3.1.64',
    'huaweicloudsdkcodeartsinspector==3.1.64',
    'huaweicloudsdkcodeartspipeline==3.1.64',
    'huaweicloudsdkcodecraft==3.1.64',
    'huaweicloudsdkcodehub==3.1.64',
    'huaweicloudsdkconfig==3.1.64',
    'huaweicloudsdkcph==3.1.64',
    'huaweicloudsdkcpts==3.1.64',
    'huaweicloudsdkcse==3.1.64',
    'huaweicloudsdkcsms==3.1.64',
    'huaweicloudsdkcss==3.1.64',
    'huaweicloudsdkcts==3.1.64',
    'huaweicloudsdkdas==3.1.64',
    'huaweicloudsdkdataartsstudio==3.1.64',
    'huaweicloudsdkdbss==3.1.64',
    'huaweicloudsdkdc==3.1.64',
    'huaweicloudsdkdcs==3.1.64',
    'huaweicloudsdkddm==3.1.64',
    'huaweicloudsdkdds==3.1.64',
    'huaweicloudsdkdeh==3.1.64',
    'huaweicloudsdkdevsecurity==3.1.64',
    'huaweicloudsdkdevstar==3.1.64',
    'huaweicloudsdkdgc==3.1.64',
    'huaweicloudsdkdlf==3.1.64',
    'huaweicloudsdkdli==3.1.64',
    'huaweicloudsdkdns==3.1.64',
    'huaweicloudsdkdris==3.1.64',
    'huaweicloudsdkdrs==3.1.64',
    'huaweicloudsdkdsc==3.1.64',
    'huaweicloudsdkdwr==3.1.64',
    'huaweicloudsdkdws==3.1.64',
    'huaweicloudsdkec==3.1.64',
    'huaweicloudsdkecs==3.1.64',
    'huaweicloudsdkedgesec==3.1.64',
    'huaweicloudsdkeg==3.1.64',
    'huaweicloudsdkeihealth==3.1.64',
    'huaweicloudsdkeip==3.1.64',
    'huaweicloudsdkelb==3.1.64',
    'huaweicloudsdkeps==3.1.64',
    'huaweicloudsdker==3.1.64',
    'huaweicloudsdkevs==3.1.64',
    'huaweicloudsdkfrs==3.1.64',
    'huaweicloudsdkfunctiongraph==3.1.64',
    'huaweicloudsdkga==3.1.64',
    'huaweicloudsdkgaussdb==3.1.64',
    'huaweicloudsdkgaussdbfornosql==3.1.64',
    'huaweicloudsdkgaussdbforopengauss==3.1.64',
    'huaweicloudsdkges==3.1.64',
    'huaweicloudsdkgsl==3.1.64',
    'huaweicloudsdkhilens==3.1.64',
    'huaweicloudsdkhss==3.1.64',
    'huaweicloudsdkiam==3.1.64',
    'huaweicloudsdkidentitycenter==3.1.64',
    'huaweicloudsdkidentitycenterstore==3.1.64',
    'huaweicloudsdkidme==3.1.64',
    'huaweicloudsdkiec==3.1.64',
    'huaweicloudsdkief==3.1.64',
    'huaweicloudsdkimage==3.1.64',
    'huaweicloudsdkimagesearch==3.1.64',
    'huaweicloudsdkims==3.1.64',
    'huaweicloudsdkiotanalytics==3.1.64',
    'huaweicloudsdkiotda==3.1.64',
    'huaweicloudsdkiotedge==3.1.64',
    'huaweicloudsdkivs==3.1.64',
    'huaweicloudsdkkafka==3.1.64',
    'huaweicloudsdkkms==3.1.64',
    'huaweicloudsdkkoomessage==3.1.64',
    'huaweicloudsdkkps==3.1.64',
    'huaweicloudsdklakeformation==3.1.64',
    'huaweicloudsdklive==3.1.64',
    'huaweicloudsdklts==3.1.64',
    'huaweicloudsdkmapds==3.1.64',
    'huaweicloudsdkmas==3.1.64',
    'huaweicloudsdkmeeting==3.1.64',
    'huaweicloudsdkmetastudio==3.1.64',
    'huaweicloudsdkmoderation==3.1.64',
    'huaweicloudsdkmpc==3.1.64',
    'huaweicloudsdkmrs==3.1.64',
    'huaweicloudsdkmsgsms==3.1.64',
    'huaweicloudsdkmssi==3.1.64',
    'huaweicloudsdknat==3.1.64',
    'huaweicloudsdknlp==3.1.64',
    'huaweicloudsdkocr==3.1.64',
    'huaweicloudsdkoms==3.1.64',
    'huaweicloudsdkoptverse==3.1.64',
    'huaweicloudsdkorganizations==3.1.64',
    'huaweicloudsdkoroas==3.1.64',
    'huaweicloudsdkosm==3.1.64',
    'huaweicloudsdkpangulargemodels==3.1.64',
    'huaweicloudsdkprojectman==3.1.64',
    'huaweicloudsdkrabbitmq==3.1.64',
    'huaweicloudsdkram==3.1.64',
    'huaweicloudsdkrds==3.1.64',
    'huaweicloudsdkres==3.1.64',
    'huaweicloudsdkrms==3.1.64',
    'huaweicloudsdkrocketmq==3.1.64',
    'huaweicloudsdkroma==3.1.64',
    'huaweicloudsdksa==3.1.64',
    'huaweicloudsdkscm==3.1.64',
    'huaweicloudsdksdrs==3.1.64',
    'huaweicloudsdksecmaster==3.1.64',
    'huaweicloudsdkservicestage==3.1.64',
    'huaweicloudsdksfsturbo==3.1.64',
    'huaweicloudsdksis==3.1.64',
    'huaweicloudsdksmn==3.1.64',
    'huaweicloudsdksms==3.1.64',
    'huaweicloudsdkswr==3.1.64',
    'huaweicloudsdktms==3.1.64',
    'huaweicloudsdkugo==3.1.64',
    'huaweicloudsdkvas==3.1.64',
    'huaweicloudsdkvcm==3.1.64',
    'huaweicloudsdkvod==3.1.64',
    'huaweicloudsdkvpc==3.1.64',
    'huaweicloudsdkvpcep==3.1.64',
    'huaweicloudsdkwaf==3.1.64',
    'huaweicloudsdkworkspace==3.1.64',
    'huaweicloudsdkworkspaceapp==3.1.64',
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
