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
VERSION = "3.1.120"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.120',
    'huaweicloudsdkaad==3.1.120',
    'huaweicloudsdkantiddos==3.1.120',
    'huaweicloudsdkaom==3.1.120',
    'huaweicloudsdkaos==3.1.120',
    'huaweicloudsdkapig==3.1.120',
    'huaweicloudsdkapm==3.1.120',
    'huaweicloudsdkas==3.1.120',
    'huaweicloudsdkasm==3.1.120',
    'huaweicloudsdkbcs==3.1.120',
    'huaweicloudsdkbms==3.1.120',
    'huaweicloudsdkbss==3.1.120',
    'huaweicloudsdkbssintl==3.1.120',
    'huaweicloudsdkcae==3.1.120',
    'huaweicloudsdkcampusgo==3.1.120',
    'huaweicloudsdkcbh==3.1.120',
    'huaweicloudsdkcbr==3.1.120',
    'huaweicloudsdkcbs==3.1.120',
    'huaweicloudsdkcc==3.1.120',
    'huaweicloudsdkcce==3.1.120',
    'huaweicloudsdkccm==3.1.120',
    'huaweicloudsdkcdm==3.1.120',
    'huaweicloudsdkcdn==3.1.120',
    'huaweicloudsdkces==3.1.120',
    'huaweicloudsdkcfw==3.1.120',
    'huaweicloudsdkcgs==3.1.120',
    'huaweicloudsdkclassroom==3.1.120',
    'huaweicloudsdkcloudide==3.1.120',
    'huaweicloudsdkcloudpond==3.1.120',
    'huaweicloudsdkcloudrtc==3.1.120',
    'huaweicloudsdkcloudtable==3.1.120',
    'huaweicloudsdkcloudtest==3.1.120',
    'huaweicloudsdkcoc==3.1.120',
    'huaweicloudsdkcodeartsartifact==3.1.120',
    'huaweicloudsdkcodeartsbuild==3.1.120',
    'huaweicloudsdkcodeartscheck==3.1.120',
    'huaweicloudsdkcodeartsdeploy==3.1.120',
    'huaweicloudsdkcodeartsgovernance==3.1.120',
    'huaweicloudsdkcodeartsinspector==3.1.120',
    'huaweicloudsdkcodeartspipeline==3.1.120',
    'huaweicloudsdkcodecraft==3.1.120',
    'huaweicloudsdkcodehub==3.1.120',
    'huaweicloudsdkconfig==3.1.120',
    'huaweicloudsdkcph==3.1.120',
    'huaweicloudsdkcpts==3.1.120',
    'huaweicloudsdkcse==3.1.120',
    'huaweicloudsdkcsms==3.1.120',
    'huaweicloudsdkcss==3.1.120',
    'huaweicloudsdkcts==3.1.120',
    'huaweicloudsdkdas==3.1.120',
    'huaweicloudsdkdataartsfabric==3.1.120',
    'huaweicloudsdkdataartsfabricep==3.1.120',
    'huaweicloudsdkdataartsstudio==3.1.120',
    'huaweicloudsdkdbss==3.1.120',
    'huaweicloudsdkdc==3.1.120',
    'huaweicloudsdkdcs==3.1.120',
    'huaweicloudsdkddm==3.1.120',
    'huaweicloudsdkdds==3.1.120',
    'huaweicloudsdkdeh==3.1.120',
    'huaweicloudsdkdevstar==3.1.120',
    'huaweicloudsdkdgc==3.1.120',
    'huaweicloudsdkdis==3.1.120',
    'huaweicloudsdkdlf==3.1.120',
    'huaweicloudsdkdli==3.1.120',
    'huaweicloudsdkdns==3.1.120',
    'huaweicloudsdkdris==3.1.120',
    'huaweicloudsdkdrs==3.1.120',
    'huaweicloudsdkdsc==3.1.120',
    'huaweicloudsdkdwr==3.1.120',
    'huaweicloudsdkdws==3.1.120',
    'huaweicloudsdkec==3.1.120',
    'huaweicloudsdkecs==3.1.120',
    'huaweicloudsdkedgesec==3.1.120',
    'huaweicloudsdkeg==3.1.120',
    'huaweicloudsdkeihealth==3.1.120',
    'huaweicloudsdkeip==3.1.120',
    'huaweicloudsdkelb==3.1.120',
    'huaweicloudsdkeps==3.1.120',
    'huaweicloudsdker==3.1.120',
    'huaweicloudsdkevs==3.1.120',
    'huaweicloudsdkfrs==3.1.120',
    'huaweicloudsdkfunctiongraph==3.1.120',
    'huaweicloudsdkga==3.1.120',
    'huaweicloudsdkgaussdb==3.1.120',
    'huaweicloudsdkgaussdbfornosql==3.1.120',
    'huaweicloudsdkgaussdbforopengauss==3.1.120',
    'huaweicloudsdkgeip==3.1.120',
    'huaweicloudsdkges==3.1.120',
    'huaweicloudsdkgsl==3.1.120',
    'huaweicloudsdkhilens==3.1.120',
    'huaweicloudsdkhss==3.1.120',
    'huaweicloudsdkiam==3.1.120',
    'huaweicloudsdkiamaccessanalyzer==3.1.120',
    'huaweicloudsdkidentitycenter==3.1.120',
    'huaweicloudsdkidentitycenterstore==3.1.120',
    'huaweicloudsdkidme==3.1.120',
    'huaweicloudsdkidmeclassicapi==3.1.120',
    'huaweicloudsdkiec==3.1.120',
    'huaweicloudsdkief==3.1.120',
    'huaweicloudsdkimage==3.1.120',
    'huaweicloudsdkimagesearch==3.1.120',
    'huaweicloudsdkims==3.1.120',
    'huaweicloudsdkiotanalytics==3.1.120',
    'huaweicloudsdkiotda==3.1.120',
    'huaweicloudsdkiotdm==3.1.120',
    'huaweicloudsdkiotedge==3.1.120',
    'huaweicloudsdkivs==3.1.120',
    'huaweicloudsdkkafka==3.1.120',
    'huaweicloudsdkkms==3.1.120',
    'huaweicloudsdkkoomessage==3.1.120',
    'huaweicloudsdkkps==3.1.120',
    'huaweicloudsdklakeformation==3.1.120',
    'huaweicloudsdklive==3.1.120',
    'huaweicloudsdklts==3.1.120',
    'huaweicloudsdkmapds==3.1.120',
    'huaweicloudsdkmas==3.1.120',
    'huaweicloudsdkmeeting==3.1.120',
    'huaweicloudsdkmetastudio==3.1.120',
    'huaweicloudsdkmoderation==3.1.120',
    'huaweicloudsdkmpc==3.1.120',
    'huaweicloudsdkmrs==3.1.120',
    'huaweicloudsdkmsgsms==3.1.120',
    'huaweicloudsdkmssi==3.1.120',
    'huaweicloudsdknat==3.1.120',
    'huaweicloudsdknlp==3.1.120',
    'huaweicloudsdkobs==3.1.120',
    'huaweicloudsdkocr==3.1.120',
    'huaweicloudsdkoctopus==3.1.120',
    'huaweicloudsdkoms==3.1.120',
    'huaweicloudsdkoptverse==3.1.120',
    'huaweicloudsdkorganizations==3.1.120',
    'huaweicloudsdkorgid==3.1.120',
    'huaweicloudsdkoroas==3.1.120',
    'huaweicloudsdkosm==3.1.120',
    'huaweicloudsdkpangulargemodels==3.1.120',
    'huaweicloudsdkprojectman==3.1.120',
    'huaweicloudsdkrabbitmq==3.1.120',
    'huaweicloudsdkram==3.1.120',
    'huaweicloudsdkrds==3.1.120',
    'huaweicloudsdkres==3.1.120',
    'huaweicloudsdkrgc==3.1.120',
    'huaweicloudsdkrms==3.1.120',
    'huaweicloudsdkrocketmq==3.1.120',
    'huaweicloudsdkroma==3.1.120',
    'huaweicloudsdksa==3.1.120',
    'huaweicloudsdkscm==3.1.120',
    'huaweicloudsdksdrs==3.1.120',
    'huaweicloudsdksecmaster==3.1.120',
    'huaweicloudsdkservicestage==3.1.120',
    'huaweicloudsdksfsturbo==3.1.120',
    'huaweicloudsdksis==3.1.120',
    'huaweicloudsdksmn==3.1.120',
    'huaweicloudsdksms==3.1.120',
    'huaweicloudsdksts==3.1.120',
    'huaweicloudsdkswr==3.1.120',
    'huaweicloudsdktics==3.1.120',
    'huaweicloudsdktms==3.1.120',
    'huaweicloudsdkugo==3.1.120',
    'huaweicloudsdkvas==3.1.120',
    'huaweicloudsdkvcm==3.1.120',
    'huaweicloudsdkvod==3.1.120',
    'huaweicloudsdkvpc==3.1.120',
    'huaweicloudsdkvpcep==3.1.120',
    'huaweicloudsdkvpn==3.1.120',
    'huaweicloudsdkwaf==3.1.120',
    'huaweicloudsdkworkspace==3.1.120',
    'huaweicloudsdkworkspaceapp==3.1.120',
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
