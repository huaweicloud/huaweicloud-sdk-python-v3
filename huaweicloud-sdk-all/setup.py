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
VERSION = "3.1.80"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.80',
    'huaweicloudsdkaad==3.1.80',
    'huaweicloudsdkantiddos==3.1.80',
    'huaweicloudsdkaom==3.1.80',
    'huaweicloudsdkaos==3.1.80',
    'huaweicloudsdkapig==3.1.80',
    'huaweicloudsdkapm==3.1.80',
    'huaweicloudsdkas==3.1.80',
    'huaweicloudsdkasm==3.1.80',
    'huaweicloudsdkbcs==3.1.80',
    'huaweicloudsdkbms==3.1.80',
    'huaweicloudsdkbss==3.1.80',
    'huaweicloudsdkbssintl==3.1.80',
    'huaweicloudsdkcae==3.1.80',
    'huaweicloudsdkcampusgo==3.1.80',
    'huaweicloudsdkcbh==3.1.80',
    'huaweicloudsdkcbr==3.1.80',
    'huaweicloudsdkcbs==3.1.80',
    'huaweicloudsdkcc==3.1.80',
    'huaweicloudsdkcce==3.1.80',
    'huaweicloudsdkccm==3.1.80',
    'huaweicloudsdkcdm==3.1.80',
    'huaweicloudsdkcdn==3.1.80',
    'huaweicloudsdkces==3.1.80',
    'huaweicloudsdkcfw==3.1.80',
    'huaweicloudsdkcgs==3.1.80',
    'huaweicloudsdkclassroom==3.1.80',
    'huaweicloudsdkcloudide==3.1.80',
    'huaweicloudsdkcloudpond==3.1.80',
    'huaweicloudsdkcloudrtc==3.1.80',
    'huaweicloudsdkcloudtable==3.1.80',
    'huaweicloudsdkcloudtest==3.1.80',
    'huaweicloudsdkcodeartsartifact==3.1.80',
    'huaweicloudsdkcodeartsbuild==3.1.80',
    'huaweicloudsdkcodeartscheck==3.1.80',
    'huaweicloudsdkcodeartsdeploy==3.1.80',
    'huaweicloudsdkcodeartsinspector==3.1.80',
    'huaweicloudsdkcodeartspipeline==3.1.80',
    'huaweicloudsdkcodecraft==3.1.80',
    'huaweicloudsdkcodehub==3.1.80',
    'huaweicloudsdkconfig==3.1.80',
    'huaweicloudsdkcph==3.1.80',
    'huaweicloudsdkcpts==3.1.80',
    'huaweicloudsdkcse==3.1.80',
    'huaweicloudsdkcsms==3.1.80',
    'huaweicloudsdkcss==3.1.80',
    'huaweicloudsdkcts==3.1.80',
    'huaweicloudsdkdas==3.1.80',
    'huaweicloudsdkdataartsstudio==3.1.80',
    'huaweicloudsdkdbss==3.1.80',
    'huaweicloudsdkdc==3.1.80',
    'huaweicloudsdkdcs==3.1.80',
    'huaweicloudsdkddm==3.1.80',
    'huaweicloudsdkdds==3.1.80',
    'huaweicloudsdkdeh==3.1.80',
    'huaweicloudsdkdevsecurity==3.1.80',
    'huaweicloudsdkdevstar==3.1.80',
    'huaweicloudsdkdgc==3.1.80',
    'huaweicloudsdkdis==3.1.80',
    'huaweicloudsdkdlf==3.1.80',
    'huaweicloudsdkdli==3.1.80',
    'huaweicloudsdkdns==3.1.80',
    'huaweicloudsdkdris==3.1.80',
    'huaweicloudsdkdrs==3.1.80',
    'huaweicloudsdkdsc==3.1.80',
    'huaweicloudsdkdwr==3.1.80',
    'huaweicloudsdkdws==3.1.80',
    'huaweicloudsdkec==3.1.80',
    'huaweicloudsdkecs==3.1.80',
    'huaweicloudsdkedgesec==3.1.80',
    'huaweicloudsdkeg==3.1.80',
    'huaweicloudsdkeihealth==3.1.80',
    'huaweicloudsdkeip==3.1.80',
    'huaweicloudsdkelb==3.1.80',
    'huaweicloudsdkeps==3.1.80',
    'huaweicloudsdker==3.1.80',
    'huaweicloudsdkevs==3.1.80',
    'huaweicloudsdkfrs==3.1.80',
    'huaweicloudsdkfunctiongraph==3.1.80',
    'huaweicloudsdkga==3.1.80',
    'huaweicloudsdkgaussdb==3.1.80',
    'huaweicloudsdkgaussdbfornosql==3.1.80',
    'huaweicloudsdkgaussdbforopengauss==3.1.80',
    'huaweicloudsdkges==3.1.80',
    'huaweicloudsdkgsl==3.1.80',
    'huaweicloudsdkhilens==3.1.80',
    'huaweicloudsdkhss==3.1.80',
    'huaweicloudsdkiam==3.1.80',
    'huaweicloudsdkidentitycenter==3.1.80',
    'huaweicloudsdkidentitycenterstore==3.1.80',
    'huaweicloudsdkidme==3.1.80',
    'huaweicloudsdkidmeclassicapi==3.1.80',
    'huaweicloudsdkiec==3.1.80',
    'huaweicloudsdkief==3.1.80',
    'huaweicloudsdkimage==3.1.80',
    'huaweicloudsdkimagesearch==3.1.80',
    'huaweicloudsdkims==3.1.80',
    'huaweicloudsdkiotanalytics==3.1.80',
    'huaweicloudsdkiotda==3.1.80',
    'huaweicloudsdkiotedge==3.1.80',
    'huaweicloudsdkivs==3.1.80',
    'huaweicloudsdkkafka==3.1.80',
    'huaweicloudsdkkms==3.1.80',
    'huaweicloudsdkkoomessage==3.1.80',
    'huaweicloudsdkkps==3.1.80',
    'huaweicloudsdklakeformation==3.1.80',
    'huaweicloudsdklive==3.1.80',
    'huaweicloudsdklts==3.1.80',
    'huaweicloudsdkmapds==3.1.80',
    'huaweicloudsdkmas==3.1.80',
    'huaweicloudsdkmeeting==3.1.80',
    'huaweicloudsdkmetastudio==3.1.80',
    'huaweicloudsdkmoderation==3.1.80',
    'huaweicloudsdkmpc==3.1.80',
    'huaweicloudsdkmrs==3.1.80',
    'huaweicloudsdkmsgsms==3.1.80',
    'huaweicloudsdkmssi==3.1.80',
    'huaweicloudsdknat==3.1.80',
    'huaweicloudsdknlp==3.1.80',
    'huaweicloudsdkobs==3.1.80',
    'huaweicloudsdkocr==3.1.80',
    'huaweicloudsdkoctopus==3.1.80',
    'huaweicloudsdkoms==3.1.80',
    'huaweicloudsdkoptverse==3.1.80',
    'huaweicloudsdkorganizations==3.1.80',
    'huaweicloudsdkoroas==3.1.80',
    'huaweicloudsdkosm==3.1.80',
    'huaweicloudsdkpangulargemodels==3.1.80',
    'huaweicloudsdkprojectman==3.1.80',
    'huaweicloudsdkrabbitmq==3.1.80',
    'huaweicloudsdkram==3.1.80',
    'huaweicloudsdkrds==3.1.80',
    'huaweicloudsdkres==3.1.80',
    'huaweicloudsdkrgc==3.1.80',
    'huaweicloudsdkrms==3.1.80',
    'huaweicloudsdkrocketmq==3.1.80',
    'huaweicloudsdkroma==3.1.80',
    'huaweicloudsdksa==3.1.80',
    'huaweicloudsdkscm==3.1.80',
    'huaweicloudsdksdrs==3.1.80',
    'huaweicloudsdksecmaster==3.1.80',
    'huaweicloudsdkservicestage==3.1.80',
    'huaweicloudsdksfsturbo==3.1.80',
    'huaweicloudsdksis==3.1.80',
    'huaweicloudsdksmn==3.1.80',
    'huaweicloudsdksms==3.1.80',
    'huaweicloudsdkswr==3.1.80',
    'huaweicloudsdktics==3.1.80',
    'huaweicloudsdktms==3.1.80',
    'huaweicloudsdkugo==3.1.80',
    'huaweicloudsdkvas==3.1.80',
    'huaweicloudsdkvcm==3.1.80',
    'huaweicloudsdkvod==3.1.80',
    'huaweicloudsdkvpc==3.1.80',
    'huaweicloudsdkvpcep==3.1.80',
    'huaweicloudsdkvpn==3.1.80',
    'huaweicloudsdkwaf==3.1.80',
    'huaweicloudsdkworkspace==3.1.80',
    'huaweicloudsdkworkspaceapp==3.1.80',
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
