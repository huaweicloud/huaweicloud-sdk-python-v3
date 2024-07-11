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
VERSION = "3.1.105"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.105',
    'huaweicloudsdkaad==3.1.105',
    'huaweicloudsdkantiddos==3.1.105',
    'huaweicloudsdkaom==3.1.105',
    'huaweicloudsdkaos==3.1.105',
    'huaweicloudsdkapig==3.1.105',
    'huaweicloudsdkapm==3.1.105',
    'huaweicloudsdkas==3.1.105',
    'huaweicloudsdkasm==3.1.105',
    'huaweicloudsdkbcs==3.1.105',
    'huaweicloudsdkbms==3.1.105',
    'huaweicloudsdkbss==3.1.105',
    'huaweicloudsdkbssintl==3.1.105',
    'huaweicloudsdkcae==3.1.105',
    'huaweicloudsdkcampusgo==3.1.105',
    'huaweicloudsdkcbh==3.1.105',
    'huaweicloudsdkcbr==3.1.105',
    'huaweicloudsdkcbs==3.1.105',
    'huaweicloudsdkcc==3.1.105',
    'huaweicloudsdkcce==3.1.105',
    'huaweicloudsdkccm==3.1.105',
    'huaweicloudsdkcdm==3.1.105',
    'huaweicloudsdkcdn==3.1.105',
    'huaweicloudsdkces==3.1.105',
    'huaweicloudsdkcfw==3.1.105',
    'huaweicloudsdkcgs==3.1.105',
    'huaweicloudsdkclassroom==3.1.105',
    'huaweicloudsdkcloudide==3.1.105',
    'huaweicloudsdkcloudpond==3.1.105',
    'huaweicloudsdkcloudrtc==3.1.105',
    'huaweicloudsdkcloudtable==3.1.105',
    'huaweicloudsdkcloudtest==3.1.105',
    'huaweicloudsdkcodeartsartifact==3.1.105',
    'huaweicloudsdkcodeartsbuild==3.1.105',
    'huaweicloudsdkcodeartscheck==3.1.105',
    'huaweicloudsdkcodeartsdeploy==3.1.105',
    'huaweicloudsdkcodeartsinspector==3.1.105',
    'huaweicloudsdkcodeartspipeline==3.1.105',
    'huaweicloudsdkcodecraft==3.1.105',
    'huaweicloudsdkcodehub==3.1.105',
    'huaweicloudsdkconfig==3.1.105',
    'huaweicloudsdkcph==3.1.105',
    'huaweicloudsdkcpts==3.1.105',
    'huaweicloudsdkcse==3.1.105',
    'huaweicloudsdkcsms==3.1.105',
    'huaweicloudsdkcss==3.1.105',
    'huaweicloudsdkcts==3.1.105',
    'huaweicloudsdkdas==3.1.105',
    'huaweicloudsdkdataartsstudio==3.1.105',
    'huaweicloudsdkdbss==3.1.105',
    'huaweicloudsdkdc==3.1.105',
    'huaweicloudsdkdcs==3.1.105',
    'huaweicloudsdkddm==3.1.105',
    'huaweicloudsdkdds==3.1.105',
    'huaweicloudsdkdeh==3.1.105',
    'huaweicloudsdkdevsecurity==3.1.105',
    'huaweicloudsdkdevstar==3.1.105',
    'huaweicloudsdkdgc==3.1.105',
    'huaweicloudsdkdis==3.1.105',
    'huaweicloudsdkdlf==3.1.105',
    'huaweicloudsdkdli==3.1.105',
    'huaweicloudsdkdns==3.1.105',
    'huaweicloudsdkdris==3.1.105',
    'huaweicloudsdkdrs==3.1.105',
    'huaweicloudsdkdsc==3.1.105',
    'huaweicloudsdkdwr==3.1.105',
    'huaweicloudsdkdws==3.1.105',
    'huaweicloudsdkec==3.1.105',
    'huaweicloudsdkecs==3.1.105',
    'huaweicloudsdkedgesec==3.1.105',
    'huaweicloudsdkeg==3.1.105',
    'huaweicloudsdkeihealth==3.1.105',
    'huaweicloudsdkeip==3.1.105',
    'huaweicloudsdkelb==3.1.105',
    'huaweicloudsdkeps==3.1.105',
    'huaweicloudsdker==3.1.105',
    'huaweicloudsdkevs==3.1.105',
    'huaweicloudsdkfrs==3.1.105',
    'huaweicloudsdkfunctiongraph==3.1.105',
    'huaweicloudsdkga==3.1.105',
    'huaweicloudsdkgaussdb==3.1.105',
    'huaweicloudsdkgaussdbfornosql==3.1.105',
    'huaweicloudsdkgaussdbforopengauss==3.1.105',
    'huaweicloudsdkgeip==3.1.105',
    'huaweicloudsdkges==3.1.105',
    'huaweicloudsdkgsl==3.1.105',
    'huaweicloudsdkhilens==3.1.105',
    'huaweicloudsdkhss==3.1.105',
    'huaweicloudsdkiam==3.1.105',
    'huaweicloudsdkiamaccessanalyzer==3.1.105',
    'huaweicloudsdkidentitycenter==3.1.105',
    'huaweicloudsdkidentitycenterstore==3.1.105',
    'huaweicloudsdkidme==3.1.105',
    'huaweicloudsdkidmeclassicapi==3.1.105',
    'huaweicloudsdkiec==3.1.105',
    'huaweicloudsdkief==3.1.105',
    'huaweicloudsdkimage==3.1.105',
    'huaweicloudsdkimagesearch==3.1.105',
    'huaweicloudsdkims==3.1.105',
    'huaweicloudsdkiotanalytics==3.1.105',
    'huaweicloudsdkiotda==3.1.105',
    'huaweicloudsdkiotedge==3.1.105',
    'huaweicloudsdkivs==3.1.105',
    'huaweicloudsdkkafka==3.1.105',
    'huaweicloudsdkkms==3.1.105',
    'huaweicloudsdkkoomessage==3.1.105',
    'huaweicloudsdkkps==3.1.105',
    'huaweicloudsdklakeformation==3.1.105',
    'huaweicloudsdklive==3.1.105',
    'huaweicloudsdklts==3.1.105',
    'huaweicloudsdkmapds==3.1.105',
    'huaweicloudsdkmas==3.1.105',
    'huaweicloudsdkmeeting==3.1.105',
    'huaweicloudsdkmetastudio==3.1.105',
    'huaweicloudsdkmoderation==3.1.105',
    'huaweicloudsdkmpc==3.1.105',
    'huaweicloudsdkmrs==3.1.105',
    'huaweicloudsdkmsgsms==3.1.105',
    'huaweicloudsdkmssi==3.1.105',
    'huaweicloudsdknat==3.1.105',
    'huaweicloudsdknlp==3.1.105',
    'huaweicloudsdkobs==3.1.105',
    'huaweicloudsdkocr==3.1.105',
    'huaweicloudsdkoctopus==3.1.105',
    'huaweicloudsdkoms==3.1.105',
    'huaweicloudsdkoptverse==3.1.105',
    'huaweicloudsdkorganizations==3.1.105',
    'huaweicloudsdkorgid==3.1.105',
    'huaweicloudsdkoroas==3.1.105',
    'huaweicloudsdkosm==3.1.105',
    'huaweicloudsdkpangulargemodels==3.1.105',
    'huaweicloudsdkprojectman==3.1.105',
    'huaweicloudsdkrabbitmq==3.1.105',
    'huaweicloudsdkram==3.1.105',
    'huaweicloudsdkrds==3.1.105',
    'huaweicloudsdkres==3.1.105',
    'huaweicloudsdkrgc==3.1.105',
    'huaweicloudsdkrms==3.1.105',
    'huaweicloudsdkrocketmq==3.1.105',
    'huaweicloudsdkroma==3.1.105',
    'huaweicloudsdksa==3.1.105',
    'huaweicloudsdkscm==3.1.105',
    'huaweicloudsdksdrs==3.1.105',
    'huaweicloudsdksecmaster==3.1.105',
    'huaweicloudsdkservicestage==3.1.105',
    'huaweicloudsdksfsturbo==3.1.105',
    'huaweicloudsdksis==3.1.105',
    'huaweicloudsdksmn==3.1.105',
    'huaweicloudsdksms==3.1.105',
    'huaweicloudsdksts==3.1.105',
    'huaweicloudsdkswr==3.1.105',
    'huaweicloudsdktics==3.1.105',
    'huaweicloudsdktms==3.1.105',
    'huaweicloudsdkugo==3.1.105',
    'huaweicloudsdkvas==3.1.105',
    'huaweicloudsdkvcm==3.1.105',
    'huaweicloudsdkvod==3.1.105',
    'huaweicloudsdkvpc==3.1.105',
    'huaweicloudsdkvpcep==3.1.105',
    'huaweicloudsdkvpn==3.1.105',
    'huaweicloudsdkwaf==3.1.105',
    'huaweicloudsdkworkspace==3.1.105',
    'huaweicloudsdkworkspaceapp==3.1.105',
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
