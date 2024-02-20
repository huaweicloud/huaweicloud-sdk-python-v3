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
VERSION = "3.1.82"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.82',
    'huaweicloudsdkaad==3.1.82',
    'huaweicloudsdkantiddos==3.1.82',
    'huaweicloudsdkaom==3.1.82',
    'huaweicloudsdkaos==3.1.82',
    'huaweicloudsdkapig==3.1.82',
    'huaweicloudsdkapm==3.1.82',
    'huaweicloudsdkas==3.1.82',
    'huaweicloudsdkasm==3.1.82',
    'huaweicloudsdkbcs==3.1.82',
    'huaweicloudsdkbms==3.1.82',
    'huaweicloudsdkbss==3.1.82',
    'huaweicloudsdkbssintl==3.1.82',
    'huaweicloudsdkcae==3.1.82',
    'huaweicloudsdkcampusgo==3.1.82',
    'huaweicloudsdkcbh==3.1.82',
    'huaweicloudsdkcbr==3.1.82',
    'huaweicloudsdkcbs==3.1.82',
    'huaweicloudsdkcc==3.1.82',
    'huaweicloudsdkcce==3.1.82',
    'huaweicloudsdkccm==3.1.82',
    'huaweicloudsdkcdm==3.1.82',
    'huaweicloudsdkcdn==3.1.82',
    'huaweicloudsdkces==3.1.82',
    'huaweicloudsdkcfw==3.1.82',
    'huaweicloudsdkcgs==3.1.82',
    'huaweicloudsdkclassroom==3.1.82',
    'huaweicloudsdkcloudide==3.1.82',
    'huaweicloudsdkcloudpond==3.1.82',
    'huaweicloudsdkcloudrtc==3.1.82',
    'huaweicloudsdkcloudtable==3.1.82',
    'huaweicloudsdkcloudtest==3.1.82',
    'huaweicloudsdkcodeartsartifact==3.1.82',
    'huaweicloudsdkcodeartsbuild==3.1.82',
    'huaweicloudsdkcodeartscheck==3.1.82',
    'huaweicloudsdkcodeartsdeploy==3.1.82',
    'huaweicloudsdkcodeartsinspector==3.1.82',
    'huaweicloudsdkcodeartspipeline==3.1.82',
    'huaweicloudsdkcodecraft==3.1.82',
    'huaweicloudsdkcodehub==3.1.82',
    'huaweicloudsdkconfig==3.1.82',
    'huaweicloudsdkcph==3.1.82',
    'huaweicloudsdkcpts==3.1.82',
    'huaweicloudsdkcse==3.1.82',
    'huaweicloudsdkcsms==3.1.82',
    'huaweicloudsdkcss==3.1.82',
    'huaweicloudsdkcts==3.1.82',
    'huaweicloudsdkdas==3.1.82',
    'huaweicloudsdkdataartsstudio==3.1.82',
    'huaweicloudsdkdbss==3.1.82',
    'huaweicloudsdkdc==3.1.82',
    'huaweicloudsdkdcs==3.1.82',
    'huaweicloudsdkddm==3.1.82',
    'huaweicloudsdkdds==3.1.82',
    'huaweicloudsdkdeh==3.1.82',
    'huaweicloudsdkdevsecurity==3.1.82',
    'huaweicloudsdkdevstar==3.1.82',
    'huaweicloudsdkdgc==3.1.82',
    'huaweicloudsdkdis==3.1.82',
    'huaweicloudsdkdlf==3.1.82',
    'huaweicloudsdkdli==3.1.82',
    'huaweicloudsdkdns==3.1.82',
    'huaweicloudsdkdris==3.1.82',
    'huaweicloudsdkdrs==3.1.82',
    'huaweicloudsdkdsc==3.1.82',
    'huaweicloudsdkdwr==3.1.82',
    'huaweicloudsdkdws==3.1.82',
    'huaweicloudsdkec==3.1.82',
    'huaweicloudsdkecs==3.1.82',
    'huaweicloudsdkedgesec==3.1.82',
    'huaweicloudsdkeg==3.1.82',
    'huaweicloudsdkeihealth==3.1.82',
    'huaweicloudsdkeip==3.1.82',
    'huaweicloudsdkelb==3.1.82',
    'huaweicloudsdkeps==3.1.82',
    'huaweicloudsdker==3.1.82',
    'huaweicloudsdkevs==3.1.82',
    'huaweicloudsdkfrs==3.1.82',
    'huaweicloudsdkfunctiongraph==3.1.82',
    'huaweicloudsdkga==3.1.82',
    'huaweicloudsdkgaussdb==3.1.82',
    'huaweicloudsdkgaussdbfornosql==3.1.82',
    'huaweicloudsdkgaussdbforopengauss==3.1.82',
    'huaweicloudsdkgeip==3.1.82',
    'huaweicloudsdkges==3.1.82',
    'huaweicloudsdkgsl==3.1.82',
    'huaweicloudsdkhilens==3.1.82',
    'huaweicloudsdkhss==3.1.82',
    'huaweicloudsdkiam==3.1.82',
    'huaweicloudsdkiamaccessanalyzer==3.1.82',
    'huaweicloudsdkidentitycenter==3.1.82',
    'huaweicloudsdkidentitycenterstore==3.1.82',
    'huaweicloudsdkidme==3.1.82',
    'huaweicloudsdkidmeclassicapi==3.1.82',
    'huaweicloudsdkiec==3.1.82',
    'huaweicloudsdkief==3.1.82',
    'huaweicloudsdkimage==3.1.82',
    'huaweicloudsdkimagesearch==3.1.82',
    'huaweicloudsdkims==3.1.82',
    'huaweicloudsdkiotanalytics==3.1.82',
    'huaweicloudsdkiotda==3.1.82',
    'huaweicloudsdkiotedge==3.1.82',
    'huaweicloudsdkivs==3.1.82',
    'huaweicloudsdkkafka==3.1.82',
    'huaweicloudsdkkms==3.1.82',
    'huaweicloudsdkkoomessage==3.1.82',
    'huaweicloudsdkkps==3.1.82',
    'huaweicloudsdklakeformation==3.1.82',
    'huaweicloudsdklive==3.1.82',
    'huaweicloudsdklts==3.1.82',
    'huaweicloudsdkmapds==3.1.82',
    'huaweicloudsdkmas==3.1.82',
    'huaweicloudsdkmeeting==3.1.82',
    'huaweicloudsdkmetastudio==3.1.82',
    'huaweicloudsdkmoderation==3.1.82',
    'huaweicloudsdkmpc==3.1.82',
    'huaweicloudsdkmrs==3.1.82',
    'huaweicloudsdkmsgsms==3.1.82',
    'huaweicloudsdkmssi==3.1.82',
    'huaweicloudsdknat==3.1.82',
    'huaweicloudsdknlp==3.1.82',
    'huaweicloudsdkobs==3.1.82',
    'huaweicloudsdkocr==3.1.82',
    'huaweicloudsdkoctopus==3.1.82',
    'huaweicloudsdkoms==3.1.82',
    'huaweicloudsdkoptverse==3.1.82',
    'huaweicloudsdkorganizations==3.1.82',
    'huaweicloudsdkorgid==3.1.82',
    'huaweicloudsdkoroas==3.1.82',
    'huaweicloudsdkosm==3.1.82',
    'huaweicloudsdkpangulargemodels==3.1.82',
    'huaweicloudsdkprojectman==3.1.82',
    'huaweicloudsdkrabbitmq==3.1.82',
    'huaweicloudsdkram==3.1.82',
    'huaweicloudsdkrds==3.1.82',
    'huaweicloudsdkres==3.1.82',
    'huaweicloudsdkrgc==3.1.82',
    'huaweicloudsdkrms==3.1.82',
    'huaweicloudsdkrocketmq==3.1.82',
    'huaweicloudsdkroma==3.1.82',
    'huaweicloudsdksa==3.1.82',
    'huaweicloudsdkscm==3.1.82',
    'huaweicloudsdksdrs==3.1.82',
    'huaweicloudsdksecmaster==3.1.82',
    'huaweicloudsdkservicestage==3.1.82',
    'huaweicloudsdksfsturbo==3.1.82',
    'huaweicloudsdksis==3.1.82',
    'huaweicloudsdksmn==3.1.82',
    'huaweicloudsdksms==3.1.82',
    'huaweicloudsdkswr==3.1.82',
    'huaweicloudsdktics==3.1.82',
    'huaweicloudsdktms==3.1.82',
    'huaweicloudsdkugo==3.1.82',
    'huaweicloudsdkvas==3.1.82',
    'huaweicloudsdkvcm==3.1.82',
    'huaweicloudsdkvod==3.1.82',
    'huaweicloudsdkvpc==3.1.82',
    'huaweicloudsdkvpcep==3.1.82',
    'huaweicloudsdkvpn==3.1.82',
    'huaweicloudsdkwaf==3.1.82',
    'huaweicloudsdkworkspace==3.1.82',
    'huaweicloudsdkworkspaceapp==3.1.82',
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
