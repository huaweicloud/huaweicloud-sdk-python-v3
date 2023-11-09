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
VERSION = "3.1.65"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.65',
    'huaweicloudsdkantiddos==3.1.65',
    'huaweicloudsdkaom==3.1.65',
    'huaweicloudsdkaos==3.1.65',
    'huaweicloudsdkapig==3.1.65',
    'huaweicloudsdkapm==3.1.65',
    'huaweicloudsdkas==3.1.65',
    'huaweicloudsdkasm==3.1.65',
    'huaweicloudsdkbcs==3.1.65',
    'huaweicloudsdkbms==3.1.65',
    'huaweicloudsdkbss==3.1.65',
    'huaweicloudsdkbssintl==3.1.65',
    'huaweicloudsdkcae==3.1.65',
    'huaweicloudsdkcampusgo==3.1.65',
    'huaweicloudsdkcbh==3.1.65',
    'huaweicloudsdkcbr==3.1.65',
    'huaweicloudsdkcbs==3.1.65',
    'huaweicloudsdkcc==3.1.65',
    'huaweicloudsdkcce==3.1.65',
    'huaweicloudsdkccm==3.1.65',
    'huaweicloudsdkcdm==3.1.65',
    'huaweicloudsdkcdn==3.1.65',
    'huaweicloudsdkces==3.1.65',
    'huaweicloudsdkcfw==3.1.65',
    'huaweicloudsdkcgs==3.1.65',
    'huaweicloudsdkclassroom==3.1.65',
    'huaweicloudsdkcloudide==3.1.65',
    'huaweicloudsdkcloudpond==3.1.65',
    'huaweicloudsdkcloudrtc==3.1.65',
    'huaweicloudsdkcloudtable==3.1.65',
    'huaweicloudsdkcloudtest==3.1.65',
    'huaweicloudsdkcodeartsartifact==3.1.65',
    'huaweicloudsdkcodeartsbuild==3.1.65',
    'huaweicloudsdkcodeartscheck==3.1.65',
    'huaweicloudsdkcodeartsdeploy==3.1.65',
    'huaweicloudsdkcodeartsinspector==3.1.65',
    'huaweicloudsdkcodeartspipeline==3.1.65',
    'huaweicloudsdkcodecraft==3.1.65',
    'huaweicloudsdkcodehub==3.1.65',
    'huaweicloudsdkconfig==3.1.65',
    'huaweicloudsdkcph==3.1.65',
    'huaweicloudsdkcpts==3.1.65',
    'huaweicloudsdkcse==3.1.65',
    'huaweicloudsdkcsms==3.1.65',
    'huaweicloudsdkcss==3.1.65',
    'huaweicloudsdkcts==3.1.65',
    'huaweicloudsdkdas==3.1.65',
    'huaweicloudsdkdataartsstudio==3.1.65',
    'huaweicloudsdkdbss==3.1.65',
    'huaweicloudsdkdc==3.1.65',
    'huaweicloudsdkdcs==3.1.65',
    'huaweicloudsdkddm==3.1.65',
    'huaweicloudsdkdds==3.1.65',
    'huaweicloudsdkdeh==3.1.65',
    'huaweicloudsdkdevsecurity==3.1.65',
    'huaweicloudsdkdevstar==3.1.65',
    'huaweicloudsdkdgc==3.1.65',
    'huaweicloudsdkdlf==3.1.65',
    'huaweicloudsdkdli==3.1.65',
    'huaweicloudsdkdns==3.1.65',
    'huaweicloudsdkdris==3.1.65',
    'huaweicloudsdkdrs==3.1.65',
    'huaweicloudsdkdsc==3.1.65',
    'huaweicloudsdkdwr==3.1.65',
    'huaweicloudsdkdws==3.1.65',
    'huaweicloudsdkec==3.1.65',
    'huaweicloudsdkecs==3.1.65',
    'huaweicloudsdkedgesec==3.1.65',
    'huaweicloudsdkeg==3.1.65',
    'huaweicloudsdkeihealth==3.1.65',
    'huaweicloudsdkeip==3.1.65',
    'huaweicloudsdkelb==3.1.65',
    'huaweicloudsdkeps==3.1.65',
    'huaweicloudsdker==3.1.65',
    'huaweicloudsdkevs==3.1.65',
    'huaweicloudsdkfrs==3.1.65',
    'huaweicloudsdkfunctiongraph==3.1.65',
    'huaweicloudsdkga==3.1.65',
    'huaweicloudsdkgaussdb==3.1.65',
    'huaweicloudsdkgaussdbfornosql==3.1.65',
    'huaweicloudsdkgaussdbforopengauss==3.1.65',
    'huaweicloudsdkges==3.1.65',
    'huaweicloudsdkgsl==3.1.65',
    'huaweicloudsdkhilens==3.1.65',
    'huaweicloudsdkhss==3.1.65',
    'huaweicloudsdkiam==3.1.65',
    'huaweicloudsdkidentitycenter==3.1.65',
    'huaweicloudsdkidentitycenterstore==3.1.65',
    'huaweicloudsdkidme==3.1.65',
    'huaweicloudsdkiec==3.1.65',
    'huaweicloudsdkief==3.1.65',
    'huaweicloudsdkimage==3.1.65',
    'huaweicloudsdkimagesearch==3.1.65',
    'huaweicloudsdkims==3.1.65',
    'huaweicloudsdkiotanalytics==3.1.65',
    'huaweicloudsdkiotda==3.1.65',
    'huaweicloudsdkiotedge==3.1.65',
    'huaweicloudsdkivs==3.1.65',
    'huaweicloudsdkkafka==3.1.65',
    'huaweicloudsdkkms==3.1.65',
    'huaweicloudsdkkoomessage==3.1.65',
    'huaweicloudsdkkps==3.1.65',
    'huaweicloudsdklakeformation==3.1.65',
    'huaweicloudsdklive==3.1.65',
    'huaweicloudsdklts==3.1.65',
    'huaweicloudsdkmapds==3.1.65',
    'huaweicloudsdkmas==3.1.65',
    'huaweicloudsdkmeeting==3.1.65',
    'huaweicloudsdkmetastudio==3.1.65',
    'huaweicloudsdkmoderation==3.1.65',
    'huaweicloudsdkmpc==3.1.65',
    'huaweicloudsdkmrs==3.1.65',
    'huaweicloudsdkmsgsms==3.1.65',
    'huaweicloudsdkmssi==3.1.65',
    'huaweicloudsdknat==3.1.65',
    'huaweicloudsdknlp==3.1.65',
    'huaweicloudsdkocr==3.1.65',
    'huaweicloudsdkoms==3.1.65',
    'huaweicloudsdkoptverse==3.1.65',
    'huaweicloudsdkorganizations==3.1.65',
    'huaweicloudsdkoroas==3.1.65',
    'huaweicloudsdkosm==3.1.65',
    'huaweicloudsdkpangulargemodels==3.1.65',
    'huaweicloudsdkprojectman==3.1.65',
    'huaweicloudsdkrabbitmq==3.1.65',
    'huaweicloudsdkram==3.1.65',
    'huaweicloudsdkrds==3.1.65',
    'huaweicloudsdkres==3.1.65',
    'huaweicloudsdkrms==3.1.65',
    'huaweicloudsdkrocketmq==3.1.65',
    'huaweicloudsdkroma==3.1.65',
    'huaweicloudsdksa==3.1.65',
    'huaweicloudsdkscm==3.1.65',
    'huaweicloudsdksdrs==3.1.65',
    'huaweicloudsdksecmaster==3.1.65',
    'huaweicloudsdkservicestage==3.1.65',
    'huaweicloudsdksfsturbo==3.1.65',
    'huaweicloudsdksis==3.1.65',
    'huaweicloudsdksmn==3.1.65',
    'huaweicloudsdksms==3.1.65',
    'huaweicloudsdkswr==3.1.65',
    'huaweicloudsdktics==3.1.65',
    'huaweicloudsdktms==3.1.65',
    'huaweicloudsdkugo==3.1.65',
    'huaweicloudsdkvas==3.1.65',
    'huaweicloudsdkvcm==3.1.65',
    'huaweicloudsdkvod==3.1.65',
    'huaweicloudsdkvpc==3.1.65',
    'huaweicloudsdkvpcep==3.1.65',
    'huaweicloudsdkvpn==3.1.65',
    'huaweicloudsdkwaf==3.1.65',
    'huaweicloudsdkworkspace==3.1.65',
    'huaweicloudsdkworkspaceapp==3.1.65',
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
