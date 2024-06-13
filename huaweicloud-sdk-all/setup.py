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
VERSION = "3.1.100"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.100',
    'huaweicloudsdkaad==3.1.100',
    'huaweicloudsdkantiddos==3.1.100',
    'huaweicloudsdkaom==3.1.100',
    'huaweicloudsdkaos==3.1.100',
    'huaweicloudsdkapig==3.1.100',
    'huaweicloudsdkapm==3.1.100',
    'huaweicloudsdkas==3.1.100',
    'huaweicloudsdkasm==3.1.100',
    'huaweicloudsdkbcs==3.1.100',
    'huaweicloudsdkbms==3.1.100',
    'huaweicloudsdkbss==3.1.100',
    'huaweicloudsdkbssintl==3.1.100',
    'huaweicloudsdkcae==3.1.100',
    'huaweicloudsdkcampusgo==3.1.100',
    'huaweicloudsdkcbh==3.1.100',
    'huaweicloudsdkcbr==3.1.100',
    'huaweicloudsdkcbs==3.1.100',
    'huaweicloudsdkcc==3.1.100',
    'huaweicloudsdkcce==3.1.100',
    'huaweicloudsdkccm==3.1.100',
    'huaweicloudsdkcdm==3.1.100',
    'huaweicloudsdkcdn==3.1.100',
    'huaweicloudsdkces==3.1.100',
    'huaweicloudsdkcfw==3.1.100',
    'huaweicloudsdkcgs==3.1.100',
    'huaweicloudsdkclassroom==3.1.100',
    'huaweicloudsdkcloudide==3.1.100',
    'huaweicloudsdkcloudpond==3.1.100',
    'huaweicloudsdkcloudrtc==3.1.100',
    'huaweicloudsdkcloudtable==3.1.100',
    'huaweicloudsdkcloudtest==3.1.100',
    'huaweicloudsdkcodeartsartifact==3.1.100',
    'huaweicloudsdkcodeartsbuild==3.1.100',
    'huaweicloudsdkcodeartscheck==3.1.100',
    'huaweicloudsdkcodeartsdeploy==3.1.100',
    'huaweicloudsdkcodeartsinspector==3.1.100',
    'huaweicloudsdkcodeartspipeline==3.1.100',
    'huaweicloudsdkcodecraft==3.1.100',
    'huaweicloudsdkcodehub==3.1.100',
    'huaweicloudsdkconfig==3.1.100',
    'huaweicloudsdkcph==3.1.100',
    'huaweicloudsdkcpts==3.1.100',
    'huaweicloudsdkcse==3.1.100',
    'huaweicloudsdkcsms==3.1.100',
    'huaweicloudsdkcss==3.1.100',
    'huaweicloudsdkcts==3.1.100',
    'huaweicloudsdkdas==3.1.100',
    'huaweicloudsdkdataartsstudio==3.1.100',
    'huaweicloudsdkdbss==3.1.100',
    'huaweicloudsdkdc==3.1.100',
    'huaweicloudsdkdcs==3.1.100',
    'huaweicloudsdkddm==3.1.100',
    'huaweicloudsdkdds==3.1.100',
    'huaweicloudsdkdeh==3.1.100',
    'huaweicloudsdkdevsecurity==3.1.100',
    'huaweicloudsdkdevstar==3.1.100',
    'huaweicloudsdkdgc==3.1.100',
    'huaweicloudsdkdis==3.1.100',
    'huaweicloudsdkdlf==3.1.100',
    'huaweicloudsdkdli==3.1.100',
    'huaweicloudsdkdns==3.1.100',
    'huaweicloudsdkdris==3.1.100',
    'huaweicloudsdkdrs==3.1.100',
    'huaweicloudsdkdsc==3.1.100',
    'huaweicloudsdkdwr==3.1.100',
    'huaweicloudsdkdws==3.1.100',
    'huaweicloudsdkec==3.1.100',
    'huaweicloudsdkecs==3.1.100',
    'huaweicloudsdkedgesec==3.1.100',
    'huaweicloudsdkeg==3.1.100',
    'huaweicloudsdkeihealth==3.1.100',
    'huaweicloudsdkeip==3.1.100',
    'huaweicloudsdkelb==3.1.100',
    'huaweicloudsdkeps==3.1.100',
    'huaweicloudsdker==3.1.100',
    'huaweicloudsdkevs==3.1.100',
    'huaweicloudsdkfrs==3.1.100',
    'huaweicloudsdkfunctiongraph==3.1.100',
    'huaweicloudsdkga==3.1.100',
    'huaweicloudsdkgaussdb==3.1.100',
    'huaweicloudsdkgaussdbfornosql==3.1.100',
    'huaweicloudsdkgaussdbforopengauss==3.1.100',
    'huaweicloudsdkgeip==3.1.100',
    'huaweicloudsdkges==3.1.100',
    'huaweicloudsdkgsl==3.1.100',
    'huaweicloudsdkhilens==3.1.100',
    'huaweicloudsdkhss==3.1.100',
    'huaweicloudsdkiam==3.1.100',
    'huaweicloudsdkiamaccessanalyzer==3.1.100',
    'huaweicloudsdkidentitycenter==3.1.100',
    'huaweicloudsdkidentitycenterstore==3.1.100',
    'huaweicloudsdkidme==3.1.100',
    'huaweicloudsdkidmeclassicapi==3.1.100',
    'huaweicloudsdkiec==3.1.100',
    'huaweicloudsdkief==3.1.100',
    'huaweicloudsdkimage==3.1.100',
    'huaweicloudsdkimagesearch==3.1.100',
    'huaweicloudsdkims==3.1.100',
    'huaweicloudsdkiotanalytics==3.1.100',
    'huaweicloudsdkiotda==3.1.100',
    'huaweicloudsdkiotedge==3.1.100',
    'huaweicloudsdkivs==3.1.100',
    'huaweicloudsdkkafka==3.1.100',
    'huaweicloudsdkkms==3.1.100',
    'huaweicloudsdkkoomessage==3.1.100',
    'huaweicloudsdkkps==3.1.100',
    'huaweicloudsdklakeformation==3.1.100',
    'huaweicloudsdklive==3.1.100',
    'huaweicloudsdklts==3.1.100',
    'huaweicloudsdkmapds==3.1.100',
    'huaweicloudsdkmas==3.1.100',
    'huaweicloudsdkmeeting==3.1.100',
    'huaweicloudsdkmetastudio==3.1.100',
    'huaweicloudsdkmoderation==3.1.100',
    'huaweicloudsdkmpc==3.1.100',
    'huaweicloudsdkmrs==3.1.100',
    'huaweicloudsdkmsgsms==3.1.100',
    'huaweicloudsdkmssi==3.1.100',
    'huaweicloudsdknat==3.1.100',
    'huaweicloudsdknlp==3.1.100',
    'huaweicloudsdkobs==3.1.100',
    'huaweicloudsdkocr==3.1.100',
    'huaweicloudsdkoctopus==3.1.100',
    'huaweicloudsdkoms==3.1.100',
    'huaweicloudsdkoptverse==3.1.100',
    'huaweicloudsdkorganizations==3.1.100',
    'huaweicloudsdkorgid==3.1.100',
    'huaweicloudsdkoroas==3.1.100',
    'huaweicloudsdkosm==3.1.100',
    'huaweicloudsdkpangulargemodels==3.1.100',
    'huaweicloudsdkprojectman==3.1.100',
    'huaweicloudsdkrabbitmq==3.1.100',
    'huaweicloudsdkram==3.1.100',
    'huaweicloudsdkrds==3.1.100',
    'huaweicloudsdkres==3.1.100',
    'huaweicloudsdkrgc==3.1.100',
    'huaweicloudsdkrms==3.1.100',
    'huaweicloudsdkrocketmq==3.1.100',
    'huaweicloudsdkroma==3.1.100',
    'huaweicloudsdksa==3.1.100',
    'huaweicloudsdkscm==3.1.100',
    'huaweicloudsdksdrs==3.1.100',
    'huaweicloudsdksecmaster==3.1.100',
    'huaweicloudsdkservicestage==3.1.100',
    'huaweicloudsdksfsturbo==3.1.100',
    'huaweicloudsdksis==3.1.100',
    'huaweicloudsdksmn==3.1.100',
    'huaweicloudsdksms==3.1.100',
    'huaweicloudsdksts==3.1.100',
    'huaweicloudsdkswr==3.1.100',
    'huaweicloudsdktics==3.1.100',
    'huaweicloudsdktms==3.1.100',
    'huaweicloudsdkugo==3.1.100',
    'huaweicloudsdkvas==3.1.100',
    'huaweicloudsdkvcm==3.1.100',
    'huaweicloudsdkvod==3.1.100',
    'huaweicloudsdkvpc==3.1.100',
    'huaweicloudsdkvpcep==3.1.100',
    'huaweicloudsdkvpn==3.1.100',
    'huaweicloudsdkwaf==3.1.100',
    'huaweicloudsdkworkspace==3.1.100',
    'huaweicloudsdkworkspaceapp==3.1.100',
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
