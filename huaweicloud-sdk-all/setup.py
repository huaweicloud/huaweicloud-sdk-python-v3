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
VERSION = "3.1.130"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.130',
    'huaweicloudsdkaad==3.1.130',
    'huaweicloudsdkantiddos==3.1.130',
    'huaweicloudsdkaom==3.1.130',
    'huaweicloudsdkaos==3.1.130',
    'huaweicloudsdkapig==3.1.130',
    'huaweicloudsdkapm==3.1.130',
    'huaweicloudsdkas==3.1.130',
    'huaweicloudsdkasm==3.1.130',
    'huaweicloudsdkbcs==3.1.130',
    'huaweicloudsdkbms==3.1.130',
    'huaweicloudsdkbss==3.1.130',
    'huaweicloudsdkbssintl==3.1.130',
    'huaweicloudsdkcae==3.1.130',
    'huaweicloudsdkcampusgo==3.1.130',
    'huaweicloudsdkcbh==3.1.130',
    'huaweicloudsdkcbr==3.1.130',
    'huaweicloudsdkcbs==3.1.130',
    'huaweicloudsdkcc==3.1.130',
    'huaweicloudsdkcce==3.1.130',
    'huaweicloudsdkccm==3.1.130',
    'huaweicloudsdkcdm==3.1.130',
    'huaweicloudsdkcdn==3.1.130',
    'huaweicloudsdkces==3.1.130',
    'huaweicloudsdkcfw==3.1.130',
    'huaweicloudsdkcgs==3.1.130',
    'huaweicloudsdkclassroom==3.1.130',
    'huaweicloudsdkcloudide==3.1.130',
    'huaweicloudsdkcloudpond==3.1.130',
    'huaweicloudsdkcloudrtc==3.1.130',
    'huaweicloudsdkcloudtable==3.1.130',
    'huaweicloudsdkcloudtest==3.1.130',
    'huaweicloudsdkcoc==3.1.130',
    'huaweicloudsdkcodeartsartifact==3.1.130',
    'huaweicloudsdkcodeartsbuild==3.1.130',
    'huaweicloudsdkcodeartscheck==3.1.130',
    'huaweicloudsdkcodeartsdeploy==3.1.130',
    'huaweicloudsdkcodeartsgovernance==3.1.130',
    'huaweicloudsdkcodeartsinspector==3.1.130',
    'huaweicloudsdkcodeartspipeline==3.1.130',
    'huaweicloudsdkcodecraft==3.1.130',
    'huaweicloudsdkcodehub==3.1.130',
    'huaweicloudsdkconfig==3.1.130',
    'huaweicloudsdkcph==3.1.130',
    'huaweicloudsdkcpts==3.1.130',
    'huaweicloudsdkcse==3.1.130',
    'huaweicloudsdkcsms==3.1.130',
    'huaweicloudsdkcss==3.1.130',
    'huaweicloudsdkcts==3.1.130',
    'huaweicloudsdkdas==3.1.130',
    'huaweicloudsdkdataartsfabric==3.1.130',
    'huaweicloudsdkdataartsfabricep==3.1.130',
    'huaweicloudsdkdataartsstudio==3.1.130',
    'huaweicloudsdkdbss==3.1.130',
    'huaweicloudsdkdc==3.1.130',
    'huaweicloudsdkdcs==3.1.130',
    'huaweicloudsdkddm==3.1.130',
    'huaweicloudsdkdds==3.1.130',
    'huaweicloudsdkdeh==3.1.130',
    'huaweicloudsdkdevstar==3.1.130',
    'huaweicloudsdkdgc==3.1.130',
    'huaweicloudsdkdis==3.1.130',
    'huaweicloudsdkdlf==3.1.130',
    'huaweicloudsdkdli==3.1.130',
    'huaweicloudsdkdns==3.1.130',
    'huaweicloudsdkdris==3.1.130',
    'huaweicloudsdkdrs==3.1.130',
    'huaweicloudsdkdsc==3.1.130',
    'huaweicloudsdkdwr==3.1.130',
    'huaweicloudsdkdws==3.1.130',
    'huaweicloudsdkec==3.1.130',
    'huaweicloudsdkecs==3.1.130',
    'huaweicloudsdkedgesec==3.1.130',
    'huaweicloudsdkeg==3.1.130',
    'huaweicloudsdkeihealth==3.1.130',
    'huaweicloudsdkeip==3.1.130',
    'huaweicloudsdkelb==3.1.130',
    'huaweicloudsdkeps==3.1.130',
    'huaweicloudsdker==3.1.130',
    'huaweicloudsdkevs==3.1.130',
    'huaweicloudsdkfrs==3.1.130',
    'huaweicloudsdkfunctiongraph==3.1.130',
    'huaweicloudsdkga==3.1.130',
    'huaweicloudsdkgaussdb==3.1.130',
    'huaweicloudsdkgaussdbfornosql==3.1.130',
    'huaweicloudsdkgaussdbforopengauss==3.1.130',
    'huaweicloudsdkgeip==3.1.130',
    'huaweicloudsdkges==3.1.130',
    'huaweicloudsdkgsl==3.1.130',
    'huaweicloudsdkhilens==3.1.130',
    'huaweicloudsdkhss==3.1.130',
    'huaweicloudsdkiam==3.1.130',
    'huaweicloudsdkiamaccessanalyzer==3.1.130',
    'huaweicloudsdkidentitycenter==3.1.130',
    'huaweicloudsdkidentitycenterstore==3.1.130',
    'huaweicloudsdkidme==3.1.130',
    'huaweicloudsdkidmeclassicapi==3.1.130',
    'huaweicloudsdkiec==3.1.130',
    'huaweicloudsdkief==3.1.130',
    'huaweicloudsdkimage==3.1.130',
    'huaweicloudsdkimagesearch==3.1.130',
    'huaweicloudsdkims==3.1.130',
    'huaweicloudsdkiotanalytics==3.1.130',
    'huaweicloudsdkiotda==3.1.130',
    'huaweicloudsdkiotdm==3.1.130',
    'huaweicloudsdkiotedge==3.1.130',
    'huaweicloudsdkivs==3.1.130',
    'huaweicloudsdkkafka==3.1.130',
    'huaweicloudsdkkms==3.1.130',
    'huaweicloudsdkkoomessage==3.1.130',
    'huaweicloudsdkkps==3.1.130',
    'huaweicloudsdklakeformation==3.1.130',
    'huaweicloudsdklive==3.1.130',
    'huaweicloudsdklts==3.1.130',
    'huaweicloudsdkmapds==3.1.130',
    'huaweicloudsdkmas==3.1.130',
    'huaweicloudsdkmastudio==3.1.130',
    'huaweicloudsdkmeeting==3.1.130',
    'huaweicloudsdkmetastudio==3.1.130',
    'huaweicloudsdkmoderation==3.1.130',
    'huaweicloudsdkmpc==3.1.130',
    'huaweicloudsdkmrs==3.1.130',
    'huaweicloudsdkmsgsms==3.1.130',
    'huaweicloudsdkmssi==3.1.130',
    'huaweicloudsdknat==3.1.130',
    'huaweicloudsdknlp==3.1.130',
    'huaweicloudsdkobs==3.1.130',
    'huaweicloudsdkocr==3.1.130',
    'huaweicloudsdkoctopus==3.1.130',
    'huaweicloudsdkoms==3.1.130',
    'huaweicloudsdkoptverse==3.1.130',
    'huaweicloudsdkorganizations==3.1.130',
    'huaweicloudsdkorgid==3.1.130',
    'huaweicloudsdkoroas==3.1.130',
    'huaweicloudsdkosm==3.1.130',
    'huaweicloudsdkpangulargemodels==3.1.130',
    'huaweicloudsdkprojectman==3.1.130',
    'huaweicloudsdkrabbitmq==3.1.130',
    'huaweicloudsdkram==3.1.130',
    'huaweicloudsdkrds==3.1.130',
    'huaweicloudsdkres==3.1.130',
    'huaweicloudsdkrgc==3.1.130',
    'huaweicloudsdkrms==3.1.130',
    'huaweicloudsdkrocketmq==3.1.130',
    'huaweicloudsdkroma==3.1.130',
    'huaweicloudsdksa==3.1.130',
    'huaweicloudsdkscm==3.1.130',
    'huaweicloudsdksdrs==3.1.130',
    'huaweicloudsdksecmaster==3.1.130',
    'huaweicloudsdkservicestage==3.1.130',
    'huaweicloudsdksfsturbo==3.1.130',
    'huaweicloudsdksis==3.1.130',
    'huaweicloudsdksmn==3.1.130',
    'huaweicloudsdksms==3.1.130',
    'huaweicloudsdksmsapi==3.1.130',
    'huaweicloudsdksts==3.1.130',
    'huaweicloudsdkswr==3.1.130',
    'huaweicloudsdktics==3.1.130',
    'huaweicloudsdktms==3.1.130',
    'huaweicloudsdkugo==3.1.130',
    'huaweicloudsdkvas==3.1.130',
    'huaweicloudsdkvcm==3.1.130',
    'huaweicloudsdkvod==3.1.130',
    'huaweicloudsdkvpc==3.1.130',
    'huaweicloudsdkvpcep==3.1.130',
    'huaweicloudsdkvpn==3.1.130',
    'huaweicloudsdkwaf==3.1.130',
    'huaweicloudsdkworkspace==3.1.130',
    'huaweicloudsdkworkspaceapp==3.1.130',
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
