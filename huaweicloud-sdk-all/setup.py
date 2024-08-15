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
VERSION = "3.1.110"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.110',
    'huaweicloudsdkaad==3.1.110',
    'huaweicloudsdkantiddos==3.1.110',
    'huaweicloudsdkaom==3.1.110',
    'huaweicloudsdkaos==3.1.110',
    'huaweicloudsdkapig==3.1.110',
    'huaweicloudsdkapm==3.1.110',
    'huaweicloudsdkas==3.1.110',
    'huaweicloudsdkasm==3.1.110',
    'huaweicloudsdkbcs==3.1.110',
    'huaweicloudsdkbms==3.1.110',
    'huaweicloudsdkbss==3.1.110',
    'huaweicloudsdkbssintl==3.1.110',
    'huaweicloudsdkcae==3.1.110',
    'huaweicloudsdkcampusgo==3.1.110',
    'huaweicloudsdkcbh==3.1.110',
    'huaweicloudsdkcbr==3.1.110',
    'huaweicloudsdkcbs==3.1.110',
    'huaweicloudsdkcc==3.1.110',
    'huaweicloudsdkcce==3.1.110',
    'huaweicloudsdkccm==3.1.110',
    'huaweicloudsdkcdm==3.1.110',
    'huaweicloudsdkcdn==3.1.110',
    'huaweicloudsdkces==3.1.110',
    'huaweicloudsdkcfw==3.1.110',
    'huaweicloudsdkcgs==3.1.110',
    'huaweicloudsdkclassroom==3.1.110',
    'huaweicloudsdkcloudide==3.1.110',
    'huaweicloudsdkcloudpond==3.1.110',
    'huaweicloudsdkcloudrtc==3.1.110',
    'huaweicloudsdkcloudtable==3.1.110',
    'huaweicloudsdkcloudtest==3.1.110',
    'huaweicloudsdkcoc==3.1.110',
    'huaweicloudsdkcodeartsartifact==3.1.110',
    'huaweicloudsdkcodeartsbuild==3.1.110',
    'huaweicloudsdkcodeartscheck==3.1.110',
    'huaweicloudsdkcodeartsdeploy==3.1.110',
    'huaweicloudsdkcodeartsgovernance==3.1.110',
    'huaweicloudsdkcodeartsinspector==3.1.110',
    'huaweicloudsdkcodeartspipeline==3.1.110',
    'huaweicloudsdkcodecraft==3.1.110',
    'huaweicloudsdkcodehub==3.1.110',
    'huaweicloudsdkconfig==3.1.110',
    'huaweicloudsdkcph==3.1.110',
    'huaweicloudsdkcpts==3.1.110',
    'huaweicloudsdkcse==3.1.110',
    'huaweicloudsdkcsms==3.1.110',
    'huaweicloudsdkcss==3.1.110',
    'huaweicloudsdkcts==3.1.110',
    'huaweicloudsdkdas==3.1.110',
    'huaweicloudsdkdataartsstudio==3.1.110',
    'huaweicloudsdkdbss==3.1.110',
    'huaweicloudsdkdc==3.1.110',
    'huaweicloudsdkdcs==3.1.110',
    'huaweicloudsdkddm==3.1.110',
    'huaweicloudsdkdds==3.1.110',
    'huaweicloudsdkdeh==3.1.110',
    'huaweicloudsdkdevstar==3.1.110',
    'huaweicloudsdkdgc==3.1.110',
    'huaweicloudsdkdis==3.1.110',
    'huaweicloudsdkdlf==3.1.110',
    'huaweicloudsdkdli==3.1.110',
    'huaweicloudsdkdns==3.1.110',
    'huaweicloudsdkdris==3.1.110',
    'huaweicloudsdkdrs==3.1.110',
    'huaweicloudsdkdsc==3.1.110',
    'huaweicloudsdkdwr==3.1.110',
    'huaweicloudsdkdws==3.1.110',
    'huaweicloudsdkec==3.1.110',
    'huaweicloudsdkecs==3.1.110',
    'huaweicloudsdkedgesec==3.1.110',
    'huaweicloudsdkeg==3.1.110',
    'huaweicloudsdkeihealth==3.1.110',
    'huaweicloudsdkeip==3.1.110',
    'huaweicloudsdkelb==3.1.110',
    'huaweicloudsdkeps==3.1.110',
    'huaweicloudsdker==3.1.110',
    'huaweicloudsdkevs==3.1.110',
    'huaweicloudsdkfrs==3.1.110',
    'huaweicloudsdkfunctiongraph==3.1.110',
    'huaweicloudsdkga==3.1.110',
    'huaweicloudsdkgaussdb==3.1.110',
    'huaweicloudsdkgaussdbfornosql==3.1.110',
    'huaweicloudsdkgaussdbforopengauss==3.1.110',
    'huaweicloudsdkgeip==3.1.110',
    'huaweicloudsdkges==3.1.110',
    'huaweicloudsdkgsl==3.1.110',
    'huaweicloudsdkhilens==3.1.110',
    'huaweicloudsdkhss==3.1.110',
    'huaweicloudsdkiam==3.1.110',
    'huaweicloudsdkiamaccessanalyzer==3.1.110',
    'huaweicloudsdkidentitycenter==3.1.110',
    'huaweicloudsdkidentitycenterstore==3.1.110',
    'huaweicloudsdkidme==3.1.110',
    'huaweicloudsdkidmeclassicapi==3.1.110',
    'huaweicloudsdkiec==3.1.110',
    'huaweicloudsdkief==3.1.110',
    'huaweicloudsdkimage==3.1.110',
    'huaweicloudsdkimagesearch==3.1.110',
    'huaweicloudsdkims==3.1.110',
    'huaweicloudsdkiotanalytics==3.1.110',
    'huaweicloudsdkiotda==3.1.110',
    'huaweicloudsdkiotdm==3.1.110',
    'huaweicloudsdkiotedge==3.1.110',
    'huaweicloudsdkivs==3.1.110',
    'huaweicloudsdkkafka==3.1.110',
    'huaweicloudsdkkms==3.1.110',
    'huaweicloudsdkkoomessage==3.1.110',
    'huaweicloudsdkkps==3.1.110',
    'huaweicloudsdklakeformation==3.1.110',
    'huaweicloudsdklive==3.1.110',
    'huaweicloudsdklts==3.1.110',
    'huaweicloudsdkmapds==3.1.110',
    'huaweicloudsdkmas==3.1.110',
    'huaweicloudsdkmeeting==3.1.110',
    'huaweicloudsdkmetastudio==3.1.110',
    'huaweicloudsdkmoderation==3.1.110',
    'huaweicloudsdkmpc==3.1.110',
    'huaweicloudsdkmrs==3.1.110',
    'huaweicloudsdkmsgsms==3.1.110',
    'huaweicloudsdkmssi==3.1.110',
    'huaweicloudsdknat==3.1.110',
    'huaweicloudsdknlp==3.1.110',
    'huaweicloudsdkobs==3.1.110',
    'huaweicloudsdkocr==3.1.110',
    'huaweicloudsdkoctopus==3.1.110',
    'huaweicloudsdkoms==3.1.110',
    'huaweicloudsdkoptverse==3.1.110',
    'huaweicloudsdkorganizations==3.1.110',
    'huaweicloudsdkorgid==3.1.110',
    'huaweicloudsdkoroas==3.1.110',
    'huaweicloudsdkosm==3.1.110',
    'huaweicloudsdkpangulargemodels==3.1.110',
    'huaweicloudsdkprojectman==3.1.110',
    'huaweicloudsdkrabbitmq==3.1.110',
    'huaweicloudsdkram==3.1.110',
    'huaweicloudsdkrds==3.1.110',
    'huaweicloudsdkres==3.1.110',
    'huaweicloudsdkrgc==3.1.110',
    'huaweicloudsdkrms==3.1.110',
    'huaweicloudsdkrocketmq==3.1.110',
    'huaweicloudsdkroma==3.1.110',
    'huaweicloudsdksa==3.1.110',
    'huaweicloudsdkscm==3.1.110',
    'huaweicloudsdksdrs==3.1.110',
    'huaweicloudsdksecmaster==3.1.110',
    'huaweicloudsdkservicestage==3.1.110',
    'huaweicloudsdksfsturbo==3.1.110',
    'huaweicloudsdksis==3.1.110',
    'huaweicloudsdksmn==3.1.110',
    'huaweicloudsdksms==3.1.110',
    'huaweicloudsdksts==3.1.110',
    'huaweicloudsdkswr==3.1.110',
    'huaweicloudsdktics==3.1.110',
    'huaweicloudsdktms==3.1.110',
    'huaweicloudsdkugo==3.1.110',
    'huaweicloudsdkvas==3.1.110',
    'huaweicloudsdkvcm==3.1.110',
    'huaweicloudsdkvod==3.1.110',
    'huaweicloudsdkvpc==3.1.110',
    'huaweicloudsdkvpcep==3.1.110',
    'huaweicloudsdkvpn==3.1.110',
    'huaweicloudsdkwaf==3.1.110',
    'huaweicloudsdkworkspace==3.1.110',
    'huaweicloudsdkworkspaceapp==3.1.110',
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
