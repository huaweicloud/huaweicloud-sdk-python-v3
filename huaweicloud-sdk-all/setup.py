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
VERSION = "3.1.121"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.121',
    'huaweicloudsdkaad==3.1.121',
    'huaweicloudsdkantiddos==3.1.121',
    'huaweicloudsdkaom==3.1.121',
    'huaweicloudsdkaos==3.1.121',
    'huaweicloudsdkapig==3.1.121',
    'huaweicloudsdkapm==3.1.121',
    'huaweicloudsdkas==3.1.121',
    'huaweicloudsdkasm==3.1.121',
    'huaweicloudsdkbcs==3.1.121',
    'huaweicloudsdkbms==3.1.121',
    'huaweicloudsdkbss==3.1.121',
    'huaweicloudsdkbssintl==3.1.121',
    'huaweicloudsdkcae==3.1.121',
    'huaweicloudsdkcampusgo==3.1.121',
    'huaweicloudsdkcbh==3.1.121',
    'huaweicloudsdkcbr==3.1.121',
    'huaweicloudsdkcbs==3.1.121',
    'huaweicloudsdkcc==3.1.121',
    'huaweicloudsdkcce==3.1.121',
    'huaweicloudsdkccm==3.1.121',
    'huaweicloudsdkcdm==3.1.121',
    'huaweicloudsdkcdn==3.1.121',
    'huaweicloudsdkces==3.1.121',
    'huaweicloudsdkcfw==3.1.121',
    'huaweicloudsdkcgs==3.1.121',
    'huaweicloudsdkclassroom==3.1.121',
    'huaweicloudsdkcloudide==3.1.121',
    'huaweicloudsdkcloudpond==3.1.121',
    'huaweicloudsdkcloudrtc==3.1.121',
    'huaweicloudsdkcloudtable==3.1.121',
    'huaweicloudsdkcloudtest==3.1.121',
    'huaweicloudsdkcoc==3.1.121',
    'huaweicloudsdkcodeartsartifact==3.1.121',
    'huaweicloudsdkcodeartsbuild==3.1.121',
    'huaweicloudsdkcodeartscheck==3.1.121',
    'huaweicloudsdkcodeartsdeploy==3.1.121',
    'huaweicloudsdkcodeartsgovernance==3.1.121',
    'huaweicloudsdkcodeartsinspector==3.1.121',
    'huaweicloudsdkcodeartspipeline==3.1.121',
    'huaweicloudsdkcodecraft==3.1.121',
    'huaweicloudsdkcodehub==3.1.121',
    'huaweicloudsdkconfig==3.1.121',
    'huaweicloudsdkcph==3.1.121',
    'huaweicloudsdkcpts==3.1.121',
    'huaweicloudsdkcse==3.1.121',
    'huaweicloudsdkcsms==3.1.121',
    'huaweicloudsdkcss==3.1.121',
    'huaweicloudsdkcts==3.1.121',
    'huaweicloudsdkdas==3.1.121',
    'huaweicloudsdkdataartsfabric==3.1.121',
    'huaweicloudsdkdataartsfabricep==3.1.121',
    'huaweicloudsdkdataartsstudio==3.1.121',
    'huaweicloudsdkdbss==3.1.121',
    'huaweicloudsdkdc==3.1.121',
    'huaweicloudsdkdcs==3.1.121',
    'huaweicloudsdkddm==3.1.121',
    'huaweicloudsdkdds==3.1.121',
    'huaweicloudsdkdeh==3.1.121',
    'huaweicloudsdkdevstar==3.1.121',
    'huaweicloudsdkdgc==3.1.121',
    'huaweicloudsdkdis==3.1.121',
    'huaweicloudsdkdlf==3.1.121',
    'huaweicloudsdkdli==3.1.121',
    'huaweicloudsdkdns==3.1.121',
    'huaweicloudsdkdris==3.1.121',
    'huaweicloudsdkdrs==3.1.121',
    'huaweicloudsdkdsc==3.1.121',
    'huaweicloudsdkdwr==3.1.121',
    'huaweicloudsdkdws==3.1.121',
    'huaweicloudsdkec==3.1.121',
    'huaweicloudsdkecs==3.1.121',
    'huaweicloudsdkedgesec==3.1.121',
    'huaweicloudsdkeg==3.1.121',
    'huaweicloudsdkeihealth==3.1.121',
    'huaweicloudsdkeip==3.1.121',
    'huaweicloudsdkelb==3.1.121',
    'huaweicloudsdkeps==3.1.121',
    'huaweicloudsdker==3.1.121',
    'huaweicloudsdkevs==3.1.121',
    'huaweicloudsdkfrs==3.1.121',
    'huaweicloudsdkfunctiongraph==3.1.121',
    'huaweicloudsdkga==3.1.121',
    'huaweicloudsdkgaussdb==3.1.121',
    'huaweicloudsdkgaussdbfornosql==3.1.121',
    'huaweicloudsdkgaussdbforopengauss==3.1.121',
    'huaweicloudsdkgeip==3.1.121',
    'huaweicloudsdkges==3.1.121',
    'huaweicloudsdkgsl==3.1.121',
    'huaweicloudsdkhilens==3.1.121',
    'huaweicloudsdkhss==3.1.121',
    'huaweicloudsdkiam==3.1.121',
    'huaweicloudsdkiamaccessanalyzer==3.1.121',
    'huaweicloudsdkidentitycenter==3.1.121',
    'huaweicloudsdkidentitycenterstore==3.1.121',
    'huaweicloudsdkidme==3.1.121',
    'huaweicloudsdkidmeclassicapi==3.1.121',
    'huaweicloudsdkiec==3.1.121',
    'huaweicloudsdkief==3.1.121',
    'huaweicloudsdkimage==3.1.121',
    'huaweicloudsdkimagesearch==3.1.121',
    'huaweicloudsdkims==3.1.121',
    'huaweicloudsdkiotanalytics==3.1.121',
    'huaweicloudsdkiotda==3.1.121',
    'huaweicloudsdkiotdm==3.1.121',
    'huaweicloudsdkiotedge==3.1.121',
    'huaweicloudsdkivs==3.1.121',
    'huaweicloudsdkkafka==3.1.121',
    'huaweicloudsdkkms==3.1.121',
    'huaweicloudsdkkoomessage==3.1.121',
    'huaweicloudsdkkps==3.1.121',
    'huaweicloudsdklakeformation==3.1.121',
    'huaweicloudsdklive==3.1.121',
    'huaweicloudsdklts==3.1.121',
    'huaweicloudsdkmapds==3.1.121',
    'huaweicloudsdkmas==3.1.121',
    'huaweicloudsdkmeeting==3.1.121',
    'huaweicloudsdkmetastudio==3.1.121',
    'huaweicloudsdkmoderation==3.1.121',
    'huaweicloudsdkmpc==3.1.121',
    'huaweicloudsdkmrs==3.1.121',
    'huaweicloudsdkmsgsms==3.1.121',
    'huaweicloudsdkmssi==3.1.121',
    'huaweicloudsdknat==3.1.121',
    'huaweicloudsdknlp==3.1.121',
    'huaweicloudsdkobs==3.1.121',
    'huaweicloudsdkocr==3.1.121',
    'huaweicloudsdkoctopus==3.1.121',
    'huaweicloudsdkoms==3.1.121',
    'huaweicloudsdkoptverse==3.1.121',
    'huaweicloudsdkorganizations==3.1.121',
    'huaweicloudsdkorgid==3.1.121',
    'huaweicloudsdkoroas==3.1.121',
    'huaweicloudsdkosm==3.1.121',
    'huaweicloudsdkpangulargemodels==3.1.121',
    'huaweicloudsdkprojectman==3.1.121',
    'huaweicloudsdkrabbitmq==3.1.121',
    'huaweicloudsdkram==3.1.121',
    'huaweicloudsdkrds==3.1.121',
    'huaweicloudsdkres==3.1.121',
    'huaweicloudsdkrgc==3.1.121',
    'huaweicloudsdkrms==3.1.121',
    'huaweicloudsdkrocketmq==3.1.121',
    'huaweicloudsdkroma==3.1.121',
    'huaweicloudsdksa==3.1.121',
    'huaweicloudsdkscm==3.1.121',
    'huaweicloudsdksdrs==3.1.121',
    'huaweicloudsdksecmaster==3.1.121',
    'huaweicloudsdkservicestage==3.1.121',
    'huaweicloudsdksfsturbo==3.1.121',
    'huaweicloudsdksis==3.1.121',
    'huaweicloudsdksmn==3.1.121',
    'huaweicloudsdksms==3.1.121',
    'huaweicloudsdksts==3.1.121',
    'huaweicloudsdkswr==3.1.121',
    'huaweicloudsdktics==3.1.121',
    'huaweicloudsdktms==3.1.121',
    'huaweicloudsdkugo==3.1.121',
    'huaweicloudsdkvas==3.1.121',
    'huaweicloudsdkvcm==3.1.121',
    'huaweicloudsdkvod==3.1.121',
    'huaweicloudsdkvpc==3.1.121',
    'huaweicloudsdkvpcep==3.1.121',
    'huaweicloudsdkvpn==3.1.121',
    'huaweicloudsdkwaf==3.1.121',
    'huaweicloudsdkworkspace==3.1.121',
    'huaweicloudsdkworkspaceapp==3.1.121',
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
