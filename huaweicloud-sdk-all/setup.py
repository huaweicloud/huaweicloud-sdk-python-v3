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
VERSION = "3.1.124"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.124',
    'huaweicloudsdkaad==3.1.124',
    'huaweicloudsdkantiddos==3.1.124',
    'huaweicloudsdkaom==3.1.124',
    'huaweicloudsdkaos==3.1.124',
    'huaweicloudsdkapig==3.1.124',
    'huaweicloudsdkapm==3.1.124',
    'huaweicloudsdkas==3.1.124',
    'huaweicloudsdkasm==3.1.124',
    'huaweicloudsdkbcs==3.1.124',
    'huaweicloudsdkbms==3.1.124',
    'huaweicloudsdkbss==3.1.124',
    'huaweicloudsdkbssintl==3.1.124',
    'huaweicloudsdkcae==3.1.124',
    'huaweicloudsdkcampusgo==3.1.124',
    'huaweicloudsdkcbh==3.1.124',
    'huaweicloudsdkcbr==3.1.124',
    'huaweicloudsdkcbs==3.1.124',
    'huaweicloudsdkcc==3.1.124',
    'huaweicloudsdkcce==3.1.124',
    'huaweicloudsdkccm==3.1.124',
    'huaweicloudsdkcdm==3.1.124',
    'huaweicloudsdkcdn==3.1.124',
    'huaweicloudsdkces==3.1.124',
    'huaweicloudsdkcfw==3.1.124',
    'huaweicloudsdkcgs==3.1.124',
    'huaweicloudsdkclassroom==3.1.124',
    'huaweicloudsdkcloudide==3.1.124',
    'huaweicloudsdkcloudpond==3.1.124',
    'huaweicloudsdkcloudrtc==3.1.124',
    'huaweicloudsdkcloudtable==3.1.124',
    'huaweicloudsdkcloudtest==3.1.124',
    'huaweicloudsdkcoc==3.1.124',
    'huaweicloudsdkcodeartsartifact==3.1.124',
    'huaweicloudsdkcodeartsbuild==3.1.124',
    'huaweicloudsdkcodeartscheck==3.1.124',
    'huaweicloudsdkcodeartsdeploy==3.1.124',
    'huaweicloudsdkcodeartsgovernance==3.1.124',
    'huaweicloudsdkcodeartsinspector==3.1.124',
    'huaweicloudsdkcodeartspipeline==3.1.124',
    'huaweicloudsdkcodecraft==3.1.124',
    'huaweicloudsdkcodehub==3.1.124',
    'huaweicloudsdkconfig==3.1.124',
    'huaweicloudsdkcph==3.1.124',
    'huaweicloudsdkcpts==3.1.124',
    'huaweicloudsdkcse==3.1.124',
    'huaweicloudsdkcsms==3.1.124',
    'huaweicloudsdkcss==3.1.124',
    'huaweicloudsdkcts==3.1.124',
    'huaweicloudsdkdas==3.1.124',
    'huaweicloudsdkdataartsfabric==3.1.124',
    'huaweicloudsdkdataartsfabricep==3.1.124',
    'huaweicloudsdkdataartsstudio==3.1.124',
    'huaweicloudsdkdbss==3.1.124',
    'huaweicloudsdkdc==3.1.124',
    'huaweicloudsdkdcs==3.1.124',
    'huaweicloudsdkddm==3.1.124',
    'huaweicloudsdkdds==3.1.124',
    'huaweicloudsdkdeh==3.1.124',
    'huaweicloudsdkdevstar==3.1.124',
    'huaweicloudsdkdgc==3.1.124',
    'huaweicloudsdkdis==3.1.124',
    'huaweicloudsdkdlf==3.1.124',
    'huaweicloudsdkdli==3.1.124',
    'huaweicloudsdkdns==3.1.124',
    'huaweicloudsdkdris==3.1.124',
    'huaweicloudsdkdrs==3.1.124',
    'huaweicloudsdkdsc==3.1.124',
    'huaweicloudsdkdwr==3.1.124',
    'huaweicloudsdkdws==3.1.124',
    'huaweicloudsdkec==3.1.124',
    'huaweicloudsdkecs==3.1.124',
    'huaweicloudsdkedgesec==3.1.124',
    'huaweicloudsdkeg==3.1.124',
    'huaweicloudsdkeihealth==3.1.124',
    'huaweicloudsdkeip==3.1.124',
    'huaweicloudsdkelb==3.1.124',
    'huaweicloudsdkeps==3.1.124',
    'huaweicloudsdker==3.1.124',
    'huaweicloudsdkevs==3.1.124',
    'huaweicloudsdkfrs==3.1.124',
    'huaweicloudsdkfunctiongraph==3.1.124',
    'huaweicloudsdkga==3.1.124',
    'huaweicloudsdkgaussdb==3.1.124',
    'huaweicloudsdkgaussdbfornosql==3.1.124',
    'huaweicloudsdkgaussdbforopengauss==3.1.124',
    'huaweicloudsdkgeip==3.1.124',
    'huaweicloudsdkges==3.1.124',
    'huaweicloudsdkgsl==3.1.124',
    'huaweicloudsdkhilens==3.1.124',
    'huaweicloudsdkhss==3.1.124',
    'huaweicloudsdkiam==3.1.124',
    'huaweicloudsdkiamaccessanalyzer==3.1.124',
    'huaweicloudsdkidentitycenter==3.1.124',
    'huaweicloudsdkidentitycenterstore==3.1.124',
    'huaweicloudsdkidme==3.1.124',
    'huaweicloudsdkidmeclassicapi==3.1.124',
    'huaweicloudsdkiec==3.1.124',
    'huaweicloudsdkief==3.1.124',
    'huaweicloudsdkimage==3.1.124',
    'huaweicloudsdkimagesearch==3.1.124',
    'huaweicloudsdkims==3.1.124',
    'huaweicloudsdkiotanalytics==3.1.124',
    'huaweicloudsdkiotda==3.1.124',
    'huaweicloudsdkiotdm==3.1.124',
    'huaweicloudsdkiotedge==3.1.124',
    'huaweicloudsdkivs==3.1.124',
    'huaweicloudsdkkafka==3.1.124',
    'huaweicloudsdkkms==3.1.124',
    'huaweicloudsdkkoomessage==3.1.124',
    'huaweicloudsdkkps==3.1.124',
    'huaweicloudsdklakeformation==3.1.124',
    'huaweicloudsdklive==3.1.124',
    'huaweicloudsdklts==3.1.124',
    'huaweicloudsdkmapds==3.1.124',
    'huaweicloudsdkmas==3.1.124',
    'huaweicloudsdkmastudio==3.1.124',
    'huaweicloudsdkmeeting==3.1.124',
    'huaweicloudsdkmetastudio==3.1.124',
    'huaweicloudsdkmoderation==3.1.124',
    'huaweicloudsdkmpc==3.1.124',
    'huaweicloudsdkmrs==3.1.124',
    'huaweicloudsdkmsgsms==3.1.124',
    'huaweicloudsdkmssi==3.1.124',
    'huaweicloudsdknat==3.1.124',
    'huaweicloudsdknlp==3.1.124',
    'huaweicloudsdkobs==3.1.124',
    'huaweicloudsdkocr==3.1.124',
    'huaweicloudsdkoctopus==3.1.124',
    'huaweicloudsdkoms==3.1.124',
    'huaweicloudsdkoptverse==3.1.124',
    'huaweicloudsdkorganizations==3.1.124',
    'huaweicloudsdkorgid==3.1.124',
    'huaweicloudsdkoroas==3.1.124',
    'huaweicloudsdkosm==3.1.124',
    'huaweicloudsdkpangulargemodels==3.1.124',
    'huaweicloudsdkprojectman==3.1.124',
    'huaweicloudsdkrabbitmq==3.1.124',
    'huaweicloudsdkram==3.1.124',
    'huaweicloudsdkrds==3.1.124',
    'huaweicloudsdkres==3.1.124',
    'huaweicloudsdkrgc==3.1.124',
    'huaweicloudsdkrms==3.1.124',
    'huaweicloudsdkrocketmq==3.1.124',
    'huaweicloudsdkroma==3.1.124',
    'huaweicloudsdksa==3.1.124',
    'huaweicloudsdkscm==3.1.124',
    'huaweicloudsdksdrs==3.1.124',
    'huaweicloudsdksecmaster==3.1.124',
    'huaweicloudsdkservicestage==3.1.124',
    'huaweicloudsdksfsturbo==3.1.124',
    'huaweicloudsdksis==3.1.124',
    'huaweicloudsdksmn==3.1.124',
    'huaweicloudsdksms==3.1.124',
    'huaweicloudsdksts==3.1.124',
    'huaweicloudsdkswr==3.1.124',
    'huaweicloudsdktics==3.1.124',
    'huaweicloudsdktms==3.1.124',
    'huaweicloudsdkugo==3.1.124',
    'huaweicloudsdkvas==3.1.124',
    'huaweicloudsdkvcm==3.1.124',
    'huaweicloudsdkvod==3.1.124',
    'huaweicloudsdkvpc==3.1.124',
    'huaweicloudsdkvpcep==3.1.124',
    'huaweicloudsdkvpn==3.1.124',
    'huaweicloudsdkwaf==3.1.124',
    'huaweicloudsdkworkspace==3.1.124',
    'huaweicloudsdkworkspaceapp==3.1.124',
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
