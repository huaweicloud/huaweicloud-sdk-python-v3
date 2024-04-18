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
VERSION = "3.1.92"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.92',
    'huaweicloudsdkaad==3.1.92',
    'huaweicloudsdkantiddos==3.1.92',
    'huaweicloudsdkaom==3.1.92',
    'huaweicloudsdkaos==3.1.92',
    'huaweicloudsdkapig==3.1.92',
    'huaweicloudsdkapm==3.1.92',
    'huaweicloudsdkas==3.1.92',
    'huaweicloudsdkasm==3.1.92',
    'huaweicloudsdkbcs==3.1.92',
    'huaweicloudsdkbms==3.1.92',
    'huaweicloudsdkbss==3.1.92',
    'huaweicloudsdkbssintl==3.1.92',
    'huaweicloudsdkcae==3.1.92',
    'huaweicloudsdkcampusgo==3.1.92',
    'huaweicloudsdkcbh==3.1.92',
    'huaweicloudsdkcbr==3.1.92',
    'huaweicloudsdkcbs==3.1.92',
    'huaweicloudsdkcc==3.1.92',
    'huaweicloudsdkcce==3.1.92',
    'huaweicloudsdkccm==3.1.92',
    'huaweicloudsdkcdm==3.1.92',
    'huaweicloudsdkcdn==3.1.92',
    'huaweicloudsdkces==3.1.92',
    'huaweicloudsdkcfw==3.1.92',
    'huaweicloudsdkcgs==3.1.92',
    'huaweicloudsdkclassroom==3.1.92',
    'huaweicloudsdkcloudide==3.1.92',
    'huaweicloudsdkcloudpond==3.1.92',
    'huaweicloudsdkcloudrtc==3.1.92',
    'huaweicloudsdkcloudtable==3.1.92',
    'huaweicloudsdkcloudtest==3.1.92',
    'huaweicloudsdkcodeartsartifact==3.1.92',
    'huaweicloudsdkcodeartsbuild==3.1.92',
    'huaweicloudsdkcodeartscheck==3.1.92',
    'huaweicloudsdkcodeartsdeploy==3.1.92',
    'huaweicloudsdkcodeartsinspector==3.1.92',
    'huaweicloudsdkcodeartspipeline==3.1.92',
    'huaweicloudsdkcodecraft==3.1.92',
    'huaweicloudsdkcodehub==3.1.92',
    'huaweicloudsdkconfig==3.1.92',
    'huaweicloudsdkcph==3.1.92',
    'huaweicloudsdkcpts==3.1.92',
    'huaweicloudsdkcse==3.1.92',
    'huaweicloudsdkcsms==3.1.92',
    'huaweicloudsdkcss==3.1.92',
    'huaweicloudsdkcts==3.1.92',
    'huaweicloudsdkdas==3.1.92',
    'huaweicloudsdkdataartsstudio==3.1.92',
    'huaweicloudsdkdbss==3.1.92',
    'huaweicloudsdkdc==3.1.92',
    'huaweicloudsdkdcs==3.1.92',
    'huaweicloudsdkddm==3.1.92',
    'huaweicloudsdkdds==3.1.92',
    'huaweicloudsdkdeh==3.1.92',
    'huaweicloudsdkdevsecurity==3.1.92',
    'huaweicloudsdkdevstar==3.1.92',
    'huaweicloudsdkdgc==3.1.92',
    'huaweicloudsdkdis==3.1.92',
    'huaweicloudsdkdlf==3.1.92',
    'huaweicloudsdkdli==3.1.92',
    'huaweicloudsdkdns==3.1.92',
    'huaweicloudsdkdris==3.1.92',
    'huaweicloudsdkdrs==3.1.92',
    'huaweicloudsdkdsc==3.1.92',
    'huaweicloudsdkdwr==3.1.92',
    'huaweicloudsdkdws==3.1.92',
    'huaweicloudsdkec==3.1.92',
    'huaweicloudsdkecs==3.1.92',
    'huaweicloudsdkedgesec==3.1.92',
    'huaweicloudsdkeg==3.1.92',
    'huaweicloudsdkeihealth==3.1.92',
    'huaweicloudsdkeip==3.1.92',
    'huaweicloudsdkelb==3.1.92',
    'huaweicloudsdkeps==3.1.92',
    'huaweicloudsdker==3.1.92',
    'huaweicloudsdkevs==3.1.92',
    'huaweicloudsdkfrs==3.1.92',
    'huaweicloudsdkfunctiongraph==3.1.92',
    'huaweicloudsdkga==3.1.92',
    'huaweicloudsdkgaussdb==3.1.92',
    'huaweicloudsdkgaussdbfornosql==3.1.92',
    'huaweicloudsdkgaussdbforopengauss==3.1.92',
    'huaweicloudsdkgeip==3.1.92',
    'huaweicloudsdkges==3.1.92',
    'huaweicloudsdkgsl==3.1.92',
    'huaweicloudsdkhilens==3.1.92',
    'huaweicloudsdkhss==3.1.92',
    'huaweicloudsdkiam==3.1.92',
    'huaweicloudsdkiamaccessanalyzer==3.1.92',
    'huaweicloudsdkidentitycenter==3.1.92',
    'huaweicloudsdkidentitycenterstore==3.1.92',
    'huaweicloudsdkidme==3.1.92',
    'huaweicloudsdkidmeclassicapi==3.1.92',
    'huaweicloudsdkiec==3.1.92',
    'huaweicloudsdkief==3.1.92',
    'huaweicloudsdkimage==3.1.92',
    'huaweicloudsdkimagesearch==3.1.92',
    'huaweicloudsdkims==3.1.92',
    'huaweicloudsdkiotanalytics==3.1.92',
    'huaweicloudsdkiotda==3.1.92',
    'huaweicloudsdkiotedge==3.1.92',
    'huaweicloudsdkivs==3.1.92',
    'huaweicloudsdkkafka==3.1.92',
    'huaweicloudsdkkms==3.1.92',
    'huaweicloudsdkkoomessage==3.1.92',
    'huaweicloudsdkkps==3.1.92',
    'huaweicloudsdklakeformation==3.1.92',
    'huaweicloudsdklive==3.1.92',
    'huaweicloudsdklts==3.1.92',
    'huaweicloudsdkmapds==3.1.92',
    'huaweicloudsdkmas==3.1.92',
    'huaweicloudsdkmeeting==3.1.92',
    'huaweicloudsdkmetastudio==3.1.92',
    'huaweicloudsdkmoderation==3.1.92',
    'huaweicloudsdkmpc==3.1.92',
    'huaweicloudsdkmrs==3.1.92',
    'huaweicloudsdkmsgsms==3.1.92',
    'huaweicloudsdkmssi==3.1.92',
    'huaweicloudsdknat==3.1.92',
    'huaweicloudsdknlp==3.1.92',
    'huaweicloudsdkobs==3.1.92',
    'huaweicloudsdkocr==3.1.92',
    'huaweicloudsdkoctopus==3.1.92',
    'huaweicloudsdkoms==3.1.92',
    'huaweicloudsdkoptverse==3.1.92',
    'huaweicloudsdkorganizations==3.1.92',
    'huaweicloudsdkorgid==3.1.92',
    'huaweicloudsdkoroas==3.1.92',
    'huaweicloudsdkosm==3.1.92',
    'huaweicloudsdkpangulargemodels==3.1.92',
    'huaweicloudsdkprojectman==3.1.92',
    'huaweicloudsdkrabbitmq==3.1.92',
    'huaweicloudsdkram==3.1.92',
    'huaweicloudsdkrds==3.1.92',
    'huaweicloudsdkres==3.1.92',
    'huaweicloudsdkrgc==3.1.92',
    'huaweicloudsdkrms==3.1.92',
    'huaweicloudsdkrocketmq==3.1.92',
    'huaweicloudsdkroma==3.1.92',
    'huaweicloudsdksa==3.1.92',
    'huaweicloudsdkscm==3.1.92',
    'huaweicloudsdksdrs==3.1.92',
    'huaweicloudsdksecmaster==3.1.92',
    'huaweicloudsdkservicestage==3.1.92',
    'huaweicloudsdksfsturbo==3.1.92',
    'huaweicloudsdksis==3.1.92',
    'huaweicloudsdksmn==3.1.92',
    'huaweicloudsdksms==3.1.92',
    'huaweicloudsdksts==3.1.92',
    'huaweicloudsdkswr==3.1.92',
    'huaweicloudsdktics==3.1.92',
    'huaweicloudsdktms==3.1.92',
    'huaweicloudsdkugo==3.1.92',
    'huaweicloudsdkvas==3.1.92',
    'huaweicloudsdkvcm==3.1.92',
    'huaweicloudsdkvod==3.1.92',
    'huaweicloudsdkvpc==3.1.92',
    'huaweicloudsdkvpcep==3.1.92',
    'huaweicloudsdkvpn==3.1.92',
    'huaweicloudsdkwaf==3.1.92',
    'huaweicloudsdkworkspace==3.1.92',
    'huaweicloudsdkworkspaceapp==3.1.92',
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
