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
VERSION = "3.1.123"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.123',
    'huaweicloudsdkaad==3.1.123',
    'huaweicloudsdkantiddos==3.1.123',
    'huaweicloudsdkaom==3.1.123',
    'huaweicloudsdkaos==3.1.123',
    'huaweicloudsdkapig==3.1.123',
    'huaweicloudsdkapm==3.1.123',
    'huaweicloudsdkas==3.1.123',
    'huaweicloudsdkasm==3.1.123',
    'huaweicloudsdkbcs==3.1.123',
    'huaweicloudsdkbms==3.1.123',
    'huaweicloudsdkbss==3.1.123',
    'huaweicloudsdkbssintl==3.1.123',
    'huaweicloudsdkcae==3.1.123',
    'huaweicloudsdkcampusgo==3.1.123',
    'huaweicloudsdkcbh==3.1.123',
    'huaweicloudsdkcbr==3.1.123',
    'huaweicloudsdkcbs==3.1.123',
    'huaweicloudsdkcc==3.1.123',
    'huaweicloudsdkcce==3.1.123',
    'huaweicloudsdkccm==3.1.123',
    'huaweicloudsdkcdm==3.1.123',
    'huaweicloudsdkcdn==3.1.123',
    'huaweicloudsdkces==3.1.123',
    'huaweicloudsdkcfw==3.1.123',
    'huaweicloudsdkcgs==3.1.123',
    'huaweicloudsdkclassroom==3.1.123',
    'huaweicloudsdkcloudide==3.1.123',
    'huaweicloudsdkcloudpond==3.1.123',
    'huaweicloudsdkcloudrtc==3.1.123',
    'huaweicloudsdkcloudtable==3.1.123',
    'huaweicloudsdkcloudtest==3.1.123',
    'huaweicloudsdkcoc==3.1.123',
    'huaweicloudsdkcodeartsartifact==3.1.123',
    'huaweicloudsdkcodeartsbuild==3.1.123',
    'huaweicloudsdkcodeartscheck==3.1.123',
    'huaweicloudsdkcodeartsdeploy==3.1.123',
    'huaweicloudsdkcodeartsgovernance==3.1.123',
    'huaweicloudsdkcodeartsinspector==3.1.123',
    'huaweicloudsdkcodeartspipeline==3.1.123',
    'huaweicloudsdkcodecraft==3.1.123',
    'huaweicloudsdkcodehub==3.1.123',
    'huaweicloudsdkconfig==3.1.123',
    'huaweicloudsdkcph==3.1.123',
    'huaweicloudsdkcpts==3.1.123',
    'huaweicloudsdkcse==3.1.123',
    'huaweicloudsdkcsms==3.1.123',
    'huaweicloudsdkcss==3.1.123',
    'huaweicloudsdkcts==3.1.123',
    'huaweicloudsdkdas==3.1.123',
    'huaweicloudsdkdataartsfabric==3.1.123',
    'huaweicloudsdkdataartsfabricep==3.1.123',
    'huaweicloudsdkdataartsstudio==3.1.123',
    'huaweicloudsdkdbss==3.1.123',
    'huaweicloudsdkdc==3.1.123',
    'huaweicloudsdkdcs==3.1.123',
    'huaweicloudsdkddm==3.1.123',
    'huaweicloudsdkdds==3.1.123',
    'huaweicloudsdkdeh==3.1.123',
    'huaweicloudsdkdevstar==3.1.123',
    'huaweicloudsdkdgc==3.1.123',
    'huaweicloudsdkdis==3.1.123',
    'huaweicloudsdkdlf==3.1.123',
    'huaweicloudsdkdli==3.1.123',
    'huaweicloudsdkdns==3.1.123',
    'huaweicloudsdkdris==3.1.123',
    'huaweicloudsdkdrs==3.1.123',
    'huaweicloudsdkdsc==3.1.123',
    'huaweicloudsdkdwr==3.1.123',
    'huaweicloudsdkdws==3.1.123',
    'huaweicloudsdkec==3.1.123',
    'huaweicloudsdkecs==3.1.123',
    'huaweicloudsdkedgesec==3.1.123',
    'huaweicloudsdkeg==3.1.123',
    'huaweicloudsdkeihealth==3.1.123',
    'huaweicloudsdkeip==3.1.123',
    'huaweicloudsdkelb==3.1.123',
    'huaweicloudsdkeps==3.1.123',
    'huaweicloudsdker==3.1.123',
    'huaweicloudsdkevs==3.1.123',
    'huaweicloudsdkfrs==3.1.123',
    'huaweicloudsdkfunctiongraph==3.1.123',
    'huaweicloudsdkga==3.1.123',
    'huaweicloudsdkgaussdb==3.1.123',
    'huaweicloudsdkgaussdbfornosql==3.1.123',
    'huaweicloudsdkgaussdbforopengauss==3.1.123',
    'huaweicloudsdkgeip==3.1.123',
    'huaweicloudsdkges==3.1.123',
    'huaweicloudsdkgsl==3.1.123',
    'huaweicloudsdkhilens==3.1.123',
    'huaweicloudsdkhss==3.1.123',
    'huaweicloudsdkiam==3.1.123',
    'huaweicloudsdkiamaccessanalyzer==3.1.123',
    'huaweicloudsdkidentitycenter==3.1.123',
    'huaweicloudsdkidentitycenterstore==3.1.123',
    'huaweicloudsdkidme==3.1.123',
    'huaweicloudsdkidmeclassicapi==3.1.123',
    'huaweicloudsdkiec==3.1.123',
    'huaweicloudsdkief==3.1.123',
    'huaweicloudsdkimage==3.1.123',
    'huaweicloudsdkimagesearch==3.1.123',
    'huaweicloudsdkims==3.1.123',
    'huaweicloudsdkiotanalytics==3.1.123',
    'huaweicloudsdkiotda==3.1.123',
    'huaweicloudsdkiotdm==3.1.123',
    'huaweicloudsdkiotedge==3.1.123',
    'huaweicloudsdkivs==3.1.123',
    'huaweicloudsdkkafka==3.1.123',
    'huaweicloudsdkkms==3.1.123',
    'huaweicloudsdkkoomessage==3.1.123',
    'huaweicloudsdkkps==3.1.123',
    'huaweicloudsdklakeformation==3.1.123',
    'huaweicloudsdklive==3.1.123',
    'huaweicloudsdklts==3.1.123',
    'huaweicloudsdkmapds==3.1.123',
    'huaweicloudsdkmas==3.1.123',
    'huaweicloudsdkmeeting==3.1.123',
    'huaweicloudsdkmetastudio==3.1.123',
    'huaweicloudsdkmoderation==3.1.123',
    'huaweicloudsdkmpc==3.1.123',
    'huaweicloudsdkmrs==3.1.123',
    'huaweicloudsdkmsgsms==3.1.123',
    'huaweicloudsdkmssi==3.1.123',
    'huaweicloudsdknat==3.1.123',
    'huaweicloudsdknlp==3.1.123',
    'huaweicloudsdkobs==3.1.123',
    'huaweicloudsdkocr==3.1.123',
    'huaweicloudsdkoctopus==3.1.123',
    'huaweicloudsdkoms==3.1.123',
    'huaweicloudsdkoptverse==3.1.123',
    'huaweicloudsdkorganizations==3.1.123',
    'huaweicloudsdkorgid==3.1.123',
    'huaweicloudsdkoroas==3.1.123',
    'huaweicloudsdkosm==3.1.123',
    'huaweicloudsdkpangulargemodels==3.1.123',
    'huaweicloudsdkprojectman==3.1.123',
    'huaweicloudsdkrabbitmq==3.1.123',
    'huaweicloudsdkram==3.1.123',
    'huaweicloudsdkrds==3.1.123',
    'huaweicloudsdkres==3.1.123',
    'huaweicloudsdkrgc==3.1.123',
    'huaweicloudsdkrms==3.1.123',
    'huaweicloudsdkrocketmq==3.1.123',
    'huaweicloudsdkroma==3.1.123',
    'huaweicloudsdksa==3.1.123',
    'huaweicloudsdkscm==3.1.123',
    'huaweicloudsdksdrs==3.1.123',
    'huaweicloudsdksecmaster==3.1.123',
    'huaweicloudsdkservicestage==3.1.123',
    'huaweicloudsdksfsturbo==3.1.123',
    'huaweicloudsdksis==3.1.123',
    'huaweicloudsdksmn==3.1.123',
    'huaweicloudsdksms==3.1.123',
    'huaweicloudsdksts==3.1.123',
    'huaweicloudsdkswr==3.1.123',
    'huaweicloudsdktics==3.1.123',
    'huaweicloudsdktms==3.1.123',
    'huaweicloudsdkugo==3.1.123',
    'huaweicloudsdkvas==3.1.123',
    'huaweicloudsdkvcm==3.1.123',
    'huaweicloudsdkvod==3.1.123',
    'huaweicloudsdkvpc==3.1.123',
    'huaweicloudsdkvpcep==3.1.123',
    'huaweicloudsdkvpn==3.1.123',
    'huaweicloudsdkwaf==3.1.123',
    'huaweicloudsdkworkspace==3.1.123',
    'huaweicloudsdkworkspaceapp==3.1.123',
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
