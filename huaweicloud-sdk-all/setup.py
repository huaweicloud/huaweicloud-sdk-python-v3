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
VERSION = "3.1.109"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.109',
    'huaweicloudsdkaad==3.1.109',
    'huaweicloudsdkantiddos==3.1.109',
    'huaweicloudsdkaom==3.1.109',
    'huaweicloudsdkaos==3.1.109',
    'huaweicloudsdkapig==3.1.109',
    'huaweicloudsdkapm==3.1.109',
    'huaweicloudsdkas==3.1.109',
    'huaweicloudsdkasm==3.1.109',
    'huaweicloudsdkbcs==3.1.109',
    'huaweicloudsdkbms==3.1.109',
    'huaweicloudsdkbss==3.1.109',
    'huaweicloudsdkbssintl==3.1.109',
    'huaweicloudsdkcae==3.1.109',
    'huaweicloudsdkcampusgo==3.1.109',
    'huaweicloudsdkcbh==3.1.109',
    'huaweicloudsdkcbr==3.1.109',
    'huaweicloudsdkcbs==3.1.109',
    'huaweicloudsdkcc==3.1.109',
    'huaweicloudsdkcce==3.1.109',
    'huaweicloudsdkccm==3.1.109',
    'huaweicloudsdkcdm==3.1.109',
    'huaweicloudsdkcdn==3.1.109',
    'huaweicloudsdkces==3.1.109',
    'huaweicloudsdkcfw==3.1.109',
    'huaweicloudsdkcgs==3.1.109',
    'huaweicloudsdkclassroom==3.1.109',
    'huaweicloudsdkcloudide==3.1.109',
    'huaweicloudsdkcloudpond==3.1.109',
    'huaweicloudsdkcloudrtc==3.1.109',
    'huaweicloudsdkcloudtable==3.1.109',
    'huaweicloudsdkcloudtest==3.1.109',
    'huaweicloudsdkcodeartsartifact==3.1.109',
    'huaweicloudsdkcodeartsbuild==3.1.109',
    'huaweicloudsdkcodeartscheck==3.1.109',
    'huaweicloudsdkcodeartsdeploy==3.1.109',
    'huaweicloudsdkcodeartsgovernance==3.1.109',
    'huaweicloudsdkcodeartsinspector==3.1.109',
    'huaweicloudsdkcodeartspipeline==3.1.109',
    'huaweicloudsdkcodecraft==3.1.109',
    'huaweicloudsdkcodehub==3.1.109',
    'huaweicloudsdkconfig==3.1.109',
    'huaweicloudsdkcph==3.1.109',
    'huaweicloudsdkcpts==3.1.109',
    'huaweicloudsdkcse==3.1.109',
    'huaweicloudsdkcsms==3.1.109',
    'huaweicloudsdkcss==3.1.109',
    'huaweicloudsdkcts==3.1.109',
    'huaweicloudsdkdas==3.1.109',
    'huaweicloudsdkdataartsstudio==3.1.109',
    'huaweicloudsdkdbss==3.1.109',
    'huaweicloudsdkdc==3.1.109',
    'huaweicloudsdkdcs==3.1.109',
    'huaweicloudsdkddm==3.1.109',
    'huaweicloudsdkdds==3.1.109',
    'huaweicloudsdkdeh==3.1.109',
    'huaweicloudsdkdevstar==3.1.109',
    'huaweicloudsdkdgc==3.1.109',
    'huaweicloudsdkdis==3.1.109',
    'huaweicloudsdkdlf==3.1.109',
    'huaweicloudsdkdli==3.1.109',
    'huaweicloudsdkdns==3.1.109',
    'huaweicloudsdkdris==3.1.109',
    'huaweicloudsdkdrs==3.1.109',
    'huaweicloudsdkdsc==3.1.109',
    'huaweicloudsdkdwr==3.1.109',
    'huaweicloudsdkdws==3.1.109',
    'huaweicloudsdkec==3.1.109',
    'huaweicloudsdkecs==3.1.109',
    'huaweicloudsdkedgesec==3.1.109',
    'huaweicloudsdkeg==3.1.109',
    'huaweicloudsdkeihealth==3.1.109',
    'huaweicloudsdkeip==3.1.109',
    'huaweicloudsdkelb==3.1.109',
    'huaweicloudsdkeps==3.1.109',
    'huaweicloudsdker==3.1.109',
    'huaweicloudsdkevs==3.1.109',
    'huaweicloudsdkfrs==3.1.109',
    'huaweicloudsdkfunctiongraph==3.1.109',
    'huaweicloudsdkga==3.1.109',
    'huaweicloudsdkgaussdb==3.1.109',
    'huaweicloudsdkgaussdbfornosql==3.1.109',
    'huaweicloudsdkgaussdbforopengauss==3.1.109',
    'huaweicloudsdkgeip==3.1.109',
    'huaweicloudsdkges==3.1.109',
    'huaweicloudsdkgsl==3.1.109',
    'huaweicloudsdkhilens==3.1.109',
    'huaweicloudsdkhss==3.1.109',
    'huaweicloudsdkiam==3.1.109',
    'huaweicloudsdkiamaccessanalyzer==3.1.109',
    'huaweicloudsdkidentitycenter==3.1.109',
    'huaweicloudsdkidentitycenterstore==3.1.109',
    'huaweicloudsdkidme==3.1.109',
    'huaweicloudsdkidmeclassicapi==3.1.109',
    'huaweicloudsdkiec==3.1.109',
    'huaweicloudsdkief==3.1.109',
    'huaweicloudsdkimage==3.1.109',
    'huaweicloudsdkimagesearch==3.1.109',
    'huaweicloudsdkims==3.1.109',
    'huaweicloudsdkiotanalytics==3.1.109',
    'huaweicloudsdkiotda==3.1.109',
    'huaweicloudsdkiotdm==3.1.109',
    'huaweicloudsdkiotedge==3.1.109',
    'huaweicloudsdkivs==3.1.109',
    'huaweicloudsdkkafka==3.1.109',
    'huaweicloudsdkkms==3.1.109',
    'huaweicloudsdkkoomessage==3.1.109',
    'huaweicloudsdkkps==3.1.109',
    'huaweicloudsdklakeformation==3.1.109',
    'huaweicloudsdklive==3.1.109',
    'huaweicloudsdklts==3.1.109',
    'huaweicloudsdkmapds==3.1.109',
    'huaweicloudsdkmas==3.1.109',
    'huaweicloudsdkmeeting==3.1.109',
    'huaweicloudsdkmetastudio==3.1.109',
    'huaweicloudsdkmoderation==3.1.109',
    'huaweicloudsdkmpc==3.1.109',
    'huaweicloudsdkmrs==3.1.109',
    'huaweicloudsdkmsgsms==3.1.109',
    'huaweicloudsdkmssi==3.1.109',
    'huaweicloudsdknat==3.1.109',
    'huaweicloudsdknlp==3.1.109',
    'huaweicloudsdkobs==3.1.109',
    'huaweicloudsdkocr==3.1.109',
    'huaweicloudsdkoctopus==3.1.109',
    'huaweicloudsdkoms==3.1.109',
    'huaweicloudsdkoptverse==3.1.109',
    'huaweicloudsdkorganizations==3.1.109',
    'huaweicloudsdkorgid==3.1.109',
    'huaweicloudsdkoroas==3.1.109',
    'huaweicloudsdkosm==3.1.109',
    'huaweicloudsdkpangulargemodels==3.1.109',
    'huaweicloudsdkprojectman==3.1.109',
    'huaweicloudsdkrabbitmq==3.1.109',
    'huaweicloudsdkram==3.1.109',
    'huaweicloudsdkrds==3.1.109',
    'huaweicloudsdkres==3.1.109',
    'huaweicloudsdkrgc==3.1.109',
    'huaweicloudsdkrms==3.1.109',
    'huaweicloudsdkrocketmq==3.1.109',
    'huaweicloudsdkroma==3.1.109',
    'huaweicloudsdksa==3.1.109',
    'huaweicloudsdkscm==3.1.109',
    'huaweicloudsdksdrs==3.1.109',
    'huaweicloudsdksecmaster==3.1.109',
    'huaweicloudsdkservicestage==3.1.109',
    'huaweicloudsdksfsturbo==3.1.109',
    'huaweicloudsdksis==3.1.109',
    'huaweicloudsdksmn==3.1.109',
    'huaweicloudsdksms==3.1.109',
    'huaweicloudsdksts==3.1.109',
    'huaweicloudsdkswr==3.1.109',
    'huaweicloudsdktics==3.1.109',
    'huaweicloudsdktms==3.1.109',
    'huaweicloudsdkugo==3.1.109',
    'huaweicloudsdkvas==3.1.109',
    'huaweicloudsdkvcm==3.1.109',
    'huaweicloudsdkvod==3.1.109',
    'huaweicloudsdkvpc==3.1.109',
    'huaweicloudsdkvpcep==3.1.109',
    'huaweicloudsdkvpn==3.1.109',
    'huaweicloudsdkwaf==3.1.109',
    'huaweicloudsdkworkspace==3.1.109',
    'huaweicloudsdkworkspaceapp==3.1.109',
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
