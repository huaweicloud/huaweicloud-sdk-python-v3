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
VERSION = "3.1.117"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.117',
    'huaweicloudsdkaad==3.1.117',
    'huaweicloudsdkantiddos==3.1.117',
    'huaweicloudsdkaom==3.1.117',
    'huaweicloudsdkaos==3.1.117',
    'huaweicloudsdkapig==3.1.117',
    'huaweicloudsdkapm==3.1.117',
    'huaweicloudsdkas==3.1.117',
    'huaweicloudsdkasm==3.1.117',
    'huaweicloudsdkbcs==3.1.117',
    'huaweicloudsdkbms==3.1.117',
    'huaweicloudsdkbss==3.1.117',
    'huaweicloudsdkbssintl==3.1.117',
    'huaweicloudsdkcae==3.1.117',
    'huaweicloudsdkcampusgo==3.1.117',
    'huaweicloudsdkcbh==3.1.117',
    'huaweicloudsdkcbr==3.1.117',
    'huaweicloudsdkcbs==3.1.117',
    'huaweicloudsdkcc==3.1.117',
    'huaweicloudsdkcce==3.1.117',
    'huaweicloudsdkccm==3.1.117',
    'huaweicloudsdkcdm==3.1.117',
    'huaweicloudsdkcdn==3.1.117',
    'huaweicloudsdkces==3.1.117',
    'huaweicloudsdkcfw==3.1.117',
    'huaweicloudsdkcgs==3.1.117',
    'huaweicloudsdkclassroom==3.1.117',
    'huaweicloudsdkcloudide==3.1.117',
    'huaweicloudsdkcloudpond==3.1.117',
    'huaweicloudsdkcloudrtc==3.1.117',
    'huaweicloudsdkcloudtable==3.1.117',
    'huaweicloudsdkcloudtest==3.1.117',
    'huaweicloudsdkcoc==3.1.117',
    'huaweicloudsdkcodeartsartifact==3.1.117',
    'huaweicloudsdkcodeartsbuild==3.1.117',
    'huaweicloudsdkcodeartscheck==3.1.117',
    'huaweicloudsdkcodeartsdeploy==3.1.117',
    'huaweicloudsdkcodeartsgovernance==3.1.117',
    'huaweicloudsdkcodeartsinspector==3.1.117',
    'huaweicloudsdkcodeartspipeline==3.1.117',
    'huaweicloudsdkcodecraft==3.1.117',
    'huaweicloudsdkcodehub==3.1.117',
    'huaweicloudsdkconfig==3.1.117',
    'huaweicloudsdkcph==3.1.117',
    'huaweicloudsdkcpts==3.1.117',
    'huaweicloudsdkcse==3.1.117',
    'huaweicloudsdkcsms==3.1.117',
    'huaweicloudsdkcss==3.1.117',
    'huaweicloudsdkcts==3.1.117',
    'huaweicloudsdkdas==3.1.117',
    'huaweicloudsdkdataartsstudio==3.1.117',
    'huaweicloudsdkdbss==3.1.117',
    'huaweicloudsdkdc==3.1.117',
    'huaweicloudsdkdcs==3.1.117',
    'huaweicloudsdkddm==3.1.117',
    'huaweicloudsdkdds==3.1.117',
    'huaweicloudsdkdeh==3.1.117',
    'huaweicloudsdkdevstar==3.1.117',
    'huaweicloudsdkdgc==3.1.117',
    'huaweicloudsdkdis==3.1.117',
    'huaweicloudsdkdlf==3.1.117',
    'huaweicloudsdkdli==3.1.117',
    'huaweicloudsdkdns==3.1.117',
    'huaweicloudsdkdris==3.1.117',
    'huaweicloudsdkdrs==3.1.117',
    'huaweicloudsdkdsc==3.1.117',
    'huaweicloudsdkdwr==3.1.117',
    'huaweicloudsdkdws==3.1.117',
    'huaweicloudsdkec==3.1.117',
    'huaweicloudsdkecs==3.1.117',
    'huaweicloudsdkedgesec==3.1.117',
    'huaweicloudsdkeg==3.1.117',
    'huaweicloudsdkeihealth==3.1.117',
    'huaweicloudsdkeip==3.1.117',
    'huaweicloudsdkelb==3.1.117',
    'huaweicloudsdkeps==3.1.117',
    'huaweicloudsdker==3.1.117',
    'huaweicloudsdkevs==3.1.117',
    'huaweicloudsdkfrs==3.1.117',
    'huaweicloudsdkfunctiongraph==3.1.117',
    'huaweicloudsdkga==3.1.117',
    'huaweicloudsdkgaussdb==3.1.117',
    'huaweicloudsdkgaussdbfornosql==3.1.117',
    'huaweicloudsdkgaussdbforopengauss==3.1.117',
    'huaweicloudsdkgeip==3.1.117',
    'huaweicloudsdkges==3.1.117',
    'huaweicloudsdkgsl==3.1.117',
    'huaweicloudsdkhilens==3.1.117',
    'huaweicloudsdkhss==3.1.117',
    'huaweicloudsdkiam==3.1.117',
    'huaweicloudsdkiamaccessanalyzer==3.1.117',
    'huaweicloudsdkidentitycenter==3.1.117',
    'huaweicloudsdkidentitycenterstore==3.1.117',
    'huaweicloudsdkidme==3.1.117',
    'huaweicloudsdkidmeclassicapi==3.1.117',
    'huaweicloudsdkiec==3.1.117',
    'huaweicloudsdkief==3.1.117',
    'huaweicloudsdkimage==3.1.117',
    'huaweicloudsdkimagesearch==3.1.117',
    'huaweicloudsdkims==3.1.117',
    'huaweicloudsdkiotanalytics==3.1.117',
    'huaweicloudsdkiotda==3.1.117',
    'huaweicloudsdkiotdm==3.1.117',
    'huaweicloudsdkiotedge==3.1.117',
    'huaweicloudsdkivs==3.1.117',
    'huaweicloudsdkkafka==3.1.117',
    'huaweicloudsdkkms==3.1.117',
    'huaweicloudsdkkoomessage==3.1.117',
    'huaweicloudsdkkps==3.1.117',
    'huaweicloudsdklakeformation==3.1.117',
    'huaweicloudsdklive==3.1.117',
    'huaweicloudsdklts==3.1.117',
    'huaweicloudsdkmapds==3.1.117',
    'huaweicloudsdkmas==3.1.117',
    'huaweicloudsdkmeeting==3.1.117',
    'huaweicloudsdkmetastudio==3.1.117',
    'huaweicloudsdkmoderation==3.1.117',
    'huaweicloudsdkmpc==3.1.117',
    'huaweicloudsdkmrs==3.1.117',
    'huaweicloudsdkmsgsms==3.1.117',
    'huaweicloudsdkmssi==3.1.117',
    'huaweicloudsdknat==3.1.117',
    'huaweicloudsdknlp==3.1.117',
    'huaweicloudsdkobs==3.1.117',
    'huaweicloudsdkocr==3.1.117',
    'huaweicloudsdkoctopus==3.1.117',
    'huaweicloudsdkoms==3.1.117',
    'huaweicloudsdkoptverse==3.1.117',
    'huaweicloudsdkorganizations==3.1.117',
    'huaweicloudsdkorgid==3.1.117',
    'huaweicloudsdkoroas==3.1.117',
    'huaweicloudsdkosm==3.1.117',
    'huaweicloudsdkpangulargemodels==3.1.117',
    'huaweicloudsdkprojectman==3.1.117',
    'huaweicloudsdkrabbitmq==3.1.117',
    'huaweicloudsdkram==3.1.117',
    'huaweicloudsdkrds==3.1.117',
    'huaweicloudsdkres==3.1.117',
    'huaweicloudsdkrgc==3.1.117',
    'huaweicloudsdkrms==3.1.117',
    'huaweicloudsdkrocketmq==3.1.117',
    'huaweicloudsdkroma==3.1.117',
    'huaweicloudsdksa==3.1.117',
    'huaweicloudsdkscm==3.1.117',
    'huaweicloudsdksdrs==3.1.117',
    'huaweicloudsdksecmaster==3.1.117',
    'huaweicloudsdkservicestage==3.1.117',
    'huaweicloudsdksfsturbo==3.1.117',
    'huaweicloudsdksis==3.1.117',
    'huaweicloudsdksmn==3.1.117',
    'huaweicloudsdksms==3.1.117',
    'huaweicloudsdksts==3.1.117',
    'huaweicloudsdkswr==3.1.117',
    'huaweicloudsdktics==3.1.117',
    'huaweicloudsdktms==3.1.117',
    'huaweicloudsdkugo==3.1.117',
    'huaweicloudsdkvas==3.1.117',
    'huaweicloudsdkvcm==3.1.117',
    'huaweicloudsdkvod==3.1.117',
    'huaweicloudsdkvpc==3.1.117',
    'huaweicloudsdkvpcep==3.1.117',
    'huaweicloudsdkvpn==3.1.117',
    'huaweicloudsdkwaf==3.1.117',
    'huaweicloudsdkworkspace==3.1.117',
    'huaweicloudsdkworkspaceapp==3.1.117',
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
