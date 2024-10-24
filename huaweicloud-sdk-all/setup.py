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
VERSION = "3.1.119"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.119',
    'huaweicloudsdkaad==3.1.119',
    'huaweicloudsdkantiddos==3.1.119',
    'huaweicloudsdkaom==3.1.119',
    'huaweicloudsdkaos==3.1.119',
    'huaweicloudsdkapig==3.1.119',
    'huaweicloudsdkapm==3.1.119',
    'huaweicloudsdkas==3.1.119',
    'huaweicloudsdkasm==3.1.119',
    'huaweicloudsdkbcs==3.1.119',
    'huaweicloudsdkbms==3.1.119',
    'huaweicloudsdkbss==3.1.119',
    'huaweicloudsdkbssintl==3.1.119',
    'huaweicloudsdkcae==3.1.119',
    'huaweicloudsdkcampusgo==3.1.119',
    'huaweicloudsdkcbh==3.1.119',
    'huaweicloudsdkcbr==3.1.119',
    'huaweicloudsdkcbs==3.1.119',
    'huaweicloudsdkcc==3.1.119',
    'huaweicloudsdkcce==3.1.119',
    'huaweicloudsdkccm==3.1.119',
    'huaweicloudsdkcdm==3.1.119',
    'huaweicloudsdkcdn==3.1.119',
    'huaweicloudsdkces==3.1.119',
    'huaweicloudsdkcfw==3.1.119',
    'huaweicloudsdkcgs==3.1.119',
    'huaweicloudsdkclassroom==3.1.119',
    'huaweicloudsdkcloudide==3.1.119',
    'huaweicloudsdkcloudpond==3.1.119',
    'huaweicloudsdkcloudrtc==3.1.119',
    'huaweicloudsdkcloudtable==3.1.119',
    'huaweicloudsdkcloudtest==3.1.119',
    'huaweicloudsdkcoc==3.1.119',
    'huaweicloudsdkcodeartsartifact==3.1.119',
    'huaweicloudsdkcodeartsbuild==3.1.119',
    'huaweicloudsdkcodeartscheck==3.1.119',
    'huaweicloudsdkcodeartsdeploy==3.1.119',
    'huaweicloudsdkcodeartsgovernance==3.1.119',
    'huaweicloudsdkcodeartsinspector==3.1.119',
    'huaweicloudsdkcodeartspipeline==3.1.119',
    'huaweicloudsdkcodecraft==3.1.119',
    'huaweicloudsdkcodehub==3.1.119',
    'huaweicloudsdkconfig==3.1.119',
    'huaweicloudsdkcph==3.1.119',
    'huaweicloudsdkcpts==3.1.119',
    'huaweicloudsdkcse==3.1.119',
    'huaweicloudsdkcsms==3.1.119',
    'huaweicloudsdkcss==3.1.119',
    'huaweicloudsdkcts==3.1.119',
    'huaweicloudsdkdas==3.1.119',
    'huaweicloudsdkdataartsfabric==3.1.119',
    'huaweicloudsdkdataartsstudio==3.1.119',
    'huaweicloudsdkdbss==3.1.119',
    'huaweicloudsdkdc==3.1.119',
    'huaweicloudsdkdcs==3.1.119',
    'huaweicloudsdkddm==3.1.119',
    'huaweicloudsdkdds==3.1.119',
    'huaweicloudsdkdeh==3.1.119',
    'huaweicloudsdkdevstar==3.1.119',
    'huaweicloudsdkdgc==3.1.119',
    'huaweicloudsdkdis==3.1.119',
    'huaweicloudsdkdlf==3.1.119',
    'huaweicloudsdkdli==3.1.119',
    'huaweicloudsdkdns==3.1.119',
    'huaweicloudsdkdris==3.1.119',
    'huaweicloudsdkdrs==3.1.119',
    'huaweicloudsdkdsc==3.1.119',
    'huaweicloudsdkdwr==3.1.119',
    'huaweicloudsdkdws==3.1.119',
    'huaweicloudsdkec==3.1.119',
    'huaweicloudsdkecs==3.1.119',
    'huaweicloudsdkedgesec==3.1.119',
    'huaweicloudsdkeg==3.1.119',
    'huaweicloudsdkeihealth==3.1.119',
    'huaweicloudsdkeip==3.1.119',
    'huaweicloudsdkelb==3.1.119',
    'huaweicloudsdkeps==3.1.119',
    'huaweicloudsdker==3.1.119',
    'huaweicloudsdkevs==3.1.119',
    'huaweicloudsdkfrs==3.1.119',
    'huaweicloudsdkfunctiongraph==3.1.119',
    'huaweicloudsdkga==3.1.119',
    'huaweicloudsdkgaussdb==3.1.119',
    'huaweicloudsdkgaussdbfornosql==3.1.119',
    'huaweicloudsdkgaussdbforopengauss==3.1.119',
    'huaweicloudsdkgeip==3.1.119',
    'huaweicloudsdkges==3.1.119',
    'huaweicloudsdkgsl==3.1.119',
    'huaweicloudsdkhilens==3.1.119',
    'huaweicloudsdkhss==3.1.119',
    'huaweicloudsdkiam==3.1.119',
    'huaweicloudsdkiamaccessanalyzer==3.1.119',
    'huaweicloudsdkidentitycenter==3.1.119',
    'huaweicloudsdkidentitycenterstore==3.1.119',
    'huaweicloudsdkidme==3.1.119',
    'huaweicloudsdkidmeclassicapi==3.1.119',
    'huaweicloudsdkiec==3.1.119',
    'huaweicloudsdkief==3.1.119',
    'huaweicloudsdkimage==3.1.119',
    'huaweicloudsdkimagesearch==3.1.119',
    'huaweicloudsdkims==3.1.119',
    'huaweicloudsdkiotanalytics==3.1.119',
    'huaweicloudsdkiotda==3.1.119',
    'huaweicloudsdkiotdm==3.1.119',
    'huaweicloudsdkiotedge==3.1.119',
    'huaweicloudsdkivs==3.1.119',
    'huaweicloudsdkkafka==3.1.119',
    'huaweicloudsdkkms==3.1.119',
    'huaweicloudsdkkoomessage==3.1.119',
    'huaweicloudsdkkps==3.1.119',
    'huaweicloudsdklakeformation==3.1.119',
    'huaweicloudsdklive==3.1.119',
    'huaweicloudsdklts==3.1.119',
    'huaweicloudsdkmapds==3.1.119',
    'huaweicloudsdkmas==3.1.119',
    'huaweicloudsdkmeeting==3.1.119',
    'huaweicloudsdkmetastudio==3.1.119',
    'huaweicloudsdkmoderation==3.1.119',
    'huaweicloudsdkmpc==3.1.119',
    'huaweicloudsdkmrs==3.1.119',
    'huaweicloudsdkmsgsms==3.1.119',
    'huaweicloudsdkmssi==3.1.119',
    'huaweicloudsdknat==3.1.119',
    'huaweicloudsdknlp==3.1.119',
    'huaweicloudsdkobs==3.1.119',
    'huaweicloudsdkocr==3.1.119',
    'huaweicloudsdkoctopus==3.1.119',
    'huaweicloudsdkoms==3.1.119',
    'huaweicloudsdkoptverse==3.1.119',
    'huaweicloudsdkorganizations==3.1.119',
    'huaweicloudsdkorgid==3.1.119',
    'huaweicloudsdkoroas==3.1.119',
    'huaweicloudsdkosm==3.1.119',
    'huaweicloudsdkpangulargemodels==3.1.119',
    'huaweicloudsdkprojectman==3.1.119',
    'huaweicloudsdkrabbitmq==3.1.119',
    'huaweicloudsdkram==3.1.119',
    'huaweicloudsdkrds==3.1.119',
    'huaweicloudsdkres==3.1.119',
    'huaweicloudsdkrgc==3.1.119',
    'huaweicloudsdkrms==3.1.119',
    'huaweicloudsdkrocketmq==3.1.119',
    'huaweicloudsdkroma==3.1.119',
    'huaweicloudsdksa==3.1.119',
    'huaweicloudsdkscm==3.1.119',
    'huaweicloudsdksdrs==3.1.119',
    'huaweicloudsdksecmaster==3.1.119',
    'huaweicloudsdkservicestage==3.1.119',
    'huaweicloudsdksfsturbo==3.1.119',
    'huaweicloudsdksis==3.1.119',
    'huaweicloudsdksmn==3.1.119',
    'huaweicloudsdksms==3.1.119',
    'huaweicloudsdksts==3.1.119',
    'huaweicloudsdkswr==3.1.119',
    'huaweicloudsdktics==3.1.119',
    'huaweicloudsdktms==3.1.119',
    'huaweicloudsdkugo==3.1.119',
    'huaweicloudsdkvas==3.1.119',
    'huaweicloudsdkvcm==3.1.119',
    'huaweicloudsdkvod==3.1.119',
    'huaweicloudsdkvpc==3.1.119',
    'huaweicloudsdkvpcep==3.1.119',
    'huaweicloudsdkvpn==3.1.119',
    'huaweicloudsdkwaf==3.1.119',
    'huaweicloudsdkworkspace==3.1.119',
    'huaweicloudsdkworkspaceapp==3.1.119',
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
