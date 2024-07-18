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
VERSION = "3.1.106"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.106',
    'huaweicloudsdkaad==3.1.106',
    'huaweicloudsdkantiddos==3.1.106',
    'huaweicloudsdkaom==3.1.106',
    'huaweicloudsdkaos==3.1.106',
    'huaweicloudsdkapig==3.1.106',
    'huaweicloudsdkapm==3.1.106',
    'huaweicloudsdkas==3.1.106',
    'huaweicloudsdkasm==3.1.106',
    'huaweicloudsdkbcs==3.1.106',
    'huaweicloudsdkbms==3.1.106',
    'huaweicloudsdkbss==3.1.106',
    'huaweicloudsdkbssintl==3.1.106',
    'huaweicloudsdkcae==3.1.106',
    'huaweicloudsdkcampusgo==3.1.106',
    'huaweicloudsdkcbh==3.1.106',
    'huaweicloudsdkcbr==3.1.106',
    'huaweicloudsdkcbs==3.1.106',
    'huaweicloudsdkcc==3.1.106',
    'huaweicloudsdkcce==3.1.106',
    'huaweicloudsdkccm==3.1.106',
    'huaweicloudsdkcdm==3.1.106',
    'huaweicloudsdkcdn==3.1.106',
    'huaweicloudsdkces==3.1.106',
    'huaweicloudsdkcfw==3.1.106',
    'huaweicloudsdkcgs==3.1.106',
    'huaweicloudsdkclassroom==3.1.106',
    'huaweicloudsdkcloudide==3.1.106',
    'huaweicloudsdkcloudpond==3.1.106',
    'huaweicloudsdkcloudrtc==3.1.106',
    'huaweicloudsdkcloudtable==3.1.106',
    'huaweicloudsdkcloudtest==3.1.106',
    'huaweicloudsdkcodeartsartifact==3.1.106',
    'huaweicloudsdkcodeartsbuild==3.1.106',
    'huaweicloudsdkcodeartscheck==3.1.106',
    'huaweicloudsdkcodeartsdeploy==3.1.106',
    'huaweicloudsdkcodeartsgovernance==3.1.106',
    'huaweicloudsdkcodeartsinspector==3.1.106',
    'huaweicloudsdkcodeartspipeline==3.1.106',
    'huaweicloudsdkcodecraft==3.1.106',
    'huaweicloudsdkcodehub==3.1.106',
    'huaweicloudsdkconfig==3.1.106',
    'huaweicloudsdkcph==3.1.106',
    'huaweicloudsdkcpts==3.1.106',
    'huaweicloudsdkcse==3.1.106',
    'huaweicloudsdkcsms==3.1.106',
    'huaweicloudsdkcss==3.1.106',
    'huaweicloudsdkcts==3.1.106',
    'huaweicloudsdkdas==3.1.106',
    'huaweicloudsdkdataartsstudio==3.1.106',
    'huaweicloudsdkdbss==3.1.106',
    'huaweicloudsdkdc==3.1.106',
    'huaweicloudsdkdcs==3.1.106',
    'huaweicloudsdkddm==3.1.106',
    'huaweicloudsdkdds==3.1.106',
    'huaweicloudsdkdeh==3.1.106',
    'huaweicloudsdkdevstar==3.1.106',
    'huaweicloudsdkdgc==3.1.106',
    'huaweicloudsdkdis==3.1.106',
    'huaweicloudsdkdlf==3.1.106',
    'huaweicloudsdkdli==3.1.106',
    'huaweicloudsdkdns==3.1.106',
    'huaweicloudsdkdris==3.1.106',
    'huaweicloudsdkdrs==3.1.106',
    'huaweicloudsdkdsc==3.1.106',
    'huaweicloudsdkdwr==3.1.106',
    'huaweicloudsdkdws==3.1.106',
    'huaweicloudsdkec==3.1.106',
    'huaweicloudsdkecs==3.1.106',
    'huaweicloudsdkedgesec==3.1.106',
    'huaweicloudsdkeg==3.1.106',
    'huaweicloudsdkeihealth==3.1.106',
    'huaweicloudsdkeip==3.1.106',
    'huaweicloudsdkelb==3.1.106',
    'huaweicloudsdkeps==3.1.106',
    'huaweicloudsdker==3.1.106',
    'huaweicloudsdkevs==3.1.106',
    'huaweicloudsdkfrs==3.1.106',
    'huaweicloudsdkfunctiongraph==3.1.106',
    'huaweicloudsdkga==3.1.106',
    'huaweicloudsdkgaussdb==3.1.106',
    'huaweicloudsdkgaussdbfornosql==3.1.106',
    'huaweicloudsdkgaussdbforopengauss==3.1.106',
    'huaweicloudsdkgeip==3.1.106',
    'huaweicloudsdkges==3.1.106',
    'huaweicloudsdkgsl==3.1.106',
    'huaweicloudsdkhilens==3.1.106',
    'huaweicloudsdkhss==3.1.106',
    'huaweicloudsdkiam==3.1.106',
    'huaweicloudsdkiamaccessanalyzer==3.1.106',
    'huaweicloudsdkidentitycenter==3.1.106',
    'huaweicloudsdkidentitycenterstore==3.1.106',
    'huaweicloudsdkidme==3.1.106',
    'huaweicloudsdkidmeclassicapi==3.1.106',
    'huaweicloudsdkiec==3.1.106',
    'huaweicloudsdkief==3.1.106',
    'huaweicloudsdkimage==3.1.106',
    'huaweicloudsdkimagesearch==3.1.106',
    'huaweicloudsdkims==3.1.106',
    'huaweicloudsdkiotanalytics==3.1.106',
    'huaweicloudsdkiotda==3.1.106',
    'huaweicloudsdkiotedge==3.1.106',
    'huaweicloudsdkivs==3.1.106',
    'huaweicloudsdkkafka==3.1.106',
    'huaweicloudsdkkms==3.1.106',
    'huaweicloudsdkkoomessage==3.1.106',
    'huaweicloudsdkkps==3.1.106',
    'huaweicloudsdklakeformation==3.1.106',
    'huaweicloudsdklive==3.1.106',
    'huaweicloudsdklts==3.1.106',
    'huaweicloudsdkmapds==3.1.106',
    'huaweicloudsdkmas==3.1.106',
    'huaweicloudsdkmeeting==3.1.106',
    'huaweicloudsdkmetastudio==3.1.106',
    'huaweicloudsdkmoderation==3.1.106',
    'huaweicloudsdkmpc==3.1.106',
    'huaweicloudsdkmrs==3.1.106',
    'huaweicloudsdkmsgsms==3.1.106',
    'huaweicloudsdkmssi==3.1.106',
    'huaweicloudsdknat==3.1.106',
    'huaweicloudsdknlp==3.1.106',
    'huaweicloudsdkobs==3.1.106',
    'huaweicloudsdkocr==3.1.106',
    'huaweicloudsdkoctopus==3.1.106',
    'huaweicloudsdkoms==3.1.106',
    'huaweicloudsdkoptverse==3.1.106',
    'huaweicloudsdkorganizations==3.1.106',
    'huaweicloudsdkorgid==3.1.106',
    'huaweicloudsdkoroas==3.1.106',
    'huaweicloudsdkosm==3.1.106',
    'huaweicloudsdkpangulargemodels==3.1.106',
    'huaweicloudsdkprojectman==3.1.106',
    'huaweicloudsdkrabbitmq==3.1.106',
    'huaweicloudsdkram==3.1.106',
    'huaweicloudsdkrds==3.1.106',
    'huaweicloudsdkres==3.1.106',
    'huaweicloudsdkrgc==3.1.106',
    'huaweicloudsdkrms==3.1.106',
    'huaweicloudsdkrocketmq==3.1.106',
    'huaweicloudsdkroma==3.1.106',
    'huaweicloudsdksa==3.1.106',
    'huaweicloudsdkscm==3.1.106',
    'huaweicloudsdksdrs==3.1.106',
    'huaweicloudsdksecmaster==3.1.106',
    'huaweicloudsdkservicestage==3.1.106',
    'huaweicloudsdksfsturbo==3.1.106',
    'huaweicloudsdksis==3.1.106',
    'huaweicloudsdksmn==3.1.106',
    'huaweicloudsdksms==3.1.106',
    'huaweicloudsdksts==3.1.106',
    'huaweicloudsdkswr==3.1.106',
    'huaweicloudsdktics==3.1.106',
    'huaweicloudsdktms==3.1.106',
    'huaweicloudsdkugo==3.1.106',
    'huaweicloudsdkvas==3.1.106',
    'huaweicloudsdkvcm==3.1.106',
    'huaweicloudsdkvod==3.1.106',
    'huaweicloudsdkvpc==3.1.106',
    'huaweicloudsdkvpcep==3.1.106',
    'huaweicloudsdkvpn==3.1.106',
    'huaweicloudsdkwaf==3.1.106',
    'huaweicloudsdkworkspace==3.1.106',
    'huaweicloudsdkworkspaceapp==3.1.106',
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
