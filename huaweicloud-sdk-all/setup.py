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
VERSION = "3.1.85"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.85',
    'huaweicloudsdkaad==3.1.85',
    'huaweicloudsdkantiddos==3.1.85',
    'huaweicloudsdkaom==3.1.85',
    'huaweicloudsdkaos==3.1.85',
    'huaweicloudsdkapig==3.1.85',
    'huaweicloudsdkapm==3.1.85',
    'huaweicloudsdkas==3.1.85',
    'huaweicloudsdkasm==3.1.85',
    'huaweicloudsdkbcs==3.1.85',
    'huaweicloudsdkbms==3.1.85',
    'huaweicloudsdkbss==3.1.85',
    'huaweicloudsdkbssintl==3.1.85',
    'huaweicloudsdkcae==3.1.85',
    'huaweicloudsdkcampusgo==3.1.85',
    'huaweicloudsdkcbh==3.1.85',
    'huaweicloudsdkcbr==3.1.85',
    'huaweicloudsdkcbs==3.1.85',
    'huaweicloudsdkcc==3.1.85',
    'huaweicloudsdkcce==3.1.85',
    'huaweicloudsdkccm==3.1.85',
    'huaweicloudsdkcdm==3.1.85',
    'huaweicloudsdkcdn==3.1.85',
    'huaweicloudsdkces==3.1.85',
    'huaweicloudsdkcfw==3.1.85',
    'huaweicloudsdkcgs==3.1.85',
    'huaweicloudsdkclassroom==3.1.85',
    'huaweicloudsdkcloudide==3.1.85',
    'huaweicloudsdkcloudpond==3.1.85',
    'huaweicloudsdkcloudrtc==3.1.85',
    'huaweicloudsdkcloudtable==3.1.85',
    'huaweicloudsdkcloudtest==3.1.85',
    'huaweicloudsdkcodeartsartifact==3.1.85',
    'huaweicloudsdkcodeartsbuild==3.1.85',
    'huaweicloudsdkcodeartscheck==3.1.85',
    'huaweicloudsdkcodeartsdeploy==3.1.85',
    'huaweicloudsdkcodeartsinspector==3.1.85',
    'huaweicloudsdkcodeartspipeline==3.1.85',
    'huaweicloudsdkcodecraft==3.1.85',
    'huaweicloudsdkcodehub==3.1.85',
    'huaweicloudsdkconfig==3.1.85',
    'huaweicloudsdkcph==3.1.85',
    'huaweicloudsdkcpts==3.1.85',
    'huaweicloudsdkcse==3.1.85',
    'huaweicloudsdkcsms==3.1.85',
    'huaweicloudsdkcss==3.1.85',
    'huaweicloudsdkcts==3.1.85',
    'huaweicloudsdkdas==3.1.85',
    'huaweicloudsdkdataartsstudio==3.1.85',
    'huaweicloudsdkdbss==3.1.85',
    'huaweicloudsdkdc==3.1.85',
    'huaweicloudsdkdcs==3.1.85',
    'huaweicloudsdkddm==3.1.85',
    'huaweicloudsdkdds==3.1.85',
    'huaweicloudsdkdeh==3.1.85',
    'huaweicloudsdkdevsecurity==3.1.85',
    'huaweicloudsdkdevstar==3.1.85',
    'huaweicloudsdkdgc==3.1.85',
    'huaweicloudsdkdis==3.1.85',
    'huaweicloudsdkdlf==3.1.85',
    'huaweicloudsdkdli==3.1.85',
    'huaweicloudsdkdns==3.1.85',
    'huaweicloudsdkdris==3.1.85',
    'huaweicloudsdkdrs==3.1.85',
    'huaweicloudsdkdsc==3.1.85',
    'huaweicloudsdkdwr==3.1.85',
    'huaweicloudsdkdws==3.1.85',
    'huaweicloudsdkec==3.1.85',
    'huaweicloudsdkecs==3.1.85',
    'huaweicloudsdkedgesec==3.1.85',
    'huaweicloudsdkeg==3.1.85',
    'huaweicloudsdkeihealth==3.1.85',
    'huaweicloudsdkeip==3.1.85',
    'huaweicloudsdkelb==3.1.85',
    'huaweicloudsdkeps==3.1.85',
    'huaweicloudsdker==3.1.85',
    'huaweicloudsdkevs==3.1.85',
    'huaweicloudsdkfrs==3.1.85',
    'huaweicloudsdkfunctiongraph==3.1.85',
    'huaweicloudsdkga==3.1.85',
    'huaweicloudsdkgaussdb==3.1.85',
    'huaweicloudsdkgaussdbfornosql==3.1.85',
    'huaweicloudsdkgaussdbforopengauss==3.1.85',
    'huaweicloudsdkgeip==3.1.85',
    'huaweicloudsdkges==3.1.85',
    'huaweicloudsdkgsl==3.1.85',
    'huaweicloudsdkhilens==3.1.85',
    'huaweicloudsdkhss==3.1.85',
    'huaweicloudsdkiam==3.1.85',
    'huaweicloudsdkiamaccessanalyzer==3.1.85',
    'huaweicloudsdkidentitycenter==3.1.85',
    'huaweicloudsdkidentitycenterstore==3.1.85',
    'huaweicloudsdkidme==3.1.85',
    'huaweicloudsdkidmeclassicapi==3.1.85',
    'huaweicloudsdkiec==3.1.85',
    'huaweicloudsdkief==3.1.85',
    'huaweicloudsdkimage==3.1.85',
    'huaweicloudsdkimagesearch==3.1.85',
    'huaweicloudsdkims==3.1.85',
    'huaweicloudsdkiotanalytics==3.1.85',
    'huaweicloudsdkiotda==3.1.85',
    'huaweicloudsdkiotedge==3.1.85',
    'huaweicloudsdkivs==3.1.85',
    'huaweicloudsdkkafka==3.1.85',
    'huaweicloudsdkkms==3.1.85',
    'huaweicloudsdkkoomessage==3.1.85',
    'huaweicloudsdkkps==3.1.85',
    'huaweicloudsdklakeformation==3.1.85',
    'huaweicloudsdklive==3.1.85',
    'huaweicloudsdklts==3.1.85',
    'huaweicloudsdkmapds==3.1.85',
    'huaweicloudsdkmas==3.1.85',
    'huaweicloudsdkmeeting==3.1.85',
    'huaweicloudsdkmetastudio==3.1.85',
    'huaweicloudsdkmoderation==3.1.85',
    'huaweicloudsdkmpc==3.1.85',
    'huaweicloudsdkmrs==3.1.85',
    'huaweicloudsdkmsgsms==3.1.85',
    'huaweicloudsdkmssi==3.1.85',
    'huaweicloudsdknat==3.1.85',
    'huaweicloudsdknlp==3.1.85',
    'huaweicloudsdkobs==3.1.85',
    'huaweicloudsdkocr==3.1.85',
    'huaweicloudsdkoctopus==3.1.85',
    'huaweicloudsdkoms==3.1.85',
    'huaweicloudsdkoptverse==3.1.85',
    'huaweicloudsdkorganizations==3.1.85',
    'huaweicloudsdkorgid==3.1.85',
    'huaweicloudsdkoroas==3.1.85',
    'huaweicloudsdkosm==3.1.85',
    'huaweicloudsdkpangulargemodels==3.1.85',
    'huaweicloudsdkprojectman==3.1.85',
    'huaweicloudsdkrabbitmq==3.1.85',
    'huaweicloudsdkram==3.1.85',
    'huaweicloudsdkrds==3.1.85',
    'huaweicloudsdkres==3.1.85',
    'huaweicloudsdkrgc==3.1.85',
    'huaweicloudsdkrms==3.1.85',
    'huaweicloudsdkrocketmq==3.1.85',
    'huaweicloudsdkroma==3.1.85',
    'huaweicloudsdksa==3.1.85',
    'huaweicloudsdkscm==3.1.85',
    'huaweicloudsdksdrs==3.1.85',
    'huaweicloudsdksecmaster==3.1.85',
    'huaweicloudsdkservicestage==3.1.85',
    'huaweicloudsdksfsturbo==3.1.85',
    'huaweicloudsdksis==3.1.85',
    'huaweicloudsdksmn==3.1.85',
    'huaweicloudsdksms==3.1.85',
    'huaweicloudsdkswr==3.1.85',
    'huaweicloudsdktics==3.1.85',
    'huaweicloudsdktms==3.1.85',
    'huaweicloudsdkugo==3.1.85',
    'huaweicloudsdkvas==3.1.85',
    'huaweicloudsdkvcm==3.1.85',
    'huaweicloudsdkvod==3.1.85',
    'huaweicloudsdkvpc==3.1.85',
    'huaweicloudsdkvpcep==3.1.85',
    'huaweicloudsdkvpn==3.1.85',
    'huaweicloudsdkwaf==3.1.85',
    'huaweicloudsdkworkspace==3.1.85',
    'huaweicloudsdkworkspaceapp==3.1.85',
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
