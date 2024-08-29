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
VERSION = "3.1.112"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.112',
    'huaweicloudsdkaad==3.1.112',
    'huaweicloudsdkantiddos==3.1.112',
    'huaweicloudsdkaom==3.1.112',
    'huaweicloudsdkaos==3.1.112',
    'huaweicloudsdkapig==3.1.112',
    'huaweicloudsdkapm==3.1.112',
    'huaweicloudsdkas==3.1.112',
    'huaweicloudsdkasm==3.1.112',
    'huaweicloudsdkbcs==3.1.112',
    'huaweicloudsdkbms==3.1.112',
    'huaweicloudsdkbss==3.1.112',
    'huaweicloudsdkbssintl==3.1.112',
    'huaweicloudsdkcae==3.1.112',
    'huaweicloudsdkcampusgo==3.1.112',
    'huaweicloudsdkcbh==3.1.112',
    'huaweicloudsdkcbr==3.1.112',
    'huaweicloudsdkcbs==3.1.112',
    'huaweicloudsdkcc==3.1.112',
    'huaweicloudsdkcce==3.1.112',
    'huaweicloudsdkccm==3.1.112',
    'huaweicloudsdkcdm==3.1.112',
    'huaweicloudsdkcdn==3.1.112',
    'huaweicloudsdkces==3.1.112',
    'huaweicloudsdkcfw==3.1.112',
    'huaweicloudsdkcgs==3.1.112',
    'huaweicloudsdkclassroom==3.1.112',
    'huaweicloudsdkcloudide==3.1.112',
    'huaweicloudsdkcloudpond==3.1.112',
    'huaweicloudsdkcloudrtc==3.1.112',
    'huaweicloudsdkcloudtable==3.1.112',
    'huaweicloudsdkcloudtest==3.1.112',
    'huaweicloudsdkcoc==3.1.112',
    'huaweicloudsdkcodeartsartifact==3.1.112',
    'huaweicloudsdkcodeartsbuild==3.1.112',
    'huaweicloudsdkcodeartscheck==3.1.112',
    'huaweicloudsdkcodeartsdeploy==3.1.112',
    'huaweicloudsdkcodeartsgovernance==3.1.112',
    'huaweicloudsdkcodeartsinspector==3.1.112',
    'huaweicloudsdkcodeartspipeline==3.1.112',
    'huaweicloudsdkcodecraft==3.1.112',
    'huaweicloudsdkcodehub==3.1.112',
    'huaweicloudsdkconfig==3.1.112',
    'huaweicloudsdkcph==3.1.112',
    'huaweicloudsdkcpts==3.1.112',
    'huaweicloudsdkcse==3.1.112',
    'huaweicloudsdkcsms==3.1.112',
    'huaweicloudsdkcss==3.1.112',
    'huaweicloudsdkcts==3.1.112',
    'huaweicloudsdkdas==3.1.112',
    'huaweicloudsdkdataartsstudio==3.1.112',
    'huaweicloudsdkdbss==3.1.112',
    'huaweicloudsdkdc==3.1.112',
    'huaweicloudsdkdcs==3.1.112',
    'huaweicloudsdkddm==3.1.112',
    'huaweicloudsdkdds==3.1.112',
    'huaweicloudsdkdeh==3.1.112',
    'huaweicloudsdkdevstar==3.1.112',
    'huaweicloudsdkdgc==3.1.112',
    'huaweicloudsdkdis==3.1.112',
    'huaweicloudsdkdlf==3.1.112',
    'huaweicloudsdkdli==3.1.112',
    'huaweicloudsdkdns==3.1.112',
    'huaweicloudsdkdris==3.1.112',
    'huaweicloudsdkdrs==3.1.112',
    'huaweicloudsdkdsc==3.1.112',
    'huaweicloudsdkdwr==3.1.112',
    'huaweicloudsdkdws==3.1.112',
    'huaweicloudsdkec==3.1.112',
    'huaweicloudsdkecs==3.1.112',
    'huaweicloudsdkedgesec==3.1.112',
    'huaweicloudsdkeg==3.1.112',
    'huaweicloudsdkeihealth==3.1.112',
    'huaweicloudsdkeip==3.1.112',
    'huaweicloudsdkelb==3.1.112',
    'huaweicloudsdkeps==3.1.112',
    'huaweicloudsdker==3.1.112',
    'huaweicloudsdkevs==3.1.112',
    'huaweicloudsdkfrs==3.1.112',
    'huaweicloudsdkfunctiongraph==3.1.112',
    'huaweicloudsdkga==3.1.112',
    'huaweicloudsdkgaussdb==3.1.112',
    'huaweicloudsdkgaussdbfornosql==3.1.112',
    'huaweicloudsdkgaussdbforopengauss==3.1.112',
    'huaweicloudsdkgeip==3.1.112',
    'huaweicloudsdkges==3.1.112',
    'huaweicloudsdkgsl==3.1.112',
    'huaweicloudsdkhilens==3.1.112',
    'huaweicloudsdkhss==3.1.112',
    'huaweicloudsdkiam==3.1.112',
    'huaweicloudsdkiamaccessanalyzer==3.1.112',
    'huaweicloudsdkidentitycenter==3.1.112',
    'huaweicloudsdkidentitycenterstore==3.1.112',
    'huaweicloudsdkidme==3.1.112',
    'huaweicloudsdkidmeclassicapi==3.1.112',
    'huaweicloudsdkiec==3.1.112',
    'huaweicloudsdkief==3.1.112',
    'huaweicloudsdkimage==3.1.112',
    'huaweicloudsdkimagesearch==3.1.112',
    'huaweicloudsdkims==3.1.112',
    'huaweicloudsdkiotanalytics==3.1.112',
    'huaweicloudsdkiotda==3.1.112',
    'huaweicloudsdkiotdm==3.1.112',
    'huaweicloudsdkiotedge==3.1.112',
    'huaweicloudsdkivs==3.1.112',
    'huaweicloudsdkkafka==3.1.112',
    'huaweicloudsdkkms==3.1.112',
    'huaweicloudsdkkoomessage==3.1.112',
    'huaweicloudsdkkps==3.1.112',
    'huaweicloudsdklakeformation==3.1.112',
    'huaweicloudsdklive==3.1.112',
    'huaweicloudsdklts==3.1.112',
    'huaweicloudsdkmapds==3.1.112',
    'huaweicloudsdkmas==3.1.112',
    'huaweicloudsdkmeeting==3.1.112',
    'huaweicloudsdkmetastudio==3.1.112',
    'huaweicloudsdkmoderation==3.1.112',
    'huaweicloudsdkmpc==3.1.112',
    'huaweicloudsdkmrs==3.1.112',
    'huaweicloudsdkmsgsms==3.1.112',
    'huaweicloudsdkmssi==3.1.112',
    'huaweicloudsdknat==3.1.112',
    'huaweicloudsdknlp==3.1.112',
    'huaweicloudsdkobs==3.1.112',
    'huaweicloudsdkocr==3.1.112',
    'huaweicloudsdkoctopus==3.1.112',
    'huaweicloudsdkoms==3.1.112',
    'huaweicloudsdkoptverse==3.1.112',
    'huaweicloudsdkorganizations==3.1.112',
    'huaweicloudsdkorgid==3.1.112',
    'huaweicloudsdkoroas==3.1.112',
    'huaweicloudsdkosm==3.1.112',
    'huaweicloudsdkpangulargemodels==3.1.112',
    'huaweicloudsdkprojectman==3.1.112',
    'huaweicloudsdkrabbitmq==3.1.112',
    'huaweicloudsdkram==3.1.112',
    'huaweicloudsdkrds==3.1.112',
    'huaweicloudsdkres==3.1.112',
    'huaweicloudsdkrgc==3.1.112',
    'huaweicloudsdkrms==3.1.112',
    'huaweicloudsdkrocketmq==3.1.112',
    'huaweicloudsdkroma==3.1.112',
    'huaweicloudsdksa==3.1.112',
    'huaweicloudsdkscm==3.1.112',
    'huaweicloudsdksdrs==3.1.112',
    'huaweicloudsdksecmaster==3.1.112',
    'huaweicloudsdkservicestage==3.1.112',
    'huaweicloudsdksfsturbo==3.1.112',
    'huaweicloudsdksis==3.1.112',
    'huaweicloudsdksmn==3.1.112',
    'huaweicloudsdksms==3.1.112',
    'huaweicloudsdksts==3.1.112',
    'huaweicloudsdkswr==3.1.112',
    'huaweicloudsdktics==3.1.112',
    'huaweicloudsdktms==3.1.112',
    'huaweicloudsdkugo==3.1.112',
    'huaweicloudsdkvas==3.1.112',
    'huaweicloudsdkvcm==3.1.112',
    'huaweicloudsdkvod==3.1.112',
    'huaweicloudsdkvpc==3.1.112',
    'huaweicloudsdkvpcep==3.1.112',
    'huaweicloudsdkvpn==3.1.112',
    'huaweicloudsdkwaf==3.1.112',
    'huaweicloudsdkworkspace==3.1.112',
    'huaweicloudsdkworkspaceapp==3.1.112',
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
