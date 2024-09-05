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
VERSION = "3.1.113"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.113',
    'huaweicloudsdkaad==3.1.113',
    'huaweicloudsdkantiddos==3.1.113',
    'huaweicloudsdkaom==3.1.113',
    'huaweicloudsdkaos==3.1.113',
    'huaweicloudsdkapig==3.1.113',
    'huaweicloudsdkapm==3.1.113',
    'huaweicloudsdkas==3.1.113',
    'huaweicloudsdkasm==3.1.113',
    'huaweicloudsdkbcs==3.1.113',
    'huaweicloudsdkbms==3.1.113',
    'huaweicloudsdkbss==3.1.113',
    'huaweicloudsdkbssintl==3.1.113',
    'huaweicloudsdkcae==3.1.113',
    'huaweicloudsdkcampusgo==3.1.113',
    'huaweicloudsdkcbh==3.1.113',
    'huaweicloudsdkcbr==3.1.113',
    'huaweicloudsdkcbs==3.1.113',
    'huaweicloudsdkcc==3.1.113',
    'huaweicloudsdkcce==3.1.113',
    'huaweicloudsdkccm==3.1.113',
    'huaweicloudsdkcdm==3.1.113',
    'huaweicloudsdkcdn==3.1.113',
    'huaweicloudsdkces==3.1.113',
    'huaweicloudsdkcfw==3.1.113',
    'huaweicloudsdkcgs==3.1.113',
    'huaweicloudsdkclassroom==3.1.113',
    'huaweicloudsdkcloudide==3.1.113',
    'huaweicloudsdkcloudpond==3.1.113',
    'huaweicloudsdkcloudrtc==3.1.113',
    'huaweicloudsdkcloudtable==3.1.113',
    'huaweicloudsdkcloudtest==3.1.113',
    'huaweicloudsdkcoc==3.1.113',
    'huaweicloudsdkcodeartsartifact==3.1.113',
    'huaweicloudsdkcodeartsbuild==3.1.113',
    'huaweicloudsdkcodeartscheck==3.1.113',
    'huaweicloudsdkcodeartsdeploy==3.1.113',
    'huaweicloudsdkcodeartsgovernance==3.1.113',
    'huaweicloudsdkcodeartsinspector==3.1.113',
    'huaweicloudsdkcodeartspipeline==3.1.113',
    'huaweicloudsdkcodecraft==3.1.113',
    'huaweicloudsdkcodehub==3.1.113',
    'huaweicloudsdkconfig==3.1.113',
    'huaweicloudsdkcph==3.1.113',
    'huaweicloudsdkcpts==3.1.113',
    'huaweicloudsdkcse==3.1.113',
    'huaweicloudsdkcsms==3.1.113',
    'huaweicloudsdkcss==3.1.113',
    'huaweicloudsdkcts==3.1.113',
    'huaweicloudsdkdas==3.1.113',
    'huaweicloudsdkdataartsstudio==3.1.113',
    'huaweicloudsdkdbss==3.1.113',
    'huaweicloudsdkdc==3.1.113',
    'huaweicloudsdkdcs==3.1.113',
    'huaweicloudsdkddm==3.1.113',
    'huaweicloudsdkdds==3.1.113',
    'huaweicloudsdkdeh==3.1.113',
    'huaweicloudsdkdevstar==3.1.113',
    'huaweicloudsdkdgc==3.1.113',
    'huaweicloudsdkdis==3.1.113',
    'huaweicloudsdkdlf==3.1.113',
    'huaweicloudsdkdli==3.1.113',
    'huaweicloudsdkdns==3.1.113',
    'huaweicloudsdkdris==3.1.113',
    'huaweicloudsdkdrs==3.1.113',
    'huaweicloudsdkdsc==3.1.113',
    'huaweicloudsdkdwr==3.1.113',
    'huaweicloudsdkdws==3.1.113',
    'huaweicloudsdkec==3.1.113',
    'huaweicloudsdkecs==3.1.113',
    'huaweicloudsdkedgesec==3.1.113',
    'huaweicloudsdkeg==3.1.113',
    'huaweicloudsdkeihealth==3.1.113',
    'huaweicloudsdkeip==3.1.113',
    'huaweicloudsdkelb==3.1.113',
    'huaweicloudsdkeps==3.1.113',
    'huaweicloudsdker==3.1.113',
    'huaweicloudsdkevs==3.1.113',
    'huaweicloudsdkfrs==3.1.113',
    'huaweicloudsdkfunctiongraph==3.1.113',
    'huaweicloudsdkga==3.1.113',
    'huaweicloudsdkgaussdb==3.1.113',
    'huaweicloudsdkgaussdbfornosql==3.1.113',
    'huaweicloudsdkgaussdbforopengauss==3.1.113',
    'huaweicloudsdkgeip==3.1.113',
    'huaweicloudsdkges==3.1.113',
    'huaweicloudsdkgsl==3.1.113',
    'huaweicloudsdkhilens==3.1.113',
    'huaweicloudsdkhss==3.1.113',
    'huaweicloudsdkiam==3.1.113',
    'huaweicloudsdkiamaccessanalyzer==3.1.113',
    'huaweicloudsdkidentitycenter==3.1.113',
    'huaweicloudsdkidentitycenterstore==3.1.113',
    'huaweicloudsdkidme==3.1.113',
    'huaweicloudsdkidmeclassicapi==3.1.113',
    'huaweicloudsdkiec==3.1.113',
    'huaweicloudsdkief==3.1.113',
    'huaweicloudsdkimage==3.1.113',
    'huaweicloudsdkimagesearch==3.1.113',
    'huaweicloudsdkims==3.1.113',
    'huaweicloudsdkiotanalytics==3.1.113',
    'huaweicloudsdkiotda==3.1.113',
    'huaweicloudsdkiotdm==3.1.113',
    'huaweicloudsdkiotedge==3.1.113',
    'huaweicloudsdkivs==3.1.113',
    'huaweicloudsdkkafka==3.1.113',
    'huaweicloudsdkkms==3.1.113',
    'huaweicloudsdkkoomessage==3.1.113',
    'huaweicloudsdkkps==3.1.113',
    'huaweicloudsdklakeformation==3.1.113',
    'huaweicloudsdklive==3.1.113',
    'huaweicloudsdklts==3.1.113',
    'huaweicloudsdkmapds==3.1.113',
    'huaweicloudsdkmas==3.1.113',
    'huaweicloudsdkmeeting==3.1.113',
    'huaweicloudsdkmetastudio==3.1.113',
    'huaweicloudsdkmoderation==3.1.113',
    'huaweicloudsdkmpc==3.1.113',
    'huaweicloudsdkmrs==3.1.113',
    'huaweicloudsdkmsgsms==3.1.113',
    'huaweicloudsdkmssi==3.1.113',
    'huaweicloudsdknat==3.1.113',
    'huaweicloudsdknlp==3.1.113',
    'huaweicloudsdkobs==3.1.113',
    'huaweicloudsdkocr==3.1.113',
    'huaweicloudsdkoctopus==3.1.113',
    'huaweicloudsdkoms==3.1.113',
    'huaweicloudsdkoptverse==3.1.113',
    'huaweicloudsdkorganizations==3.1.113',
    'huaweicloudsdkorgid==3.1.113',
    'huaweicloudsdkoroas==3.1.113',
    'huaweicloudsdkosm==3.1.113',
    'huaweicloudsdkpangulargemodels==3.1.113',
    'huaweicloudsdkprojectman==3.1.113',
    'huaweicloudsdkrabbitmq==3.1.113',
    'huaweicloudsdkram==3.1.113',
    'huaweicloudsdkrds==3.1.113',
    'huaweicloudsdkres==3.1.113',
    'huaweicloudsdkrgc==3.1.113',
    'huaweicloudsdkrms==3.1.113',
    'huaweicloudsdkrocketmq==3.1.113',
    'huaweicloudsdkroma==3.1.113',
    'huaweicloudsdksa==3.1.113',
    'huaweicloudsdkscm==3.1.113',
    'huaweicloudsdksdrs==3.1.113',
    'huaweicloudsdksecmaster==3.1.113',
    'huaweicloudsdkservicestage==3.1.113',
    'huaweicloudsdksfsturbo==3.1.113',
    'huaweicloudsdksis==3.1.113',
    'huaweicloudsdksmn==3.1.113',
    'huaweicloudsdksms==3.1.113',
    'huaweicloudsdksts==3.1.113',
    'huaweicloudsdkswr==3.1.113',
    'huaweicloudsdktics==3.1.113',
    'huaweicloudsdktms==3.1.113',
    'huaweicloudsdkugo==3.1.113',
    'huaweicloudsdkvas==3.1.113',
    'huaweicloudsdkvcm==3.1.113',
    'huaweicloudsdkvod==3.1.113',
    'huaweicloudsdkvpc==3.1.113',
    'huaweicloudsdkvpcep==3.1.113',
    'huaweicloudsdkvpn==3.1.113',
    'huaweicloudsdkwaf==3.1.113',
    'huaweicloudsdkworkspace==3.1.113',
    'huaweicloudsdkworkspaceapp==3.1.113',
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
