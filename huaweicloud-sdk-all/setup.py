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
VERSION = "3.1.94"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.94',
    'huaweicloudsdkaad==3.1.94',
    'huaweicloudsdkantiddos==3.1.94',
    'huaweicloudsdkaom==3.1.94',
    'huaweicloudsdkaos==3.1.94',
    'huaweicloudsdkapig==3.1.94',
    'huaweicloudsdkapm==3.1.94',
    'huaweicloudsdkas==3.1.94',
    'huaweicloudsdkasm==3.1.94',
    'huaweicloudsdkbcs==3.1.94',
    'huaweicloudsdkbms==3.1.94',
    'huaweicloudsdkbss==3.1.94',
    'huaweicloudsdkbssintl==3.1.94',
    'huaweicloudsdkcae==3.1.94',
    'huaweicloudsdkcampusgo==3.1.94',
    'huaweicloudsdkcbh==3.1.94',
    'huaweicloudsdkcbr==3.1.94',
    'huaweicloudsdkcbs==3.1.94',
    'huaweicloudsdkcc==3.1.94',
    'huaweicloudsdkcce==3.1.94',
    'huaweicloudsdkccm==3.1.94',
    'huaweicloudsdkcdm==3.1.94',
    'huaweicloudsdkcdn==3.1.94',
    'huaweicloudsdkces==3.1.94',
    'huaweicloudsdkcfw==3.1.94',
    'huaweicloudsdkcgs==3.1.94',
    'huaweicloudsdkclassroom==3.1.94',
    'huaweicloudsdkcloudide==3.1.94',
    'huaweicloudsdkcloudpond==3.1.94',
    'huaweicloudsdkcloudrtc==3.1.94',
    'huaweicloudsdkcloudtable==3.1.94',
    'huaweicloudsdkcloudtest==3.1.94',
    'huaweicloudsdkcodeartsartifact==3.1.94',
    'huaweicloudsdkcodeartsbuild==3.1.94',
    'huaweicloudsdkcodeartscheck==3.1.94',
    'huaweicloudsdkcodeartsdeploy==3.1.94',
    'huaweicloudsdkcodeartsinspector==3.1.94',
    'huaweicloudsdkcodeartspipeline==3.1.94',
    'huaweicloudsdkcodecraft==3.1.94',
    'huaweicloudsdkcodehub==3.1.94',
    'huaweicloudsdkconfig==3.1.94',
    'huaweicloudsdkcph==3.1.94',
    'huaweicloudsdkcpts==3.1.94',
    'huaweicloudsdkcse==3.1.94',
    'huaweicloudsdkcsms==3.1.94',
    'huaweicloudsdkcss==3.1.94',
    'huaweicloudsdkcts==3.1.94',
    'huaweicloudsdkdas==3.1.94',
    'huaweicloudsdkdataartsstudio==3.1.94',
    'huaweicloudsdkdbss==3.1.94',
    'huaweicloudsdkdc==3.1.94',
    'huaweicloudsdkdcs==3.1.94',
    'huaweicloudsdkddm==3.1.94',
    'huaweicloudsdkdds==3.1.94',
    'huaweicloudsdkdeh==3.1.94',
    'huaweicloudsdkdevsecurity==3.1.94',
    'huaweicloudsdkdevstar==3.1.94',
    'huaweicloudsdkdgc==3.1.94',
    'huaweicloudsdkdis==3.1.94',
    'huaweicloudsdkdlf==3.1.94',
    'huaweicloudsdkdli==3.1.94',
    'huaweicloudsdkdns==3.1.94',
    'huaweicloudsdkdris==3.1.94',
    'huaweicloudsdkdrs==3.1.94',
    'huaweicloudsdkdsc==3.1.94',
    'huaweicloudsdkdwr==3.1.94',
    'huaweicloudsdkdws==3.1.94',
    'huaweicloudsdkec==3.1.94',
    'huaweicloudsdkecs==3.1.94',
    'huaweicloudsdkedgesec==3.1.94',
    'huaweicloudsdkeg==3.1.94',
    'huaweicloudsdkeihealth==3.1.94',
    'huaweicloudsdkeip==3.1.94',
    'huaweicloudsdkelb==3.1.94',
    'huaweicloudsdkeps==3.1.94',
    'huaweicloudsdker==3.1.94',
    'huaweicloudsdkevs==3.1.94',
    'huaweicloudsdkfrs==3.1.94',
    'huaweicloudsdkfunctiongraph==3.1.94',
    'huaweicloudsdkga==3.1.94',
    'huaweicloudsdkgaussdb==3.1.94',
    'huaweicloudsdkgaussdbfornosql==3.1.94',
    'huaweicloudsdkgaussdbforopengauss==3.1.94',
    'huaweicloudsdkgeip==3.1.94',
    'huaweicloudsdkges==3.1.94',
    'huaweicloudsdkgsl==3.1.94',
    'huaweicloudsdkhilens==3.1.94',
    'huaweicloudsdkhss==3.1.94',
    'huaweicloudsdkiam==3.1.94',
    'huaweicloudsdkiamaccessanalyzer==3.1.94',
    'huaweicloudsdkidentitycenter==3.1.94',
    'huaweicloudsdkidentitycenterstore==3.1.94',
    'huaweicloudsdkidme==3.1.94',
    'huaweicloudsdkidmeclassicapi==3.1.94',
    'huaweicloudsdkiec==3.1.94',
    'huaweicloudsdkief==3.1.94',
    'huaweicloudsdkimage==3.1.94',
    'huaweicloudsdkimagesearch==3.1.94',
    'huaweicloudsdkims==3.1.94',
    'huaweicloudsdkiotanalytics==3.1.94',
    'huaweicloudsdkiotda==3.1.94',
    'huaweicloudsdkiotedge==3.1.94',
    'huaweicloudsdkivs==3.1.94',
    'huaweicloudsdkkafka==3.1.94',
    'huaweicloudsdkkms==3.1.94',
    'huaweicloudsdkkoomessage==3.1.94',
    'huaweicloudsdkkps==3.1.94',
    'huaweicloudsdklakeformation==3.1.94',
    'huaweicloudsdklive==3.1.94',
    'huaweicloudsdklts==3.1.94',
    'huaweicloudsdkmapds==3.1.94',
    'huaweicloudsdkmas==3.1.94',
    'huaweicloudsdkmeeting==3.1.94',
    'huaweicloudsdkmetastudio==3.1.94',
    'huaweicloudsdkmoderation==3.1.94',
    'huaweicloudsdkmpc==3.1.94',
    'huaweicloudsdkmrs==3.1.94',
    'huaweicloudsdkmsgsms==3.1.94',
    'huaweicloudsdkmssi==3.1.94',
    'huaweicloudsdknat==3.1.94',
    'huaweicloudsdknlp==3.1.94',
    'huaweicloudsdkobs==3.1.94',
    'huaweicloudsdkocr==3.1.94',
    'huaweicloudsdkoctopus==3.1.94',
    'huaweicloudsdkoms==3.1.94',
    'huaweicloudsdkoptverse==3.1.94',
    'huaweicloudsdkorganizations==3.1.94',
    'huaweicloudsdkorgid==3.1.94',
    'huaweicloudsdkoroas==3.1.94',
    'huaweicloudsdkosm==3.1.94',
    'huaweicloudsdkpangulargemodels==3.1.94',
    'huaweicloudsdkprojectman==3.1.94',
    'huaweicloudsdkrabbitmq==3.1.94',
    'huaweicloudsdkram==3.1.94',
    'huaweicloudsdkrds==3.1.94',
    'huaweicloudsdkres==3.1.94',
    'huaweicloudsdkrgc==3.1.94',
    'huaweicloudsdkrms==3.1.94',
    'huaweicloudsdkrocketmq==3.1.94',
    'huaweicloudsdkroma==3.1.94',
    'huaweicloudsdksa==3.1.94',
    'huaweicloudsdkscm==3.1.94',
    'huaweicloudsdksdrs==3.1.94',
    'huaweicloudsdksecmaster==3.1.94',
    'huaweicloudsdkservicestage==3.1.94',
    'huaweicloudsdksfsturbo==3.1.94',
    'huaweicloudsdksis==3.1.94',
    'huaweicloudsdksmn==3.1.94',
    'huaweicloudsdksms==3.1.94',
    'huaweicloudsdksts==3.1.94',
    'huaweicloudsdkswr==3.1.94',
    'huaweicloudsdktics==3.1.94',
    'huaweicloudsdktms==3.1.94',
    'huaweicloudsdkugo==3.1.94',
    'huaweicloudsdkvas==3.1.94',
    'huaweicloudsdkvcm==3.1.94',
    'huaweicloudsdkvod==3.1.94',
    'huaweicloudsdkvpc==3.1.94',
    'huaweicloudsdkvpcep==3.1.94',
    'huaweicloudsdkvpn==3.1.94',
    'huaweicloudsdkwaf==3.1.94',
    'huaweicloudsdkworkspace==3.1.94',
    'huaweicloudsdkworkspaceapp==3.1.94',
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
