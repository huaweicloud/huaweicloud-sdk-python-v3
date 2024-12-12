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
VERSION = "3.1.127"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.127',
    'huaweicloudsdkaad==3.1.127',
    'huaweicloudsdkantiddos==3.1.127',
    'huaweicloudsdkaom==3.1.127',
    'huaweicloudsdkaos==3.1.127',
    'huaweicloudsdkapig==3.1.127',
    'huaweicloudsdkapm==3.1.127',
    'huaweicloudsdkas==3.1.127',
    'huaweicloudsdkasm==3.1.127',
    'huaweicloudsdkbcs==3.1.127',
    'huaweicloudsdkbms==3.1.127',
    'huaweicloudsdkbss==3.1.127',
    'huaweicloudsdkbssintl==3.1.127',
    'huaweicloudsdkcae==3.1.127',
    'huaweicloudsdkcampusgo==3.1.127',
    'huaweicloudsdkcbh==3.1.127',
    'huaweicloudsdkcbr==3.1.127',
    'huaweicloudsdkcbs==3.1.127',
    'huaweicloudsdkcc==3.1.127',
    'huaweicloudsdkcce==3.1.127',
    'huaweicloudsdkccm==3.1.127',
    'huaweicloudsdkcdm==3.1.127',
    'huaweicloudsdkcdn==3.1.127',
    'huaweicloudsdkces==3.1.127',
    'huaweicloudsdkcfw==3.1.127',
    'huaweicloudsdkcgs==3.1.127',
    'huaweicloudsdkclassroom==3.1.127',
    'huaweicloudsdkcloudide==3.1.127',
    'huaweicloudsdkcloudpond==3.1.127',
    'huaweicloudsdkcloudrtc==3.1.127',
    'huaweicloudsdkcloudtable==3.1.127',
    'huaweicloudsdkcloudtest==3.1.127',
    'huaweicloudsdkcoc==3.1.127',
    'huaweicloudsdkcodeartsartifact==3.1.127',
    'huaweicloudsdkcodeartsbuild==3.1.127',
    'huaweicloudsdkcodeartscheck==3.1.127',
    'huaweicloudsdkcodeartsdeploy==3.1.127',
    'huaweicloudsdkcodeartsgovernance==3.1.127',
    'huaweicloudsdkcodeartsinspector==3.1.127',
    'huaweicloudsdkcodeartspipeline==3.1.127',
    'huaweicloudsdkcodecraft==3.1.127',
    'huaweicloudsdkcodehub==3.1.127',
    'huaweicloudsdkconfig==3.1.127',
    'huaweicloudsdkcph==3.1.127',
    'huaweicloudsdkcpts==3.1.127',
    'huaweicloudsdkcse==3.1.127',
    'huaweicloudsdkcsms==3.1.127',
    'huaweicloudsdkcss==3.1.127',
    'huaweicloudsdkcts==3.1.127',
    'huaweicloudsdkdas==3.1.127',
    'huaweicloudsdkdataartsfabric==3.1.127',
    'huaweicloudsdkdataartsfabricep==3.1.127',
    'huaweicloudsdkdataartsstudio==3.1.127',
    'huaweicloudsdkdbss==3.1.127',
    'huaweicloudsdkdc==3.1.127',
    'huaweicloudsdkdcs==3.1.127',
    'huaweicloudsdkddm==3.1.127',
    'huaweicloudsdkdds==3.1.127',
    'huaweicloudsdkdeh==3.1.127',
    'huaweicloudsdkdevstar==3.1.127',
    'huaweicloudsdkdgc==3.1.127',
    'huaweicloudsdkdis==3.1.127',
    'huaweicloudsdkdlf==3.1.127',
    'huaweicloudsdkdli==3.1.127',
    'huaweicloudsdkdns==3.1.127',
    'huaweicloudsdkdris==3.1.127',
    'huaweicloudsdkdrs==3.1.127',
    'huaweicloudsdkdsc==3.1.127',
    'huaweicloudsdkdwr==3.1.127',
    'huaweicloudsdkdws==3.1.127',
    'huaweicloudsdkec==3.1.127',
    'huaweicloudsdkecs==3.1.127',
    'huaweicloudsdkedgesec==3.1.127',
    'huaweicloudsdkeg==3.1.127',
    'huaweicloudsdkeihealth==3.1.127',
    'huaweicloudsdkeip==3.1.127',
    'huaweicloudsdkelb==3.1.127',
    'huaweicloudsdkeps==3.1.127',
    'huaweicloudsdker==3.1.127',
    'huaweicloudsdkevs==3.1.127',
    'huaweicloudsdkfrs==3.1.127',
    'huaweicloudsdkfunctiongraph==3.1.127',
    'huaweicloudsdkga==3.1.127',
    'huaweicloudsdkgaussdb==3.1.127',
    'huaweicloudsdkgaussdbfornosql==3.1.127',
    'huaweicloudsdkgaussdbforopengauss==3.1.127',
    'huaweicloudsdkgeip==3.1.127',
    'huaweicloudsdkges==3.1.127',
    'huaweicloudsdkgsl==3.1.127',
    'huaweicloudsdkhilens==3.1.127',
    'huaweicloudsdkhss==3.1.127',
    'huaweicloudsdkiam==3.1.127',
    'huaweicloudsdkiamaccessanalyzer==3.1.127',
    'huaweicloudsdkidentitycenter==3.1.127',
    'huaweicloudsdkidentitycenterstore==3.1.127',
    'huaweicloudsdkidme==3.1.127',
    'huaweicloudsdkidmeclassicapi==3.1.127',
    'huaweicloudsdkiec==3.1.127',
    'huaweicloudsdkief==3.1.127',
    'huaweicloudsdkimage==3.1.127',
    'huaweicloudsdkimagesearch==3.1.127',
    'huaweicloudsdkims==3.1.127',
    'huaweicloudsdkiotanalytics==3.1.127',
    'huaweicloudsdkiotda==3.1.127',
    'huaweicloudsdkiotdm==3.1.127',
    'huaweicloudsdkiotedge==3.1.127',
    'huaweicloudsdkivs==3.1.127',
    'huaweicloudsdkkafka==3.1.127',
    'huaweicloudsdkkms==3.1.127',
    'huaweicloudsdkkoomessage==3.1.127',
    'huaweicloudsdkkps==3.1.127',
    'huaweicloudsdklakeformation==3.1.127',
    'huaweicloudsdklive==3.1.127',
    'huaweicloudsdklts==3.1.127',
    'huaweicloudsdkmapds==3.1.127',
    'huaweicloudsdkmas==3.1.127',
    'huaweicloudsdkmastudio==3.1.127',
    'huaweicloudsdkmeeting==3.1.127',
    'huaweicloudsdkmetastudio==3.1.127',
    'huaweicloudsdkmoderation==3.1.127',
    'huaweicloudsdkmpc==3.1.127',
    'huaweicloudsdkmrs==3.1.127',
    'huaweicloudsdkmsgsms==3.1.127',
    'huaweicloudsdkmssi==3.1.127',
    'huaweicloudsdknat==3.1.127',
    'huaweicloudsdknlp==3.1.127',
    'huaweicloudsdkobs==3.1.127',
    'huaweicloudsdkocr==3.1.127',
    'huaweicloudsdkoctopus==3.1.127',
    'huaweicloudsdkoms==3.1.127',
    'huaweicloudsdkoptverse==3.1.127',
    'huaweicloudsdkorganizations==3.1.127',
    'huaweicloudsdkorgid==3.1.127',
    'huaweicloudsdkoroas==3.1.127',
    'huaweicloudsdkosm==3.1.127',
    'huaweicloudsdkpangulargemodels==3.1.127',
    'huaweicloudsdkprojectman==3.1.127',
    'huaweicloudsdkrabbitmq==3.1.127',
    'huaweicloudsdkram==3.1.127',
    'huaweicloudsdkrds==3.1.127',
    'huaweicloudsdkres==3.1.127',
    'huaweicloudsdkrgc==3.1.127',
    'huaweicloudsdkrms==3.1.127',
    'huaweicloudsdkrocketmq==3.1.127',
    'huaweicloudsdkroma==3.1.127',
    'huaweicloudsdksa==3.1.127',
    'huaweicloudsdkscm==3.1.127',
    'huaweicloudsdksdrs==3.1.127',
    'huaweicloudsdksecmaster==3.1.127',
    'huaweicloudsdkservicestage==3.1.127',
    'huaweicloudsdksfsturbo==3.1.127',
    'huaweicloudsdksis==3.1.127',
    'huaweicloudsdksmn==3.1.127',
    'huaweicloudsdksms==3.1.127',
    'huaweicloudsdksmsapi==3.1.127',
    'huaweicloudsdksts==3.1.127',
    'huaweicloudsdkswr==3.1.127',
    'huaweicloudsdktics==3.1.127',
    'huaweicloudsdktms==3.1.127',
    'huaweicloudsdkugo==3.1.127',
    'huaweicloudsdkvas==3.1.127',
    'huaweicloudsdkvcm==3.1.127',
    'huaweicloudsdkvod==3.1.127',
    'huaweicloudsdkvpc==3.1.127',
    'huaweicloudsdkvpcep==3.1.127',
    'huaweicloudsdkvpn==3.1.127',
    'huaweicloudsdkwaf==3.1.127',
    'huaweicloudsdkworkspace==3.1.127',
    'huaweicloudsdkworkspaceapp==3.1.127',
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
