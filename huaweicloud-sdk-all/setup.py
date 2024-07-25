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
VERSION = "3.1.107"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.107',
    'huaweicloudsdkaad==3.1.107',
    'huaweicloudsdkantiddos==3.1.107',
    'huaweicloudsdkaom==3.1.107',
    'huaweicloudsdkaos==3.1.107',
    'huaweicloudsdkapig==3.1.107',
    'huaweicloudsdkapm==3.1.107',
    'huaweicloudsdkas==3.1.107',
    'huaweicloudsdkasm==3.1.107',
    'huaweicloudsdkbcs==3.1.107',
    'huaweicloudsdkbms==3.1.107',
    'huaweicloudsdkbss==3.1.107',
    'huaweicloudsdkbssintl==3.1.107',
    'huaweicloudsdkcae==3.1.107',
    'huaweicloudsdkcampusgo==3.1.107',
    'huaweicloudsdkcbh==3.1.107',
    'huaweicloudsdkcbr==3.1.107',
    'huaweicloudsdkcbs==3.1.107',
    'huaweicloudsdkcc==3.1.107',
    'huaweicloudsdkcce==3.1.107',
    'huaweicloudsdkccm==3.1.107',
    'huaweicloudsdkcdm==3.1.107',
    'huaweicloudsdkcdn==3.1.107',
    'huaweicloudsdkces==3.1.107',
    'huaweicloudsdkcfw==3.1.107',
    'huaweicloudsdkcgs==3.1.107',
    'huaweicloudsdkclassroom==3.1.107',
    'huaweicloudsdkcloudide==3.1.107',
    'huaweicloudsdkcloudpond==3.1.107',
    'huaweicloudsdkcloudrtc==3.1.107',
    'huaweicloudsdkcloudtable==3.1.107',
    'huaweicloudsdkcloudtest==3.1.107',
    'huaweicloudsdkcodeartsartifact==3.1.107',
    'huaweicloudsdkcodeartsbuild==3.1.107',
    'huaweicloudsdkcodeartscheck==3.1.107',
    'huaweicloudsdkcodeartsdeploy==3.1.107',
    'huaweicloudsdkcodeartsgovernance==3.1.107',
    'huaweicloudsdkcodeartsinspector==3.1.107',
    'huaweicloudsdkcodeartspipeline==3.1.107',
    'huaweicloudsdkcodecraft==3.1.107',
    'huaweicloudsdkcodehub==3.1.107',
    'huaweicloudsdkconfig==3.1.107',
    'huaweicloudsdkcph==3.1.107',
    'huaweicloudsdkcpts==3.1.107',
    'huaweicloudsdkcse==3.1.107',
    'huaweicloudsdkcsms==3.1.107',
    'huaweicloudsdkcss==3.1.107',
    'huaweicloudsdkcts==3.1.107',
    'huaweicloudsdkdas==3.1.107',
    'huaweicloudsdkdataartsstudio==3.1.107',
    'huaweicloudsdkdbss==3.1.107',
    'huaweicloudsdkdc==3.1.107',
    'huaweicloudsdkdcs==3.1.107',
    'huaweicloudsdkddm==3.1.107',
    'huaweicloudsdkdds==3.1.107',
    'huaweicloudsdkdeh==3.1.107',
    'huaweicloudsdkdevstar==3.1.107',
    'huaweicloudsdkdgc==3.1.107',
    'huaweicloudsdkdis==3.1.107',
    'huaweicloudsdkdlf==3.1.107',
    'huaweicloudsdkdli==3.1.107',
    'huaweicloudsdkdns==3.1.107',
    'huaweicloudsdkdris==3.1.107',
    'huaweicloudsdkdrs==3.1.107',
    'huaweicloudsdkdsc==3.1.107',
    'huaweicloudsdkdwr==3.1.107',
    'huaweicloudsdkdws==3.1.107',
    'huaweicloudsdkec==3.1.107',
    'huaweicloudsdkecs==3.1.107',
    'huaweicloudsdkedgesec==3.1.107',
    'huaweicloudsdkeg==3.1.107',
    'huaweicloudsdkeihealth==3.1.107',
    'huaweicloudsdkeip==3.1.107',
    'huaweicloudsdkelb==3.1.107',
    'huaweicloudsdkeps==3.1.107',
    'huaweicloudsdker==3.1.107',
    'huaweicloudsdkevs==3.1.107',
    'huaweicloudsdkfrs==3.1.107',
    'huaweicloudsdkfunctiongraph==3.1.107',
    'huaweicloudsdkga==3.1.107',
    'huaweicloudsdkgaussdb==3.1.107',
    'huaweicloudsdkgaussdbfornosql==3.1.107',
    'huaweicloudsdkgaussdbforopengauss==3.1.107',
    'huaweicloudsdkgeip==3.1.107',
    'huaweicloudsdkges==3.1.107',
    'huaweicloudsdkgsl==3.1.107',
    'huaweicloudsdkhilens==3.1.107',
    'huaweicloudsdkhss==3.1.107',
    'huaweicloudsdkiam==3.1.107',
    'huaweicloudsdkiamaccessanalyzer==3.1.107',
    'huaweicloudsdkidentitycenter==3.1.107',
    'huaweicloudsdkidentitycenterstore==3.1.107',
    'huaweicloudsdkidme==3.1.107',
    'huaweicloudsdkidmeclassicapi==3.1.107',
    'huaweicloudsdkiec==3.1.107',
    'huaweicloudsdkief==3.1.107',
    'huaweicloudsdkimage==3.1.107',
    'huaweicloudsdkimagesearch==3.1.107',
    'huaweicloudsdkims==3.1.107',
    'huaweicloudsdkiotanalytics==3.1.107',
    'huaweicloudsdkiotda==3.1.107',
    'huaweicloudsdkiotedge==3.1.107',
    'huaweicloudsdkivs==3.1.107',
    'huaweicloudsdkkafka==3.1.107',
    'huaweicloudsdkkms==3.1.107',
    'huaweicloudsdkkoomessage==3.1.107',
    'huaweicloudsdkkps==3.1.107',
    'huaweicloudsdklakeformation==3.1.107',
    'huaweicloudsdklive==3.1.107',
    'huaweicloudsdklts==3.1.107',
    'huaweicloudsdkmapds==3.1.107',
    'huaweicloudsdkmas==3.1.107',
    'huaweicloudsdkmeeting==3.1.107',
    'huaweicloudsdkmetastudio==3.1.107',
    'huaweicloudsdkmoderation==3.1.107',
    'huaweicloudsdkmpc==3.1.107',
    'huaweicloudsdkmrs==3.1.107',
    'huaweicloudsdkmsgsms==3.1.107',
    'huaweicloudsdkmssi==3.1.107',
    'huaweicloudsdknat==3.1.107',
    'huaweicloudsdknlp==3.1.107',
    'huaweicloudsdkobs==3.1.107',
    'huaweicloudsdkocr==3.1.107',
    'huaweicloudsdkoctopus==3.1.107',
    'huaweicloudsdkoms==3.1.107',
    'huaweicloudsdkoptverse==3.1.107',
    'huaweicloudsdkorganizations==3.1.107',
    'huaweicloudsdkorgid==3.1.107',
    'huaweicloudsdkoroas==3.1.107',
    'huaweicloudsdkosm==3.1.107',
    'huaweicloudsdkpangulargemodels==3.1.107',
    'huaweicloudsdkprojectman==3.1.107',
    'huaweicloudsdkrabbitmq==3.1.107',
    'huaweicloudsdkram==3.1.107',
    'huaweicloudsdkrds==3.1.107',
    'huaweicloudsdkres==3.1.107',
    'huaweicloudsdkrgc==3.1.107',
    'huaweicloudsdkrms==3.1.107',
    'huaweicloudsdkrocketmq==3.1.107',
    'huaweicloudsdkroma==3.1.107',
    'huaweicloudsdksa==3.1.107',
    'huaweicloudsdkscm==3.1.107',
    'huaweicloudsdksdrs==3.1.107',
    'huaweicloudsdksecmaster==3.1.107',
    'huaweicloudsdkservicestage==3.1.107',
    'huaweicloudsdksfsturbo==3.1.107',
    'huaweicloudsdksis==3.1.107',
    'huaweicloudsdksmn==3.1.107',
    'huaweicloudsdksms==3.1.107',
    'huaweicloudsdksts==3.1.107',
    'huaweicloudsdkswr==3.1.107',
    'huaweicloudsdktics==3.1.107',
    'huaweicloudsdktms==3.1.107',
    'huaweicloudsdkugo==3.1.107',
    'huaweicloudsdkvas==3.1.107',
    'huaweicloudsdkvcm==3.1.107',
    'huaweicloudsdkvod==3.1.107',
    'huaweicloudsdkvpc==3.1.107',
    'huaweicloudsdkvpcep==3.1.107',
    'huaweicloudsdkvpn==3.1.107',
    'huaweicloudsdkwaf==3.1.107',
    'huaweicloudsdkworkspace==3.1.107',
    'huaweicloudsdkworkspaceapp==3.1.107',
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
