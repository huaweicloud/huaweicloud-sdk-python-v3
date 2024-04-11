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
VERSION = "3.1.91"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.91',
    'huaweicloudsdkaad==3.1.91',
    'huaweicloudsdkantiddos==3.1.91',
    'huaweicloudsdkaom==3.1.91',
    'huaweicloudsdkaos==3.1.91',
    'huaweicloudsdkapig==3.1.91',
    'huaweicloudsdkapm==3.1.91',
    'huaweicloudsdkas==3.1.91',
    'huaweicloudsdkasm==3.1.91',
    'huaweicloudsdkbcs==3.1.91',
    'huaweicloudsdkbms==3.1.91',
    'huaweicloudsdkbss==3.1.91',
    'huaweicloudsdkbssintl==3.1.91',
    'huaweicloudsdkcae==3.1.91',
    'huaweicloudsdkcampusgo==3.1.91',
    'huaweicloudsdkcbh==3.1.91',
    'huaweicloudsdkcbr==3.1.91',
    'huaweicloudsdkcbs==3.1.91',
    'huaweicloudsdkcc==3.1.91',
    'huaweicloudsdkcce==3.1.91',
    'huaweicloudsdkccm==3.1.91',
    'huaweicloudsdkcdm==3.1.91',
    'huaweicloudsdkcdn==3.1.91',
    'huaweicloudsdkces==3.1.91',
    'huaweicloudsdkcfw==3.1.91',
    'huaweicloudsdkcgs==3.1.91',
    'huaweicloudsdkclassroom==3.1.91',
    'huaweicloudsdkcloudide==3.1.91',
    'huaweicloudsdkcloudpond==3.1.91',
    'huaweicloudsdkcloudrtc==3.1.91',
    'huaweicloudsdkcloudtable==3.1.91',
    'huaweicloudsdkcloudtest==3.1.91',
    'huaweicloudsdkcodeartsartifact==3.1.91',
    'huaweicloudsdkcodeartsbuild==3.1.91',
    'huaweicloudsdkcodeartscheck==3.1.91',
    'huaweicloudsdkcodeartsdeploy==3.1.91',
    'huaweicloudsdkcodeartsinspector==3.1.91',
    'huaweicloudsdkcodeartspipeline==3.1.91',
    'huaweicloudsdkcodecraft==3.1.91',
    'huaweicloudsdkcodehub==3.1.91',
    'huaweicloudsdkconfig==3.1.91',
    'huaweicloudsdkcph==3.1.91',
    'huaweicloudsdkcpts==3.1.91',
    'huaweicloudsdkcse==3.1.91',
    'huaweicloudsdkcsms==3.1.91',
    'huaweicloudsdkcss==3.1.91',
    'huaweicloudsdkcts==3.1.91',
    'huaweicloudsdkdas==3.1.91',
    'huaweicloudsdkdataartsstudio==3.1.91',
    'huaweicloudsdkdbss==3.1.91',
    'huaweicloudsdkdc==3.1.91',
    'huaweicloudsdkdcs==3.1.91',
    'huaweicloudsdkddm==3.1.91',
    'huaweicloudsdkdds==3.1.91',
    'huaweicloudsdkdeh==3.1.91',
    'huaweicloudsdkdevsecurity==3.1.91',
    'huaweicloudsdkdevstar==3.1.91',
    'huaweicloudsdkdgc==3.1.91',
    'huaweicloudsdkdis==3.1.91',
    'huaweicloudsdkdlf==3.1.91',
    'huaweicloudsdkdli==3.1.91',
    'huaweicloudsdkdns==3.1.91',
    'huaweicloudsdkdris==3.1.91',
    'huaweicloudsdkdrs==3.1.91',
    'huaweicloudsdkdsc==3.1.91',
    'huaweicloudsdkdwr==3.1.91',
    'huaweicloudsdkdws==3.1.91',
    'huaweicloudsdkec==3.1.91',
    'huaweicloudsdkecs==3.1.91',
    'huaweicloudsdkedgesec==3.1.91',
    'huaweicloudsdkeg==3.1.91',
    'huaweicloudsdkeihealth==3.1.91',
    'huaweicloudsdkeip==3.1.91',
    'huaweicloudsdkelb==3.1.91',
    'huaweicloudsdkeps==3.1.91',
    'huaweicloudsdker==3.1.91',
    'huaweicloudsdkevs==3.1.91',
    'huaweicloudsdkfrs==3.1.91',
    'huaweicloudsdkfunctiongraph==3.1.91',
    'huaweicloudsdkga==3.1.91',
    'huaweicloudsdkgaussdb==3.1.91',
    'huaweicloudsdkgaussdbfornosql==3.1.91',
    'huaweicloudsdkgaussdbforopengauss==3.1.91',
    'huaweicloudsdkgeip==3.1.91',
    'huaweicloudsdkges==3.1.91',
    'huaweicloudsdkgsl==3.1.91',
    'huaweicloudsdkhilens==3.1.91',
    'huaweicloudsdkhss==3.1.91',
    'huaweicloudsdkiam==3.1.91',
    'huaweicloudsdkiamaccessanalyzer==3.1.91',
    'huaweicloudsdkidentitycenter==3.1.91',
    'huaweicloudsdkidentitycenterstore==3.1.91',
    'huaweicloudsdkidme==3.1.91',
    'huaweicloudsdkidmeclassicapi==3.1.91',
    'huaweicloudsdkiec==3.1.91',
    'huaweicloudsdkief==3.1.91',
    'huaweicloudsdkimage==3.1.91',
    'huaweicloudsdkimagesearch==3.1.91',
    'huaweicloudsdkims==3.1.91',
    'huaweicloudsdkiotanalytics==3.1.91',
    'huaweicloudsdkiotda==3.1.91',
    'huaweicloudsdkiotedge==3.1.91',
    'huaweicloudsdkivs==3.1.91',
    'huaweicloudsdkkafka==3.1.91',
    'huaweicloudsdkkms==3.1.91',
    'huaweicloudsdkkoomessage==3.1.91',
    'huaweicloudsdkkps==3.1.91',
    'huaweicloudsdklakeformation==3.1.91',
    'huaweicloudsdklive==3.1.91',
    'huaweicloudsdklts==3.1.91',
    'huaweicloudsdkmapds==3.1.91',
    'huaweicloudsdkmas==3.1.91',
    'huaweicloudsdkmeeting==3.1.91',
    'huaweicloudsdkmetastudio==3.1.91',
    'huaweicloudsdkmoderation==3.1.91',
    'huaweicloudsdkmpc==3.1.91',
    'huaweicloudsdkmrs==3.1.91',
    'huaweicloudsdkmsgsms==3.1.91',
    'huaweicloudsdkmssi==3.1.91',
    'huaweicloudsdknat==3.1.91',
    'huaweicloudsdknlp==3.1.91',
    'huaweicloudsdkobs==3.1.91',
    'huaweicloudsdkocr==3.1.91',
    'huaweicloudsdkoctopus==3.1.91',
    'huaweicloudsdkoms==3.1.91',
    'huaweicloudsdkoptverse==3.1.91',
    'huaweicloudsdkorganizations==3.1.91',
    'huaweicloudsdkorgid==3.1.91',
    'huaweicloudsdkoroas==3.1.91',
    'huaweicloudsdkosm==3.1.91',
    'huaweicloudsdkpangulargemodels==3.1.91',
    'huaweicloudsdkprojectman==3.1.91',
    'huaweicloudsdkrabbitmq==3.1.91',
    'huaweicloudsdkram==3.1.91',
    'huaweicloudsdkrds==3.1.91',
    'huaweicloudsdkres==3.1.91',
    'huaweicloudsdkrgc==3.1.91',
    'huaweicloudsdkrms==3.1.91',
    'huaweicloudsdkrocketmq==3.1.91',
    'huaweicloudsdkroma==3.1.91',
    'huaweicloudsdksa==3.1.91',
    'huaweicloudsdkscm==3.1.91',
    'huaweicloudsdksdrs==3.1.91',
    'huaweicloudsdksecmaster==3.1.91',
    'huaweicloudsdkservicestage==3.1.91',
    'huaweicloudsdksfsturbo==3.1.91',
    'huaweicloudsdksis==3.1.91',
    'huaweicloudsdksmn==3.1.91',
    'huaweicloudsdksms==3.1.91',
    'huaweicloudsdkswr==3.1.91',
    'huaweicloudsdktics==3.1.91',
    'huaweicloudsdktms==3.1.91',
    'huaweicloudsdkugo==3.1.91',
    'huaweicloudsdkvas==3.1.91',
    'huaweicloudsdkvcm==3.1.91',
    'huaweicloudsdkvod==3.1.91',
    'huaweicloudsdkvpc==3.1.91',
    'huaweicloudsdkvpcep==3.1.91',
    'huaweicloudsdkvpn==3.1.91',
    'huaweicloudsdkwaf==3.1.91',
    'huaweicloudsdkworkspace==3.1.91',
    'huaweicloudsdkworkspaceapp==3.1.91',
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
