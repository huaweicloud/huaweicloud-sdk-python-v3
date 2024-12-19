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
VERSION = "3.1.128"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.128',
    'huaweicloudsdkaad==3.1.128',
    'huaweicloudsdkantiddos==3.1.128',
    'huaweicloudsdkaom==3.1.128',
    'huaweicloudsdkaos==3.1.128',
    'huaweicloudsdkapig==3.1.128',
    'huaweicloudsdkapm==3.1.128',
    'huaweicloudsdkas==3.1.128',
    'huaweicloudsdkasm==3.1.128',
    'huaweicloudsdkbcs==3.1.128',
    'huaweicloudsdkbms==3.1.128',
    'huaweicloudsdkbss==3.1.128',
    'huaweicloudsdkbssintl==3.1.128',
    'huaweicloudsdkcae==3.1.128',
    'huaweicloudsdkcampusgo==3.1.128',
    'huaweicloudsdkcbh==3.1.128',
    'huaweicloudsdkcbr==3.1.128',
    'huaweicloudsdkcbs==3.1.128',
    'huaweicloudsdkcc==3.1.128',
    'huaweicloudsdkcce==3.1.128',
    'huaweicloudsdkccm==3.1.128',
    'huaweicloudsdkcdm==3.1.128',
    'huaweicloudsdkcdn==3.1.128',
    'huaweicloudsdkces==3.1.128',
    'huaweicloudsdkcfw==3.1.128',
    'huaweicloudsdkcgs==3.1.128',
    'huaweicloudsdkclassroom==3.1.128',
    'huaweicloudsdkcloudide==3.1.128',
    'huaweicloudsdkcloudpond==3.1.128',
    'huaweicloudsdkcloudrtc==3.1.128',
    'huaweicloudsdkcloudtable==3.1.128',
    'huaweicloudsdkcloudtest==3.1.128',
    'huaweicloudsdkcoc==3.1.128',
    'huaweicloudsdkcodeartsartifact==3.1.128',
    'huaweicloudsdkcodeartsbuild==3.1.128',
    'huaweicloudsdkcodeartscheck==3.1.128',
    'huaweicloudsdkcodeartsdeploy==3.1.128',
    'huaweicloudsdkcodeartsgovernance==3.1.128',
    'huaweicloudsdkcodeartsinspector==3.1.128',
    'huaweicloudsdkcodeartspipeline==3.1.128',
    'huaweicloudsdkcodecraft==3.1.128',
    'huaweicloudsdkcodehub==3.1.128',
    'huaweicloudsdkconfig==3.1.128',
    'huaweicloudsdkcph==3.1.128',
    'huaweicloudsdkcpts==3.1.128',
    'huaweicloudsdkcse==3.1.128',
    'huaweicloudsdkcsms==3.1.128',
    'huaweicloudsdkcss==3.1.128',
    'huaweicloudsdkcts==3.1.128',
    'huaweicloudsdkdas==3.1.128',
    'huaweicloudsdkdataartsfabric==3.1.128',
    'huaweicloudsdkdataartsfabricep==3.1.128',
    'huaweicloudsdkdataartsstudio==3.1.128',
    'huaweicloudsdkdbss==3.1.128',
    'huaweicloudsdkdc==3.1.128',
    'huaweicloudsdkdcs==3.1.128',
    'huaweicloudsdkddm==3.1.128',
    'huaweicloudsdkdds==3.1.128',
    'huaweicloudsdkdeh==3.1.128',
    'huaweicloudsdkdevstar==3.1.128',
    'huaweicloudsdkdgc==3.1.128',
    'huaweicloudsdkdis==3.1.128',
    'huaweicloudsdkdlf==3.1.128',
    'huaweicloudsdkdli==3.1.128',
    'huaweicloudsdkdns==3.1.128',
    'huaweicloudsdkdris==3.1.128',
    'huaweicloudsdkdrs==3.1.128',
    'huaweicloudsdkdsc==3.1.128',
    'huaweicloudsdkdwr==3.1.128',
    'huaweicloudsdkdws==3.1.128',
    'huaweicloudsdkec==3.1.128',
    'huaweicloudsdkecs==3.1.128',
    'huaweicloudsdkedgesec==3.1.128',
    'huaweicloudsdkeg==3.1.128',
    'huaweicloudsdkeihealth==3.1.128',
    'huaweicloudsdkeip==3.1.128',
    'huaweicloudsdkelb==3.1.128',
    'huaweicloudsdkeps==3.1.128',
    'huaweicloudsdker==3.1.128',
    'huaweicloudsdkevs==3.1.128',
    'huaweicloudsdkfrs==3.1.128',
    'huaweicloudsdkfunctiongraph==3.1.128',
    'huaweicloudsdkga==3.1.128',
    'huaweicloudsdkgaussdb==3.1.128',
    'huaweicloudsdkgaussdbfornosql==3.1.128',
    'huaweicloudsdkgaussdbforopengauss==3.1.128',
    'huaweicloudsdkgeip==3.1.128',
    'huaweicloudsdkges==3.1.128',
    'huaweicloudsdkgsl==3.1.128',
    'huaweicloudsdkhilens==3.1.128',
    'huaweicloudsdkhss==3.1.128',
    'huaweicloudsdkiam==3.1.128',
    'huaweicloudsdkiamaccessanalyzer==3.1.128',
    'huaweicloudsdkidentitycenter==3.1.128',
    'huaweicloudsdkidentitycenterstore==3.1.128',
    'huaweicloudsdkidme==3.1.128',
    'huaweicloudsdkidmeclassicapi==3.1.128',
    'huaweicloudsdkiec==3.1.128',
    'huaweicloudsdkief==3.1.128',
    'huaweicloudsdkimage==3.1.128',
    'huaweicloudsdkimagesearch==3.1.128',
    'huaweicloudsdkims==3.1.128',
    'huaweicloudsdkiotanalytics==3.1.128',
    'huaweicloudsdkiotda==3.1.128',
    'huaweicloudsdkiotdm==3.1.128',
    'huaweicloudsdkiotedge==3.1.128',
    'huaweicloudsdkivs==3.1.128',
    'huaweicloudsdkkafka==3.1.128',
    'huaweicloudsdkkms==3.1.128',
    'huaweicloudsdkkoomessage==3.1.128',
    'huaweicloudsdkkps==3.1.128',
    'huaweicloudsdklakeformation==3.1.128',
    'huaweicloudsdklive==3.1.128',
    'huaweicloudsdklts==3.1.128',
    'huaweicloudsdkmapds==3.1.128',
    'huaweicloudsdkmas==3.1.128',
    'huaweicloudsdkmastudio==3.1.128',
    'huaweicloudsdkmeeting==3.1.128',
    'huaweicloudsdkmetastudio==3.1.128',
    'huaweicloudsdkmoderation==3.1.128',
    'huaweicloudsdkmpc==3.1.128',
    'huaweicloudsdkmrs==3.1.128',
    'huaweicloudsdkmsgsms==3.1.128',
    'huaweicloudsdkmssi==3.1.128',
    'huaweicloudsdknat==3.1.128',
    'huaweicloudsdknlp==3.1.128',
    'huaweicloudsdkobs==3.1.128',
    'huaweicloudsdkocr==3.1.128',
    'huaweicloudsdkoctopus==3.1.128',
    'huaweicloudsdkoms==3.1.128',
    'huaweicloudsdkoptverse==3.1.128',
    'huaweicloudsdkorganizations==3.1.128',
    'huaweicloudsdkorgid==3.1.128',
    'huaweicloudsdkoroas==3.1.128',
    'huaweicloudsdkosm==3.1.128',
    'huaweicloudsdkpangulargemodels==3.1.128',
    'huaweicloudsdkprojectman==3.1.128',
    'huaweicloudsdkrabbitmq==3.1.128',
    'huaweicloudsdkram==3.1.128',
    'huaweicloudsdkrds==3.1.128',
    'huaweicloudsdkres==3.1.128',
    'huaweicloudsdkrgc==3.1.128',
    'huaweicloudsdkrms==3.1.128',
    'huaweicloudsdkrocketmq==3.1.128',
    'huaweicloudsdkroma==3.1.128',
    'huaweicloudsdksa==3.1.128',
    'huaweicloudsdkscm==3.1.128',
    'huaweicloudsdksdrs==3.1.128',
    'huaweicloudsdksecmaster==3.1.128',
    'huaweicloudsdkservicestage==3.1.128',
    'huaweicloudsdksfsturbo==3.1.128',
    'huaweicloudsdksis==3.1.128',
    'huaweicloudsdksmn==3.1.128',
    'huaweicloudsdksms==3.1.128',
    'huaweicloudsdksmsapi==3.1.128',
    'huaweicloudsdksts==3.1.128',
    'huaweicloudsdkswr==3.1.128',
    'huaweicloudsdktics==3.1.128',
    'huaweicloudsdktms==3.1.128',
    'huaweicloudsdkugo==3.1.128',
    'huaweicloudsdkvas==3.1.128',
    'huaweicloudsdkvcm==3.1.128',
    'huaweicloudsdkvod==3.1.128',
    'huaweicloudsdkvpc==3.1.128',
    'huaweicloudsdkvpcep==3.1.128',
    'huaweicloudsdkvpn==3.1.128',
    'huaweicloudsdkwaf==3.1.128',
    'huaweicloudsdkworkspace==3.1.128',
    'huaweicloudsdkworkspaceapp==3.1.128',
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
