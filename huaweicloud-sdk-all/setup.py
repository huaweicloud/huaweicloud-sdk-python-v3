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
VERSION = "3.1.132"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.132',
    'huaweicloudsdkaad==3.1.132',
    'huaweicloudsdkantiddos==3.1.132',
    'huaweicloudsdkaom==3.1.132',
    'huaweicloudsdkaos==3.1.132',
    'huaweicloudsdkapig==3.1.132',
    'huaweicloudsdkapm==3.1.132',
    'huaweicloudsdkas==3.1.132',
    'huaweicloudsdkasm==3.1.132',
    'huaweicloudsdkbcs==3.1.132',
    'huaweicloudsdkbms==3.1.132',
    'huaweicloudsdkbss==3.1.132',
    'huaweicloudsdkbssintl==3.1.132',
    'huaweicloudsdkcae==3.1.132',
    'huaweicloudsdkcampusgo==3.1.132',
    'huaweicloudsdkcbh==3.1.132',
    'huaweicloudsdkcbr==3.1.132',
    'huaweicloudsdkcbs==3.1.132',
    'huaweicloudsdkcc==3.1.132',
    'huaweicloudsdkcce==3.1.132',
    'huaweicloudsdkccm==3.1.132',
    'huaweicloudsdkcdm==3.1.132',
    'huaweicloudsdkcdn==3.1.132',
    'huaweicloudsdkces==3.1.132',
    'huaweicloudsdkcfw==3.1.132',
    'huaweicloudsdkcgs==3.1.132',
    'huaweicloudsdkclassroom==3.1.132',
    'huaweicloudsdkcloudide==3.1.132',
    'huaweicloudsdkcloudpond==3.1.132',
    'huaweicloudsdkcloudrtc==3.1.132',
    'huaweicloudsdkcloudtable==3.1.132',
    'huaweicloudsdkcloudtest==3.1.132',
    'huaweicloudsdkcoc==3.1.132',
    'huaweicloudsdkcodeartsartifact==3.1.132',
    'huaweicloudsdkcodeartsbuild==3.1.132',
    'huaweicloudsdkcodeartscheck==3.1.132',
    'huaweicloudsdkcodeartsdeploy==3.1.132',
    'huaweicloudsdkcodeartsgovernance==3.1.132',
    'huaweicloudsdkcodeartsinspector==3.1.132',
    'huaweicloudsdkcodeartspipeline==3.1.132',
    'huaweicloudsdkcodecraft==3.1.132',
    'huaweicloudsdkcodehub==3.1.132',
    'huaweicloudsdkconfig==3.1.132',
    'huaweicloudsdkcph==3.1.132',
    'huaweicloudsdkcpts==3.1.132',
    'huaweicloudsdkcse==3.1.132',
    'huaweicloudsdkcsms==3.1.132',
    'huaweicloudsdkcss==3.1.132',
    'huaweicloudsdkcts==3.1.132',
    'huaweicloudsdkdas==3.1.132',
    'huaweicloudsdkdataartsfabric==3.1.132',
    'huaweicloudsdkdataartsfabricep==3.1.132',
    'huaweicloudsdkdataartsstudio==3.1.132',
    'huaweicloudsdkdbss==3.1.132',
    'huaweicloudsdkdc==3.1.132',
    'huaweicloudsdkdcs==3.1.132',
    'huaweicloudsdkddm==3.1.132',
    'huaweicloudsdkdds==3.1.132',
    'huaweicloudsdkdeh==3.1.132',
    'huaweicloudsdkdevstar==3.1.132',
    'huaweicloudsdkdgc==3.1.132',
    'huaweicloudsdkdis==3.1.132',
    'huaweicloudsdkdlf==3.1.132',
    'huaweicloudsdkdli==3.1.132',
    'huaweicloudsdkdns==3.1.132',
    'huaweicloudsdkdris==3.1.132',
    'huaweicloudsdkdrs==3.1.132',
    'huaweicloudsdkdsc==3.1.132',
    'huaweicloudsdkdwr==3.1.132',
    'huaweicloudsdkdws==3.1.132',
    'huaweicloudsdkec==3.1.132',
    'huaweicloudsdkecs==3.1.132',
    'huaweicloudsdkedgesec==3.1.132',
    'huaweicloudsdkeg==3.1.132',
    'huaweicloudsdkeihealth==3.1.132',
    'huaweicloudsdkeip==3.1.132',
    'huaweicloudsdkelb==3.1.132',
    'huaweicloudsdkeps==3.1.132',
    'huaweicloudsdker==3.1.132',
    'huaweicloudsdkevs==3.1.132',
    'huaweicloudsdkfrs==3.1.132',
    'huaweicloudsdkfunctiongraph==3.1.132',
    'huaweicloudsdkga==3.1.132',
    'huaweicloudsdkgaussdb==3.1.132',
    'huaweicloudsdkgaussdbfornosql==3.1.132',
    'huaweicloudsdkgaussdbforopengauss==3.1.132',
    'huaweicloudsdkgeip==3.1.132',
    'huaweicloudsdkges==3.1.132',
    'huaweicloudsdkgsl==3.1.132',
    'huaweicloudsdkhilens==3.1.132',
    'huaweicloudsdkhss==3.1.132',
    'huaweicloudsdkiam==3.1.132',
    'huaweicloudsdkiamaccessanalyzer==3.1.132',
    'huaweicloudsdkidentitycenter==3.1.132',
    'huaweicloudsdkidentitycenterstore==3.1.132',
    'huaweicloudsdkidme==3.1.132',
    'huaweicloudsdkidmeclassicapi==3.1.132',
    'huaweicloudsdkiec==3.1.132',
    'huaweicloudsdkief==3.1.132',
    'huaweicloudsdkimage==3.1.132',
    'huaweicloudsdkimagesearch==3.1.132',
    'huaweicloudsdkims==3.1.132',
    'huaweicloudsdkiotanalytics==3.1.132',
    'huaweicloudsdkiotda==3.1.132',
    'huaweicloudsdkiotdm==3.1.132',
    'huaweicloudsdkiotedge==3.1.132',
    'huaweicloudsdkivs==3.1.132',
    'huaweicloudsdkkafka==3.1.132',
    'huaweicloudsdkkms==3.1.132',
    'huaweicloudsdkkoomessage==3.1.132',
    'huaweicloudsdkkps==3.1.132',
    'huaweicloudsdklakeformation==3.1.132',
    'huaweicloudsdklive==3.1.132',
    'huaweicloudsdklts==3.1.132',
    'huaweicloudsdkmapds==3.1.132',
    'huaweicloudsdkmas==3.1.132',
    'huaweicloudsdkmastudio==3.1.132',
    'huaweicloudsdkmeeting==3.1.132',
    'huaweicloudsdkmetastudio==3.1.132',
    'huaweicloudsdkmoderation==3.1.132',
    'huaweicloudsdkmpc==3.1.132',
    'huaweicloudsdkmrs==3.1.132',
    'huaweicloudsdkmsgsms==3.1.132',
    'huaweicloudsdkmssi==3.1.132',
    'huaweicloudsdknat==3.1.132',
    'huaweicloudsdknlp==3.1.132',
    'huaweicloudsdkobs==3.1.132',
    'huaweicloudsdkocr==3.1.132',
    'huaweicloudsdkoctopus==3.1.132',
    'huaweicloudsdkoms==3.1.132',
    'huaweicloudsdkoptverse==3.1.132',
    'huaweicloudsdkorganizations==3.1.132',
    'huaweicloudsdkorgid==3.1.132',
    'huaweicloudsdkoroas==3.1.132',
    'huaweicloudsdkosm==3.1.132',
    'huaweicloudsdkpangulargemodels==3.1.132',
    'huaweicloudsdkprojectman==3.1.132',
    'huaweicloudsdkrabbitmq==3.1.132',
    'huaweicloudsdkram==3.1.132',
    'huaweicloudsdkrds==3.1.132',
    'huaweicloudsdkres==3.1.132',
    'huaweicloudsdkrgc==3.1.132',
    'huaweicloudsdkrms==3.1.132',
    'huaweicloudsdkrocketmq==3.1.132',
    'huaweicloudsdkroma==3.1.132',
    'huaweicloudsdksa==3.1.132',
    'huaweicloudsdkscm==3.1.132',
    'huaweicloudsdksdrs==3.1.132',
    'huaweicloudsdksecmaster==3.1.132',
    'huaweicloudsdkservicestage==3.1.132',
    'huaweicloudsdksfsturbo==3.1.132',
    'huaweicloudsdksis==3.1.132',
    'huaweicloudsdksmn==3.1.132',
    'huaweicloudsdksms==3.1.132',
    'huaweicloudsdksmsapi==3.1.132',
    'huaweicloudsdksts==3.1.132',
    'huaweicloudsdkswr==3.1.132',
    'huaweicloudsdktics==3.1.132',
    'huaweicloudsdktms==3.1.132',
    'huaweicloudsdkugo==3.1.132',
    'huaweicloudsdkvas==3.1.132',
    'huaweicloudsdkvcm==3.1.132',
    'huaweicloudsdkvod==3.1.132',
    'huaweicloudsdkvpc==3.1.132',
    'huaweicloudsdkvpcep==3.1.132',
    'huaweicloudsdkvpn==3.1.132',
    'huaweicloudsdkwaf==3.1.132',
    'huaweicloudsdkworkspace==3.1.132',
    'huaweicloudsdkworkspaceapp==3.1.132',
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
