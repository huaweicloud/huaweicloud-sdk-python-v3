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
VERSION = "3.1.73"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.73',
    'huaweicloudsdkaad==3.1.73',
    'huaweicloudsdkantiddos==3.1.73',
    'huaweicloudsdkaom==3.1.73',
    'huaweicloudsdkaos==3.1.73',
    'huaweicloudsdkapig==3.1.73',
    'huaweicloudsdkapm==3.1.73',
    'huaweicloudsdkas==3.1.73',
    'huaweicloudsdkasm==3.1.73',
    'huaweicloudsdkbcs==3.1.73',
    'huaweicloudsdkbms==3.1.73',
    'huaweicloudsdkbss==3.1.73',
    'huaweicloudsdkbssintl==3.1.73',
    'huaweicloudsdkcae==3.1.73',
    'huaweicloudsdkcampusgo==3.1.73',
    'huaweicloudsdkcbh==3.1.73',
    'huaweicloudsdkcbr==3.1.73',
    'huaweicloudsdkcbs==3.1.73',
    'huaweicloudsdkcc==3.1.73',
    'huaweicloudsdkcce==3.1.73',
    'huaweicloudsdkccm==3.1.73',
    'huaweicloudsdkcdm==3.1.73',
    'huaweicloudsdkcdn==3.1.73',
    'huaweicloudsdkces==3.1.73',
    'huaweicloudsdkcfw==3.1.73',
    'huaweicloudsdkcgs==3.1.73',
    'huaweicloudsdkclassroom==3.1.73',
    'huaweicloudsdkcloudide==3.1.73',
    'huaweicloudsdkcloudpond==3.1.73',
    'huaweicloudsdkcloudrtc==3.1.73',
    'huaweicloudsdkcloudtable==3.1.73',
    'huaweicloudsdkcloudtest==3.1.73',
    'huaweicloudsdkcodeartsartifact==3.1.73',
    'huaweicloudsdkcodeartsbuild==3.1.73',
    'huaweicloudsdkcodeartscheck==3.1.73',
    'huaweicloudsdkcodeartsdeploy==3.1.73',
    'huaweicloudsdkcodeartsinspector==3.1.73',
    'huaweicloudsdkcodeartspipeline==3.1.73',
    'huaweicloudsdkcodecraft==3.1.73',
    'huaweicloudsdkcodehub==3.1.73',
    'huaweicloudsdkconfig==3.1.73',
    'huaweicloudsdkcph==3.1.73',
    'huaweicloudsdkcpts==3.1.73',
    'huaweicloudsdkcse==3.1.73',
    'huaweicloudsdkcsms==3.1.73',
    'huaweicloudsdkcss==3.1.73',
    'huaweicloudsdkcts==3.1.73',
    'huaweicloudsdkdas==3.1.73',
    'huaweicloudsdkdataartsstudio==3.1.73',
    'huaweicloudsdkdbss==3.1.73',
    'huaweicloudsdkdc==3.1.73',
    'huaweicloudsdkdcs==3.1.73',
    'huaweicloudsdkddm==3.1.73',
    'huaweicloudsdkdds==3.1.73',
    'huaweicloudsdkdeh==3.1.73',
    'huaweicloudsdkdevsecurity==3.1.73',
    'huaweicloudsdkdevstar==3.1.73',
    'huaweicloudsdkdgc==3.1.73',
    'huaweicloudsdkdis==3.1.73',
    'huaweicloudsdkdlf==3.1.73',
    'huaweicloudsdkdli==3.1.73',
    'huaweicloudsdkdns==3.1.73',
    'huaweicloudsdkdris==3.1.73',
    'huaweicloudsdkdrs==3.1.73',
    'huaweicloudsdkdsc==3.1.73',
    'huaweicloudsdkdwr==3.1.73',
    'huaweicloudsdkdws==3.1.73',
    'huaweicloudsdkec==3.1.73',
    'huaweicloudsdkecs==3.1.73',
    'huaweicloudsdkedgesec==3.1.73',
    'huaweicloudsdkeg==3.1.73',
    'huaweicloudsdkeihealth==3.1.73',
    'huaweicloudsdkeip==3.1.73',
    'huaweicloudsdkelb==3.1.73',
    'huaweicloudsdkeps==3.1.73',
    'huaweicloudsdker==3.1.73',
    'huaweicloudsdkevs==3.1.73',
    'huaweicloudsdkfrs==3.1.73',
    'huaweicloudsdkfunctiongraph==3.1.73',
    'huaweicloudsdkga==3.1.73',
    'huaweicloudsdkgaussdb==3.1.73',
    'huaweicloudsdkgaussdbfornosql==3.1.73',
    'huaweicloudsdkgaussdbforopengauss==3.1.73',
    'huaweicloudsdkges==3.1.73',
    'huaweicloudsdkgsl==3.1.73',
    'huaweicloudsdkhilens==3.1.73',
    'huaweicloudsdkhss==3.1.73',
    'huaweicloudsdkiam==3.1.73',
    'huaweicloudsdkidentitycenter==3.1.73',
    'huaweicloudsdkidentitycenterstore==3.1.73',
    'huaweicloudsdkidme==3.1.73',
    'huaweicloudsdkidmeclassicapi==3.1.73',
    'huaweicloudsdkiec==3.1.73',
    'huaweicloudsdkief==3.1.73',
    'huaweicloudsdkimage==3.1.73',
    'huaweicloudsdkimagesearch==3.1.73',
    'huaweicloudsdkims==3.1.73',
    'huaweicloudsdkiotanalytics==3.1.73',
    'huaweicloudsdkiotda==3.1.73',
    'huaweicloudsdkiotedge==3.1.73',
    'huaweicloudsdkivs==3.1.73',
    'huaweicloudsdkkafka==3.1.73',
    'huaweicloudsdkkms==3.1.73',
    'huaweicloudsdkkoomessage==3.1.73',
    'huaweicloudsdkkps==3.1.73',
    'huaweicloudsdklakeformation==3.1.73',
    'huaweicloudsdklive==3.1.73',
    'huaweicloudsdklts==3.1.73',
    'huaweicloudsdkmapds==3.1.73',
    'huaweicloudsdkmas==3.1.73',
    'huaweicloudsdkmeeting==3.1.73',
    'huaweicloudsdkmetastudio==3.1.73',
    'huaweicloudsdkmoderation==3.1.73',
    'huaweicloudsdkmpc==3.1.73',
    'huaweicloudsdkmrs==3.1.73',
    'huaweicloudsdkmsgsms==3.1.73',
    'huaweicloudsdkmssi==3.1.73',
    'huaweicloudsdknat==3.1.73',
    'huaweicloudsdknlp==3.1.73',
    'huaweicloudsdkocr==3.1.73',
    'huaweicloudsdkoctopus==3.1.73',
    'huaweicloudsdkoms==3.1.73',
    'huaweicloudsdkoptverse==3.1.73',
    'huaweicloudsdkorganizations==3.1.73',
    'huaweicloudsdkoroas==3.1.73',
    'huaweicloudsdkosm==3.1.73',
    'huaweicloudsdkpangulargemodels==3.1.73',
    'huaweicloudsdkprojectman==3.1.73',
    'huaweicloudsdkrabbitmq==3.1.73',
    'huaweicloudsdkram==3.1.73',
    'huaweicloudsdkrds==3.1.73',
    'huaweicloudsdkres==3.1.73',
    'huaweicloudsdkrgc==3.1.73',
    'huaweicloudsdkrms==3.1.73',
    'huaweicloudsdkrocketmq==3.1.73',
    'huaweicloudsdkroma==3.1.73',
    'huaweicloudsdksa==3.1.73',
    'huaweicloudsdkscm==3.1.73',
    'huaweicloudsdksdrs==3.1.73',
    'huaweicloudsdksecmaster==3.1.73',
    'huaweicloudsdkservicestage==3.1.73',
    'huaweicloudsdksfsturbo==3.1.73',
    'huaweicloudsdksis==3.1.73',
    'huaweicloudsdksmn==3.1.73',
    'huaweicloudsdksms==3.1.73',
    'huaweicloudsdkswr==3.1.73',
    'huaweicloudsdktics==3.1.73',
    'huaweicloudsdktms==3.1.73',
    'huaweicloudsdkugo==3.1.73',
    'huaweicloudsdkvas==3.1.73',
    'huaweicloudsdkvcm==3.1.73',
    'huaweicloudsdkvod==3.1.73',
    'huaweicloudsdkvpc==3.1.73',
    'huaweicloudsdkvpcep==3.1.73',
    'huaweicloudsdkvpn==3.1.73',
    'huaweicloudsdkwaf==3.1.73',
    'huaweicloudsdkworkspace==3.1.73',
    'huaweicloudsdkworkspaceapp==3.1.73',
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
