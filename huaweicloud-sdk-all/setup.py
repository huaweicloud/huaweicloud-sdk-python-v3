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
VERSION = "3.1.102"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.102',
    'huaweicloudsdkaad==3.1.102',
    'huaweicloudsdkantiddos==3.1.102',
    'huaweicloudsdkaom==3.1.102',
    'huaweicloudsdkaos==3.1.102',
    'huaweicloudsdkapig==3.1.102',
    'huaweicloudsdkapm==3.1.102',
    'huaweicloudsdkas==3.1.102',
    'huaweicloudsdkasm==3.1.102',
    'huaweicloudsdkbcs==3.1.102',
    'huaweicloudsdkbms==3.1.102',
    'huaweicloudsdkbss==3.1.102',
    'huaweicloudsdkbssintl==3.1.102',
    'huaweicloudsdkcae==3.1.102',
    'huaweicloudsdkcampusgo==3.1.102',
    'huaweicloudsdkcbh==3.1.102',
    'huaweicloudsdkcbr==3.1.102',
    'huaweicloudsdkcbs==3.1.102',
    'huaweicloudsdkcc==3.1.102',
    'huaweicloudsdkcce==3.1.102',
    'huaweicloudsdkccm==3.1.102',
    'huaweicloudsdkcdm==3.1.102',
    'huaweicloudsdkcdn==3.1.102',
    'huaweicloudsdkces==3.1.102',
    'huaweicloudsdkcfw==3.1.102',
    'huaweicloudsdkcgs==3.1.102',
    'huaweicloudsdkclassroom==3.1.102',
    'huaweicloudsdkcloudide==3.1.102',
    'huaweicloudsdkcloudpond==3.1.102',
    'huaweicloudsdkcloudrtc==3.1.102',
    'huaweicloudsdkcloudtable==3.1.102',
    'huaweicloudsdkcloudtest==3.1.102',
    'huaweicloudsdkcodeartsartifact==3.1.102',
    'huaweicloudsdkcodeartsbuild==3.1.102',
    'huaweicloudsdkcodeartscheck==3.1.102',
    'huaweicloudsdkcodeartsdeploy==3.1.102',
    'huaweicloudsdkcodeartsinspector==3.1.102',
    'huaweicloudsdkcodeartspipeline==3.1.102',
    'huaweicloudsdkcodecraft==3.1.102',
    'huaweicloudsdkcodehub==3.1.102',
    'huaweicloudsdkconfig==3.1.102',
    'huaweicloudsdkcph==3.1.102',
    'huaweicloudsdkcpts==3.1.102',
    'huaweicloudsdkcse==3.1.102',
    'huaweicloudsdkcsms==3.1.102',
    'huaweicloudsdkcss==3.1.102',
    'huaweicloudsdkcts==3.1.102',
    'huaweicloudsdkdas==3.1.102',
    'huaweicloudsdkdataartsstudio==3.1.102',
    'huaweicloudsdkdbss==3.1.102',
    'huaweicloudsdkdc==3.1.102',
    'huaweicloudsdkdcs==3.1.102',
    'huaweicloudsdkddm==3.1.102',
    'huaweicloudsdkdds==3.1.102',
    'huaweicloudsdkdeh==3.1.102',
    'huaweicloudsdkdevsecurity==3.1.102',
    'huaweicloudsdkdevstar==3.1.102',
    'huaweicloudsdkdgc==3.1.102',
    'huaweicloudsdkdis==3.1.102',
    'huaweicloudsdkdlf==3.1.102',
    'huaweicloudsdkdli==3.1.102',
    'huaweicloudsdkdns==3.1.102',
    'huaweicloudsdkdris==3.1.102',
    'huaweicloudsdkdrs==3.1.102',
    'huaweicloudsdkdsc==3.1.102',
    'huaweicloudsdkdwr==3.1.102',
    'huaweicloudsdkdws==3.1.102',
    'huaweicloudsdkec==3.1.102',
    'huaweicloudsdkecs==3.1.102',
    'huaweicloudsdkedgesec==3.1.102',
    'huaweicloudsdkeg==3.1.102',
    'huaweicloudsdkeihealth==3.1.102',
    'huaweicloudsdkeip==3.1.102',
    'huaweicloudsdkelb==3.1.102',
    'huaweicloudsdkeps==3.1.102',
    'huaweicloudsdker==3.1.102',
    'huaweicloudsdkevs==3.1.102',
    'huaweicloudsdkfrs==3.1.102',
    'huaweicloudsdkfunctiongraph==3.1.102',
    'huaweicloudsdkga==3.1.102',
    'huaweicloudsdkgaussdb==3.1.102',
    'huaweicloudsdkgaussdbfornosql==3.1.102',
    'huaweicloudsdkgaussdbforopengauss==3.1.102',
    'huaweicloudsdkgeip==3.1.102',
    'huaweicloudsdkges==3.1.102',
    'huaweicloudsdkgsl==3.1.102',
    'huaweicloudsdkhilens==3.1.102',
    'huaweicloudsdkhss==3.1.102',
    'huaweicloudsdkiam==3.1.102',
    'huaweicloudsdkiamaccessanalyzer==3.1.102',
    'huaweicloudsdkidentitycenter==3.1.102',
    'huaweicloudsdkidentitycenterstore==3.1.102',
    'huaweicloudsdkidme==3.1.102',
    'huaweicloudsdkidmeclassicapi==3.1.102',
    'huaweicloudsdkiec==3.1.102',
    'huaweicloudsdkief==3.1.102',
    'huaweicloudsdkimage==3.1.102',
    'huaweicloudsdkimagesearch==3.1.102',
    'huaweicloudsdkims==3.1.102',
    'huaweicloudsdkiotanalytics==3.1.102',
    'huaweicloudsdkiotda==3.1.102',
    'huaweicloudsdkiotedge==3.1.102',
    'huaweicloudsdkivs==3.1.102',
    'huaweicloudsdkkafka==3.1.102',
    'huaweicloudsdkkms==3.1.102',
    'huaweicloudsdkkoomessage==3.1.102',
    'huaweicloudsdkkps==3.1.102',
    'huaweicloudsdklakeformation==3.1.102',
    'huaweicloudsdklive==3.1.102',
    'huaweicloudsdklts==3.1.102',
    'huaweicloudsdkmapds==3.1.102',
    'huaweicloudsdkmas==3.1.102',
    'huaweicloudsdkmeeting==3.1.102',
    'huaweicloudsdkmetastudio==3.1.102',
    'huaweicloudsdkmoderation==3.1.102',
    'huaweicloudsdkmpc==3.1.102',
    'huaweicloudsdkmrs==3.1.102',
    'huaweicloudsdkmsgsms==3.1.102',
    'huaweicloudsdkmssi==3.1.102',
    'huaweicloudsdknat==3.1.102',
    'huaweicloudsdknlp==3.1.102',
    'huaweicloudsdkobs==3.1.102',
    'huaweicloudsdkocr==3.1.102',
    'huaweicloudsdkoctopus==3.1.102',
    'huaweicloudsdkoms==3.1.102',
    'huaweicloudsdkoptverse==3.1.102',
    'huaweicloudsdkorganizations==3.1.102',
    'huaweicloudsdkorgid==3.1.102',
    'huaweicloudsdkoroas==3.1.102',
    'huaweicloudsdkosm==3.1.102',
    'huaweicloudsdkpangulargemodels==3.1.102',
    'huaweicloudsdkprojectman==3.1.102',
    'huaweicloudsdkrabbitmq==3.1.102',
    'huaweicloudsdkram==3.1.102',
    'huaweicloudsdkrds==3.1.102',
    'huaweicloudsdkres==3.1.102',
    'huaweicloudsdkrgc==3.1.102',
    'huaweicloudsdkrms==3.1.102',
    'huaweicloudsdkrocketmq==3.1.102',
    'huaweicloudsdkroma==3.1.102',
    'huaweicloudsdksa==3.1.102',
    'huaweicloudsdkscm==3.1.102',
    'huaweicloudsdksdrs==3.1.102',
    'huaweicloudsdksecmaster==3.1.102',
    'huaweicloudsdkservicestage==3.1.102',
    'huaweicloudsdksfsturbo==3.1.102',
    'huaweicloudsdksis==3.1.102',
    'huaweicloudsdksmn==3.1.102',
    'huaweicloudsdksms==3.1.102',
    'huaweicloudsdksts==3.1.102',
    'huaweicloudsdkswr==3.1.102',
    'huaweicloudsdktics==3.1.102',
    'huaweicloudsdktms==3.1.102',
    'huaweicloudsdkugo==3.1.102',
    'huaweicloudsdkvas==3.1.102',
    'huaweicloudsdkvcm==3.1.102',
    'huaweicloudsdkvod==3.1.102',
    'huaweicloudsdkvpc==3.1.102',
    'huaweicloudsdkvpcep==3.1.102',
    'huaweicloudsdkvpn==3.1.102',
    'huaweicloudsdkwaf==3.1.102',
    'huaweicloudsdkworkspace==3.1.102',
    'huaweicloudsdkworkspaceapp==3.1.102',
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
