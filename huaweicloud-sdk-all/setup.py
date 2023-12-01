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
VERSION = "3.1.70"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.70',
    'huaweicloudsdkaad==3.1.70',
    'huaweicloudsdkantiddos==3.1.70',
    'huaweicloudsdkaom==3.1.70',
    'huaweicloudsdkaos==3.1.70',
    'huaweicloudsdkapig==3.1.70',
    'huaweicloudsdkapm==3.1.70',
    'huaweicloudsdkas==3.1.70',
    'huaweicloudsdkasm==3.1.70',
    'huaweicloudsdkbcs==3.1.70',
    'huaweicloudsdkbms==3.1.70',
    'huaweicloudsdkbss==3.1.70',
    'huaweicloudsdkbssintl==3.1.70',
    'huaweicloudsdkcae==3.1.70',
    'huaweicloudsdkcampusgo==3.1.70',
    'huaweicloudsdkcbh==3.1.70',
    'huaweicloudsdkcbr==3.1.70',
    'huaweicloudsdkcbs==3.1.70',
    'huaweicloudsdkcc==3.1.70',
    'huaweicloudsdkcce==3.1.70',
    'huaweicloudsdkccm==3.1.70',
    'huaweicloudsdkcdm==3.1.70',
    'huaweicloudsdkcdn==3.1.70',
    'huaweicloudsdkces==3.1.70',
    'huaweicloudsdkcfw==3.1.70',
    'huaweicloudsdkcgs==3.1.70',
    'huaweicloudsdkclassroom==3.1.70',
    'huaweicloudsdkcloudide==3.1.70',
    'huaweicloudsdkcloudpond==3.1.70',
    'huaweicloudsdkcloudrtc==3.1.70',
    'huaweicloudsdkcloudtable==3.1.70',
    'huaweicloudsdkcloudtest==3.1.70',
    'huaweicloudsdkcodeartsartifact==3.1.70',
    'huaweicloudsdkcodeartsbuild==3.1.70',
    'huaweicloudsdkcodeartscheck==3.1.70',
    'huaweicloudsdkcodeartsdeploy==3.1.70',
    'huaweicloudsdkcodeartsinspector==3.1.70',
    'huaweicloudsdkcodeartspipeline==3.1.70',
    'huaweicloudsdkcodecraft==3.1.70',
    'huaweicloudsdkcodehub==3.1.70',
    'huaweicloudsdkconfig==3.1.70',
    'huaweicloudsdkcph==3.1.70',
    'huaweicloudsdkcpts==3.1.70',
    'huaweicloudsdkcse==3.1.70',
    'huaweicloudsdkcsms==3.1.70',
    'huaweicloudsdkcss==3.1.70',
    'huaweicloudsdkcts==3.1.70',
    'huaweicloudsdkdas==3.1.70',
    'huaweicloudsdkdataartsstudio==3.1.70',
    'huaweicloudsdkdbss==3.1.70',
    'huaweicloudsdkdc==3.1.70',
    'huaweicloudsdkdcs==3.1.70',
    'huaweicloudsdkddm==3.1.70',
    'huaweicloudsdkdds==3.1.70',
    'huaweicloudsdkdeh==3.1.70',
    'huaweicloudsdkdevsecurity==3.1.70',
    'huaweicloudsdkdevstar==3.1.70',
    'huaweicloudsdkdgc==3.1.70',
    'huaweicloudsdkdis==3.1.70',
    'huaweicloudsdkdlf==3.1.70',
    'huaweicloudsdkdli==3.1.70',
    'huaweicloudsdkdns==3.1.70',
    'huaweicloudsdkdris==3.1.70',
    'huaweicloudsdkdrs==3.1.70',
    'huaweicloudsdkdsc==3.1.70',
    'huaweicloudsdkdwr==3.1.70',
    'huaweicloudsdkdws==3.1.70',
    'huaweicloudsdkec==3.1.70',
    'huaweicloudsdkecs==3.1.70',
    'huaweicloudsdkedgesec==3.1.70',
    'huaweicloudsdkeg==3.1.70',
    'huaweicloudsdkeihealth==3.1.70',
    'huaweicloudsdkeip==3.1.70',
    'huaweicloudsdkelb==3.1.70',
    'huaweicloudsdkeps==3.1.70',
    'huaweicloudsdker==3.1.70',
    'huaweicloudsdkevs==3.1.70',
    'huaweicloudsdkfrs==3.1.70',
    'huaweicloudsdkfunctiongraph==3.1.70',
    'huaweicloudsdkga==3.1.70',
    'huaweicloudsdkgaussdb==3.1.70',
    'huaweicloudsdkgaussdbfornosql==3.1.70',
    'huaweicloudsdkgaussdbforopengauss==3.1.70',
    'huaweicloudsdkges==3.1.70',
    'huaweicloudsdkgsl==3.1.70',
    'huaweicloudsdkhilens==3.1.70',
    'huaweicloudsdkhss==3.1.70',
    'huaweicloudsdkiam==3.1.70',
    'huaweicloudsdkidentitycenter==3.1.70',
    'huaweicloudsdkidentitycenterstore==3.1.70',
    'huaweicloudsdkidme==3.1.70',
    'huaweicloudsdkiec==3.1.70',
    'huaweicloudsdkief==3.1.70',
    'huaweicloudsdkimage==3.1.70',
    'huaweicloudsdkimagesearch==3.1.70',
    'huaweicloudsdkims==3.1.70',
    'huaweicloudsdkiotanalytics==3.1.70',
    'huaweicloudsdkiotda==3.1.70',
    'huaweicloudsdkiotedge==3.1.70',
    'huaweicloudsdkivs==3.1.70',
    'huaweicloudsdkkafka==3.1.70',
    'huaweicloudsdkkms==3.1.70',
    'huaweicloudsdkkoomessage==3.1.70',
    'huaweicloudsdkkps==3.1.70',
    'huaweicloudsdklakeformation==3.1.70',
    'huaweicloudsdklive==3.1.70',
    'huaweicloudsdklts==3.1.70',
    'huaweicloudsdkmapds==3.1.70',
    'huaweicloudsdkmas==3.1.70',
    'huaweicloudsdkmeeting==3.1.70',
    'huaweicloudsdkmetastudio==3.1.70',
    'huaweicloudsdkmoderation==3.1.70',
    'huaweicloudsdkmpc==3.1.70',
    'huaweicloudsdkmrs==3.1.70',
    'huaweicloudsdkmsgsms==3.1.70',
    'huaweicloudsdkmssi==3.1.70',
    'huaweicloudsdknat==3.1.70',
    'huaweicloudsdknlp==3.1.70',
    'huaweicloudsdkocr==3.1.70',
    'huaweicloudsdkoms==3.1.70',
    'huaweicloudsdkoptverse==3.1.70',
    'huaweicloudsdkorganizations==3.1.70',
    'huaweicloudsdkoroas==3.1.70',
    'huaweicloudsdkosm==3.1.70',
    'huaweicloudsdkpangulargemodels==3.1.70',
    'huaweicloudsdkprojectman==3.1.70',
    'huaweicloudsdkrabbitmq==3.1.70',
    'huaweicloudsdkram==3.1.70',
    'huaweicloudsdkrds==3.1.70',
    'huaweicloudsdkres==3.1.70',
    'huaweicloudsdkrms==3.1.70',
    'huaweicloudsdkrocketmq==3.1.70',
    'huaweicloudsdkroma==3.1.70',
    'huaweicloudsdksa==3.1.70',
    'huaweicloudsdkscm==3.1.70',
    'huaweicloudsdksdrs==3.1.70',
    'huaweicloudsdksecmaster==3.1.70',
    'huaweicloudsdkservicestage==3.1.70',
    'huaweicloudsdksfsturbo==3.1.70',
    'huaweicloudsdksis==3.1.70',
    'huaweicloudsdksmn==3.1.70',
    'huaweicloudsdksms==3.1.70',
    'huaweicloudsdkswr==3.1.70',
    'huaweicloudsdktics==3.1.70',
    'huaweicloudsdktms==3.1.70',
    'huaweicloudsdkugo==3.1.70',
    'huaweicloudsdkvas==3.1.70',
    'huaweicloudsdkvcm==3.1.70',
    'huaweicloudsdkvod==3.1.70',
    'huaweicloudsdkvpc==3.1.70',
    'huaweicloudsdkvpcep==3.1.70',
    'huaweicloudsdkvpn==3.1.70',
    'huaweicloudsdkwaf==3.1.70',
    'huaweicloudsdkworkspace==3.1.70',
    'huaweicloudsdkworkspaceapp==3.1.70',
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
