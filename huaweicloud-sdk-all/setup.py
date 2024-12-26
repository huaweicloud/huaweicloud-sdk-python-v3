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
VERSION = "3.1.129"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.129',
    'huaweicloudsdkaad==3.1.129',
    'huaweicloudsdkantiddos==3.1.129',
    'huaweicloudsdkaom==3.1.129',
    'huaweicloudsdkaos==3.1.129',
    'huaweicloudsdkapig==3.1.129',
    'huaweicloudsdkapm==3.1.129',
    'huaweicloudsdkas==3.1.129',
    'huaweicloudsdkasm==3.1.129',
    'huaweicloudsdkbcs==3.1.129',
    'huaweicloudsdkbms==3.1.129',
    'huaweicloudsdkbss==3.1.129',
    'huaweicloudsdkbssintl==3.1.129',
    'huaweicloudsdkcae==3.1.129',
    'huaweicloudsdkcampusgo==3.1.129',
    'huaweicloudsdkcbh==3.1.129',
    'huaweicloudsdkcbr==3.1.129',
    'huaweicloudsdkcbs==3.1.129',
    'huaweicloudsdkcc==3.1.129',
    'huaweicloudsdkcce==3.1.129',
    'huaweicloudsdkccm==3.1.129',
    'huaweicloudsdkcdm==3.1.129',
    'huaweicloudsdkcdn==3.1.129',
    'huaweicloudsdkces==3.1.129',
    'huaweicloudsdkcfw==3.1.129',
    'huaweicloudsdkcgs==3.1.129',
    'huaweicloudsdkclassroom==3.1.129',
    'huaweicloudsdkcloudide==3.1.129',
    'huaweicloudsdkcloudpond==3.1.129',
    'huaweicloudsdkcloudrtc==3.1.129',
    'huaweicloudsdkcloudtable==3.1.129',
    'huaweicloudsdkcloudtest==3.1.129',
    'huaweicloudsdkcoc==3.1.129',
    'huaweicloudsdkcodeartsartifact==3.1.129',
    'huaweicloudsdkcodeartsbuild==3.1.129',
    'huaweicloudsdkcodeartscheck==3.1.129',
    'huaweicloudsdkcodeartsdeploy==3.1.129',
    'huaweicloudsdkcodeartsgovernance==3.1.129',
    'huaweicloudsdkcodeartsinspector==3.1.129',
    'huaweicloudsdkcodeartspipeline==3.1.129',
    'huaweicloudsdkcodecraft==3.1.129',
    'huaweicloudsdkcodehub==3.1.129',
    'huaweicloudsdkconfig==3.1.129',
    'huaweicloudsdkcph==3.1.129',
    'huaweicloudsdkcpts==3.1.129',
    'huaweicloudsdkcse==3.1.129',
    'huaweicloudsdkcsms==3.1.129',
    'huaweicloudsdkcss==3.1.129',
    'huaweicloudsdkcts==3.1.129',
    'huaweicloudsdkdas==3.1.129',
    'huaweicloudsdkdataartsfabric==3.1.129',
    'huaweicloudsdkdataartsfabricep==3.1.129',
    'huaweicloudsdkdataartsstudio==3.1.129',
    'huaweicloudsdkdbss==3.1.129',
    'huaweicloudsdkdc==3.1.129',
    'huaweicloudsdkdcs==3.1.129',
    'huaweicloudsdkddm==3.1.129',
    'huaweicloudsdkdds==3.1.129',
    'huaweicloudsdkdeh==3.1.129',
    'huaweicloudsdkdevstar==3.1.129',
    'huaweicloudsdkdgc==3.1.129',
    'huaweicloudsdkdis==3.1.129',
    'huaweicloudsdkdlf==3.1.129',
    'huaweicloudsdkdli==3.1.129',
    'huaweicloudsdkdns==3.1.129',
    'huaweicloudsdkdris==3.1.129',
    'huaweicloudsdkdrs==3.1.129',
    'huaweicloudsdkdsc==3.1.129',
    'huaweicloudsdkdwr==3.1.129',
    'huaweicloudsdkdws==3.1.129',
    'huaweicloudsdkec==3.1.129',
    'huaweicloudsdkecs==3.1.129',
    'huaweicloudsdkedgesec==3.1.129',
    'huaweicloudsdkeg==3.1.129',
    'huaweicloudsdkeihealth==3.1.129',
    'huaweicloudsdkeip==3.1.129',
    'huaweicloudsdkelb==3.1.129',
    'huaweicloudsdkeps==3.1.129',
    'huaweicloudsdker==3.1.129',
    'huaweicloudsdkevs==3.1.129',
    'huaweicloudsdkfrs==3.1.129',
    'huaweicloudsdkfunctiongraph==3.1.129',
    'huaweicloudsdkga==3.1.129',
    'huaweicloudsdkgaussdb==3.1.129',
    'huaweicloudsdkgaussdbfornosql==3.1.129',
    'huaweicloudsdkgaussdbforopengauss==3.1.129',
    'huaweicloudsdkgeip==3.1.129',
    'huaweicloudsdkges==3.1.129',
    'huaweicloudsdkgsl==3.1.129',
    'huaweicloudsdkhilens==3.1.129',
    'huaweicloudsdkhss==3.1.129',
    'huaweicloudsdkiam==3.1.129',
    'huaweicloudsdkiamaccessanalyzer==3.1.129',
    'huaweicloudsdkidentitycenter==3.1.129',
    'huaweicloudsdkidentitycenterstore==3.1.129',
    'huaweicloudsdkidme==3.1.129',
    'huaweicloudsdkidmeclassicapi==3.1.129',
    'huaweicloudsdkiec==3.1.129',
    'huaweicloudsdkief==3.1.129',
    'huaweicloudsdkimage==3.1.129',
    'huaweicloudsdkimagesearch==3.1.129',
    'huaweicloudsdkims==3.1.129',
    'huaweicloudsdkiotanalytics==3.1.129',
    'huaweicloudsdkiotda==3.1.129',
    'huaweicloudsdkiotdm==3.1.129',
    'huaweicloudsdkiotedge==3.1.129',
    'huaweicloudsdkivs==3.1.129',
    'huaweicloudsdkkafka==3.1.129',
    'huaweicloudsdkkms==3.1.129',
    'huaweicloudsdkkoomessage==3.1.129',
    'huaweicloudsdkkps==3.1.129',
    'huaweicloudsdklakeformation==3.1.129',
    'huaweicloudsdklive==3.1.129',
    'huaweicloudsdklts==3.1.129',
    'huaweicloudsdkmapds==3.1.129',
    'huaweicloudsdkmas==3.1.129',
    'huaweicloudsdkmastudio==3.1.129',
    'huaweicloudsdkmeeting==3.1.129',
    'huaweicloudsdkmetastudio==3.1.129',
    'huaweicloudsdkmoderation==3.1.129',
    'huaweicloudsdkmpc==3.1.129',
    'huaweicloudsdkmrs==3.1.129',
    'huaweicloudsdkmsgsms==3.1.129',
    'huaweicloudsdkmssi==3.1.129',
    'huaweicloudsdknat==3.1.129',
    'huaweicloudsdknlp==3.1.129',
    'huaweicloudsdkobs==3.1.129',
    'huaweicloudsdkocr==3.1.129',
    'huaweicloudsdkoctopus==3.1.129',
    'huaweicloudsdkoms==3.1.129',
    'huaweicloudsdkoptverse==3.1.129',
    'huaweicloudsdkorganizations==3.1.129',
    'huaweicloudsdkorgid==3.1.129',
    'huaweicloudsdkoroas==3.1.129',
    'huaweicloudsdkosm==3.1.129',
    'huaweicloudsdkpangulargemodels==3.1.129',
    'huaweicloudsdkprojectman==3.1.129',
    'huaweicloudsdkrabbitmq==3.1.129',
    'huaweicloudsdkram==3.1.129',
    'huaweicloudsdkrds==3.1.129',
    'huaweicloudsdkres==3.1.129',
    'huaweicloudsdkrgc==3.1.129',
    'huaweicloudsdkrms==3.1.129',
    'huaweicloudsdkrocketmq==3.1.129',
    'huaweicloudsdkroma==3.1.129',
    'huaweicloudsdksa==3.1.129',
    'huaweicloudsdkscm==3.1.129',
    'huaweicloudsdksdrs==3.1.129',
    'huaweicloudsdksecmaster==3.1.129',
    'huaweicloudsdkservicestage==3.1.129',
    'huaweicloudsdksfsturbo==3.1.129',
    'huaweicloudsdksis==3.1.129',
    'huaweicloudsdksmn==3.1.129',
    'huaweicloudsdksms==3.1.129',
    'huaweicloudsdksmsapi==3.1.129',
    'huaweicloudsdksts==3.1.129',
    'huaweicloudsdkswr==3.1.129',
    'huaweicloudsdktics==3.1.129',
    'huaweicloudsdktms==3.1.129',
    'huaweicloudsdkugo==3.1.129',
    'huaweicloudsdkvas==3.1.129',
    'huaweicloudsdkvcm==3.1.129',
    'huaweicloudsdkvod==3.1.129',
    'huaweicloudsdkvpc==3.1.129',
    'huaweicloudsdkvpcep==3.1.129',
    'huaweicloudsdkvpn==3.1.129',
    'huaweicloudsdkwaf==3.1.129',
    'huaweicloudsdkworkspace==3.1.129',
    'huaweicloudsdkworkspaceapp==3.1.129',
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
