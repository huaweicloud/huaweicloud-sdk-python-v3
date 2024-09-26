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
VERSION = "3.1.116"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.116',
    'huaweicloudsdkaad==3.1.116',
    'huaweicloudsdkantiddos==3.1.116',
    'huaweicloudsdkaom==3.1.116',
    'huaweicloudsdkaos==3.1.116',
    'huaweicloudsdkapig==3.1.116',
    'huaweicloudsdkapm==3.1.116',
    'huaweicloudsdkas==3.1.116',
    'huaweicloudsdkasm==3.1.116',
    'huaweicloudsdkbcs==3.1.116',
    'huaweicloudsdkbms==3.1.116',
    'huaweicloudsdkbss==3.1.116',
    'huaweicloudsdkbssintl==3.1.116',
    'huaweicloudsdkcae==3.1.116',
    'huaweicloudsdkcampusgo==3.1.116',
    'huaweicloudsdkcbh==3.1.116',
    'huaweicloudsdkcbr==3.1.116',
    'huaweicloudsdkcbs==3.1.116',
    'huaweicloudsdkcc==3.1.116',
    'huaweicloudsdkcce==3.1.116',
    'huaweicloudsdkccm==3.1.116',
    'huaweicloudsdkcdm==3.1.116',
    'huaweicloudsdkcdn==3.1.116',
    'huaweicloudsdkces==3.1.116',
    'huaweicloudsdkcfw==3.1.116',
    'huaweicloudsdkcgs==3.1.116',
    'huaweicloudsdkclassroom==3.1.116',
    'huaweicloudsdkcloudide==3.1.116',
    'huaweicloudsdkcloudpond==3.1.116',
    'huaweicloudsdkcloudrtc==3.1.116',
    'huaweicloudsdkcloudtable==3.1.116',
    'huaweicloudsdkcloudtest==3.1.116',
    'huaweicloudsdkcoc==3.1.116',
    'huaweicloudsdkcodeartsartifact==3.1.116',
    'huaweicloudsdkcodeartsbuild==3.1.116',
    'huaweicloudsdkcodeartscheck==3.1.116',
    'huaweicloudsdkcodeartsdeploy==3.1.116',
    'huaweicloudsdkcodeartsgovernance==3.1.116',
    'huaweicloudsdkcodeartsinspector==3.1.116',
    'huaweicloudsdkcodeartspipeline==3.1.116',
    'huaweicloudsdkcodecraft==3.1.116',
    'huaweicloudsdkcodehub==3.1.116',
    'huaweicloudsdkconfig==3.1.116',
    'huaweicloudsdkcph==3.1.116',
    'huaweicloudsdkcpts==3.1.116',
    'huaweicloudsdkcse==3.1.116',
    'huaweicloudsdkcsms==3.1.116',
    'huaweicloudsdkcss==3.1.116',
    'huaweicloudsdkcts==3.1.116',
    'huaweicloudsdkdas==3.1.116',
    'huaweicloudsdkdataartsstudio==3.1.116',
    'huaweicloudsdkdbss==3.1.116',
    'huaweicloudsdkdc==3.1.116',
    'huaweicloudsdkdcs==3.1.116',
    'huaweicloudsdkddm==3.1.116',
    'huaweicloudsdkdds==3.1.116',
    'huaweicloudsdkdeh==3.1.116',
    'huaweicloudsdkdevstar==3.1.116',
    'huaweicloudsdkdgc==3.1.116',
    'huaweicloudsdkdis==3.1.116',
    'huaweicloudsdkdlf==3.1.116',
    'huaweicloudsdkdli==3.1.116',
    'huaweicloudsdkdns==3.1.116',
    'huaweicloudsdkdris==3.1.116',
    'huaweicloudsdkdrs==3.1.116',
    'huaweicloudsdkdsc==3.1.116',
    'huaweicloudsdkdwr==3.1.116',
    'huaweicloudsdkdws==3.1.116',
    'huaweicloudsdkec==3.1.116',
    'huaweicloudsdkecs==3.1.116',
    'huaweicloudsdkedgesec==3.1.116',
    'huaweicloudsdkeg==3.1.116',
    'huaweicloudsdkeihealth==3.1.116',
    'huaweicloudsdkeip==3.1.116',
    'huaweicloudsdkelb==3.1.116',
    'huaweicloudsdkeps==3.1.116',
    'huaweicloudsdker==3.1.116',
    'huaweicloudsdkevs==3.1.116',
    'huaweicloudsdkfrs==3.1.116',
    'huaweicloudsdkfunctiongraph==3.1.116',
    'huaweicloudsdkga==3.1.116',
    'huaweicloudsdkgaussdb==3.1.116',
    'huaweicloudsdkgaussdbfornosql==3.1.116',
    'huaweicloudsdkgaussdbforopengauss==3.1.116',
    'huaweicloudsdkgeip==3.1.116',
    'huaweicloudsdkges==3.1.116',
    'huaweicloudsdkgsl==3.1.116',
    'huaweicloudsdkhilens==3.1.116',
    'huaweicloudsdkhss==3.1.116',
    'huaweicloudsdkiam==3.1.116',
    'huaweicloudsdkiamaccessanalyzer==3.1.116',
    'huaweicloudsdkidentitycenter==3.1.116',
    'huaweicloudsdkidentitycenterstore==3.1.116',
    'huaweicloudsdkidme==3.1.116',
    'huaweicloudsdkidmeclassicapi==3.1.116',
    'huaweicloudsdkiec==3.1.116',
    'huaweicloudsdkief==3.1.116',
    'huaweicloudsdkimage==3.1.116',
    'huaweicloudsdkimagesearch==3.1.116',
    'huaweicloudsdkims==3.1.116',
    'huaweicloudsdkiotanalytics==3.1.116',
    'huaweicloudsdkiotda==3.1.116',
    'huaweicloudsdkiotdm==3.1.116',
    'huaweicloudsdkiotedge==3.1.116',
    'huaweicloudsdkivs==3.1.116',
    'huaweicloudsdkkafka==3.1.116',
    'huaweicloudsdkkms==3.1.116',
    'huaweicloudsdkkoomessage==3.1.116',
    'huaweicloudsdkkps==3.1.116',
    'huaweicloudsdklakeformation==3.1.116',
    'huaweicloudsdklive==3.1.116',
    'huaweicloudsdklts==3.1.116',
    'huaweicloudsdkmapds==3.1.116',
    'huaweicloudsdkmas==3.1.116',
    'huaweicloudsdkmeeting==3.1.116',
    'huaweicloudsdkmetastudio==3.1.116',
    'huaweicloudsdkmoderation==3.1.116',
    'huaweicloudsdkmpc==3.1.116',
    'huaweicloudsdkmrs==3.1.116',
    'huaweicloudsdkmsgsms==3.1.116',
    'huaweicloudsdkmssi==3.1.116',
    'huaweicloudsdknat==3.1.116',
    'huaweicloudsdknlp==3.1.116',
    'huaweicloudsdkobs==3.1.116',
    'huaweicloudsdkocr==3.1.116',
    'huaweicloudsdkoctopus==3.1.116',
    'huaweicloudsdkoms==3.1.116',
    'huaweicloudsdkoptverse==3.1.116',
    'huaweicloudsdkorganizations==3.1.116',
    'huaweicloudsdkorgid==3.1.116',
    'huaweicloudsdkoroas==3.1.116',
    'huaweicloudsdkosm==3.1.116',
    'huaweicloudsdkpangulargemodels==3.1.116',
    'huaweicloudsdkprojectman==3.1.116',
    'huaweicloudsdkrabbitmq==3.1.116',
    'huaweicloudsdkram==3.1.116',
    'huaweicloudsdkrds==3.1.116',
    'huaweicloudsdkres==3.1.116',
    'huaweicloudsdkrgc==3.1.116',
    'huaweicloudsdkrms==3.1.116',
    'huaweicloudsdkrocketmq==3.1.116',
    'huaweicloudsdkroma==3.1.116',
    'huaweicloudsdksa==3.1.116',
    'huaweicloudsdkscm==3.1.116',
    'huaweicloudsdksdrs==3.1.116',
    'huaweicloudsdksecmaster==3.1.116',
    'huaweicloudsdkservicestage==3.1.116',
    'huaweicloudsdksfsturbo==3.1.116',
    'huaweicloudsdksis==3.1.116',
    'huaweicloudsdksmn==3.1.116',
    'huaweicloudsdksms==3.1.116',
    'huaweicloudsdksts==3.1.116',
    'huaweicloudsdkswr==3.1.116',
    'huaweicloudsdktics==3.1.116',
    'huaweicloudsdktms==3.1.116',
    'huaweicloudsdkugo==3.1.116',
    'huaweicloudsdkvas==3.1.116',
    'huaweicloudsdkvcm==3.1.116',
    'huaweicloudsdkvod==3.1.116',
    'huaweicloudsdkvpc==3.1.116',
    'huaweicloudsdkvpcep==3.1.116',
    'huaweicloudsdkvpn==3.1.116',
    'huaweicloudsdkwaf==3.1.116',
    'huaweicloudsdkworkspace==3.1.116',
    'huaweicloudsdkworkspaceapp==3.1.116',
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
