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
VERSION = "3.1.74"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.74',
    'huaweicloudsdkaad==3.1.74',
    'huaweicloudsdkantiddos==3.1.74',
    'huaweicloudsdkaom==3.1.74',
    'huaweicloudsdkaos==3.1.74',
    'huaweicloudsdkapig==3.1.74',
    'huaweicloudsdkapm==3.1.74',
    'huaweicloudsdkas==3.1.74',
    'huaweicloudsdkasm==3.1.74',
    'huaweicloudsdkbcs==3.1.74',
    'huaweicloudsdkbms==3.1.74',
    'huaweicloudsdkbss==3.1.74',
    'huaweicloudsdkbssintl==3.1.74',
    'huaweicloudsdkcae==3.1.74',
    'huaweicloudsdkcampusgo==3.1.74',
    'huaweicloudsdkcbh==3.1.74',
    'huaweicloudsdkcbr==3.1.74',
    'huaweicloudsdkcbs==3.1.74',
    'huaweicloudsdkcc==3.1.74',
    'huaweicloudsdkcce==3.1.74',
    'huaweicloudsdkccm==3.1.74',
    'huaweicloudsdkcdm==3.1.74',
    'huaweicloudsdkcdn==3.1.74',
    'huaweicloudsdkces==3.1.74',
    'huaweicloudsdkcfw==3.1.74',
    'huaweicloudsdkcgs==3.1.74',
    'huaweicloudsdkclassroom==3.1.74',
    'huaweicloudsdkcloudide==3.1.74',
    'huaweicloudsdkcloudpond==3.1.74',
    'huaweicloudsdkcloudrtc==3.1.74',
    'huaweicloudsdkcloudtable==3.1.74',
    'huaweicloudsdkcloudtest==3.1.74',
    'huaweicloudsdkcodeartsartifact==3.1.74',
    'huaweicloudsdkcodeartsbuild==3.1.74',
    'huaweicloudsdkcodeartscheck==3.1.74',
    'huaweicloudsdkcodeartsdeploy==3.1.74',
    'huaweicloudsdkcodeartsinspector==3.1.74',
    'huaweicloudsdkcodeartspipeline==3.1.74',
    'huaweicloudsdkcodecraft==3.1.74',
    'huaweicloudsdkcodehub==3.1.74',
    'huaweicloudsdkconfig==3.1.74',
    'huaweicloudsdkcph==3.1.74',
    'huaweicloudsdkcpts==3.1.74',
    'huaweicloudsdkcse==3.1.74',
    'huaweicloudsdkcsms==3.1.74',
    'huaweicloudsdkcss==3.1.74',
    'huaweicloudsdkcts==3.1.74',
    'huaweicloudsdkdas==3.1.74',
    'huaweicloudsdkdataartsstudio==3.1.74',
    'huaweicloudsdkdbss==3.1.74',
    'huaweicloudsdkdc==3.1.74',
    'huaweicloudsdkdcs==3.1.74',
    'huaweicloudsdkddm==3.1.74',
    'huaweicloudsdkdds==3.1.74',
    'huaweicloudsdkdeh==3.1.74',
    'huaweicloudsdkdevsecurity==3.1.74',
    'huaweicloudsdkdevstar==3.1.74',
    'huaweicloudsdkdgc==3.1.74',
    'huaweicloudsdkdis==3.1.74',
    'huaweicloudsdkdlf==3.1.74',
    'huaweicloudsdkdli==3.1.74',
    'huaweicloudsdkdns==3.1.74',
    'huaweicloudsdkdris==3.1.74',
    'huaweicloudsdkdrs==3.1.74',
    'huaweicloudsdkdsc==3.1.74',
    'huaweicloudsdkdwr==3.1.74',
    'huaweicloudsdkdws==3.1.74',
    'huaweicloudsdkec==3.1.74',
    'huaweicloudsdkecs==3.1.74',
    'huaweicloudsdkedgesec==3.1.74',
    'huaweicloudsdkeg==3.1.74',
    'huaweicloudsdkeihealth==3.1.74',
    'huaweicloudsdkeip==3.1.74',
    'huaweicloudsdkelb==3.1.74',
    'huaweicloudsdkeps==3.1.74',
    'huaweicloudsdker==3.1.74',
    'huaweicloudsdkevs==3.1.74',
    'huaweicloudsdkfrs==3.1.74',
    'huaweicloudsdkfunctiongraph==3.1.74',
    'huaweicloudsdkga==3.1.74',
    'huaweicloudsdkgaussdb==3.1.74',
    'huaweicloudsdkgaussdbfornosql==3.1.74',
    'huaweicloudsdkgaussdbforopengauss==3.1.74',
    'huaweicloudsdkges==3.1.74',
    'huaweicloudsdkgsl==3.1.74',
    'huaweicloudsdkhilens==3.1.74',
    'huaweicloudsdkhss==3.1.74',
    'huaweicloudsdkiam==3.1.74',
    'huaweicloudsdkidentitycenter==3.1.74',
    'huaweicloudsdkidentitycenterstore==3.1.74',
    'huaweicloudsdkidme==3.1.74',
    'huaweicloudsdkidmeclassicapi==3.1.74',
    'huaweicloudsdkiec==3.1.74',
    'huaweicloudsdkief==3.1.74',
    'huaweicloudsdkimage==3.1.74',
    'huaweicloudsdkimagesearch==3.1.74',
    'huaweicloudsdkims==3.1.74',
    'huaweicloudsdkiotanalytics==3.1.74',
    'huaweicloudsdkiotda==3.1.74',
    'huaweicloudsdkiotedge==3.1.74',
    'huaweicloudsdkivs==3.1.74',
    'huaweicloudsdkkafka==3.1.74',
    'huaweicloudsdkkms==3.1.74',
    'huaweicloudsdkkoomessage==3.1.74',
    'huaweicloudsdkkps==3.1.74',
    'huaweicloudsdklakeformation==3.1.74',
    'huaweicloudsdklive==3.1.74',
    'huaweicloudsdklts==3.1.74',
    'huaweicloudsdkmapds==3.1.74',
    'huaweicloudsdkmas==3.1.74',
    'huaweicloudsdkmeeting==3.1.74',
    'huaweicloudsdkmetastudio==3.1.74',
    'huaweicloudsdkmoderation==3.1.74',
    'huaweicloudsdkmpc==3.1.74',
    'huaweicloudsdkmrs==3.1.74',
    'huaweicloudsdkmsgsms==3.1.74',
    'huaweicloudsdkmssi==3.1.74',
    'huaweicloudsdknat==3.1.74',
    'huaweicloudsdknlp==3.1.74',
    'huaweicloudsdkocr==3.1.74',
    'huaweicloudsdkoctopus==3.1.74',
    'huaweicloudsdkoms==3.1.74',
    'huaweicloudsdkoptverse==3.1.74',
    'huaweicloudsdkorganizations==3.1.74',
    'huaweicloudsdkoroas==3.1.74',
    'huaweicloudsdkosm==3.1.74',
    'huaweicloudsdkpangulargemodels==3.1.74',
    'huaweicloudsdkprojectman==3.1.74',
    'huaweicloudsdkrabbitmq==3.1.74',
    'huaweicloudsdkram==3.1.74',
    'huaweicloudsdkrds==3.1.74',
    'huaweicloudsdkres==3.1.74',
    'huaweicloudsdkrgc==3.1.74',
    'huaweicloudsdkrms==3.1.74',
    'huaweicloudsdkrocketmq==3.1.74',
    'huaweicloudsdkroma==3.1.74',
    'huaweicloudsdksa==3.1.74',
    'huaweicloudsdkscm==3.1.74',
    'huaweicloudsdksdrs==3.1.74',
    'huaweicloudsdksecmaster==3.1.74',
    'huaweicloudsdkservicestage==3.1.74',
    'huaweicloudsdksfsturbo==3.1.74',
    'huaweicloudsdksis==3.1.74',
    'huaweicloudsdksmn==3.1.74',
    'huaweicloudsdksms==3.1.74',
    'huaweicloudsdkswr==3.1.74',
    'huaweicloudsdktics==3.1.74',
    'huaweicloudsdktms==3.1.74',
    'huaweicloudsdkugo==3.1.74',
    'huaweicloudsdkvas==3.1.74',
    'huaweicloudsdkvcm==3.1.74',
    'huaweicloudsdkvod==3.1.74',
    'huaweicloudsdkvpc==3.1.74',
    'huaweicloudsdkvpcep==3.1.74',
    'huaweicloudsdkvpn==3.1.74',
    'huaweicloudsdkwaf==3.1.74',
    'huaweicloudsdkworkspace==3.1.74',
    'huaweicloudsdkworkspaceapp==3.1.74',
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
