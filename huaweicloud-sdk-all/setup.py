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
VERSION = "3.1.76"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.76',
    'huaweicloudsdkaad==3.1.76',
    'huaweicloudsdkantiddos==3.1.76',
    'huaweicloudsdkaom==3.1.76',
    'huaweicloudsdkaos==3.1.76',
    'huaweicloudsdkapig==3.1.76',
    'huaweicloudsdkapm==3.1.76',
    'huaweicloudsdkas==3.1.76',
    'huaweicloudsdkasm==3.1.76',
    'huaweicloudsdkbcs==3.1.76',
    'huaweicloudsdkbms==3.1.76',
    'huaweicloudsdkbss==3.1.76',
    'huaweicloudsdkbssintl==3.1.76',
    'huaweicloudsdkcae==3.1.76',
    'huaweicloudsdkcampusgo==3.1.76',
    'huaweicloudsdkcbh==3.1.76',
    'huaweicloudsdkcbr==3.1.76',
    'huaweicloudsdkcbs==3.1.76',
    'huaweicloudsdkcc==3.1.76',
    'huaweicloudsdkcce==3.1.76',
    'huaweicloudsdkccm==3.1.76',
    'huaweicloudsdkcdm==3.1.76',
    'huaweicloudsdkcdn==3.1.76',
    'huaweicloudsdkces==3.1.76',
    'huaweicloudsdkcfw==3.1.76',
    'huaweicloudsdkcgs==3.1.76',
    'huaweicloudsdkclassroom==3.1.76',
    'huaweicloudsdkcloudide==3.1.76',
    'huaweicloudsdkcloudpond==3.1.76',
    'huaweicloudsdkcloudrtc==3.1.76',
    'huaweicloudsdkcloudtable==3.1.76',
    'huaweicloudsdkcloudtest==3.1.76',
    'huaweicloudsdkcodeartsartifact==3.1.76',
    'huaweicloudsdkcodeartsbuild==3.1.76',
    'huaweicloudsdkcodeartscheck==3.1.76',
    'huaweicloudsdkcodeartsdeploy==3.1.76',
    'huaweicloudsdkcodeartsinspector==3.1.76',
    'huaweicloudsdkcodeartspipeline==3.1.76',
    'huaweicloudsdkcodecraft==3.1.76',
    'huaweicloudsdkcodehub==3.1.76',
    'huaweicloudsdkconfig==3.1.76',
    'huaweicloudsdkcph==3.1.76',
    'huaweicloudsdkcpts==3.1.76',
    'huaweicloudsdkcse==3.1.76',
    'huaweicloudsdkcsms==3.1.76',
    'huaweicloudsdkcss==3.1.76',
    'huaweicloudsdkcts==3.1.76',
    'huaweicloudsdkdas==3.1.76',
    'huaweicloudsdkdataartsstudio==3.1.76',
    'huaweicloudsdkdbss==3.1.76',
    'huaweicloudsdkdc==3.1.76',
    'huaweicloudsdkdcs==3.1.76',
    'huaweicloudsdkddm==3.1.76',
    'huaweicloudsdkdds==3.1.76',
    'huaweicloudsdkdeh==3.1.76',
    'huaweicloudsdkdevsecurity==3.1.76',
    'huaweicloudsdkdevstar==3.1.76',
    'huaweicloudsdkdgc==3.1.76',
    'huaweicloudsdkdis==3.1.76',
    'huaweicloudsdkdlf==3.1.76',
    'huaweicloudsdkdli==3.1.76',
    'huaweicloudsdkdns==3.1.76',
    'huaweicloudsdkdris==3.1.76',
    'huaweicloudsdkdrs==3.1.76',
    'huaweicloudsdkdsc==3.1.76',
    'huaweicloudsdkdwr==3.1.76',
    'huaweicloudsdkdws==3.1.76',
    'huaweicloudsdkec==3.1.76',
    'huaweicloudsdkecs==3.1.76',
    'huaweicloudsdkedgesec==3.1.76',
    'huaweicloudsdkeg==3.1.76',
    'huaweicloudsdkeihealth==3.1.76',
    'huaweicloudsdkeip==3.1.76',
    'huaweicloudsdkelb==3.1.76',
    'huaweicloudsdkeps==3.1.76',
    'huaweicloudsdker==3.1.76',
    'huaweicloudsdkevs==3.1.76',
    'huaweicloudsdkfrs==3.1.76',
    'huaweicloudsdkfunctiongraph==3.1.76',
    'huaweicloudsdkga==3.1.76',
    'huaweicloudsdkgaussdb==3.1.76',
    'huaweicloudsdkgaussdbfornosql==3.1.76',
    'huaweicloudsdkgaussdbforopengauss==3.1.76',
    'huaweicloudsdkges==3.1.76',
    'huaweicloudsdkgsl==3.1.76',
    'huaweicloudsdkhilens==3.1.76',
    'huaweicloudsdkhss==3.1.76',
    'huaweicloudsdkiam==3.1.76',
    'huaweicloudsdkidentitycenter==3.1.76',
    'huaweicloudsdkidentitycenterstore==3.1.76',
    'huaweicloudsdkidme==3.1.76',
    'huaweicloudsdkidmeclassicapi==3.1.76',
    'huaweicloudsdkiec==3.1.76',
    'huaweicloudsdkief==3.1.76',
    'huaweicloudsdkimage==3.1.76',
    'huaweicloudsdkimagesearch==3.1.76',
    'huaweicloudsdkims==3.1.76',
    'huaweicloudsdkiotanalytics==3.1.76',
    'huaweicloudsdkiotda==3.1.76',
    'huaweicloudsdkiotedge==3.1.76',
    'huaweicloudsdkivs==3.1.76',
    'huaweicloudsdkkafka==3.1.76',
    'huaweicloudsdkkms==3.1.76',
    'huaweicloudsdkkoomessage==3.1.76',
    'huaweicloudsdkkps==3.1.76',
    'huaweicloudsdklakeformation==3.1.76',
    'huaweicloudsdklive==3.1.76',
    'huaweicloudsdklts==3.1.76',
    'huaweicloudsdkmapds==3.1.76',
    'huaweicloudsdkmas==3.1.76',
    'huaweicloudsdkmeeting==3.1.76',
    'huaweicloudsdkmetastudio==3.1.76',
    'huaweicloudsdkmoderation==3.1.76',
    'huaweicloudsdkmpc==3.1.76',
    'huaweicloudsdkmrs==3.1.76',
    'huaweicloudsdkmsgsms==3.1.76',
    'huaweicloudsdkmssi==3.1.76',
    'huaweicloudsdknat==3.1.76',
    'huaweicloudsdknlp==3.1.76',
    'huaweicloudsdkobs==3.1.76',
    'huaweicloudsdkocr==3.1.76',
    'huaweicloudsdkoctopus==3.1.76',
    'huaweicloudsdkoms==3.1.76',
    'huaweicloudsdkoptverse==3.1.76',
    'huaweicloudsdkorganizations==3.1.76',
    'huaweicloudsdkoroas==3.1.76',
    'huaweicloudsdkosm==3.1.76',
    'huaweicloudsdkpangulargemodels==3.1.76',
    'huaweicloudsdkprojectman==3.1.76',
    'huaweicloudsdkrabbitmq==3.1.76',
    'huaweicloudsdkram==3.1.76',
    'huaweicloudsdkrds==3.1.76',
    'huaweicloudsdkres==3.1.76',
    'huaweicloudsdkrgc==3.1.76',
    'huaweicloudsdkrms==3.1.76',
    'huaweicloudsdkrocketmq==3.1.76',
    'huaweicloudsdkroma==3.1.76',
    'huaweicloudsdksa==3.1.76',
    'huaweicloudsdkscm==3.1.76',
    'huaweicloudsdksdrs==3.1.76',
    'huaweicloudsdksecmaster==3.1.76',
    'huaweicloudsdkservicestage==3.1.76',
    'huaweicloudsdksfsturbo==3.1.76',
    'huaweicloudsdksis==3.1.76',
    'huaweicloudsdksmn==3.1.76',
    'huaweicloudsdksms==3.1.76',
    'huaweicloudsdkswr==3.1.76',
    'huaweicloudsdktics==3.1.76',
    'huaweicloudsdktms==3.1.76',
    'huaweicloudsdkugo==3.1.76',
    'huaweicloudsdkvas==3.1.76',
    'huaweicloudsdkvcm==3.1.76',
    'huaweicloudsdkvod==3.1.76',
    'huaweicloudsdkvpc==3.1.76',
    'huaweicloudsdkvpcep==3.1.76',
    'huaweicloudsdkvpn==3.1.76',
    'huaweicloudsdkwaf==3.1.76',
    'huaweicloudsdkworkspace==3.1.76',
    'huaweicloudsdkworkspaceapp==3.1.76',
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
