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
VERSION = "3.1.81"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.81',
    'huaweicloudsdkaad==3.1.81',
    'huaweicloudsdkantiddos==3.1.81',
    'huaweicloudsdkaom==3.1.81',
    'huaweicloudsdkaos==3.1.81',
    'huaweicloudsdkapig==3.1.81',
    'huaweicloudsdkapm==3.1.81',
    'huaweicloudsdkas==3.1.81',
    'huaweicloudsdkasm==3.1.81',
    'huaweicloudsdkbcs==3.1.81',
    'huaweicloudsdkbms==3.1.81',
    'huaweicloudsdkbss==3.1.81',
    'huaweicloudsdkbssintl==3.1.81',
    'huaweicloudsdkcae==3.1.81',
    'huaweicloudsdkcampusgo==3.1.81',
    'huaweicloudsdkcbh==3.1.81',
    'huaweicloudsdkcbr==3.1.81',
    'huaweicloudsdkcbs==3.1.81',
    'huaweicloudsdkcc==3.1.81',
    'huaweicloudsdkcce==3.1.81',
    'huaweicloudsdkccm==3.1.81',
    'huaweicloudsdkcdm==3.1.81',
    'huaweicloudsdkcdn==3.1.81',
    'huaweicloudsdkces==3.1.81',
    'huaweicloudsdkcfw==3.1.81',
    'huaweicloudsdkcgs==3.1.81',
    'huaweicloudsdkclassroom==3.1.81',
    'huaweicloudsdkcloudide==3.1.81',
    'huaweicloudsdkcloudpond==3.1.81',
    'huaweicloudsdkcloudrtc==3.1.81',
    'huaweicloudsdkcloudtable==3.1.81',
    'huaweicloudsdkcloudtest==3.1.81',
    'huaweicloudsdkcodeartsartifact==3.1.81',
    'huaweicloudsdkcodeartsbuild==3.1.81',
    'huaweicloudsdkcodeartscheck==3.1.81',
    'huaweicloudsdkcodeartsdeploy==3.1.81',
    'huaweicloudsdkcodeartsinspector==3.1.81',
    'huaweicloudsdkcodeartspipeline==3.1.81',
    'huaweicloudsdkcodecraft==3.1.81',
    'huaweicloudsdkcodehub==3.1.81',
    'huaweicloudsdkconfig==3.1.81',
    'huaweicloudsdkcph==3.1.81',
    'huaweicloudsdkcpts==3.1.81',
    'huaweicloudsdkcse==3.1.81',
    'huaweicloudsdkcsms==3.1.81',
    'huaweicloudsdkcss==3.1.81',
    'huaweicloudsdkcts==3.1.81',
    'huaweicloudsdkdas==3.1.81',
    'huaweicloudsdkdataartsstudio==3.1.81',
    'huaweicloudsdkdbss==3.1.81',
    'huaweicloudsdkdc==3.1.81',
    'huaweicloudsdkdcs==3.1.81',
    'huaweicloudsdkddm==3.1.81',
    'huaweicloudsdkdds==3.1.81',
    'huaweicloudsdkdeh==3.1.81',
    'huaweicloudsdkdevsecurity==3.1.81',
    'huaweicloudsdkdevstar==3.1.81',
    'huaweicloudsdkdgc==3.1.81',
    'huaweicloudsdkdis==3.1.81',
    'huaweicloudsdkdlf==3.1.81',
    'huaweicloudsdkdli==3.1.81',
    'huaweicloudsdkdns==3.1.81',
    'huaweicloudsdkdris==3.1.81',
    'huaweicloudsdkdrs==3.1.81',
    'huaweicloudsdkdsc==3.1.81',
    'huaweicloudsdkdwr==3.1.81',
    'huaweicloudsdkdws==3.1.81',
    'huaweicloudsdkec==3.1.81',
    'huaweicloudsdkecs==3.1.81',
    'huaweicloudsdkedgesec==3.1.81',
    'huaweicloudsdkeg==3.1.81',
    'huaweicloudsdkeihealth==3.1.81',
    'huaweicloudsdkeip==3.1.81',
    'huaweicloudsdkelb==3.1.81',
    'huaweicloudsdkeps==3.1.81',
    'huaweicloudsdker==3.1.81',
    'huaweicloudsdkevs==3.1.81',
    'huaweicloudsdkfrs==3.1.81',
    'huaweicloudsdkfunctiongraph==3.1.81',
    'huaweicloudsdkga==3.1.81',
    'huaweicloudsdkgaussdb==3.1.81',
    'huaweicloudsdkgaussdbfornosql==3.1.81',
    'huaweicloudsdkgaussdbforopengauss==3.1.81',
    'huaweicloudsdkgeip==3.1.81',
    'huaweicloudsdkges==3.1.81',
    'huaweicloudsdkgsl==3.1.81',
    'huaweicloudsdkhilens==3.1.81',
    'huaweicloudsdkhss==3.1.81',
    'huaweicloudsdkiam==3.1.81',
    'huaweicloudsdkidentitycenter==3.1.81',
    'huaweicloudsdkidentitycenterstore==3.1.81',
    'huaweicloudsdkidme==3.1.81',
    'huaweicloudsdkidmeclassicapi==3.1.81',
    'huaweicloudsdkiec==3.1.81',
    'huaweicloudsdkief==3.1.81',
    'huaweicloudsdkimage==3.1.81',
    'huaweicloudsdkimagesearch==3.1.81',
    'huaweicloudsdkims==3.1.81',
    'huaweicloudsdkiotanalytics==3.1.81',
    'huaweicloudsdkiotda==3.1.81',
    'huaweicloudsdkiotedge==3.1.81',
    'huaweicloudsdkivs==3.1.81',
    'huaweicloudsdkkafka==3.1.81',
    'huaweicloudsdkkms==3.1.81',
    'huaweicloudsdkkoomessage==3.1.81',
    'huaweicloudsdkkps==3.1.81',
    'huaweicloudsdklakeformation==3.1.81',
    'huaweicloudsdklive==3.1.81',
    'huaweicloudsdklts==3.1.81',
    'huaweicloudsdkmapds==3.1.81',
    'huaweicloudsdkmas==3.1.81',
    'huaweicloudsdkmeeting==3.1.81',
    'huaweicloudsdkmetastudio==3.1.81',
    'huaweicloudsdkmoderation==3.1.81',
    'huaweicloudsdkmpc==3.1.81',
    'huaweicloudsdkmrs==3.1.81',
    'huaweicloudsdkmsgsms==3.1.81',
    'huaweicloudsdkmssi==3.1.81',
    'huaweicloudsdknat==3.1.81',
    'huaweicloudsdknlp==3.1.81',
    'huaweicloudsdkobs==3.1.81',
    'huaweicloudsdkocr==3.1.81',
    'huaweicloudsdkoctopus==3.1.81',
    'huaweicloudsdkoms==3.1.81',
    'huaweicloudsdkoptverse==3.1.81',
    'huaweicloudsdkorganizations==3.1.81',
    'huaweicloudsdkorgid==3.1.81',
    'huaweicloudsdkoroas==3.1.81',
    'huaweicloudsdkosm==3.1.81',
    'huaweicloudsdkpangulargemodels==3.1.81',
    'huaweicloudsdkprojectman==3.1.81',
    'huaweicloudsdkrabbitmq==3.1.81',
    'huaweicloudsdkram==3.1.81',
    'huaweicloudsdkrds==3.1.81',
    'huaweicloudsdkres==3.1.81',
    'huaweicloudsdkrgc==3.1.81',
    'huaweicloudsdkrms==3.1.81',
    'huaweicloudsdkrocketmq==3.1.81',
    'huaweicloudsdkroma==3.1.81',
    'huaweicloudsdksa==3.1.81',
    'huaweicloudsdkscm==3.1.81',
    'huaweicloudsdksdrs==3.1.81',
    'huaweicloudsdksecmaster==3.1.81',
    'huaweicloudsdkservicestage==3.1.81',
    'huaweicloudsdksfsturbo==3.1.81',
    'huaweicloudsdksis==3.1.81',
    'huaweicloudsdksmn==3.1.81',
    'huaweicloudsdksms==3.1.81',
    'huaweicloudsdkswr==3.1.81',
    'huaweicloudsdktics==3.1.81',
    'huaweicloudsdktms==3.1.81',
    'huaweicloudsdkugo==3.1.81',
    'huaweicloudsdkvas==3.1.81',
    'huaweicloudsdkvcm==3.1.81',
    'huaweicloudsdkvod==3.1.81',
    'huaweicloudsdkvpc==3.1.81',
    'huaweicloudsdkvpcep==3.1.81',
    'huaweicloudsdkvpn==3.1.81',
    'huaweicloudsdkwaf==3.1.81',
    'huaweicloudsdkworkspace==3.1.81',
    'huaweicloudsdkworkspaceapp==3.1.81',
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
