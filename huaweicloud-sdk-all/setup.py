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
VERSION = "3.1.68"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.68',
    'huaweicloudsdkaad==3.1.68',
    'huaweicloudsdkantiddos==3.1.68',
    'huaweicloudsdkaom==3.1.68',
    'huaweicloudsdkaos==3.1.68',
    'huaweicloudsdkapig==3.1.68',
    'huaweicloudsdkapm==3.1.68',
    'huaweicloudsdkas==3.1.68',
    'huaweicloudsdkasm==3.1.68',
    'huaweicloudsdkbcs==3.1.68',
    'huaweicloudsdkbms==3.1.68',
    'huaweicloudsdkbss==3.1.68',
    'huaweicloudsdkbssintl==3.1.68',
    'huaweicloudsdkcae==3.1.68',
    'huaweicloudsdkcampusgo==3.1.68',
    'huaweicloudsdkcbh==3.1.68',
    'huaweicloudsdkcbr==3.1.68',
    'huaweicloudsdkcbs==3.1.68',
    'huaweicloudsdkcc==3.1.68',
    'huaweicloudsdkcce==3.1.68',
    'huaweicloudsdkccm==3.1.68',
    'huaweicloudsdkcdm==3.1.68',
    'huaweicloudsdkcdn==3.1.68',
    'huaweicloudsdkces==3.1.68',
    'huaweicloudsdkcfw==3.1.68',
    'huaweicloudsdkcgs==3.1.68',
    'huaweicloudsdkclassroom==3.1.68',
    'huaweicloudsdkcloudide==3.1.68',
    'huaweicloudsdkcloudpond==3.1.68',
    'huaweicloudsdkcloudrtc==3.1.68',
    'huaweicloudsdkcloudtable==3.1.68',
    'huaweicloudsdkcloudtest==3.1.68',
    'huaweicloudsdkcodeartsartifact==3.1.68',
    'huaweicloudsdkcodeartsbuild==3.1.68',
    'huaweicloudsdkcodeartscheck==3.1.68',
    'huaweicloudsdkcodeartsdeploy==3.1.68',
    'huaweicloudsdkcodeartsinspector==3.1.68',
    'huaweicloudsdkcodeartspipeline==3.1.68',
    'huaweicloudsdkcodecraft==3.1.68',
    'huaweicloudsdkcodehub==3.1.68',
    'huaweicloudsdkconfig==3.1.68',
    'huaweicloudsdkcph==3.1.68',
    'huaweicloudsdkcpts==3.1.68',
    'huaweicloudsdkcse==3.1.68',
    'huaweicloudsdkcsms==3.1.68',
    'huaweicloudsdkcss==3.1.68',
    'huaweicloudsdkcts==3.1.68',
    'huaweicloudsdkdas==3.1.68',
    'huaweicloudsdkdataartsstudio==3.1.68',
    'huaweicloudsdkdbss==3.1.68',
    'huaweicloudsdkdc==3.1.68',
    'huaweicloudsdkdcs==3.1.68',
    'huaweicloudsdkddm==3.1.68',
    'huaweicloudsdkdds==3.1.68',
    'huaweicloudsdkdeh==3.1.68',
    'huaweicloudsdkdevsecurity==3.1.68',
    'huaweicloudsdkdevstar==3.1.68',
    'huaweicloudsdkdgc==3.1.68',
    'huaweicloudsdkdlf==3.1.68',
    'huaweicloudsdkdli==3.1.68',
    'huaweicloudsdkdns==3.1.68',
    'huaweicloudsdkdris==3.1.68',
    'huaweicloudsdkdrs==3.1.68',
    'huaweicloudsdkdsc==3.1.68',
    'huaweicloudsdkdwr==3.1.68',
    'huaweicloudsdkdws==3.1.68',
    'huaweicloudsdkec==3.1.68',
    'huaweicloudsdkecs==3.1.68',
    'huaweicloudsdkedgesec==3.1.68',
    'huaweicloudsdkeg==3.1.68',
    'huaweicloudsdkeihealth==3.1.68',
    'huaweicloudsdkeip==3.1.68',
    'huaweicloudsdkelb==3.1.68',
    'huaweicloudsdkeps==3.1.68',
    'huaweicloudsdker==3.1.68',
    'huaweicloudsdkevs==3.1.68',
    'huaweicloudsdkfrs==3.1.68',
    'huaweicloudsdkfunctiongraph==3.1.68',
    'huaweicloudsdkga==3.1.68',
    'huaweicloudsdkgaussdb==3.1.68',
    'huaweicloudsdkgaussdbfornosql==3.1.68',
    'huaweicloudsdkgaussdbforopengauss==3.1.68',
    'huaweicloudsdkges==3.1.68',
    'huaweicloudsdkgsl==3.1.68',
    'huaweicloudsdkhilens==3.1.68',
    'huaweicloudsdkhss==3.1.68',
    'huaweicloudsdkiam==3.1.68',
    'huaweicloudsdkidentitycenter==3.1.68',
    'huaweicloudsdkidentitycenterstore==3.1.68',
    'huaweicloudsdkidme==3.1.68',
    'huaweicloudsdkiec==3.1.68',
    'huaweicloudsdkief==3.1.68',
    'huaweicloudsdkimage==3.1.68',
    'huaweicloudsdkimagesearch==3.1.68',
    'huaweicloudsdkims==3.1.68',
    'huaweicloudsdkiotanalytics==3.1.68',
    'huaweicloudsdkiotda==3.1.68',
    'huaweicloudsdkiotedge==3.1.68',
    'huaweicloudsdkivs==3.1.68',
    'huaweicloudsdkkafka==3.1.68',
    'huaweicloudsdkkms==3.1.68',
    'huaweicloudsdkkoomessage==3.1.68',
    'huaweicloudsdkkps==3.1.68',
    'huaweicloudsdklakeformation==3.1.68',
    'huaweicloudsdklive==3.1.68',
    'huaweicloudsdklts==3.1.68',
    'huaweicloudsdkmapds==3.1.68',
    'huaweicloudsdkmas==3.1.68',
    'huaweicloudsdkmeeting==3.1.68',
    'huaweicloudsdkmetastudio==3.1.68',
    'huaweicloudsdkmoderation==3.1.68',
    'huaweicloudsdkmpc==3.1.68',
    'huaweicloudsdkmrs==3.1.68',
    'huaweicloudsdkmsgsms==3.1.68',
    'huaweicloudsdkmssi==3.1.68',
    'huaweicloudsdknat==3.1.68',
    'huaweicloudsdknlp==3.1.68',
    'huaweicloudsdkocr==3.1.68',
    'huaweicloudsdkoms==3.1.68',
    'huaweicloudsdkoptverse==3.1.68',
    'huaweicloudsdkorganizations==3.1.68',
    'huaweicloudsdkoroas==3.1.68',
    'huaweicloudsdkosm==3.1.68',
    'huaweicloudsdkpangulargemodels==3.1.68',
    'huaweicloudsdkprojectman==3.1.68',
    'huaweicloudsdkrabbitmq==3.1.68',
    'huaweicloudsdkram==3.1.68',
    'huaweicloudsdkrds==3.1.68',
    'huaweicloudsdkres==3.1.68',
    'huaweicloudsdkrms==3.1.68',
    'huaweicloudsdkrocketmq==3.1.68',
    'huaweicloudsdkroma==3.1.68',
    'huaweicloudsdksa==3.1.68',
    'huaweicloudsdkscm==3.1.68',
    'huaweicloudsdksdrs==3.1.68',
    'huaweicloudsdksecmaster==3.1.68',
    'huaweicloudsdkservicestage==3.1.68',
    'huaweicloudsdksfsturbo==3.1.68',
    'huaweicloudsdksis==3.1.68',
    'huaweicloudsdksmn==3.1.68',
    'huaweicloudsdksms==3.1.68',
    'huaweicloudsdkswr==3.1.68',
    'huaweicloudsdktics==3.1.68',
    'huaweicloudsdktms==3.1.68',
    'huaweicloudsdkugo==3.1.68',
    'huaweicloudsdkvas==3.1.68',
    'huaweicloudsdkvcm==3.1.68',
    'huaweicloudsdkvod==3.1.68',
    'huaweicloudsdkvpc==3.1.68',
    'huaweicloudsdkvpcep==3.1.68',
    'huaweicloudsdkvpn==3.1.68',
    'huaweicloudsdkwaf==3.1.68',
    'huaweicloudsdkworkspace==3.1.68',
    'huaweicloudsdkworkspaceapp==3.1.68',
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
