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
VERSION = "3.1.79"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.79',
    'huaweicloudsdkaad==3.1.79',
    'huaweicloudsdkantiddos==3.1.79',
    'huaweicloudsdkaom==3.1.79',
    'huaweicloudsdkaos==3.1.79',
    'huaweicloudsdkapig==3.1.79',
    'huaweicloudsdkapm==3.1.79',
    'huaweicloudsdkas==3.1.79',
    'huaweicloudsdkasm==3.1.79',
    'huaweicloudsdkbcs==3.1.79',
    'huaweicloudsdkbms==3.1.79',
    'huaweicloudsdkbss==3.1.79',
    'huaweicloudsdkbssintl==3.1.79',
    'huaweicloudsdkcae==3.1.79',
    'huaweicloudsdkcampusgo==3.1.79',
    'huaweicloudsdkcbh==3.1.79',
    'huaweicloudsdkcbr==3.1.79',
    'huaweicloudsdkcbs==3.1.79',
    'huaweicloudsdkcc==3.1.79',
    'huaweicloudsdkcce==3.1.79',
    'huaweicloudsdkccm==3.1.79',
    'huaweicloudsdkcdm==3.1.79',
    'huaweicloudsdkcdn==3.1.79',
    'huaweicloudsdkces==3.1.79',
    'huaweicloudsdkcfw==3.1.79',
    'huaweicloudsdkcgs==3.1.79',
    'huaweicloudsdkclassroom==3.1.79',
    'huaweicloudsdkcloudide==3.1.79',
    'huaweicloudsdkcloudpond==3.1.79',
    'huaweicloudsdkcloudrtc==3.1.79',
    'huaweicloudsdkcloudtable==3.1.79',
    'huaweicloudsdkcloudtest==3.1.79',
    'huaweicloudsdkcodeartsartifact==3.1.79',
    'huaweicloudsdkcodeartsbuild==3.1.79',
    'huaweicloudsdkcodeartscheck==3.1.79',
    'huaweicloudsdkcodeartsdeploy==3.1.79',
    'huaweicloudsdkcodeartsinspector==3.1.79',
    'huaweicloudsdkcodeartspipeline==3.1.79',
    'huaweicloudsdkcodecraft==3.1.79',
    'huaweicloudsdkcodehub==3.1.79',
    'huaweicloudsdkconfig==3.1.79',
    'huaweicloudsdkcph==3.1.79',
    'huaweicloudsdkcpts==3.1.79',
    'huaweicloudsdkcse==3.1.79',
    'huaweicloudsdkcsms==3.1.79',
    'huaweicloudsdkcss==3.1.79',
    'huaweicloudsdkcts==3.1.79',
    'huaweicloudsdkdas==3.1.79',
    'huaweicloudsdkdataartsstudio==3.1.79',
    'huaweicloudsdkdbss==3.1.79',
    'huaweicloudsdkdc==3.1.79',
    'huaweicloudsdkdcs==3.1.79',
    'huaweicloudsdkddm==3.1.79',
    'huaweicloudsdkdds==3.1.79',
    'huaweicloudsdkdeh==3.1.79',
    'huaweicloudsdkdevsecurity==3.1.79',
    'huaweicloudsdkdevstar==3.1.79',
    'huaweicloudsdkdgc==3.1.79',
    'huaweicloudsdkdis==3.1.79',
    'huaweicloudsdkdlf==3.1.79',
    'huaweicloudsdkdli==3.1.79',
    'huaweicloudsdkdns==3.1.79',
    'huaweicloudsdkdris==3.1.79',
    'huaweicloudsdkdrs==3.1.79',
    'huaweicloudsdkdsc==3.1.79',
    'huaweicloudsdkdwr==3.1.79',
    'huaweicloudsdkdws==3.1.79',
    'huaweicloudsdkec==3.1.79',
    'huaweicloudsdkecs==3.1.79',
    'huaweicloudsdkedgesec==3.1.79',
    'huaweicloudsdkeg==3.1.79',
    'huaweicloudsdkeihealth==3.1.79',
    'huaweicloudsdkeip==3.1.79',
    'huaweicloudsdkelb==3.1.79',
    'huaweicloudsdkeps==3.1.79',
    'huaweicloudsdker==3.1.79',
    'huaweicloudsdkevs==3.1.79',
    'huaweicloudsdkfrs==3.1.79',
    'huaweicloudsdkfunctiongraph==3.1.79',
    'huaweicloudsdkga==3.1.79',
    'huaweicloudsdkgaussdb==3.1.79',
    'huaweicloudsdkgaussdbfornosql==3.1.79',
    'huaweicloudsdkgaussdbforopengauss==3.1.79',
    'huaweicloudsdkges==3.1.79',
    'huaweicloudsdkgsl==3.1.79',
    'huaweicloudsdkhilens==3.1.79',
    'huaweicloudsdkhss==3.1.79',
    'huaweicloudsdkiam==3.1.79',
    'huaweicloudsdkidentitycenter==3.1.79',
    'huaweicloudsdkidentitycenterstore==3.1.79',
    'huaweicloudsdkidme==3.1.79',
    'huaweicloudsdkidmeclassicapi==3.1.79',
    'huaweicloudsdkiec==3.1.79',
    'huaweicloudsdkief==3.1.79',
    'huaweicloudsdkimage==3.1.79',
    'huaweicloudsdkimagesearch==3.1.79',
    'huaweicloudsdkims==3.1.79',
    'huaweicloudsdkiotanalytics==3.1.79',
    'huaweicloudsdkiotda==3.1.79',
    'huaweicloudsdkiotedge==3.1.79',
    'huaweicloudsdkivs==3.1.79',
    'huaweicloudsdkkafka==3.1.79',
    'huaweicloudsdkkms==3.1.79',
    'huaweicloudsdkkoomessage==3.1.79',
    'huaweicloudsdkkps==3.1.79',
    'huaweicloudsdklakeformation==3.1.79',
    'huaweicloudsdklive==3.1.79',
    'huaweicloudsdklts==3.1.79',
    'huaweicloudsdkmapds==3.1.79',
    'huaweicloudsdkmas==3.1.79',
    'huaweicloudsdkmeeting==3.1.79',
    'huaweicloudsdkmetastudio==3.1.79',
    'huaweicloudsdkmoderation==3.1.79',
    'huaweicloudsdkmpc==3.1.79',
    'huaweicloudsdkmrs==3.1.79',
    'huaweicloudsdkmsgsms==3.1.79',
    'huaweicloudsdkmssi==3.1.79',
    'huaweicloudsdknat==3.1.79',
    'huaweicloudsdknlp==3.1.79',
    'huaweicloudsdkobs==3.1.79',
    'huaweicloudsdkocr==3.1.79',
    'huaweicloudsdkoctopus==3.1.79',
    'huaweicloudsdkoms==3.1.79',
    'huaweicloudsdkoptverse==3.1.79',
    'huaweicloudsdkorganizations==3.1.79',
    'huaweicloudsdkoroas==3.1.79',
    'huaweicloudsdkosm==3.1.79',
    'huaweicloudsdkpangulargemodels==3.1.79',
    'huaweicloudsdkprojectman==3.1.79',
    'huaweicloudsdkrabbitmq==3.1.79',
    'huaweicloudsdkram==3.1.79',
    'huaweicloudsdkrds==3.1.79',
    'huaweicloudsdkres==3.1.79',
    'huaweicloudsdkrgc==3.1.79',
    'huaweicloudsdkrms==3.1.79',
    'huaweicloudsdkrocketmq==3.1.79',
    'huaweicloudsdkroma==3.1.79',
    'huaweicloudsdksa==3.1.79',
    'huaweicloudsdkscm==3.1.79',
    'huaweicloudsdksdrs==3.1.79',
    'huaweicloudsdksecmaster==3.1.79',
    'huaweicloudsdkservicestage==3.1.79',
    'huaweicloudsdksfsturbo==3.1.79',
    'huaweicloudsdksis==3.1.79',
    'huaweicloudsdksmn==3.1.79',
    'huaweicloudsdksms==3.1.79',
    'huaweicloudsdkswr==3.1.79',
    'huaweicloudsdktics==3.1.79',
    'huaweicloudsdktms==3.1.79',
    'huaweicloudsdkugo==3.1.79',
    'huaweicloudsdkvas==3.1.79',
    'huaweicloudsdkvcm==3.1.79',
    'huaweicloudsdkvod==3.1.79',
    'huaweicloudsdkvpc==3.1.79',
    'huaweicloudsdkvpcep==3.1.79',
    'huaweicloudsdkvpn==3.1.79',
    'huaweicloudsdkwaf==3.1.79',
    'huaweicloudsdkworkspace==3.1.79',
    'huaweicloudsdkworkspaceapp==3.1.79',
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
