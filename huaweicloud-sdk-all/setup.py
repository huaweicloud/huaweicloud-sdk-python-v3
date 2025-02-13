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
VERSION = "3.1.135"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.135',
    'huaweicloudsdkaad==3.1.135',
    'huaweicloudsdkantiddos==3.1.135',
    'huaweicloudsdkaom==3.1.135',
    'huaweicloudsdkaos==3.1.135',
    'huaweicloudsdkapig==3.1.135',
    'huaweicloudsdkapm==3.1.135',
    'huaweicloudsdkas==3.1.135',
    'huaweicloudsdkasm==3.1.135',
    'huaweicloudsdkbcs==3.1.135',
    'huaweicloudsdkbms==3.1.135',
    'huaweicloudsdkbss==3.1.135',
    'huaweicloudsdkbssintl==3.1.135',
    'huaweicloudsdkcae==3.1.135',
    'huaweicloudsdkcampusgo==3.1.135',
    'huaweicloudsdkcbh==3.1.135',
    'huaweicloudsdkcbr==3.1.135',
    'huaweicloudsdkcbs==3.1.135',
    'huaweicloudsdkcc==3.1.135',
    'huaweicloudsdkcce==3.1.135',
    'huaweicloudsdkccm==3.1.135',
    'huaweicloudsdkcdm==3.1.135',
    'huaweicloudsdkcdn==3.1.135',
    'huaweicloudsdkces==3.1.135',
    'huaweicloudsdkcfw==3.1.135',
    'huaweicloudsdkcgs==3.1.135',
    'huaweicloudsdkclassroom==3.1.135',
    'huaweicloudsdkcloudide==3.1.135',
    'huaweicloudsdkcloudpond==3.1.135',
    'huaweicloudsdkcloudrtc==3.1.135',
    'huaweicloudsdkcloudtable==3.1.135',
    'huaweicloudsdkcloudtest==3.1.135',
    'huaweicloudsdkcoc==3.1.135',
    'huaweicloudsdkcodeartsartifact==3.1.135',
    'huaweicloudsdkcodeartsbuild==3.1.135',
    'huaweicloudsdkcodeartscheck==3.1.135',
    'huaweicloudsdkcodeartsdeploy==3.1.135',
    'huaweicloudsdkcodeartsgovernance==3.1.135',
    'huaweicloudsdkcodeartsinspector==3.1.135',
    'huaweicloudsdkcodeartspipeline==3.1.135',
    'huaweicloudsdkcodecraft==3.1.135',
    'huaweicloudsdkcodehub==3.1.135',
    'huaweicloudsdkconfig==3.1.135',
    'huaweicloudsdkcph==3.1.135',
    'huaweicloudsdkcpts==3.1.135',
    'huaweicloudsdkcse==3.1.135',
    'huaweicloudsdkcsms==3.1.135',
    'huaweicloudsdkcss==3.1.135',
    'huaweicloudsdkcts==3.1.135',
    'huaweicloudsdkdas==3.1.135',
    'huaweicloudsdkdataartsfabric==3.1.135',
    'huaweicloudsdkdataartsfabricep==3.1.135',
    'huaweicloudsdkdataartsstudio==3.1.135',
    'huaweicloudsdkdbss==3.1.135',
    'huaweicloudsdkdc==3.1.135',
    'huaweicloudsdkdcs==3.1.135',
    'huaweicloudsdkddm==3.1.135',
    'huaweicloudsdkdds==3.1.135',
    'huaweicloudsdkdeh==3.1.135',
    'huaweicloudsdkdevstar==3.1.135',
    'huaweicloudsdkdgc==3.1.135',
    'huaweicloudsdkdis==3.1.135',
    'huaweicloudsdkdlf==3.1.135',
    'huaweicloudsdkdli==3.1.135',
    'huaweicloudsdkdns==3.1.135',
    'huaweicloudsdkdris==3.1.135',
    'huaweicloudsdkdrs==3.1.135',
    'huaweicloudsdkdsc==3.1.135',
    'huaweicloudsdkdwr==3.1.135',
    'huaweicloudsdkdws==3.1.135',
    'huaweicloudsdkec==3.1.135',
    'huaweicloudsdkecs==3.1.135',
    'huaweicloudsdkedgesec==3.1.135',
    'huaweicloudsdkeg==3.1.135',
    'huaweicloudsdkeihealth==3.1.135',
    'huaweicloudsdkeip==3.1.135',
    'huaweicloudsdkelb==3.1.135',
    'huaweicloudsdkeps==3.1.135',
    'huaweicloudsdker==3.1.135',
    'huaweicloudsdkevs==3.1.135',
    'huaweicloudsdkfrs==3.1.135',
    'huaweicloudsdkfunctiongraph==3.1.135',
    'huaweicloudsdkga==3.1.135',
    'huaweicloudsdkgaussdb==3.1.135',
    'huaweicloudsdkgaussdbfornosql==3.1.135',
    'huaweicloudsdkgaussdbforopengauss==3.1.135',
    'huaweicloudsdkgeip==3.1.135',
    'huaweicloudsdkges==3.1.135',
    'huaweicloudsdkgsl==3.1.135',
    'huaweicloudsdkhilens==3.1.135',
    'huaweicloudsdkhss==3.1.135',
    'huaweicloudsdkiam==3.1.135',
    'huaweicloudsdkiamaccessanalyzer==3.1.135',
    'huaweicloudsdkidentitycenter==3.1.135',
    'huaweicloudsdkidentitycenterstore==3.1.135',
    'huaweicloudsdkidme==3.1.135',
    'huaweicloudsdkidmeclassicapi==3.1.135',
    'huaweicloudsdkiec==3.1.135',
    'huaweicloudsdkief==3.1.135',
    'huaweicloudsdkimage==3.1.135',
    'huaweicloudsdkimagesearch==3.1.135',
    'huaweicloudsdkims==3.1.135',
    'huaweicloudsdkiotanalytics==3.1.135',
    'huaweicloudsdkiotda==3.1.135',
    'huaweicloudsdkiotdm==3.1.135',
    'huaweicloudsdkiotedge==3.1.135',
    'huaweicloudsdkivs==3.1.135',
    'huaweicloudsdkkafka==3.1.135',
    'huaweicloudsdkkms==3.1.135',
    'huaweicloudsdkkoomessage==3.1.135',
    'huaweicloudsdkkps==3.1.135',
    'huaweicloudsdklakeformation==3.1.135',
    'huaweicloudsdklive==3.1.135',
    'huaweicloudsdklts==3.1.135',
    'huaweicloudsdkmapds==3.1.135',
    'huaweicloudsdkmas==3.1.135',
    'huaweicloudsdkmastudio==3.1.135',
    'huaweicloudsdkmeeting==3.1.135',
    'huaweicloudsdkmetastudio==3.1.135',
    'huaweicloudsdkmoderation==3.1.135',
    'huaweicloudsdkmpc==3.1.135',
    'huaweicloudsdkmrs==3.1.135',
    'huaweicloudsdkmsgsms==3.1.135',
    'huaweicloudsdkmssi==3.1.135',
    'huaweicloudsdknat==3.1.135',
    'huaweicloudsdknlp==3.1.135',
    'huaweicloudsdkobs==3.1.135',
    'huaweicloudsdkocr==3.1.135',
    'huaweicloudsdkoctopus==3.1.135',
    'huaweicloudsdkoms==3.1.135',
    'huaweicloudsdkoptverse==3.1.135',
    'huaweicloudsdkorganizations==3.1.135',
    'huaweicloudsdkorgid==3.1.135',
    'huaweicloudsdkoroas==3.1.135',
    'huaweicloudsdkosm==3.1.135',
    'huaweicloudsdkpangulargemodels==3.1.135',
    'huaweicloudsdkprojectman==3.1.135',
    'huaweicloudsdkrabbitmq==3.1.135',
    'huaweicloudsdkram==3.1.135',
    'huaweicloudsdkrds==3.1.135',
    'huaweicloudsdkres==3.1.135',
    'huaweicloudsdkrgc==3.1.135',
    'huaweicloudsdkrms==3.1.135',
    'huaweicloudsdkrocketmq==3.1.135',
    'huaweicloudsdkroma==3.1.135',
    'huaweicloudsdksa==3.1.135',
    'huaweicloudsdkscm==3.1.135',
    'huaweicloudsdksdrs==3.1.135',
    'huaweicloudsdksecmaster==3.1.135',
    'huaweicloudsdkservicestage==3.1.135',
    'huaweicloudsdksfsturbo==3.1.135',
    'huaweicloudsdksis==3.1.135',
    'huaweicloudsdksmn==3.1.135',
    'huaweicloudsdksms==3.1.135',
    'huaweicloudsdksmsapi==3.1.135',
    'huaweicloudsdksts==3.1.135',
    'huaweicloudsdkswr==3.1.135',
    'huaweicloudsdktics==3.1.135',
    'huaweicloudsdktms==3.1.135',
    'huaweicloudsdkugo==3.1.135',
    'huaweicloudsdkvas==3.1.135',
    'huaweicloudsdkvcm==3.1.135',
    'huaweicloudsdkvod==3.1.135',
    'huaweicloudsdkvpc==3.1.135',
    'huaweicloudsdkvpcep==3.1.135',
    'huaweicloudsdkvpn==3.1.135',
    'huaweicloudsdkwaf==3.1.135',
    'huaweicloudsdkworkspace==3.1.135',
    'huaweicloudsdkworkspaceapp==3.1.135',
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
