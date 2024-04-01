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
VERSION = "3.1.89"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.89',
    'huaweicloudsdkaad==3.1.89',
    'huaweicloudsdkantiddos==3.1.89',
    'huaweicloudsdkaom==3.1.89',
    'huaweicloudsdkaos==3.1.89',
    'huaweicloudsdkapig==3.1.89',
    'huaweicloudsdkapm==3.1.89',
    'huaweicloudsdkas==3.1.89',
    'huaweicloudsdkasm==3.1.89',
    'huaweicloudsdkbcs==3.1.89',
    'huaweicloudsdkbms==3.1.89',
    'huaweicloudsdkbss==3.1.89',
    'huaweicloudsdkbssintl==3.1.89',
    'huaweicloudsdkcae==3.1.89',
    'huaweicloudsdkcampusgo==3.1.89',
    'huaweicloudsdkcbh==3.1.89',
    'huaweicloudsdkcbr==3.1.89',
    'huaweicloudsdkcbs==3.1.89',
    'huaweicloudsdkcc==3.1.89',
    'huaweicloudsdkcce==3.1.89',
    'huaweicloudsdkccm==3.1.89',
    'huaweicloudsdkcdm==3.1.89',
    'huaweicloudsdkcdn==3.1.89',
    'huaweicloudsdkces==3.1.89',
    'huaweicloudsdkcfw==3.1.89',
    'huaweicloudsdkcgs==3.1.89',
    'huaweicloudsdkclassroom==3.1.89',
    'huaweicloudsdkcloudide==3.1.89',
    'huaweicloudsdkcloudpond==3.1.89',
    'huaweicloudsdkcloudrtc==3.1.89',
    'huaweicloudsdkcloudtable==3.1.89',
    'huaweicloudsdkcloudtest==3.1.89',
    'huaweicloudsdkcodeartsartifact==3.1.89',
    'huaweicloudsdkcodeartsbuild==3.1.89',
    'huaweicloudsdkcodeartscheck==3.1.89',
    'huaweicloudsdkcodeartsdeploy==3.1.89',
    'huaweicloudsdkcodeartsinspector==3.1.89',
    'huaweicloudsdkcodeartspipeline==3.1.89',
    'huaweicloudsdkcodecraft==3.1.89',
    'huaweicloudsdkcodehub==3.1.89',
    'huaweicloudsdkconfig==3.1.89',
    'huaweicloudsdkcph==3.1.89',
    'huaweicloudsdkcpts==3.1.89',
    'huaweicloudsdkcse==3.1.89',
    'huaweicloudsdkcsms==3.1.89',
    'huaweicloudsdkcss==3.1.89',
    'huaweicloudsdkcts==3.1.89',
    'huaweicloudsdkdas==3.1.89',
    'huaweicloudsdkdataartsstudio==3.1.89',
    'huaweicloudsdkdbss==3.1.89',
    'huaweicloudsdkdc==3.1.89',
    'huaweicloudsdkdcs==3.1.89',
    'huaweicloudsdkddm==3.1.89',
    'huaweicloudsdkdds==3.1.89',
    'huaweicloudsdkdeh==3.1.89',
    'huaweicloudsdkdevsecurity==3.1.89',
    'huaweicloudsdkdevstar==3.1.89',
    'huaweicloudsdkdgc==3.1.89',
    'huaweicloudsdkdis==3.1.89',
    'huaweicloudsdkdlf==3.1.89',
    'huaweicloudsdkdli==3.1.89',
    'huaweicloudsdkdns==3.1.89',
    'huaweicloudsdkdris==3.1.89',
    'huaweicloudsdkdrs==3.1.89',
    'huaweicloudsdkdsc==3.1.89',
    'huaweicloudsdkdwr==3.1.89',
    'huaweicloudsdkdws==3.1.89',
    'huaweicloudsdkec==3.1.89',
    'huaweicloudsdkecs==3.1.89',
    'huaweicloudsdkedgesec==3.1.89',
    'huaweicloudsdkeg==3.1.89',
    'huaweicloudsdkeihealth==3.1.89',
    'huaweicloudsdkeip==3.1.89',
    'huaweicloudsdkelb==3.1.89',
    'huaweicloudsdkeps==3.1.89',
    'huaweicloudsdker==3.1.89',
    'huaweicloudsdkevs==3.1.89',
    'huaweicloudsdkfrs==3.1.89',
    'huaweicloudsdkfunctiongraph==3.1.89',
    'huaweicloudsdkga==3.1.89',
    'huaweicloudsdkgaussdb==3.1.89',
    'huaweicloudsdkgaussdbfornosql==3.1.89',
    'huaweicloudsdkgaussdbforopengauss==3.1.89',
    'huaweicloudsdkgeip==3.1.89',
    'huaweicloudsdkges==3.1.89',
    'huaweicloudsdkgsl==3.1.89',
    'huaweicloudsdkhilens==3.1.89',
    'huaweicloudsdkhss==3.1.89',
    'huaweicloudsdkiam==3.1.89',
    'huaweicloudsdkiamaccessanalyzer==3.1.89',
    'huaweicloudsdkidentitycenter==3.1.89',
    'huaweicloudsdkidentitycenterstore==3.1.89',
    'huaweicloudsdkidme==3.1.89',
    'huaweicloudsdkidmeclassicapi==3.1.89',
    'huaweicloudsdkiec==3.1.89',
    'huaweicloudsdkief==3.1.89',
    'huaweicloudsdkimage==3.1.89',
    'huaweicloudsdkimagesearch==3.1.89',
    'huaweicloudsdkims==3.1.89',
    'huaweicloudsdkiotanalytics==3.1.89',
    'huaweicloudsdkiotda==3.1.89',
    'huaweicloudsdkiotedge==3.1.89',
    'huaweicloudsdkivs==3.1.89',
    'huaweicloudsdkkafka==3.1.89',
    'huaweicloudsdkkms==3.1.89',
    'huaweicloudsdkkoomessage==3.1.89',
    'huaweicloudsdkkps==3.1.89',
    'huaweicloudsdklakeformation==3.1.89',
    'huaweicloudsdklive==3.1.89',
    'huaweicloudsdklts==3.1.89',
    'huaweicloudsdkmapds==3.1.89',
    'huaweicloudsdkmas==3.1.89',
    'huaweicloudsdkmeeting==3.1.89',
    'huaweicloudsdkmetastudio==3.1.89',
    'huaweicloudsdkmoderation==3.1.89',
    'huaweicloudsdkmpc==3.1.89',
    'huaweicloudsdkmrs==3.1.89',
    'huaweicloudsdkmsgsms==3.1.89',
    'huaweicloudsdkmssi==3.1.89',
    'huaweicloudsdknat==3.1.89',
    'huaweicloudsdknlp==3.1.89',
    'huaweicloudsdkobs==3.1.89',
    'huaweicloudsdkocr==3.1.89',
    'huaweicloudsdkoctopus==3.1.89',
    'huaweicloudsdkoms==3.1.89',
    'huaweicloudsdkoptverse==3.1.89',
    'huaweicloudsdkorganizations==3.1.89',
    'huaweicloudsdkorgid==3.1.89',
    'huaweicloudsdkoroas==3.1.89',
    'huaweicloudsdkosm==3.1.89',
    'huaweicloudsdkpangulargemodels==3.1.89',
    'huaweicloudsdkprojectman==3.1.89',
    'huaweicloudsdkrabbitmq==3.1.89',
    'huaweicloudsdkram==3.1.89',
    'huaweicloudsdkrds==3.1.89',
    'huaweicloudsdkres==3.1.89',
    'huaweicloudsdkrgc==3.1.89',
    'huaweicloudsdkrms==3.1.89',
    'huaweicloudsdkrocketmq==3.1.89',
    'huaweicloudsdkroma==3.1.89',
    'huaweicloudsdksa==3.1.89',
    'huaweicloudsdkscm==3.1.89',
    'huaweicloudsdksdrs==3.1.89',
    'huaweicloudsdksecmaster==3.1.89',
    'huaweicloudsdkservicestage==3.1.89',
    'huaweicloudsdksfsturbo==3.1.89',
    'huaweicloudsdksis==3.1.89',
    'huaweicloudsdksmn==3.1.89',
    'huaweicloudsdksms==3.1.89',
    'huaweicloudsdkswr==3.1.89',
    'huaweicloudsdktics==3.1.89',
    'huaweicloudsdktms==3.1.89',
    'huaweicloudsdkugo==3.1.89',
    'huaweicloudsdkvas==3.1.89',
    'huaweicloudsdkvcm==3.1.89',
    'huaweicloudsdkvod==3.1.89',
    'huaweicloudsdkvpc==3.1.89',
    'huaweicloudsdkvpcep==3.1.89',
    'huaweicloudsdkvpn==3.1.89',
    'huaweicloudsdkwaf==3.1.89',
    'huaweicloudsdkworkspace==3.1.89',
    'huaweicloudsdkworkspaceapp==3.1.89',
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
