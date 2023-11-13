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
VERSION = "3.1.66"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.66',
    'huaweicloudsdkantiddos==3.1.66',
    'huaweicloudsdkaom==3.1.66',
    'huaweicloudsdkaos==3.1.66',
    'huaweicloudsdkapig==3.1.66',
    'huaweicloudsdkapm==3.1.66',
    'huaweicloudsdkas==3.1.66',
    'huaweicloudsdkasm==3.1.66',
    'huaweicloudsdkbcs==3.1.66',
    'huaweicloudsdkbms==3.1.66',
    'huaweicloudsdkbss==3.1.66',
    'huaweicloudsdkbssintl==3.1.66',
    'huaweicloudsdkcae==3.1.66',
    'huaweicloudsdkcampusgo==3.1.66',
    'huaweicloudsdkcbh==3.1.66',
    'huaweicloudsdkcbr==3.1.66',
    'huaweicloudsdkcbs==3.1.66',
    'huaweicloudsdkcc==3.1.66',
    'huaweicloudsdkcce==3.1.66',
    'huaweicloudsdkccm==3.1.66',
    'huaweicloudsdkcdm==3.1.66',
    'huaweicloudsdkcdn==3.1.66',
    'huaweicloudsdkces==3.1.66',
    'huaweicloudsdkcfw==3.1.66',
    'huaweicloudsdkcgs==3.1.66',
    'huaweicloudsdkclassroom==3.1.66',
    'huaweicloudsdkcloudide==3.1.66',
    'huaweicloudsdkcloudpond==3.1.66',
    'huaweicloudsdkcloudrtc==3.1.66',
    'huaweicloudsdkcloudtable==3.1.66',
    'huaweicloudsdkcloudtest==3.1.66',
    'huaweicloudsdkcodeartsartifact==3.1.66',
    'huaweicloudsdkcodeartsbuild==3.1.66',
    'huaweicloudsdkcodeartscheck==3.1.66',
    'huaweicloudsdkcodeartsdeploy==3.1.66',
    'huaweicloudsdkcodeartsinspector==3.1.66',
    'huaweicloudsdkcodeartspipeline==3.1.66',
    'huaweicloudsdkcodecraft==3.1.66',
    'huaweicloudsdkcodehub==3.1.66',
    'huaweicloudsdkconfig==3.1.66',
    'huaweicloudsdkcph==3.1.66',
    'huaweicloudsdkcpts==3.1.66',
    'huaweicloudsdkcse==3.1.66',
    'huaweicloudsdkcsms==3.1.66',
    'huaweicloudsdkcss==3.1.66',
    'huaweicloudsdkcts==3.1.66',
    'huaweicloudsdkdas==3.1.66',
    'huaweicloudsdkdataartsstudio==3.1.66',
    'huaweicloudsdkdbss==3.1.66',
    'huaweicloudsdkdc==3.1.66',
    'huaweicloudsdkdcs==3.1.66',
    'huaweicloudsdkddm==3.1.66',
    'huaweicloudsdkdds==3.1.66',
    'huaweicloudsdkdeh==3.1.66',
    'huaweicloudsdkdevsecurity==3.1.66',
    'huaweicloudsdkdevstar==3.1.66',
    'huaweicloudsdkdgc==3.1.66',
    'huaweicloudsdkdlf==3.1.66',
    'huaweicloudsdkdli==3.1.66',
    'huaweicloudsdkdns==3.1.66',
    'huaweicloudsdkdris==3.1.66',
    'huaweicloudsdkdrs==3.1.66',
    'huaweicloudsdkdsc==3.1.66',
    'huaweicloudsdkdwr==3.1.66',
    'huaweicloudsdkdws==3.1.66',
    'huaweicloudsdkec==3.1.66',
    'huaweicloudsdkecs==3.1.66',
    'huaweicloudsdkedgesec==3.1.66',
    'huaweicloudsdkeg==3.1.66',
    'huaweicloudsdkeihealth==3.1.66',
    'huaweicloudsdkeip==3.1.66',
    'huaweicloudsdkelb==3.1.66',
    'huaweicloudsdkeps==3.1.66',
    'huaweicloudsdker==3.1.66',
    'huaweicloudsdkevs==3.1.66',
    'huaweicloudsdkfrs==3.1.66',
    'huaweicloudsdkfunctiongraph==3.1.66',
    'huaweicloudsdkga==3.1.66',
    'huaweicloudsdkgaussdb==3.1.66',
    'huaweicloudsdkgaussdbfornosql==3.1.66',
    'huaweicloudsdkgaussdbforopengauss==3.1.66',
    'huaweicloudsdkges==3.1.66',
    'huaweicloudsdkgsl==3.1.66',
    'huaweicloudsdkhilens==3.1.66',
    'huaweicloudsdkhss==3.1.66',
    'huaweicloudsdkiam==3.1.66',
    'huaweicloudsdkidentitycenter==3.1.66',
    'huaweicloudsdkidentitycenterstore==3.1.66',
    'huaweicloudsdkidme==3.1.66',
    'huaweicloudsdkiec==3.1.66',
    'huaweicloudsdkief==3.1.66',
    'huaweicloudsdkimage==3.1.66',
    'huaweicloudsdkimagesearch==3.1.66',
    'huaweicloudsdkims==3.1.66',
    'huaweicloudsdkiotanalytics==3.1.66',
    'huaweicloudsdkiotda==3.1.66',
    'huaweicloudsdkiotedge==3.1.66',
    'huaweicloudsdkivs==3.1.66',
    'huaweicloudsdkkafka==3.1.66',
    'huaweicloudsdkkms==3.1.66',
    'huaweicloudsdkkoomessage==3.1.66',
    'huaweicloudsdkkps==3.1.66',
    'huaweicloudsdklakeformation==3.1.66',
    'huaweicloudsdklive==3.1.66',
    'huaweicloudsdklts==3.1.66',
    'huaweicloudsdkmapds==3.1.66',
    'huaweicloudsdkmas==3.1.66',
    'huaweicloudsdkmeeting==3.1.66',
    'huaweicloudsdkmetastudio==3.1.66',
    'huaweicloudsdkmoderation==3.1.66',
    'huaweicloudsdkmpc==3.1.66',
    'huaweicloudsdkmrs==3.1.66',
    'huaweicloudsdkmsgsms==3.1.66',
    'huaweicloudsdkmssi==3.1.66',
    'huaweicloudsdknat==3.1.66',
    'huaweicloudsdknlp==3.1.66',
    'huaweicloudsdkocr==3.1.66',
    'huaweicloudsdkoms==3.1.66',
    'huaweicloudsdkoptverse==3.1.66',
    'huaweicloudsdkorganizations==3.1.66',
    'huaweicloudsdkoroas==3.1.66',
    'huaweicloudsdkosm==3.1.66',
    'huaweicloudsdkpangulargemodels==3.1.66',
    'huaweicloudsdkprojectman==3.1.66',
    'huaweicloudsdkrabbitmq==3.1.66',
    'huaweicloudsdkram==3.1.66',
    'huaweicloudsdkrds==3.1.66',
    'huaweicloudsdkres==3.1.66',
    'huaweicloudsdkrms==3.1.66',
    'huaweicloudsdkrocketmq==3.1.66',
    'huaweicloudsdkroma==3.1.66',
    'huaweicloudsdksa==3.1.66',
    'huaweicloudsdkscm==3.1.66',
    'huaweicloudsdksdrs==3.1.66',
    'huaweicloudsdksecmaster==3.1.66',
    'huaweicloudsdkservicestage==3.1.66',
    'huaweicloudsdksfsturbo==3.1.66',
    'huaweicloudsdksis==3.1.66',
    'huaweicloudsdksmn==3.1.66',
    'huaweicloudsdksms==3.1.66',
    'huaweicloudsdkswr==3.1.66',
    'huaweicloudsdktics==3.1.66',
    'huaweicloudsdktms==3.1.66',
    'huaweicloudsdkugo==3.1.66',
    'huaweicloudsdkvas==3.1.66',
    'huaweicloudsdkvcm==3.1.66',
    'huaweicloudsdkvod==3.1.66',
    'huaweicloudsdkvpc==3.1.66',
    'huaweicloudsdkvpcep==3.1.66',
    'huaweicloudsdkvpn==3.1.66',
    'huaweicloudsdkwaf==3.1.66',
    'huaweicloudsdkworkspace==3.1.66',
    'huaweicloudsdkworkspaceapp==3.1.66',
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
