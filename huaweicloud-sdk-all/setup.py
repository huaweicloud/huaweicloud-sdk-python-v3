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
VERSION = "3.1.126"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.126',
    'huaweicloudsdkaad==3.1.126',
    'huaweicloudsdkantiddos==3.1.126',
    'huaweicloudsdkaom==3.1.126',
    'huaweicloudsdkaos==3.1.126',
    'huaweicloudsdkapig==3.1.126',
    'huaweicloudsdkapm==3.1.126',
    'huaweicloudsdkas==3.1.126',
    'huaweicloudsdkasm==3.1.126',
    'huaweicloudsdkbcs==3.1.126',
    'huaweicloudsdkbms==3.1.126',
    'huaweicloudsdkbss==3.1.126',
    'huaweicloudsdkbssintl==3.1.126',
    'huaweicloudsdkcae==3.1.126',
    'huaweicloudsdkcampusgo==3.1.126',
    'huaweicloudsdkcbh==3.1.126',
    'huaweicloudsdkcbr==3.1.126',
    'huaweicloudsdkcbs==3.1.126',
    'huaweicloudsdkcc==3.1.126',
    'huaweicloudsdkcce==3.1.126',
    'huaweicloudsdkccm==3.1.126',
    'huaweicloudsdkcdm==3.1.126',
    'huaweicloudsdkcdn==3.1.126',
    'huaweicloudsdkces==3.1.126',
    'huaweicloudsdkcfw==3.1.126',
    'huaweicloudsdkcgs==3.1.126',
    'huaweicloudsdkclassroom==3.1.126',
    'huaweicloudsdkcloudide==3.1.126',
    'huaweicloudsdkcloudpond==3.1.126',
    'huaweicloudsdkcloudrtc==3.1.126',
    'huaweicloudsdkcloudtable==3.1.126',
    'huaweicloudsdkcloudtest==3.1.126',
    'huaweicloudsdkcoc==3.1.126',
    'huaweicloudsdkcodeartsartifact==3.1.126',
    'huaweicloudsdkcodeartsbuild==3.1.126',
    'huaweicloudsdkcodeartscheck==3.1.126',
    'huaweicloudsdkcodeartsdeploy==3.1.126',
    'huaweicloudsdkcodeartsgovernance==3.1.126',
    'huaweicloudsdkcodeartsinspector==3.1.126',
    'huaweicloudsdkcodeartspipeline==3.1.126',
    'huaweicloudsdkcodecraft==3.1.126',
    'huaweicloudsdkcodehub==3.1.126',
    'huaweicloudsdkconfig==3.1.126',
    'huaweicloudsdkcph==3.1.126',
    'huaweicloudsdkcpts==3.1.126',
    'huaweicloudsdkcse==3.1.126',
    'huaweicloudsdkcsms==3.1.126',
    'huaweicloudsdkcss==3.1.126',
    'huaweicloudsdkcts==3.1.126',
    'huaweicloudsdkdas==3.1.126',
    'huaweicloudsdkdataartsfabric==3.1.126',
    'huaweicloudsdkdataartsfabricep==3.1.126',
    'huaweicloudsdkdataartsstudio==3.1.126',
    'huaweicloudsdkdbss==3.1.126',
    'huaweicloudsdkdc==3.1.126',
    'huaweicloudsdkdcs==3.1.126',
    'huaweicloudsdkddm==3.1.126',
    'huaweicloudsdkdds==3.1.126',
    'huaweicloudsdkdeh==3.1.126',
    'huaweicloudsdkdevstar==3.1.126',
    'huaweicloudsdkdgc==3.1.126',
    'huaweicloudsdkdis==3.1.126',
    'huaweicloudsdkdlf==3.1.126',
    'huaweicloudsdkdli==3.1.126',
    'huaweicloudsdkdns==3.1.126',
    'huaweicloudsdkdris==3.1.126',
    'huaweicloudsdkdrs==3.1.126',
    'huaweicloudsdkdsc==3.1.126',
    'huaweicloudsdkdwr==3.1.126',
    'huaweicloudsdkdws==3.1.126',
    'huaweicloudsdkec==3.1.126',
    'huaweicloudsdkecs==3.1.126',
    'huaweicloudsdkedgesec==3.1.126',
    'huaweicloudsdkeg==3.1.126',
    'huaweicloudsdkeihealth==3.1.126',
    'huaweicloudsdkeip==3.1.126',
    'huaweicloudsdkelb==3.1.126',
    'huaweicloudsdkeps==3.1.126',
    'huaweicloudsdker==3.1.126',
    'huaweicloudsdkevs==3.1.126',
    'huaweicloudsdkfrs==3.1.126',
    'huaweicloudsdkfunctiongraph==3.1.126',
    'huaweicloudsdkga==3.1.126',
    'huaweicloudsdkgaussdb==3.1.126',
    'huaweicloudsdkgaussdbfornosql==3.1.126',
    'huaweicloudsdkgaussdbforopengauss==3.1.126',
    'huaweicloudsdkgeip==3.1.126',
    'huaweicloudsdkges==3.1.126',
    'huaweicloudsdkgsl==3.1.126',
    'huaweicloudsdkhilens==3.1.126',
    'huaweicloudsdkhss==3.1.126',
    'huaweicloudsdkiam==3.1.126',
    'huaweicloudsdkiamaccessanalyzer==3.1.126',
    'huaweicloudsdkidentitycenter==3.1.126',
    'huaweicloudsdkidentitycenterstore==3.1.126',
    'huaweicloudsdkidme==3.1.126',
    'huaweicloudsdkidmeclassicapi==3.1.126',
    'huaweicloudsdkiec==3.1.126',
    'huaweicloudsdkief==3.1.126',
    'huaweicloudsdkimage==3.1.126',
    'huaweicloudsdkimagesearch==3.1.126',
    'huaweicloudsdkims==3.1.126',
    'huaweicloudsdkiotanalytics==3.1.126',
    'huaweicloudsdkiotda==3.1.126',
    'huaweicloudsdkiotdm==3.1.126',
    'huaweicloudsdkiotedge==3.1.126',
    'huaweicloudsdkivs==3.1.126',
    'huaweicloudsdkkafka==3.1.126',
    'huaweicloudsdkkms==3.1.126',
    'huaweicloudsdkkoomessage==3.1.126',
    'huaweicloudsdkkps==3.1.126',
    'huaweicloudsdklakeformation==3.1.126',
    'huaweicloudsdklive==3.1.126',
    'huaweicloudsdklts==3.1.126',
    'huaweicloudsdkmapds==3.1.126',
    'huaweicloudsdkmas==3.1.126',
    'huaweicloudsdkmastudio==3.1.126',
    'huaweicloudsdkmeeting==3.1.126',
    'huaweicloudsdkmetastudio==3.1.126',
    'huaweicloudsdkmoderation==3.1.126',
    'huaweicloudsdkmpc==3.1.126',
    'huaweicloudsdkmrs==3.1.126',
    'huaweicloudsdkmsgsms==3.1.126',
    'huaweicloudsdkmssi==3.1.126',
    'huaweicloudsdknat==3.1.126',
    'huaweicloudsdknlp==3.1.126',
    'huaweicloudsdkobs==3.1.126',
    'huaweicloudsdkocr==3.1.126',
    'huaweicloudsdkoctopus==3.1.126',
    'huaweicloudsdkoms==3.1.126',
    'huaweicloudsdkoptverse==3.1.126',
    'huaweicloudsdkorganizations==3.1.126',
    'huaweicloudsdkorgid==3.1.126',
    'huaweicloudsdkoroas==3.1.126',
    'huaweicloudsdkosm==3.1.126',
    'huaweicloudsdkpangulargemodels==3.1.126',
    'huaweicloudsdkprojectman==3.1.126',
    'huaweicloudsdkrabbitmq==3.1.126',
    'huaweicloudsdkram==3.1.126',
    'huaweicloudsdkrds==3.1.126',
    'huaweicloudsdkres==3.1.126',
    'huaweicloudsdkrgc==3.1.126',
    'huaweicloudsdkrms==3.1.126',
    'huaweicloudsdkrocketmq==3.1.126',
    'huaweicloudsdkroma==3.1.126',
    'huaweicloudsdksa==3.1.126',
    'huaweicloudsdkscm==3.1.126',
    'huaweicloudsdksdrs==3.1.126',
    'huaweicloudsdksecmaster==3.1.126',
    'huaweicloudsdkservicestage==3.1.126',
    'huaweicloudsdksfsturbo==3.1.126',
    'huaweicloudsdksis==3.1.126',
    'huaweicloudsdksmn==3.1.126',
    'huaweicloudsdksms==3.1.126',
    'huaweicloudsdksts==3.1.126',
    'huaweicloudsdkswr==3.1.126',
    'huaweicloudsdktics==3.1.126',
    'huaweicloudsdktms==3.1.126',
    'huaweicloudsdkugo==3.1.126',
    'huaweicloudsdkvas==3.1.126',
    'huaweicloudsdkvcm==3.1.126',
    'huaweicloudsdkvod==3.1.126',
    'huaweicloudsdkvpc==3.1.126',
    'huaweicloudsdkvpcep==3.1.126',
    'huaweicloudsdkvpn==3.1.126',
    'huaweicloudsdkwaf==3.1.126',
    'huaweicloudsdkworkspace==3.1.126',
    'huaweicloudsdkworkspaceapp==3.1.126',
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
