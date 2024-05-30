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
VERSION = "3.1.98"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.98',
    'huaweicloudsdkaad==3.1.98',
    'huaweicloudsdkantiddos==3.1.98',
    'huaweicloudsdkaom==3.1.98',
    'huaweicloudsdkaos==3.1.98',
    'huaweicloudsdkapig==3.1.98',
    'huaweicloudsdkapm==3.1.98',
    'huaweicloudsdkas==3.1.98',
    'huaweicloudsdkasm==3.1.98',
    'huaweicloudsdkbcs==3.1.98',
    'huaweicloudsdkbms==3.1.98',
    'huaweicloudsdkbss==3.1.98',
    'huaweicloudsdkbssintl==3.1.98',
    'huaweicloudsdkcae==3.1.98',
    'huaweicloudsdkcampusgo==3.1.98',
    'huaweicloudsdkcbh==3.1.98',
    'huaweicloudsdkcbr==3.1.98',
    'huaweicloudsdkcbs==3.1.98',
    'huaweicloudsdkcc==3.1.98',
    'huaweicloudsdkcce==3.1.98',
    'huaweicloudsdkccm==3.1.98',
    'huaweicloudsdkcdm==3.1.98',
    'huaweicloudsdkcdn==3.1.98',
    'huaweicloudsdkces==3.1.98',
    'huaweicloudsdkcfw==3.1.98',
    'huaweicloudsdkcgs==3.1.98',
    'huaweicloudsdkclassroom==3.1.98',
    'huaweicloudsdkcloudide==3.1.98',
    'huaweicloudsdkcloudpond==3.1.98',
    'huaweicloudsdkcloudrtc==3.1.98',
    'huaweicloudsdkcloudtable==3.1.98',
    'huaweicloudsdkcloudtest==3.1.98',
    'huaweicloudsdkcodeartsartifact==3.1.98',
    'huaweicloudsdkcodeartsbuild==3.1.98',
    'huaweicloudsdkcodeartscheck==3.1.98',
    'huaweicloudsdkcodeartsdeploy==3.1.98',
    'huaweicloudsdkcodeartsinspector==3.1.98',
    'huaweicloudsdkcodeartspipeline==3.1.98',
    'huaweicloudsdkcodecraft==3.1.98',
    'huaweicloudsdkcodehub==3.1.98',
    'huaweicloudsdkconfig==3.1.98',
    'huaweicloudsdkcph==3.1.98',
    'huaweicloudsdkcpts==3.1.98',
    'huaweicloudsdkcse==3.1.98',
    'huaweicloudsdkcsms==3.1.98',
    'huaweicloudsdkcss==3.1.98',
    'huaweicloudsdkcts==3.1.98',
    'huaweicloudsdkdas==3.1.98',
    'huaweicloudsdkdataartsstudio==3.1.98',
    'huaweicloudsdkdbss==3.1.98',
    'huaweicloudsdkdc==3.1.98',
    'huaweicloudsdkdcs==3.1.98',
    'huaweicloudsdkddm==3.1.98',
    'huaweicloudsdkdds==3.1.98',
    'huaweicloudsdkdeh==3.1.98',
    'huaweicloudsdkdevsecurity==3.1.98',
    'huaweicloudsdkdevstar==3.1.98',
    'huaweicloudsdkdgc==3.1.98',
    'huaweicloudsdkdis==3.1.98',
    'huaweicloudsdkdlf==3.1.98',
    'huaweicloudsdkdli==3.1.98',
    'huaweicloudsdkdns==3.1.98',
    'huaweicloudsdkdris==3.1.98',
    'huaweicloudsdkdrs==3.1.98',
    'huaweicloudsdkdsc==3.1.98',
    'huaweicloudsdkdwr==3.1.98',
    'huaweicloudsdkdws==3.1.98',
    'huaweicloudsdkec==3.1.98',
    'huaweicloudsdkecs==3.1.98',
    'huaweicloudsdkedgesec==3.1.98',
    'huaweicloudsdkeg==3.1.98',
    'huaweicloudsdkeihealth==3.1.98',
    'huaweicloudsdkeip==3.1.98',
    'huaweicloudsdkelb==3.1.98',
    'huaweicloudsdkeps==3.1.98',
    'huaweicloudsdker==3.1.98',
    'huaweicloudsdkevs==3.1.98',
    'huaweicloudsdkfrs==3.1.98',
    'huaweicloudsdkfunctiongraph==3.1.98',
    'huaweicloudsdkga==3.1.98',
    'huaweicloudsdkgaussdb==3.1.98',
    'huaweicloudsdkgaussdbfornosql==3.1.98',
    'huaweicloudsdkgaussdbforopengauss==3.1.98',
    'huaweicloudsdkgeip==3.1.98',
    'huaweicloudsdkges==3.1.98',
    'huaweicloudsdkgsl==3.1.98',
    'huaweicloudsdkhilens==3.1.98',
    'huaweicloudsdkhss==3.1.98',
    'huaweicloudsdkiam==3.1.98',
    'huaweicloudsdkiamaccessanalyzer==3.1.98',
    'huaweicloudsdkidentitycenter==3.1.98',
    'huaweicloudsdkidentitycenterstore==3.1.98',
    'huaweicloudsdkidme==3.1.98',
    'huaweicloudsdkidmeclassicapi==3.1.98',
    'huaweicloudsdkiec==3.1.98',
    'huaweicloudsdkief==3.1.98',
    'huaweicloudsdkimage==3.1.98',
    'huaweicloudsdkimagesearch==3.1.98',
    'huaweicloudsdkims==3.1.98',
    'huaweicloudsdkiotanalytics==3.1.98',
    'huaweicloudsdkiotda==3.1.98',
    'huaweicloudsdkiotedge==3.1.98',
    'huaweicloudsdkivs==3.1.98',
    'huaweicloudsdkkafka==3.1.98',
    'huaweicloudsdkkms==3.1.98',
    'huaweicloudsdkkoomessage==3.1.98',
    'huaweicloudsdkkps==3.1.98',
    'huaweicloudsdklakeformation==3.1.98',
    'huaweicloudsdklive==3.1.98',
    'huaweicloudsdklts==3.1.98',
    'huaweicloudsdkmapds==3.1.98',
    'huaweicloudsdkmas==3.1.98',
    'huaweicloudsdkmeeting==3.1.98',
    'huaweicloudsdkmetastudio==3.1.98',
    'huaweicloudsdkmoderation==3.1.98',
    'huaweicloudsdkmpc==3.1.98',
    'huaweicloudsdkmrs==3.1.98',
    'huaweicloudsdkmsgsms==3.1.98',
    'huaweicloudsdkmssi==3.1.98',
    'huaweicloudsdknat==3.1.98',
    'huaweicloudsdknlp==3.1.98',
    'huaweicloudsdkobs==3.1.98',
    'huaweicloudsdkocr==3.1.98',
    'huaweicloudsdkoctopus==3.1.98',
    'huaweicloudsdkoms==3.1.98',
    'huaweicloudsdkoptverse==3.1.98',
    'huaweicloudsdkorganizations==3.1.98',
    'huaweicloudsdkorgid==3.1.98',
    'huaweicloudsdkoroas==3.1.98',
    'huaweicloudsdkosm==3.1.98',
    'huaweicloudsdkpangulargemodels==3.1.98',
    'huaweicloudsdkprojectman==3.1.98',
    'huaweicloudsdkrabbitmq==3.1.98',
    'huaweicloudsdkram==3.1.98',
    'huaweicloudsdkrds==3.1.98',
    'huaweicloudsdkres==3.1.98',
    'huaweicloudsdkrgc==3.1.98',
    'huaweicloudsdkrms==3.1.98',
    'huaweicloudsdkrocketmq==3.1.98',
    'huaweicloudsdkroma==3.1.98',
    'huaweicloudsdksa==3.1.98',
    'huaweicloudsdkscm==3.1.98',
    'huaweicloudsdksdrs==3.1.98',
    'huaweicloudsdksecmaster==3.1.98',
    'huaweicloudsdkservicestage==3.1.98',
    'huaweicloudsdksfsturbo==3.1.98',
    'huaweicloudsdksis==3.1.98',
    'huaweicloudsdksmn==3.1.98',
    'huaweicloudsdksms==3.1.98',
    'huaweicloudsdksts==3.1.98',
    'huaweicloudsdkswr==3.1.98',
    'huaweicloudsdktics==3.1.98',
    'huaweicloudsdktms==3.1.98',
    'huaweicloudsdkugo==3.1.98',
    'huaweicloudsdkvas==3.1.98',
    'huaweicloudsdkvcm==3.1.98',
    'huaweicloudsdkvod==3.1.98',
    'huaweicloudsdkvpc==3.1.98',
    'huaweicloudsdkvpcep==3.1.98',
    'huaweicloudsdkvpn==3.1.98',
    'huaweicloudsdkwaf==3.1.98',
    'huaweicloudsdkworkspace==3.1.98',
    'huaweicloudsdkworkspaceapp==3.1.98',
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
