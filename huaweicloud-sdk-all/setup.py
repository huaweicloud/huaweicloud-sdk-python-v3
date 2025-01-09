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
VERSION = "3.1.131"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.131',
    'huaweicloudsdkaad==3.1.131',
    'huaweicloudsdkantiddos==3.1.131',
    'huaweicloudsdkaom==3.1.131',
    'huaweicloudsdkaos==3.1.131',
    'huaweicloudsdkapig==3.1.131',
    'huaweicloudsdkapm==3.1.131',
    'huaweicloudsdkas==3.1.131',
    'huaweicloudsdkasm==3.1.131',
    'huaweicloudsdkbcs==3.1.131',
    'huaweicloudsdkbms==3.1.131',
    'huaweicloudsdkbss==3.1.131',
    'huaweicloudsdkbssintl==3.1.131',
    'huaweicloudsdkcae==3.1.131',
    'huaweicloudsdkcampusgo==3.1.131',
    'huaweicloudsdkcbh==3.1.131',
    'huaweicloudsdkcbr==3.1.131',
    'huaweicloudsdkcbs==3.1.131',
    'huaweicloudsdkcc==3.1.131',
    'huaweicloudsdkcce==3.1.131',
    'huaweicloudsdkccm==3.1.131',
    'huaweicloudsdkcdm==3.1.131',
    'huaweicloudsdkcdn==3.1.131',
    'huaweicloudsdkces==3.1.131',
    'huaweicloudsdkcfw==3.1.131',
    'huaweicloudsdkcgs==3.1.131',
    'huaweicloudsdkclassroom==3.1.131',
    'huaweicloudsdkcloudide==3.1.131',
    'huaweicloudsdkcloudpond==3.1.131',
    'huaweicloudsdkcloudrtc==3.1.131',
    'huaweicloudsdkcloudtable==3.1.131',
    'huaweicloudsdkcloudtest==3.1.131',
    'huaweicloudsdkcoc==3.1.131',
    'huaweicloudsdkcodeartsartifact==3.1.131',
    'huaweicloudsdkcodeartsbuild==3.1.131',
    'huaweicloudsdkcodeartscheck==3.1.131',
    'huaweicloudsdkcodeartsdeploy==3.1.131',
    'huaweicloudsdkcodeartsgovernance==3.1.131',
    'huaweicloudsdkcodeartsinspector==3.1.131',
    'huaweicloudsdkcodeartspipeline==3.1.131',
    'huaweicloudsdkcodecraft==3.1.131',
    'huaweicloudsdkcodehub==3.1.131',
    'huaweicloudsdkconfig==3.1.131',
    'huaweicloudsdkcph==3.1.131',
    'huaweicloudsdkcpts==3.1.131',
    'huaweicloudsdkcse==3.1.131',
    'huaweicloudsdkcsms==3.1.131',
    'huaweicloudsdkcss==3.1.131',
    'huaweicloudsdkcts==3.1.131',
    'huaweicloudsdkdas==3.1.131',
    'huaweicloudsdkdataartsfabric==3.1.131',
    'huaweicloudsdkdataartsfabricep==3.1.131',
    'huaweicloudsdkdataartsstudio==3.1.131',
    'huaweicloudsdkdbss==3.1.131',
    'huaweicloudsdkdc==3.1.131',
    'huaweicloudsdkdcs==3.1.131',
    'huaweicloudsdkddm==3.1.131',
    'huaweicloudsdkdds==3.1.131',
    'huaweicloudsdkdeh==3.1.131',
    'huaweicloudsdkdevstar==3.1.131',
    'huaweicloudsdkdgc==3.1.131',
    'huaweicloudsdkdis==3.1.131',
    'huaweicloudsdkdlf==3.1.131',
    'huaweicloudsdkdli==3.1.131',
    'huaweicloudsdkdns==3.1.131',
    'huaweicloudsdkdris==3.1.131',
    'huaweicloudsdkdrs==3.1.131',
    'huaweicloudsdkdsc==3.1.131',
    'huaweicloudsdkdwr==3.1.131',
    'huaweicloudsdkdws==3.1.131',
    'huaweicloudsdkec==3.1.131',
    'huaweicloudsdkecs==3.1.131',
    'huaweicloudsdkedgesec==3.1.131',
    'huaweicloudsdkeg==3.1.131',
    'huaweicloudsdkeihealth==3.1.131',
    'huaweicloudsdkeip==3.1.131',
    'huaweicloudsdkelb==3.1.131',
    'huaweicloudsdkeps==3.1.131',
    'huaweicloudsdker==3.1.131',
    'huaweicloudsdkevs==3.1.131',
    'huaweicloudsdkfrs==3.1.131',
    'huaweicloudsdkfunctiongraph==3.1.131',
    'huaweicloudsdkga==3.1.131',
    'huaweicloudsdkgaussdb==3.1.131',
    'huaweicloudsdkgaussdbfornosql==3.1.131',
    'huaweicloudsdkgaussdbforopengauss==3.1.131',
    'huaweicloudsdkgeip==3.1.131',
    'huaweicloudsdkges==3.1.131',
    'huaweicloudsdkgsl==3.1.131',
    'huaweicloudsdkhilens==3.1.131',
    'huaweicloudsdkhss==3.1.131',
    'huaweicloudsdkiam==3.1.131',
    'huaweicloudsdkiamaccessanalyzer==3.1.131',
    'huaweicloudsdkidentitycenter==3.1.131',
    'huaweicloudsdkidentitycenterstore==3.1.131',
    'huaweicloudsdkidme==3.1.131',
    'huaweicloudsdkidmeclassicapi==3.1.131',
    'huaweicloudsdkiec==3.1.131',
    'huaweicloudsdkief==3.1.131',
    'huaweicloudsdkimage==3.1.131',
    'huaweicloudsdkimagesearch==3.1.131',
    'huaweicloudsdkims==3.1.131',
    'huaweicloudsdkiotanalytics==3.1.131',
    'huaweicloudsdkiotda==3.1.131',
    'huaweicloudsdkiotdm==3.1.131',
    'huaweicloudsdkiotedge==3.1.131',
    'huaweicloudsdkivs==3.1.131',
    'huaweicloudsdkkafka==3.1.131',
    'huaweicloudsdkkms==3.1.131',
    'huaweicloudsdkkoomessage==3.1.131',
    'huaweicloudsdkkps==3.1.131',
    'huaweicloudsdklakeformation==3.1.131',
    'huaweicloudsdklive==3.1.131',
    'huaweicloudsdklts==3.1.131',
    'huaweicloudsdkmapds==3.1.131',
    'huaweicloudsdkmas==3.1.131',
    'huaweicloudsdkmastudio==3.1.131',
    'huaweicloudsdkmeeting==3.1.131',
    'huaweicloudsdkmetastudio==3.1.131',
    'huaweicloudsdkmoderation==3.1.131',
    'huaweicloudsdkmpc==3.1.131',
    'huaweicloudsdkmrs==3.1.131',
    'huaweicloudsdkmsgsms==3.1.131',
    'huaweicloudsdkmssi==3.1.131',
    'huaweicloudsdknat==3.1.131',
    'huaweicloudsdknlp==3.1.131',
    'huaweicloudsdkobs==3.1.131',
    'huaweicloudsdkocr==3.1.131',
    'huaweicloudsdkoctopus==3.1.131',
    'huaweicloudsdkoms==3.1.131',
    'huaweicloudsdkoptverse==3.1.131',
    'huaweicloudsdkorganizations==3.1.131',
    'huaweicloudsdkorgid==3.1.131',
    'huaweicloudsdkoroas==3.1.131',
    'huaweicloudsdkosm==3.1.131',
    'huaweicloudsdkpangulargemodels==3.1.131',
    'huaweicloudsdkprojectman==3.1.131',
    'huaweicloudsdkrabbitmq==3.1.131',
    'huaweicloudsdkram==3.1.131',
    'huaweicloudsdkrds==3.1.131',
    'huaweicloudsdkres==3.1.131',
    'huaweicloudsdkrgc==3.1.131',
    'huaweicloudsdkrms==3.1.131',
    'huaweicloudsdkrocketmq==3.1.131',
    'huaweicloudsdkroma==3.1.131',
    'huaweicloudsdksa==3.1.131',
    'huaweicloudsdkscm==3.1.131',
    'huaweicloudsdksdrs==3.1.131',
    'huaweicloudsdksecmaster==3.1.131',
    'huaweicloudsdkservicestage==3.1.131',
    'huaweicloudsdksfsturbo==3.1.131',
    'huaweicloudsdksis==3.1.131',
    'huaweicloudsdksmn==3.1.131',
    'huaweicloudsdksms==3.1.131',
    'huaweicloudsdksmsapi==3.1.131',
    'huaweicloudsdksts==3.1.131',
    'huaweicloudsdkswr==3.1.131',
    'huaweicloudsdktics==3.1.131',
    'huaweicloudsdktms==3.1.131',
    'huaweicloudsdkugo==3.1.131',
    'huaweicloudsdkvas==3.1.131',
    'huaweicloudsdkvcm==3.1.131',
    'huaweicloudsdkvod==3.1.131',
    'huaweicloudsdkvpc==3.1.131',
    'huaweicloudsdkvpcep==3.1.131',
    'huaweicloudsdkvpn==3.1.131',
    'huaweicloudsdkwaf==3.1.131',
    'huaweicloudsdkworkspace==3.1.131',
    'huaweicloudsdkworkspaceapp==3.1.131',
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
