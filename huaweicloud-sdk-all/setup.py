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
VERSION = "3.1.108"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.108',
    'huaweicloudsdkaad==3.1.108',
    'huaweicloudsdkantiddos==3.1.108',
    'huaweicloudsdkaom==3.1.108',
    'huaweicloudsdkaos==3.1.108',
    'huaweicloudsdkapig==3.1.108',
    'huaweicloudsdkapm==3.1.108',
    'huaweicloudsdkas==3.1.108',
    'huaweicloudsdkasm==3.1.108',
    'huaweicloudsdkbcs==3.1.108',
    'huaweicloudsdkbms==3.1.108',
    'huaweicloudsdkbss==3.1.108',
    'huaweicloudsdkbssintl==3.1.108',
    'huaweicloudsdkcae==3.1.108',
    'huaweicloudsdkcampusgo==3.1.108',
    'huaweicloudsdkcbh==3.1.108',
    'huaweicloudsdkcbr==3.1.108',
    'huaweicloudsdkcbs==3.1.108',
    'huaweicloudsdkcc==3.1.108',
    'huaweicloudsdkcce==3.1.108',
    'huaweicloudsdkccm==3.1.108',
    'huaweicloudsdkcdm==3.1.108',
    'huaweicloudsdkcdn==3.1.108',
    'huaweicloudsdkces==3.1.108',
    'huaweicloudsdkcfw==3.1.108',
    'huaweicloudsdkcgs==3.1.108',
    'huaweicloudsdkclassroom==3.1.108',
    'huaweicloudsdkcloudide==3.1.108',
    'huaweicloudsdkcloudpond==3.1.108',
    'huaweicloudsdkcloudrtc==3.1.108',
    'huaweicloudsdkcloudtable==3.1.108',
    'huaweicloudsdkcloudtest==3.1.108',
    'huaweicloudsdkcodeartsartifact==3.1.108',
    'huaweicloudsdkcodeartsbuild==3.1.108',
    'huaweicloudsdkcodeartscheck==3.1.108',
    'huaweicloudsdkcodeartsdeploy==3.1.108',
    'huaweicloudsdkcodeartsgovernance==3.1.108',
    'huaweicloudsdkcodeartsinspector==3.1.108',
    'huaweicloudsdkcodeartspipeline==3.1.108',
    'huaweicloudsdkcodecraft==3.1.108',
    'huaweicloudsdkcodehub==3.1.108',
    'huaweicloudsdkconfig==3.1.108',
    'huaweicloudsdkcph==3.1.108',
    'huaweicloudsdkcpts==3.1.108',
    'huaweicloudsdkcse==3.1.108',
    'huaweicloudsdkcsms==3.1.108',
    'huaweicloudsdkcss==3.1.108',
    'huaweicloudsdkcts==3.1.108',
    'huaweicloudsdkdas==3.1.108',
    'huaweicloudsdkdataartsstudio==3.1.108',
    'huaweicloudsdkdbss==3.1.108',
    'huaweicloudsdkdc==3.1.108',
    'huaweicloudsdkdcs==3.1.108',
    'huaweicloudsdkddm==3.1.108',
    'huaweicloudsdkdds==3.1.108',
    'huaweicloudsdkdeh==3.1.108',
    'huaweicloudsdkdevstar==3.1.108',
    'huaweicloudsdkdgc==3.1.108',
    'huaweicloudsdkdis==3.1.108',
    'huaweicloudsdkdlf==3.1.108',
    'huaweicloudsdkdli==3.1.108',
    'huaweicloudsdkdns==3.1.108',
    'huaweicloudsdkdris==3.1.108',
    'huaweicloudsdkdrs==3.1.108',
    'huaweicloudsdkdsc==3.1.108',
    'huaweicloudsdkdwr==3.1.108',
    'huaweicloudsdkdws==3.1.108',
    'huaweicloudsdkec==3.1.108',
    'huaweicloudsdkecs==3.1.108',
    'huaweicloudsdkedgesec==3.1.108',
    'huaweicloudsdkeg==3.1.108',
    'huaweicloudsdkeihealth==3.1.108',
    'huaweicloudsdkeip==3.1.108',
    'huaweicloudsdkelb==3.1.108',
    'huaweicloudsdkeps==3.1.108',
    'huaweicloudsdker==3.1.108',
    'huaweicloudsdkevs==3.1.108',
    'huaweicloudsdkfrs==3.1.108',
    'huaweicloudsdkfunctiongraph==3.1.108',
    'huaweicloudsdkga==3.1.108',
    'huaweicloudsdkgaussdb==3.1.108',
    'huaweicloudsdkgaussdbfornosql==3.1.108',
    'huaweicloudsdkgaussdbforopengauss==3.1.108',
    'huaweicloudsdkgeip==3.1.108',
    'huaweicloudsdkges==3.1.108',
    'huaweicloudsdkgsl==3.1.108',
    'huaweicloudsdkhilens==3.1.108',
    'huaweicloudsdkhss==3.1.108',
    'huaweicloudsdkiam==3.1.108',
    'huaweicloudsdkiamaccessanalyzer==3.1.108',
    'huaweicloudsdkidentitycenter==3.1.108',
    'huaweicloudsdkidentitycenterstore==3.1.108',
    'huaweicloudsdkidme==3.1.108',
    'huaweicloudsdkidmeclassicapi==3.1.108',
    'huaweicloudsdkiec==3.1.108',
    'huaweicloudsdkief==3.1.108',
    'huaweicloudsdkimage==3.1.108',
    'huaweicloudsdkimagesearch==3.1.108',
    'huaweicloudsdkims==3.1.108',
    'huaweicloudsdkiotanalytics==3.1.108',
    'huaweicloudsdkiotda==3.1.108',
    'huaweicloudsdkiotedge==3.1.108',
    'huaweicloudsdkivs==3.1.108',
    'huaweicloudsdkkafka==3.1.108',
    'huaweicloudsdkkms==3.1.108',
    'huaweicloudsdkkoomessage==3.1.108',
    'huaweicloudsdkkps==3.1.108',
    'huaweicloudsdklakeformation==3.1.108',
    'huaweicloudsdklive==3.1.108',
    'huaweicloudsdklts==3.1.108',
    'huaweicloudsdkmapds==3.1.108',
    'huaweicloudsdkmas==3.1.108',
    'huaweicloudsdkmeeting==3.1.108',
    'huaweicloudsdkmetastudio==3.1.108',
    'huaweicloudsdkmoderation==3.1.108',
    'huaweicloudsdkmpc==3.1.108',
    'huaweicloudsdkmrs==3.1.108',
    'huaweicloudsdkmsgsms==3.1.108',
    'huaweicloudsdkmssi==3.1.108',
    'huaweicloudsdknat==3.1.108',
    'huaweicloudsdknlp==3.1.108',
    'huaweicloudsdkobs==3.1.108',
    'huaweicloudsdkocr==3.1.108',
    'huaweicloudsdkoctopus==3.1.108',
    'huaweicloudsdkoms==3.1.108',
    'huaweicloudsdkoptverse==3.1.108',
    'huaweicloudsdkorganizations==3.1.108',
    'huaweicloudsdkorgid==3.1.108',
    'huaweicloudsdkoroas==3.1.108',
    'huaweicloudsdkosm==3.1.108',
    'huaweicloudsdkpangulargemodels==3.1.108',
    'huaweicloudsdkprojectman==3.1.108',
    'huaweicloudsdkrabbitmq==3.1.108',
    'huaweicloudsdkram==3.1.108',
    'huaweicloudsdkrds==3.1.108',
    'huaweicloudsdkres==3.1.108',
    'huaweicloudsdkrgc==3.1.108',
    'huaweicloudsdkrms==3.1.108',
    'huaweicloudsdkrocketmq==3.1.108',
    'huaweicloudsdkroma==3.1.108',
    'huaweicloudsdksa==3.1.108',
    'huaweicloudsdkscm==3.1.108',
    'huaweicloudsdksdrs==3.1.108',
    'huaweicloudsdksecmaster==3.1.108',
    'huaweicloudsdkservicestage==3.1.108',
    'huaweicloudsdksfsturbo==3.1.108',
    'huaweicloudsdksis==3.1.108',
    'huaweicloudsdksmn==3.1.108',
    'huaweicloudsdksms==3.1.108',
    'huaweicloudsdksts==3.1.108',
    'huaweicloudsdkswr==3.1.108',
    'huaweicloudsdktics==3.1.108',
    'huaweicloudsdktms==3.1.108',
    'huaweicloudsdkugo==3.1.108',
    'huaweicloudsdkvas==3.1.108',
    'huaweicloudsdkvcm==3.1.108',
    'huaweicloudsdkvod==3.1.108',
    'huaweicloudsdkvpc==3.1.108',
    'huaweicloudsdkvpcep==3.1.108',
    'huaweicloudsdkvpn==3.1.108',
    'huaweicloudsdkwaf==3.1.108',
    'huaweicloudsdkworkspace==3.1.108',
    'huaweicloudsdkworkspaceapp==3.1.108',
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
