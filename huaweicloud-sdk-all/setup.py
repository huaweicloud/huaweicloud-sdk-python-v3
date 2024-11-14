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
VERSION = "3.1.122"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.122',
    'huaweicloudsdkaad==3.1.122',
    'huaweicloudsdkantiddos==3.1.122',
    'huaweicloudsdkaom==3.1.122',
    'huaweicloudsdkaos==3.1.122',
    'huaweicloudsdkapig==3.1.122',
    'huaweicloudsdkapm==3.1.122',
    'huaweicloudsdkas==3.1.122',
    'huaweicloudsdkasm==3.1.122',
    'huaweicloudsdkbcs==3.1.122',
    'huaweicloudsdkbms==3.1.122',
    'huaweicloudsdkbss==3.1.122',
    'huaweicloudsdkbssintl==3.1.122',
    'huaweicloudsdkcae==3.1.122',
    'huaweicloudsdkcampusgo==3.1.122',
    'huaweicloudsdkcbh==3.1.122',
    'huaweicloudsdkcbr==3.1.122',
    'huaweicloudsdkcbs==3.1.122',
    'huaweicloudsdkcc==3.1.122',
    'huaweicloudsdkcce==3.1.122',
    'huaweicloudsdkccm==3.1.122',
    'huaweicloudsdkcdm==3.1.122',
    'huaweicloudsdkcdn==3.1.122',
    'huaweicloudsdkces==3.1.122',
    'huaweicloudsdkcfw==3.1.122',
    'huaweicloudsdkcgs==3.1.122',
    'huaweicloudsdkclassroom==3.1.122',
    'huaweicloudsdkcloudide==3.1.122',
    'huaweicloudsdkcloudpond==3.1.122',
    'huaweicloudsdkcloudrtc==3.1.122',
    'huaweicloudsdkcloudtable==3.1.122',
    'huaweicloudsdkcloudtest==3.1.122',
    'huaweicloudsdkcoc==3.1.122',
    'huaweicloudsdkcodeartsartifact==3.1.122',
    'huaweicloudsdkcodeartsbuild==3.1.122',
    'huaweicloudsdkcodeartscheck==3.1.122',
    'huaweicloudsdkcodeartsdeploy==3.1.122',
    'huaweicloudsdkcodeartsgovernance==3.1.122',
    'huaweicloudsdkcodeartsinspector==3.1.122',
    'huaweicloudsdkcodeartspipeline==3.1.122',
    'huaweicloudsdkcodecraft==3.1.122',
    'huaweicloudsdkcodehub==3.1.122',
    'huaweicloudsdkconfig==3.1.122',
    'huaweicloudsdkcph==3.1.122',
    'huaweicloudsdkcpts==3.1.122',
    'huaweicloudsdkcse==3.1.122',
    'huaweicloudsdkcsms==3.1.122',
    'huaweicloudsdkcss==3.1.122',
    'huaweicloudsdkcts==3.1.122',
    'huaweicloudsdkdas==3.1.122',
    'huaweicloudsdkdataartsfabric==3.1.122',
    'huaweicloudsdkdataartsfabricep==3.1.122',
    'huaweicloudsdkdataartsstudio==3.1.122',
    'huaweicloudsdkdbss==3.1.122',
    'huaweicloudsdkdc==3.1.122',
    'huaweicloudsdkdcs==3.1.122',
    'huaweicloudsdkddm==3.1.122',
    'huaweicloudsdkdds==3.1.122',
    'huaweicloudsdkdeh==3.1.122',
    'huaweicloudsdkdevstar==3.1.122',
    'huaweicloudsdkdgc==3.1.122',
    'huaweicloudsdkdis==3.1.122',
    'huaweicloudsdkdlf==3.1.122',
    'huaweicloudsdkdli==3.1.122',
    'huaweicloudsdkdns==3.1.122',
    'huaweicloudsdkdris==3.1.122',
    'huaweicloudsdkdrs==3.1.122',
    'huaweicloudsdkdsc==3.1.122',
    'huaweicloudsdkdwr==3.1.122',
    'huaweicloudsdkdws==3.1.122',
    'huaweicloudsdkec==3.1.122',
    'huaweicloudsdkecs==3.1.122',
    'huaweicloudsdkedgesec==3.1.122',
    'huaweicloudsdkeg==3.1.122',
    'huaweicloudsdkeihealth==3.1.122',
    'huaweicloudsdkeip==3.1.122',
    'huaweicloudsdkelb==3.1.122',
    'huaweicloudsdkeps==3.1.122',
    'huaweicloudsdker==3.1.122',
    'huaweicloudsdkevs==3.1.122',
    'huaweicloudsdkfrs==3.1.122',
    'huaweicloudsdkfunctiongraph==3.1.122',
    'huaweicloudsdkga==3.1.122',
    'huaweicloudsdkgaussdb==3.1.122',
    'huaweicloudsdkgaussdbfornosql==3.1.122',
    'huaweicloudsdkgaussdbforopengauss==3.1.122',
    'huaweicloudsdkgeip==3.1.122',
    'huaweicloudsdkges==3.1.122',
    'huaweicloudsdkgsl==3.1.122',
    'huaweicloudsdkhilens==3.1.122',
    'huaweicloudsdkhss==3.1.122',
    'huaweicloudsdkiam==3.1.122',
    'huaweicloudsdkiamaccessanalyzer==3.1.122',
    'huaweicloudsdkidentitycenter==3.1.122',
    'huaweicloudsdkidentitycenterstore==3.1.122',
    'huaweicloudsdkidme==3.1.122',
    'huaweicloudsdkidmeclassicapi==3.1.122',
    'huaweicloudsdkiec==3.1.122',
    'huaweicloudsdkief==3.1.122',
    'huaweicloudsdkimage==3.1.122',
    'huaweicloudsdkimagesearch==3.1.122',
    'huaweicloudsdkims==3.1.122',
    'huaweicloudsdkiotanalytics==3.1.122',
    'huaweicloudsdkiotda==3.1.122',
    'huaweicloudsdkiotdm==3.1.122',
    'huaweicloudsdkiotedge==3.1.122',
    'huaweicloudsdkivs==3.1.122',
    'huaweicloudsdkkafka==3.1.122',
    'huaweicloudsdkkms==3.1.122',
    'huaweicloudsdkkoomessage==3.1.122',
    'huaweicloudsdkkps==3.1.122',
    'huaweicloudsdklakeformation==3.1.122',
    'huaweicloudsdklive==3.1.122',
    'huaweicloudsdklts==3.1.122',
    'huaweicloudsdkmapds==3.1.122',
    'huaweicloudsdkmas==3.1.122',
    'huaweicloudsdkmeeting==3.1.122',
    'huaweicloudsdkmetastudio==3.1.122',
    'huaweicloudsdkmoderation==3.1.122',
    'huaweicloudsdkmpc==3.1.122',
    'huaweicloudsdkmrs==3.1.122',
    'huaweicloudsdkmsgsms==3.1.122',
    'huaweicloudsdkmssi==3.1.122',
    'huaweicloudsdknat==3.1.122',
    'huaweicloudsdknlp==3.1.122',
    'huaweicloudsdkobs==3.1.122',
    'huaweicloudsdkocr==3.1.122',
    'huaweicloudsdkoctopus==3.1.122',
    'huaweicloudsdkoms==3.1.122',
    'huaweicloudsdkoptverse==3.1.122',
    'huaweicloudsdkorganizations==3.1.122',
    'huaweicloudsdkorgid==3.1.122',
    'huaweicloudsdkoroas==3.1.122',
    'huaweicloudsdkosm==3.1.122',
    'huaweicloudsdkpangulargemodels==3.1.122',
    'huaweicloudsdkprojectman==3.1.122',
    'huaweicloudsdkrabbitmq==3.1.122',
    'huaweicloudsdkram==3.1.122',
    'huaweicloudsdkrds==3.1.122',
    'huaweicloudsdkres==3.1.122',
    'huaweicloudsdkrgc==3.1.122',
    'huaweicloudsdkrms==3.1.122',
    'huaweicloudsdkrocketmq==3.1.122',
    'huaweicloudsdkroma==3.1.122',
    'huaweicloudsdksa==3.1.122',
    'huaweicloudsdkscm==3.1.122',
    'huaweicloudsdksdrs==3.1.122',
    'huaweicloudsdksecmaster==3.1.122',
    'huaweicloudsdkservicestage==3.1.122',
    'huaweicloudsdksfsturbo==3.1.122',
    'huaweicloudsdksis==3.1.122',
    'huaweicloudsdksmn==3.1.122',
    'huaweicloudsdksms==3.1.122',
    'huaweicloudsdksts==3.1.122',
    'huaweicloudsdkswr==3.1.122',
    'huaweicloudsdktics==3.1.122',
    'huaweicloudsdktms==3.1.122',
    'huaweicloudsdkugo==3.1.122',
    'huaweicloudsdkvas==3.1.122',
    'huaweicloudsdkvcm==3.1.122',
    'huaweicloudsdkvod==3.1.122',
    'huaweicloudsdkvpc==3.1.122',
    'huaweicloudsdkvpcep==3.1.122',
    'huaweicloudsdkvpn==3.1.122',
    'huaweicloudsdkwaf==3.1.122',
    'huaweicloudsdkworkspace==3.1.122',
    'huaweicloudsdkworkspaceapp==3.1.122',
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
