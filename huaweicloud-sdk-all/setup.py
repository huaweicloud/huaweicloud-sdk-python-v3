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
VERSION = "3.1.118"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.118',
    'huaweicloudsdkaad==3.1.118',
    'huaweicloudsdkantiddos==3.1.118',
    'huaweicloudsdkaom==3.1.118',
    'huaweicloudsdkaos==3.1.118',
    'huaweicloudsdkapig==3.1.118',
    'huaweicloudsdkapm==3.1.118',
    'huaweicloudsdkas==3.1.118',
    'huaweicloudsdkasm==3.1.118',
    'huaweicloudsdkbcs==3.1.118',
    'huaweicloudsdkbms==3.1.118',
    'huaweicloudsdkbss==3.1.118',
    'huaweicloudsdkbssintl==3.1.118',
    'huaweicloudsdkcae==3.1.118',
    'huaweicloudsdkcampusgo==3.1.118',
    'huaweicloudsdkcbh==3.1.118',
    'huaweicloudsdkcbr==3.1.118',
    'huaweicloudsdkcbs==3.1.118',
    'huaweicloudsdkcc==3.1.118',
    'huaweicloudsdkcce==3.1.118',
    'huaweicloudsdkccm==3.1.118',
    'huaweicloudsdkcdm==3.1.118',
    'huaweicloudsdkcdn==3.1.118',
    'huaweicloudsdkces==3.1.118',
    'huaweicloudsdkcfw==3.1.118',
    'huaweicloudsdkcgs==3.1.118',
    'huaweicloudsdkclassroom==3.1.118',
    'huaweicloudsdkcloudide==3.1.118',
    'huaweicloudsdkcloudpond==3.1.118',
    'huaweicloudsdkcloudrtc==3.1.118',
    'huaweicloudsdkcloudtable==3.1.118',
    'huaweicloudsdkcloudtest==3.1.118',
    'huaweicloudsdkcoc==3.1.118',
    'huaweicloudsdkcodeartsartifact==3.1.118',
    'huaweicloudsdkcodeartsbuild==3.1.118',
    'huaweicloudsdkcodeartscheck==3.1.118',
    'huaweicloudsdkcodeartsdeploy==3.1.118',
    'huaweicloudsdkcodeartsgovernance==3.1.118',
    'huaweicloudsdkcodeartsinspector==3.1.118',
    'huaweicloudsdkcodeartspipeline==3.1.118',
    'huaweicloudsdkcodecraft==3.1.118',
    'huaweicloudsdkcodehub==3.1.118',
    'huaweicloudsdkconfig==3.1.118',
    'huaweicloudsdkcph==3.1.118',
    'huaweicloudsdkcpts==3.1.118',
    'huaweicloudsdkcse==3.1.118',
    'huaweicloudsdkcsms==3.1.118',
    'huaweicloudsdkcss==3.1.118',
    'huaweicloudsdkcts==3.1.118',
    'huaweicloudsdkdas==3.1.118',
    'huaweicloudsdkdataartsstudio==3.1.118',
    'huaweicloudsdkdbss==3.1.118',
    'huaweicloudsdkdc==3.1.118',
    'huaweicloudsdkdcs==3.1.118',
    'huaweicloudsdkddm==3.1.118',
    'huaweicloudsdkdds==3.1.118',
    'huaweicloudsdkdeh==3.1.118',
    'huaweicloudsdkdevstar==3.1.118',
    'huaweicloudsdkdgc==3.1.118',
    'huaweicloudsdkdis==3.1.118',
    'huaweicloudsdkdlf==3.1.118',
    'huaweicloudsdkdli==3.1.118',
    'huaweicloudsdkdns==3.1.118',
    'huaweicloudsdkdris==3.1.118',
    'huaweicloudsdkdrs==3.1.118',
    'huaweicloudsdkdsc==3.1.118',
    'huaweicloudsdkdwr==3.1.118',
    'huaweicloudsdkdws==3.1.118',
    'huaweicloudsdkec==3.1.118',
    'huaweicloudsdkecs==3.1.118',
    'huaweicloudsdkedgesec==3.1.118',
    'huaweicloudsdkeg==3.1.118',
    'huaweicloudsdkeihealth==3.1.118',
    'huaweicloudsdkeip==3.1.118',
    'huaweicloudsdkelb==3.1.118',
    'huaweicloudsdkeps==3.1.118',
    'huaweicloudsdker==3.1.118',
    'huaweicloudsdkevs==3.1.118',
    'huaweicloudsdkfrs==3.1.118',
    'huaweicloudsdkfunctiongraph==3.1.118',
    'huaweicloudsdkga==3.1.118',
    'huaweicloudsdkgaussdb==3.1.118',
    'huaweicloudsdkgaussdbfornosql==3.1.118',
    'huaweicloudsdkgaussdbforopengauss==3.1.118',
    'huaweicloudsdkgeip==3.1.118',
    'huaweicloudsdkges==3.1.118',
    'huaweicloudsdkgsl==3.1.118',
    'huaweicloudsdkhilens==3.1.118',
    'huaweicloudsdkhss==3.1.118',
    'huaweicloudsdkiam==3.1.118',
    'huaweicloudsdkiamaccessanalyzer==3.1.118',
    'huaweicloudsdkidentitycenter==3.1.118',
    'huaweicloudsdkidentitycenterstore==3.1.118',
    'huaweicloudsdkidme==3.1.118',
    'huaweicloudsdkidmeclassicapi==3.1.118',
    'huaweicloudsdkiec==3.1.118',
    'huaweicloudsdkief==3.1.118',
    'huaweicloudsdkimage==3.1.118',
    'huaweicloudsdkimagesearch==3.1.118',
    'huaweicloudsdkims==3.1.118',
    'huaweicloudsdkiotanalytics==3.1.118',
    'huaweicloudsdkiotda==3.1.118',
    'huaweicloudsdkiotdm==3.1.118',
    'huaweicloudsdkiotedge==3.1.118',
    'huaweicloudsdkivs==3.1.118',
    'huaweicloudsdkkafka==3.1.118',
    'huaweicloudsdkkms==3.1.118',
    'huaweicloudsdkkoomessage==3.1.118',
    'huaweicloudsdkkps==3.1.118',
    'huaweicloudsdklakeformation==3.1.118',
    'huaweicloudsdklive==3.1.118',
    'huaweicloudsdklts==3.1.118',
    'huaweicloudsdkmapds==3.1.118',
    'huaweicloudsdkmas==3.1.118',
    'huaweicloudsdkmeeting==3.1.118',
    'huaweicloudsdkmetastudio==3.1.118',
    'huaweicloudsdkmoderation==3.1.118',
    'huaweicloudsdkmpc==3.1.118',
    'huaweicloudsdkmrs==3.1.118',
    'huaweicloudsdkmsgsms==3.1.118',
    'huaweicloudsdkmssi==3.1.118',
    'huaweicloudsdknat==3.1.118',
    'huaweicloudsdknlp==3.1.118',
    'huaweicloudsdkobs==3.1.118',
    'huaweicloudsdkocr==3.1.118',
    'huaweicloudsdkoctopus==3.1.118',
    'huaweicloudsdkoms==3.1.118',
    'huaweicloudsdkoptverse==3.1.118',
    'huaweicloudsdkorganizations==3.1.118',
    'huaweicloudsdkorgid==3.1.118',
    'huaweicloudsdkoroas==3.1.118',
    'huaweicloudsdkosm==3.1.118',
    'huaweicloudsdkpangulargemodels==3.1.118',
    'huaweicloudsdkprojectman==3.1.118',
    'huaweicloudsdkrabbitmq==3.1.118',
    'huaweicloudsdkram==3.1.118',
    'huaweicloudsdkrds==3.1.118',
    'huaweicloudsdkres==3.1.118',
    'huaweicloudsdkrgc==3.1.118',
    'huaweicloudsdkrms==3.1.118',
    'huaweicloudsdkrocketmq==3.1.118',
    'huaweicloudsdkroma==3.1.118',
    'huaweicloudsdksa==3.1.118',
    'huaweicloudsdkscm==3.1.118',
    'huaweicloudsdksdrs==3.1.118',
    'huaweicloudsdksecmaster==3.1.118',
    'huaweicloudsdkservicestage==3.1.118',
    'huaweicloudsdksfsturbo==3.1.118',
    'huaweicloudsdksis==3.1.118',
    'huaweicloudsdksmn==3.1.118',
    'huaweicloudsdksms==3.1.118',
    'huaweicloudsdksts==3.1.118',
    'huaweicloudsdkswr==3.1.118',
    'huaweicloudsdktics==3.1.118',
    'huaweicloudsdktms==3.1.118',
    'huaweicloudsdkugo==3.1.118',
    'huaweicloudsdkvas==3.1.118',
    'huaweicloudsdkvcm==3.1.118',
    'huaweicloudsdkvod==3.1.118',
    'huaweicloudsdkvpc==3.1.118',
    'huaweicloudsdkvpcep==3.1.118',
    'huaweicloudsdkvpn==3.1.118',
    'huaweicloudsdkwaf==3.1.118',
    'huaweicloudsdkworkspace==3.1.118',
    'huaweicloudsdkworkspaceapp==3.1.118',
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
