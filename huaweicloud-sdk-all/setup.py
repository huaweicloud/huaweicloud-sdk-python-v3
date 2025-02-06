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
VERSION = "3.1.134"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.134',
    'huaweicloudsdkaad==3.1.134',
    'huaweicloudsdkantiddos==3.1.134',
    'huaweicloudsdkaom==3.1.134',
    'huaweicloudsdkaos==3.1.134',
    'huaweicloudsdkapig==3.1.134',
    'huaweicloudsdkapm==3.1.134',
    'huaweicloudsdkas==3.1.134',
    'huaweicloudsdkasm==3.1.134',
    'huaweicloudsdkbcs==3.1.134',
    'huaweicloudsdkbms==3.1.134',
    'huaweicloudsdkbss==3.1.134',
    'huaweicloudsdkbssintl==3.1.134',
    'huaweicloudsdkcae==3.1.134',
    'huaweicloudsdkcampusgo==3.1.134',
    'huaweicloudsdkcbh==3.1.134',
    'huaweicloudsdkcbr==3.1.134',
    'huaweicloudsdkcbs==3.1.134',
    'huaweicloudsdkcc==3.1.134',
    'huaweicloudsdkcce==3.1.134',
    'huaweicloudsdkccm==3.1.134',
    'huaweicloudsdkcdm==3.1.134',
    'huaweicloudsdkcdn==3.1.134',
    'huaweicloudsdkces==3.1.134',
    'huaweicloudsdkcfw==3.1.134',
    'huaweicloudsdkcgs==3.1.134',
    'huaweicloudsdkclassroom==3.1.134',
    'huaweicloudsdkcloudide==3.1.134',
    'huaweicloudsdkcloudpond==3.1.134',
    'huaweicloudsdkcloudrtc==3.1.134',
    'huaweicloudsdkcloudtable==3.1.134',
    'huaweicloudsdkcloudtest==3.1.134',
    'huaweicloudsdkcoc==3.1.134',
    'huaweicloudsdkcodeartsartifact==3.1.134',
    'huaweicloudsdkcodeartsbuild==3.1.134',
    'huaweicloudsdkcodeartscheck==3.1.134',
    'huaweicloudsdkcodeartsdeploy==3.1.134',
    'huaweicloudsdkcodeartsgovernance==3.1.134',
    'huaweicloudsdkcodeartsinspector==3.1.134',
    'huaweicloudsdkcodeartspipeline==3.1.134',
    'huaweicloudsdkcodecraft==3.1.134',
    'huaweicloudsdkcodehub==3.1.134',
    'huaweicloudsdkconfig==3.1.134',
    'huaweicloudsdkcph==3.1.134',
    'huaweicloudsdkcpts==3.1.134',
    'huaweicloudsdkcse==3.1.134',
    'huaweicloudsdkcsms==3.1.134',
    'huaweicloudsdkcss==3.1.134',
    'huaweicloudsdkcts==3.1.134',
    'huaweicloudsdkdas==3.1.134',
    'huaweicloudsdkdataartsfabric==3.1.134',
    'huaweicloudsdkdataartsfabricep==3.1.134',
    'huaweicloudsdkdataartsstudio==3.1.134',
    'huaweicloudsdkdbss==3.1.134',
    'huaweicloudsdkdc==3.1.134',
    'huaweicloudsdkdcs==3.1.134',
    'huaweicloudsdkddm==3.1.134',
    'huaweicloudsdkdds==3.1.134',
    'huaweicloudsdkdeh==3.1.134',
    'huaweicloudsdkdevstar==3.1.134',
    'huaweicloudsdkdgc==3.1.134',
    'huaweicloudsdkdis==3.1.134',
    'huaweicloudsdkdlf==3.1.134',
    'huaweicloudsdkdli==3.1.134',
    'huaweicloudsdkdns==3.1.134',
    'huaweicloudsdkdris==3.1.134',
    'huaweicloudsdkdrs==3.1.134',
    'huaweicloudsdkdsc==3.1.134',
    'huaweicloudsdkdwr==3.1.134',
    'huaweicloudsdkdws==3.1.134',
    'huaweicloudsdkec==3.1.134',
    'huaweicloudsdkecs==3.1.134',
    'huaweicloudsdkedgesec==3.1.134',
    'huaweicloudsdkeg==3.1.134',
    'huaweicloudsdkeihealth==3.1.134',
    'huaweicloudsdkeip==3.1.134',
    'huaweicloudsdkelb==3.1.134',
    'huaweicloudsdkeps==3.1.134',
    'huaweicloudsdker==3.1.134',
    'huaweicloudsdkevs==3.1.134',
    'huaweicloudsdkfrs==3.1.134',
    'huaweicloudsdkfunctiongraph==3.1.134',
    'huaweicloudsdkga==3.1.134',
    'huaweicloudsdkgaussdb==3.1.134',
    'huaweicloudsdkgaussdbfornosql==3.1.134',
    'huaweicloudsdkgaussdbforopengauss==3.1.134',
    'huaweicloudsdkgeip==3.1.134',
    'huaweicloudsdkges==3.1.134',
    'huaweicloudsdkgsl==3.1.134',
    'huaweicloudsdkhilens==3.1.134',
    'huaweicloudsdkhss==3.1.134',
    'huaweicloudsdkiam==3.1.134',
    'huaweicloudsdkiamaccessanalyzer==3.1.134',
    'huaweicloudsdkidentitycenter==3.1.134',
    'huaweicloudsdkidentitycenterstore==3.1.134',
    'huaweicloudsdkidme==3.1.134',
    'huaweicloudsdkidmeclassicapi==3.1.134',
    'huaweicloudsdkiec==3.1.134',
    'huaweicloudsdkief==3.1.134',
    'huaweicloudsdkimage==3.1.134',
    'huaweicloudsdkimagesearch==3.1.134',
    'huaweicloudsdkims==3.1.134',
    'huaweicloudsdkiotanalytics==3.1.134',
    'huaweicloudsdkiotda==3.1.134',
    'huaweicloudsdkiotdm==3.1.134',
    'huaweicloudsdkiotedge==3.1.134',
    'huaweicloudsdkivs==3.1.134',
    'huaweicloudsdkkafka==3.1.134',
    'huaweicloudsdkkms==3.1.134',
    'huaweicloudsdkkoomessage==3.1.134',
    'huaweicloudsdkkps==3.1.134',
    'huaweicloudsdklakeformation==3.1.134',
    'huaweicloudsdklive==3.1.134',
    'huaweicloudsdklts==3.1.134',
    'huaweicloudsdkmapds==3.1.134',
    'huaweicloudsdkmas==3.1.134',
    'huaweicloudsdkmastudio==3.1.134',
    'huaweicloudsdkmeeting==3.1.134',
    'huaweicloudsdkmetastudio==3.1.134',
    'huaweicloudsdkmoderation==3.1.134',
    'huaweicloudsdkmpc==3.1.134',
    'huaweicloudsdkmrs==3.1.134',
    'huaweicloudsdkmsgsms==3.1.134',
    'huaweicloudsdkmssi==3.1.134',
    'huaweicloudsdknat==3.1.134',
    'huaweicloudsdknlp==3.1.134',
    'huaweicloudsdkobs==3.1.134',
    'huaweicloudsdkocr==3.1.134',
    'huaweicloudsdkoctopus==3.1.134',
    'huaweicloudsdkoms==3.1.134',
    'huaweicloudsdkoptverse==3.1.134',
    'huaweicloudsdkorganizations==3.1.134',
    'huaweicloudsdkorgid==3.1.134',
    'huaweicloudsdkoroas==3.1.134',
    'huaweicloudsdkosm==3.1.134',
    'huaweicloudsdkpangulargemodels==3.1.134',
    'huaweicloudsdkprojectman==3.1.134',
    'huaweicloudsdkrabbitmq==3.1.134',
    'huaweicloudsdkram==3.1.134',
    'huaweicloudsdkrds==3.1.134',
    'huaweicloudsdkres==3.1.134',
    'huaweicloudsdkrgc==3.1.134',
    'huaweicloudsdkrms==3.1.134',
    'huaweicloudsdkrocketmq==3.1.134',
    'huaweicloudsdkroma==3.1.134',
    'huaweicloudsdksa==3.1.134',
    'huaweicloudsdkscm==3.1.134',
    'huaweicloudsdksdrs==3.1.134',
    'huaweicloudsdksecmaster==3.1.134',
    'huaweicloudsdkservicestage==3.1.134',
    'huaweicloudsdksfsturbo==3.1.134',
    'huaweicloudsdksis==3.1.134',
    'huaweicloudsdksmn==3.1.134',
    'huaweicloudsdksms==3.1.134',
    'huaweicloudsdksmsapi==3.1.134',
    'huaweicloudsdksts==3.1.134',
    'huaweicloudsdkswr==3.1.134',
    'huaweicloudsdktics==3.1.134',
    'huaweicloudsdktms==3.1.134',
    'huaweicloudsdkugo==3.1.134',
    'huaweicloudsdkvas==3.1.134',
    'huaweicloudsdkvcm==3.1.134',
    'huaweicloudsdkvod==3.1.134',
    'huaweicloudsdkvpc==3.1.134',
    'huaweicloudsdkvpcep==3.1.134',
    'huaweicloudsdkvpn==3.1.134',
    'huaweicloudsdkwaf==3.1.134',
    'huaweicloudsdkworkspace==3.1.134',
    'huaweicloudsdkworkspaceapp==3.1.134',
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
