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
VERSION = "3.1.111"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.111',
    'huaweicloudsdkaad==3.1.111',
    'huaweicloudsdkantiddos==3.1.111',
    'huaweicloudsdkaom==3.1.111',
    'huaweicloudsdkaos==3.1.111',
    'huaweicloudsdkapig==3.1.111',
    'huaweicloudsdkapm==3.1.111',
    'huaweicloudsdkas==3.1.111',
    'huaweicloudsdkasm==3.1.111',
    'huaweicloudsdkbcs==3.1.111',
    'huaweicloudsdkbms==3.1.111',
    'huaweicloudsdkbss==3.1.111',
    'huaweicloudsdkbssintl==3.1.111',
    'huaweicloudsdkcae==3.1.111',
    'huaweicloudsdkcampusgo==3.1.111',
    'huaweicloudsdkcbh==3.1.111',
    'huaweicloudsdkcbr==3.1.111',
    'huaweicloudsdkcbs==3.1.111',
    'huaweicloudsdkcc==3.1.111',
    'huaweicloudsdkcce==3.1.111',
    'huaweicloudsdkccm==3.1.111',
    'huaweicloudsdkcdm==3.1.111',
    'huaweicloudsdkcdn==3.1.111',
    'huaweicloudsdkces==3.1.111',
    'huaweicloudsdkcfw==3.1.111',
    'huaweicloudsdkcgs==3.1.111',
    'huaweicloudsdkclassroom==3.1.111',
    'huaweicloudsdkcloudide==3.1.111',
    'huaweicloudsdkcloudpond==3.1.111',
    'huaweicloudsdkcloudrtc==3.1.111',
    'huaweicloudsdkcloudtable==3.1.111',
    'huaweicloudsdkcloudtest==3.1.111',
    'huaweicloudsdkcoc==3.1.111',
    'huaweicloudsdkcodeartsartifact==3.1.111',
    'huaweicloudsdkcodeartsbuild==3.1.111',
    'huaweicloudsdkcodeartscheck==3.1.111',
    'huaweicloudsdkcodeartsdeploy==3.1.111',
    'huaweicloudsdkcodeartsgovernance==3.1.111',
    'huaweicloudsdkcodeartsinspector==3.1.111',
    'huaweicloudsdkcodeartspipeline==3.1.111',
    'huaweicloudsdkcodecraft==3.1.111',
    'huaweicloudsdkcodehub==3.1.111',
    'huaweicloudsdkconfig==3.1.111',
    'huaweicloudsdkcph==3.1.111',
    'huaweicloudsdkcpts==3.1.111',
    'huaweicloudsdkcse==3.1.111',
    'huaweicloudsdkcsms==3.1.111',
    'huaweicloudsdkcss==3.1.111',
    'huaweicloudsdkcts==3.1.111',
    'huaweicloudsdkdas==3.1.111',
    'huaweicloudsdkdataartsstudio==3.1.111',
    'huaweicloudsdkdbss==3.1.111',
    'huaweicloudsdkdc==3.1.111',
    'huaweicloudsdkdcs==3.1.111',
    'huaweicloudsdkddm==3.1.111',
    'huaweicloudsdkdds==3.1.111',
    'huaweicloudsdkdeh==3.1.111',
    'huaweicloudsdkdevstar==3.1.111',
    'huaweicloudsdkdgc==3.1.111',
    'huaweicloudsdkdis==3.1.111',
    'huaweicloudsdkdlf==3.1.111',
    'huaweicloudsdkdli==3.1.111',
    'huaweicloudsdkdns==3.1.111',
    'huaweicloudsdkdris==3.1.111',
    'huaweicloudsdkdrs==3.1.111',
    'huaweicloudsdkdsc==3.1.111',
    'huaweicloudsdkdwr==3.1.111',
    'huaweicloudsdkdws==3.1.111',
    'huaweicloudsdkec==3.1.111',
    'huaweicloudsdkecs==3.1.111',
    'huaweicloudsdkedgesec==3.1.111',
    'huaweicloudsdkeg==3.1.111',
    'huaweicloudsdkeihealth==3.1.111',
    'huaweicloudsdkeip==3.1.111',
    'huaweicloudsdkelb==3.1.111',
    'huaweicloudsdkeps==3.1.111',
    'huaweicloudsdker==3.1.111',
    'huaweicloudsdkevs==3.1.111',
    'huaweicloudsdkfrs==3.1.111',
    'huaweicloudsdkfunctiongraph==3.1.111',
    'huaweicloudsdkga==3.1.111',
    'huaweicloudsdkgaussdb==3.1.111',
    'huaweicloudsdkgaussdbfornosql==3.1.111',
    'huaweicloudsdkgaussdbforopengauss==3.1.111',
    'huaweicloudsdkgeip==3.1.111',
    'huaweicloudsdkges==3.1.111',
    'huaweicloudsdkgsl==3.1.111',
    'huaweicloudsdkhilens==3.1.111',
    'huaweicloudsdkhss==3.1.111',
    'huaweicloudsdkiam==3.1.111',
    'huaweicloudsdkiamaccessanalyzer==3.1.111',
    'huaweicloudsdkidentitycenter==3.1.111',
    'huaweicloudsdkidentitycenterstore==3.1.111',
    'huaweicloudsdkidme==3.1.111',
    'huaweicloudsdkidmeclassicapi==3.1.111',
    'huaweicloudsdkiec==3.1.111',
    'huaweicloudsdkief==3.1.111',
    'huaweicloudsdkimage==3.1.111',
    'huaweicloudsdkimagesearch==3.1.111',
    'huaweicloudsdkims==3.1.111',
    'huaweicloudsdkiotanalytics==3.1.111',
    'huaweicloudsdkiotda==3.1.111',
    'huaweicloudsdkiotdm==3.1.111',
    'huaweicloudsdkiotedge==3.1.111',
    'huaweicloudsdkivs==3.1.111',
    'huaweicloudsdkkafka==3.1.111',
    'huaweicloudsdkkms==3.1.111',
    'huaweicloudsdkkoomessage==3.1.111',
    'huaweicloudsdkkps==3.1.111',
    'huaweicloudsdklakeformation==3.1.111',
    'huaweicloudsdklive==3.1.111',
    'huaweicloudsdklts==3.1.111',
    'huaweicloudsdkmapds==3.1.111',
    'huaweicloudsdkmas==3.1.111',
    'huaweicloudsdkmeeting==3.1.111',
    'huaweicloudsdkmetastudio==3.1.111',
    'huaweicloudsdkmoderation==3.1.111',
    'huaweicloudsdkmpc==3.1.111',
    'huaweicloudsdkmrs==3.1.111',
    'huaweicloudsdkmsgsms==3.1.111',
    'huaweicloudsdkmssi==3.1.111',
    'huaweicloudsdknat==3.1.111',
    'huaweicloudsdknlp==3.1.111',
    'huaweicloudsdkobs==3.1.111',
    'huaweicloudsdkocr==3.1.111',
    'huaweicloudsdkoctopus==3.1.111',
    'huaweicloudsdkoms==3.1.111',
    'huaweicloudsdkoptverse==3.1.111',
    'huaweicloudsdkorganizations==3.1.111',
    'huaweicloudsdkorgid==3.1.111',
    'huaweicloudsdkoroas==3.1.111',
    'huaweicloudsdkosm==3.1.111',
    'huaweicloudsdkpangulargemodels==3.1.111',
    'huaweicloudsdkprojectman==3.1.111',
    'huaweicloudsdkrabbitmq==3.1.111',
    'huaweicloudsdkram==3.1.111',
    'huaweicloudsdkrds==3.1.111',
    'huaweicloudsdkres==3.1.111',
    'huaweicloudsdkrgc==3.1.111',
    'huaweicloudsdkrms==3.1.111',
    'huaweicloudsdkrocketmq==3.1.111',
    'huaweicloudsdkroma==3.1.111',
    'huaweicloudsdksa==3.1.111',
    'huaweicloudsdkscm==3.1.111',
    'huaweicloudsdksdrs==3.1.111',
    'huaweicloudsdksecmaster==3.1.111',
    'huaweicloudsdkservicestage==3.1.111',
    'huaweicloudsdksfsturbo==3.1.111',
    'huaweicloudsdksis==3.1.111',
    'huaweicloudsdksmn==3.1.111',
    'huaweicloudsdksms==3.1.111',
    'huaweicloudsdksts==3.1.111',
    'huaweicloudsdkswr==3.1.111',
    'huaweicloudsdktics==3.1.111',
    'huaweicloudsdktms==3.1.111',
    'huaweicloudsdkugo==3.1.111',
    'huaweicloudsdkvas==3.1.111',
    'huaweicloudsdkvcm==3.1.111',
    'huaweicloudsdkvod==3.1.111',
    'huaweicloudsdkvpc==3.1.111',
    'huaweicloudsdkvpcep==3.1.111',
    'huaweicloudsdkvpn==3.1.111',
    'huaweicloudsdkwaf==3.1.111',
    'huaweicloudsdkworkspace==3.1.111',
    'huaweicloudsdkworkspaceapp==3.1.111',
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
