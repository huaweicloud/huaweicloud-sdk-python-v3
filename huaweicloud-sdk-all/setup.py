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
VERSION = "3.1.144"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.144',
    'huaweicloudsdkaad==3.1.144',
    'huaweicloudsdkantiddos==3.1.144',
    'huaweicloudsdkaom==3.1.144',
    'huaweicloudsdkaos==3.1.144',
    'huaweicloudsdkapig==3.1.144',
    'huaweicloudsdkapm==3.1.144',
    'huaweicloudsdkas==3.1.144',
    'huaweicloudsdkasm==3.1.144',
    'huaweicloudsdkbcs==3.1.144',
    'huaweicloudsdkbms==3.1.144',
    'huaweicloudsdkbss==3.1.144',
    'huaweicloudsdkbssintl==3.1.144',
    'huaweicloudsdkcae==3.1.144',
    'huaweicloudsdkcampusgo==3.1.144',
    'huaweicloudsdkcbh==3.1.144',
    'huaweicloudsdkcbr==3.1.144',
    'huaweicloudsdkcbs==3.1.144',
    'huaweicloudsdkcc==3.1.144',
    'huaweicloudsdkcce==3.1.144',
    'huaweicloudsdkccm==3.1.144',
    'huaweicloudsdkcdm==3.1.144',
    'huaweicloudsdkcdn==3.1.144',
    'huaweicloudsdkces==3.1.144',
    'huaweicloudsdkcfw==3.1.144',
    'huaweicloudsdkcgs==3.1.144',
    'huaweicloudsdkclassroom==3.1.144',
    'huaweicloudsdkcloudide==3.1.144',
    'huaweicloudsdkcloudpond==3.1.144',
    'huaweicloudsdkcloudrtc==3.1.144',
    'huaweicloudsdkcloudtable==3.1.144',
    'huaweicloudsdkcloudtest==3.1.144',
    'huaweicloudsdkcoc==3.1.144',
    'huaweicloudsdkcodeartsartifact==3.1.144',
    'huaweicloudsdkcodeartsbuild==3.1.144',
    'huaweicloudsdkcodeartscheck==3.1.144',
    'huaweicloudsdkcodeartsdeploy==3.1.144',
    'huaweicloudsdkcodeartsgovernance==3.1.144',
    'huaweicloudsdkcodeartsinspector==3.1.144',
    'huaweicloudsdkcodeartspipeline==3.1.144',
    'huaweicloudsdkcodecraft==3.1.144',
    'huaweicloudsdkcodehub==3.1.144',
    'huaweicloudsdkconfig==3.1.144',
    'huaweicloudsdkcph==3.1.144',
    'huaweicloudsdkcpts==3.1.144',
    'huaweicloudsdkcse==3.1.144',
    'huaweicloudsdkcsms==3.1.144',
    'huaweicloudsdkcss==3.1.144',
    'huaweicloudsdkcts==3.1.144',
    'huaweicloudsdkdas==3.1.144',
    'huaweicloudsdkdataartsfabric==3.1.144',
    'huaweicloudsdkdataartsfabricep==3.1.144',
    'huaweicloudsdkdataartsstudio==3.1.144',
    'huaweicloudsdkdbss==3.1.144',
    'huaweicloudsdkdc==3.1.144',
    'huaweicloudsdkdcs==3.1.144',
    'huaweicloudsdkddm==3.1.144',
    'huaweicloudsdkdds==3.1.144',
    'huaweicloudsdkdeh==3.1.144',
    'huaweicloudsdkdevstar==3.1.144',
    'huaweicloudsdkdgc==3.1.144',
    'huaweicloudsdkdis==3.1.144',
    'huaweicloudsdkdlf==3.1.144',
    'huaweicloudsdkdli==3.1.144',
    'huaweicloudsdkdns==3.1.144',
    'huaweicloudsdkdris==3.1.144',
    'huaweicloudsdkdrs==3.1.144',
    'huaweicloudsdkdsc==3.1.144',
    'huaweicloudsdkdwr==3.1.144',
    'huaweicloudsdkdws==3.1.144',
    'huaweicloudsdkec==3.1.144',
    'huaweicloudsdkecs==3.1.144',
    'huaweicloudsdkedgesec==3.1.144',
    'huaweicloudsdkeg==3.1.144',
    'huaweicloudsdkeihealth==3.1.144',
    'huaweicloudsdkeip==3.1.144',
    'huaweicloudsdkelb==3.1.144',
    'huaweicloudsdkeps==3.1.144',
    'huaweicloudsdker==3.1.144',
    'huaweicloudsdkevs==3.1.144',
    'huaweicloudsdkfrs==3.1.144',
    'huaweicloudsdkfunctiongraph==3.1.144',
    'huaweicloudsdkga==3.1.144',
    'huaweicloudsdkgaussdb==3.1.144',
    'huaweicloudsdkgaussdbfornosql==3.1.144',
    'huaweicloudsdkgaussdbforopengauss==3.1.144',
    'huaweicloudsdkgeip==3.1.144',
    'huaweicloudsdkges==3.1.144',
    'huaweicloudsdkgsl==3.1.144',
    'huaweicloudsdkhilens==3.1.144',
    'huaweicloudsdkhss==3.1.144',
    'huaweicloudsdkiam==3.1.144',
    'huaweicloudsdkiamaccessanalyzer==3.1.144',
    'huaweicloudsdkidentitycenter==3.1.144',
    'huaweicloudsdkidentitycenteroidc==3.1.144',
    'huaweicloudsdkidentitycenterportalapi==3.1.144',
    'huaweicloudsdkidentitycenterscim==3.1.144',
    'huaweicloudsdkidentitycenterstore==3.1.144',
    'huaweicloudsdkidme==3.1.144',
    'huaweicloudsdkidmeclassicapi==3.1.144',
    'huaweicloudsdkiec==3.1.144',
    'huaweicloudsdkief==3.1.144',
    'huaweicloudsdkimage==3.1.144',
    'huaweicloudsdkimagesearch==3.1.144',
    'huaweicloudsdkims==3.1.144',
    'huaweicloudsdkiotanalytics==3.1.144',
    'huaweicloudsdkiotda==3.1.144',
    'huaweicloudsdkiotdm==3.1.144',
    'huaweicloudsdkiotedge==3.1.144',
    'huaweicloudsdkivs==3.1.144',
    'huaweicloudsdkkafka==3.1.144',
    'huaweicloudsdkkms==3.1.144',
    'huaweicloudsdkkoomessage==3.1.144',
    'huaweicloudsdkkps==3.1.144',
    'huaweicloudsdkkvs==3.1.144',
    'huaweicloudsdklakeformation==3.1.144',
    'huaweicloudsdklive==3.1.144',
    'huaweicloudsdklts==3.1.144',
    'huaweicloudsdkmapds==3.1.144',
    'huaweicloudsdkmas==3.1.144',
    'huaweicloudsdkmastudio==3.1.144',
    'huaweicloudsdkmeeting==3.1.144',
    'huaweicloudsdkmetastudio==3.1.144',
    'huaweicloudsdkmoderation==3.1.144',
    'huaweicloudsdkmpc==3.1.144',
    'huaweicloudsdkmrs==3.1.144',
    'huaweicloudsdkmsgsms==3.1.144',
    'huaweicloudsdkmssi==3.1.144',
    'huaweicloudsdknat==3.1.144',
    'huaweicloudsdknlp==3.1.144',
    'huaweicloudsdkobs==3.1.144',
    'huaweicloudsdkocr==3.1.144',
    'huaweicloudsdkoctopus==3.1.144',
    'huaweicloudsdkoms==3.1.144',
    'huaweicloudsdkoptverse==3.1.144',
    'huaweicloudsdkorganizations==3.1.144',
    'huaweicloudsdkorgid==3.1.144',
    'huaweicloudsdkoroas==3.1.144',
    'huaweicloudsdkosm==3.1.144',
    'huaweicloudsdkpangulargemodels==3.1.144',
    'huaweicloudsdkprojectman==3.1.144',
    'huaweicloudsdkrabbitmq==3.1.144',
    'huaweicloudsdkram==3.1.144',
    'huaweicloudsdkrds==3.1.144',
    'huaweicloudsdkres==3.1.144',
    'huaweicloudsdkrgc==3.1.144',
    'huaweicloudsdkrms==3.1.144',
    'huaweicloudsdkrocketmq==3.1.144',
    'huaweicloudsdkroma==3.1.144',
    'huaweicloudsdksa==3.1.144',
    'huaweicloudsdkscm==3.1.144',
    'huaweicloudsdksdrs==3.1.144',
    'huaweicloudsdksecmaster==3.1.144',
    'huaweicloudsdkservicestage==3.1.144',
    'huaweicloudsdksfsturbo==3.1.144',
    'huaweicloudsdksis==3.1.144',
    'huaweicloudsdksmn==3.1.144',
    'huaweicloudsdksmnglobal==3.1.144',
    'huaweicloudsdksms==3.1.144',
    'huaweicloudsdksmsapi==3.1.144',
    'huaweicloudsdksts==3.1.144',
    'huaweicloudsdkswr==3.1.144',
    'huaweicloudsdktics==3.1.144',
    'huaweicloudsdktms==3.1.144',
    'huaweicloudsdkugo==3.1.144',
    'huaweicloudsdkvas==3.1.144',
    'huaweicloudsdkvcm==3.1.144',
    'huaweicloudsdkvod==3.1.144',
    'huaweicloudsdkvpc==3.1.144',
    'huaweicloudsdkvpcep==3.1.144',
    'huaweicloudsdkvpn==3.1.144',
    'huaweicloudsdkwaf==3.1.144',
    'huaweicloudsdkworkspace==3.1.144',
    'huaweicloudsdkworkspaceapp==3.1.144',
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
