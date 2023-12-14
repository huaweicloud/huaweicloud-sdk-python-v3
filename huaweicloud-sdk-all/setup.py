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
VERSION = "3.1.72"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.72',
    'huaweicloudsdkaad==3.1.72',
    'huaweicloudsdkantiddos==3.1.72',
    'huaweicloudsdkaom==3.1.72',
    'huaweicloudsdkaos==3.1.72',
    'huaweicloudsdkapig==3.1.72',
    'huaweicloudsdkapm==3.1.72',
    'huaweicloudsdkas==3.1.72',
    'huaweicloudsdkasm==3.1.72',
    'huaweicloudsdkbcs==3.1.72',
    'huaweicloudsdkbms==3.1.72',
    'huaweicloudsdkbss==3.1.72',
    'huaweicloudsdkbssintl==3.1.72',
    'huaweicloudsdkcae==3.1.72',
    'huaweicloudsdkcampusgo==3.1.72',
    'huaweicloudsdkcbh==3.1.72',
    'huaweicloudsdkcbr==3.1.72',
    'huaweicloudsdkcbs==3.1.72',
    'huaweicloudsdkcc==3.1.72',
    'huaweicloudsdkcce==3.1.72',
    'huaweicloudsdkccm==3.1.72',
    'huaweicloudsdkcdm==3.1.72',
    'huaweicloudsdkcdn==3.1.72',
    'huaweicloudsdkces==3.1.72',
    'huaweicloudsdkcfw==3.1.72',
    'huaweicloudsdkcgs==3.1.72',
    'huaweicloudsdkclassroom==3.1.72',
    'huaweicloudsdkcloudide==3.1.72',
    'huaweicloudsdkcloudpond==3.1.72',
    'huaweicloudsdkcloudrtc==3.1.72',
    'huaweicloudsdkcloudtable==3.1.72',
    'huaweicloudsdkcloudtest==3.1.72',
    'huaweicloudsdkcodeartsartifact==3.1.72',
    'huaweicloudsdkcodeartsbuild==3.1.72',
    'huaweicloudsdkcodeartscheck==3.1.72',
    'huaweicloudsdkcodeartsdeploy==3.1.72',
    'huaweicloudsdkcodeartsinspector==3.1.72',
    'huaweicloudsdkcodeartspipeline==3.1.72',
    'huaweicloudsdkcodecraft==3.1.72',
    'huaweicloudsdkcodehub==3.1.72',
    'huaweicloudsdkconfig==3.1.72',
    'huaweicloudsdkcph==3.1.72',
    'huaweicloudsdkcpts==3.1.72',
    'huaweicloudsdkcse==3.1.72',
    'huaweicloudsdkcsms==3.1.72',
    'huaweicloudsdkcss==3.1.72',
    'huaweicloudsdkcts==3.1.72',
    'huaweicloudsdkdas==3.1.72',
    'huaweicloudsdkdataartsstudio==3.1.72',
    'huaweicloudsdkdbss==3.1.72',
    'huaweicloudsdkdc==3.1.72',
    'huaweicloudsdkdcs==3.1.72',
    'huaweicloudsdkddm==3.1.72',
    'huaweicloudsdkdds==3.1.72',
    'huaweicloudsdkdeh==3.1.72',
    'huaweicloudsdkdevsecurity==3.1.72',
    'huaweicloudsdkdevstar==3.1.72',
    'huaweicloudsdkdgc==3.1.72',
    'huaweicloudsdkdis==3.1.72',
    'huaweicloudsdkdlf==3.1.72',
    'huaweicloudsdkdli==3.1.72',
    'huaweicloudsdkdns==3.1.72',
    'huaweicloudsdkdris==3.1.72',
    'huaweicloudsdkdrs==3.1.72',
    'huaweicloudsdkdsc==3.1.72',
    'huaweicloudsdkdwr==3.1.72',
    'huaweicloudsdkdws==3.1.72',
    'huaweicloudsdkec==3.1.72',
    'huaweicloudsdkecs==3.1.72',
    'huaweicloudsdkedgesec==3.1.72',
    'huaweicloudsdkeg==3.1.72',
    'huaweicloudsdkeihealth==3.1.72',
    'huaweicloudsdkeip==3.1.72',
    'huaweicloudsdkelb==3.1.72',
    'huaweicloudsdkeps==3.1.72',
    'huaweicloudsdker==3.1.72',
    'huaweicloudsdkevs==3.1.72',
    'huaweicloudsdkfrs==3.1.72',
    'huaweicloudsdkfunctiongraph==3.1.72',
    'huaweicloudsdkga==3.1.72',
    'huaweicloudsdkgaussdb==3.1.72',
    'huaweicloudsdkgaussdbfornosql==3.1.72',
    'huaweicloudsdkgaussdbforopengauss==3.1.72',
    'huaweicloudsdkges==3.1.72',
    'huaweicloudsdkgsl==3.1.72',
    'huaweicloudsdkhilens==3.1.72',
    'huaweicloudsdkhss==3.1.72',
    'huaweicloudsdkiam==3.1.72',
    'huaweicloudsdkidentitycenter==3.1.72',
    'huaweicloudsdkidentitycenterstore==3.1.72',
    'huaweicloudsdkidme==3.1.72',
    'huaweicloudsdkiec==3.1.72',
    'huaweicloudsdkief==3.1.72',
    'huaweicloudsdkimage==3.1.72',
    'huaweicloudsdkimagesearch==3.1.72',
    'huaweicloudsdkims==3.1.72',
    'huaweicloudsdkiotanalytics==3.1.72',
    'huaweicloudsdkiotda==3.1.72',
    'huaweicloudsdkiotedge==3.1.72',
    'huaweicloudsdkivs==3.1.72',
    'huaweicloudsdkkafka==3.1.72',
    'huaweicloudsdkkms==3.1.72',
    'huaweicloudsdkkoomessage==3.1.72',
    'huaweicloudsdkkps==3.1.72',
    'huaweicloudsdklakeformation==3.1.72',
    'huaweicloudsdklive==3.1.72',
    'huaweicloudsdklts==3.1.72',
    'huaweicloudsdkmapds==3.1.72',
    'huaweicloudsdkmas==3.1.72',
    'huaweicloudsdkmeeting==3.1.72',
    'huaweicloudsdkmetastudio==3.1.72',
    'huaweicloudsdkmoderation==3.1.72',
    'huaweicloudsdkmpc==3.1.72',
    'huaweicloudsdkmrs==3.1.72',
    'huaweicloudsdkmsgsms==3.1.72',
    'huaweicloudsdkmssi==3.1.72',
    'huaweicloudsdknat==3.1.72',
    'huaweicloudsdknlp==3.1.72',
    'huaweicloudsdkocr==3.1.72',
    'huaweicloudsdkoctopus==3.1.72',
    'huaweicloudsdkoms==3.1.72',
    'huaweicloudsdkoptverse==3.1.72',
    'huaweicloudsdkorganizations==3.1.72',
    'huaweicloudsdkoroas==3.1.72',
    'huaweicloudsdkosm==3.1.72',
    'huaweicloudsdkpangulargemodels==3.1.72',
    'huaweicloudsdkprojectman==3.1.72',
    'huaweicloudsdkrabbitmq==3.1.72',
    'huaweicloudsdkram==3.1.72',
    'huaweicloudsdkrds==3.1.72',
    'huaweicloudsdkres==3.1.72',
    'huaweicloudsdkrgc==3.1.72',
    'huaweicloudsdkrms==3.1.72',
    'huaweicloudsdkrocketmq==3.1.72',
    'huaweicloudsdkroma==3.1.72',
    'huaweicloudsdksa==3.1.72',
    'huaweicloudsdkscm==3.1.72',
    'huaweicloudsdksdrs==3.1.72',
    'huaweicloudsdksecmaster==3.1.72',
    'huaweicloudsdkservicestage==3.1.72',
    'huaweicloudsdksfsturbo==3.1.72',
    'huaweicloudsdksis==3.1.72',
    'huaweicloudsdksmn==3.1.72',
    'huaweicloudsdksms==3.1.72',
    'huaweicloudsdkswr==3.1.72',
    'huaweicloudsdktics==3.1.72',
    'huaweicloudsdktms==3.1.72',
    'huaweicloudsdkugo==3.1.72',
    'huaweicloudsdkvas==3.1.72',
    'huaweicloudsdkvcm==3.1.72',
    'huaweicloudsdkvod==3.1.72',
    'huaweicloudsdkvpc==3.1.72',
    'huaweicloudsdkvpcep==3.1.72',
    'huaweicloudsdkvpn==3.1.72',
    'huaweicloudsdkwaf==3.1.72',
    'huaweicloudsdkworkspace==3.1.72',
    'huaweicloudsdkworkspaceapp==3.1.72',
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
