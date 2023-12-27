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
VERSION = "3.1.75"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.75',
    'huaweicloudsdkaad==3.1.75',
    'huaweicloudsdkantiddos==3.1.75',
    'huaweicloudsdkaom==3.1.75',
    'huaweicloudsdkaos==3.1.75',
    'huaweicloudsdkapig==3.1.75',
    'huaweicloudsdkapm==3.1.75',
    'huaweicloudsdkas==3.1.75',
    'huaweicloudsdkasm==3.1.75',
    'huaweicloudsdkbcs==3.1.75',
    'huaweicloudsdkbms==3.1.75',
    'huaweicloudsdkbss==3.1.75',
    'huaweicloudsdkbssintl==3.1.75',
    'huaweicloudsdkcae==3.1.75',
    'huaweicloudsdkcampusgo==3.1.75',
    'huaweicloudsdkcbh==3.1.75',
    'huaweicloudsdkcbr==3.1.75',
    'huaweicloudsdkcbs==3.1.75',
    'huaweicloudsdkcc==3.1.75',
    'huaweicloudsdkcce==3.1.75',
    'huaweicloudsdkccm==3.1.75',
    'huaweicloudsdkcdm==3.1.75',
    'huaweicloudsdkcdn==3.1.75',
    'huaweicloudsdkces==3.1.75',
    'huaweicloudsdkcfw==3.1.75',
    'huaweicloudsdkcgs==3.1.75',
    'huaweicloudsdkclassroom==3.1.75',
    'huaweicloudsdkcloudide==3.1.75',
    'huaweicloudsdkcloudpond==3.1.75',
    'huaweicloudsdkcloudrtc==3.1.75',
    'huaweicloudsdkcloudtable==3.1.75',
    'huaweicloudsdkcloudtest==3.1.75',
    'huaweicloudsdkcodeartsartifact==3.1.75',
    'huaweicloudsdkcodeartsbuild==3.1.75',
    'huaweicloudsdkcodeartscheck==3.1.75',
    'huaweicloudsdkcodeartsdeploy==3.1.75',
    'huaweicloudsdkcodeartsinspector==3.1.75',
    'huaweicloudsdkcodeartspipeline==3.1.75',
    'huaweicloudsdkcodecraft==3.1.75',
    'huaweicloudsdkcodehub==3.1.75',
    'huaweicloudsdkconfig==3.1.75',
    'huaweicloudsdkcph==3.1.75',
    'huaweicloudsdkcpts==3.1.75',
    'huaweicloudsdkcse==3.1.75',
    'huaweicloudsdkcsms==3.1.75',
    'huaweicloudsdkcss==3.1.75',
    'huaweicloudsdkcts==3.1.75',
    'huaweicloudsdkdas==3.1.75',
    'huaweicloudsdkdataartsstudio==3.1.75',
    'huaweicloudsdkdbss==3.1.75',
    'huaweicloudsdkdc==3.1.75',
    'huaweicloudsdkdcs==3.1.75',
    'huaweicloudsdkddm==3.1.75',
    'huaweicloudsdkdds==3.1.75',
    'huaweicloudsdkdeh==3.1.75',
    'huaweicloudsdkdevsecurity==3.1.75',
    'huaweicloudsdkdevstar==3.1.75',
    'huaweicloudsdkdgc==3.1.75',
    'huaweicloudsdkdis==3.1.75',
    'huaweicloudsdkdlf==3.1.75',
    'huaweicloudsdkdli==3.1.75',
    'huaweicloudsdkdns==3.1.75',
    'huaweicloudsdkdris==3.1.75',
    'huaweicloudsdkdrs==3.1.75',
    'huaweicloudsdkdsc==3.1.75',
    'huaweicloudsdkdwr==3.1.75',
    'huaweicloudsdkdws==3.1.75',
    'huaweicloudsdkec==3.1.75',
    'huaweicloudsdkecs==3.1.75',
    'huaweicloudsdkedgesec==3.1.75',
    'huaweicloudsdkeg==3.1.75',
    'huaweicloudsdkeihealth==3.1.75',
    'huaweicloudsdkeip==3.1.75',
    'huaweicloudsdkelb==3.1.75',
    'huaweicloudsdkeps==3.1.75',
    'huaweicloudsdker==3.1.75',
    'huaweicloudsdkevs==3.1.75',
    'huaweicloudsdkfrs==3.1.75',
    'huaweicloudsdkfunctiongraph==3.1.75',
    'huaweicloudsdkga==3.1.75',
    'huaweicloudsdkgaussdb==3.1.75',
    'huaweicloudsdkgaussdbfornosql==3.1.75',
    'huaweicloudsdkgaussdbforopengauss==3.1.75',
    'huaweicloudsdkges==3.1.75',
    'huaweicloudsdkgsl==3.1.75',
    'huaweicloudsdkhilens==3.1.75',
    'huaweicloudsdkhss==3.1.75',
    'huaweicloudsdkiam==3.1.75',
    'huaweicloudsdkidentitycenter==3.1.75',
    'huaweicloudsdkidentitycenterstore==3.1.75',
    'huaweicloudsdkidme==3.1.75',
    'huaweicloudsdkidmeclassicapi==3.1.75',
    'huaweicloudsdkiec==3.1.75',
    'huaweicloudsdkief==3.1.75',
    'huaweicloudsdkimage==3.1.75',
    'huaweicloudsdkimagesearch==3.1.75',
    'huaweicloudsdkims==3.1.75',
    'huaweicloudsdkiotanalytics==3.1.75',
    'huaweicloudsdkiotda==3.1.75',
    'huaweicloudsdkiotedge==3.1.75',
    'huaweicloudsdkivs==3.1.75',
    'huaweicloudsdkkafka==3.1.75',
    'huaweicloudsdkkms==3.1.75',
    'huaweicloudsdkkoomessage==3.1.75',
    'huaweicloudsdkkps==3.1.75',
    'huaweicloudsdklakeformation==3.1.75',
    'huaweicloudsdklive==3.1.75',
    'huaweicloudsdklts==3.1.75',
    'huaweicloudsdkmapds==3.1.75',
    'huaweicloudsdkmas==3.1.75',
    'huaweicloudsdkmeeting==3.1.75',
    'huaweicloudsdkmetastudio==3.1.75',
    'huaweicloudsdkmoderation==3.1.75',
    'huaweicloudsdkmpc==3.1.75',
    'huaweicloudsdkmrs==3.1.75',
    'huaweicloudsdkmsgsms==3.1.75',
    'huaweicloudsdkmssi==3.1.75',
    'huaweicloudsdknat==3.1.75',
    'huaweicloudsdknlp==3.1.75',
    'huaweicloudsdkobs==3.1.75',
    'huaweicloudsdkocr==3.1.75',
    'huaweicloudsdkoctopus==3.1.75',
    'huaweicloudsdkoms==3.1.75',
    'huaweicloudsdkoptverse==3.1.75',
    'huaweicloudsdkorganizations==3.1.75',
    'huaweicloudsdkoroas==3.1.75',
    'huaweicloudsdkosm==3.1.75',
    'huaweicloudsdkpangulargemodels==3.1.75',
    'huaweicloudsdkprojectman==3.1.75',
    'huaweicloudsdkrabbitmq==3.1.75',
    'huaweicloudsdkram==3.1.75',
    'huaweicloudsdkrds==3.1.75',
    'huaweicloudsdkres==3.1.75',
    'huaweicloudsdkrgc==3.1.75',
    'huaweicloudsdkrms==3.1.75',
    'huaweicloudsdkrocketmq==3.1.75',
    'huaweicloudsdkroma==3.1.75',
    'huaweicloudsdksa==3.1.75',
    'huaweicloudsdkscm==3.1.75',
    'huaweicloudsdksdrs==3.1.75',
    'huaweicloudsdksecmaster==3.1.75',
    'huaweicloudsdkservicestage==3.1.75',
    'huaweicloudsdksfsturbo==3.1.75',
    'huaweicloudsdksis==3.1.75',
    'huaweicloudsdksmn==3.1.75',
    'huaweicloudsdksms==3.1.75',
    'huaweicloudsdkswr==3.1.75',
    'huaweicloudsdktics==3.1.75',
    'huaweicloudsdktms==3.1.75',
    'huaweicloudsdkugo==3.1.75',
    'huaweicloudsdkvas==3.1.75',
    'huaweicloudsdkvcm==3.1.75',
    'huaweicloudsdkvod==3.1.75',
    'huaweicloudsdkvpc==3.1.75',
    'huaweicloudsdkvpcep==3.1.75',
    'huaweicloudsdkvpn==3.1.75',
    'huaweicloudsdkwaf==3.1.75',
    'huaweicloudsdkworkspace==3.1.75',
    'huaweicloudsdkworkspaceapp==3.1.75',
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
