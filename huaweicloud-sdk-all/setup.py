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
VERSION = "3.1.99"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.99',
    'huaweicloudsdkaad==3.1.99',
    'huaweicloudsdkantiddos==3.1.99',
    'huaweicloudsdkaom==3.1.99',
    'huaweicloudsdkaos==3.1.99',
    'huaweicloudsdkapig==3.1.99',
    'huaweicloudsdkapm==3.1.99',
    'huaweicloudsdkas==3.1.99',
    'huaweicloudsdkasm==3.1.99',
    'huaweicloudsdkbcs==3.1.99',
    'huaweicloudsdkbms==3.1.99',
    'huaweicloudsdkbss==3.1.99',
    'huaweicloudsdkbssintl==3.1.99',
    'huaweicloudsdkcae==3.1.99',
    'huaweicloudsdkcampusgo==3.1.99',
    'huaweicloudsdkcbh==3.1.99',
    'huaweicloudsdkcbr==3.1.99',
    'huaweicloudsdkcbs==3.1.99',
    'huaweicloudsdkcc==3.1.99',
    'huaweicloudsdkcce==3.1.99',
    'huaweicloudsdkccm==3.1.99',
    'huaweicloudsdkcdm==3.1.99',
    'huaweicloudsdkcdn==3.1.99',
    'huaweicloudsdkces==3.1.99',
    'huaweicloudsdkcfw==3.1.99',
    'huaweicloudsdkcgs==3.1.99',
    'huaweicloudsdkclassroom==3.1.99',
    'huaweicloudsdkcloudide==3.1.99',
    'huaweicloudsdkcloudpond==3.1.99',
    'huaweicloudsdkcloudrtc==3.1.99',
    'huaweicloudsdkcloudtable==3.1.99',
    'huaweicloudsdkcloudtest==3.1.99',
    'huaweicloudsdkcodeartsartifact==3.1.99',
    'huaweicloudsdkcodeartsbuild==3.1.99',
    'huaweicloudsdkcodeartscheck==3.1.99',
    'huaweicloudsdkcodeartsdeploy==3.1.99',
    'huaweicloudsdkcodeartsinspector==3.1.99',
    'huaweicloudsdkcodeartspipeline==3.1.99',
    'huaweicloudsdkcodecraft==3.1.99',
    'huaweicloudsdkcodehub==3.1.99',
    'huaweicloudsdkconfig==3.1.99',
    'huaweicloudsdkcph==3.1.99',
    'huaweicloudsdkcpts==3.1.99',
    'huaweicloudsdkcse==3.1.99',
    'huaweicloudsdkcsms==3.1.99',
    'huaweicloudsdkcss==3.1.99',
    'huaweicloudsdkcts==3.1.99',
    'huaweicloudsdkdas==3.1.99',
    'huaweicloudsdkdataartsstudio==3.1.99',
    'huaweicloudsdkdbss==3.1.99',
    'huaweicloudsdkdc==3.1.99',
    'huaweicloudsdkdcs==3.1.99',
    'huaweicloudsdkddm==3.1.99',
    'huaweicloudsdkdds==3.1.99',
    'huaweicloudsdkdeh==3.1.99',
    'huaweicloudsdkdevsecurity==3.1.99',
    'huaweicloudsdkdevstar==3.1.99',
    'huaweicloudsdkdgc==3.1.99',
    'huaweicloudsdkdis==3.1.99',
    'huaweicloudsdkdlf==3.1.99',
    'huaweicloudsdkdli==3.1.99',
    'huaweicloudsdkdns==3.1.99',
    'huaweicloudsdkdris==3.1.99',
    'huaweicloudsdkdrs==3.1.99',
    'huaweicloudsdkdsc==3.1.99',
    'huaweicloudsdkdwr==3.1.99',
    'huaweicloudsdkdws==3.1.99',
    'huaweicloudsdkec==3.1.99',
    'huaweicloudsdkecs==3.1.99',
    'huaweicloudsdkedgesec==3.1.99',
    'huaweicloudsdkeg==3.1.99',
    'huaweicloudsdkeihealth==3.1.99',
    'huaweicloudsdkeip==3.1.99',
    'huaweicloudsdkelb==3.1.99',
    'huaweicloudsdkeps==3.1.99',
    'huaweicloudsdker==3.1.99',
    'huaweicloudsdkevs==3.1.99',
    'huaweicloudsdkfrs==3.1.99',
    'huaweicloudsdkfunctiongraph==3.1.99',
    'huaweicloudsdkga==3.1.99',
    'huaweicloudsdkgaussdb==3.1.99',
    'huaweicloudsdkgaussdbfornosql==3.1.99',
    'huaweicloudsdkgaussdbforopengauss==3.1.99',
    'huaweicloudsdkgeip==3.1.99',
    'huaweicloudsdkges==3.1.99',
    'huaweicloudsdkgsl==3.1.99',
    'huaweicloudsdkhilens==3.1.99',
    'huaweicloudsdkhss==3.1.99',
    'huaweicloudsdkiam==3.1.99',
    'huaweicloudsdkiamaccessanalyzer==3.1.99',
    'huaweicloudsdkidentitycenter==3.1.99',
    'huaweicloudsdkidentitycenterstore==3.1.99',
    'huaweicloudsdkidme==3.1.99',
    'huaweicloudsdkidmeclassicapi==3.1.99',
    'huaweicloudsdkiec==3.1.99',
    'huaweicloudsdkief==3.1.99',
    'huaweicloudsdkimage==3.1.99',
    'huaweicloudsdkimagesearch==3.1.99',
    'huaweicloudsdkims==3.1.99',
    'huaweicloudsdkiotanalytics==3.1.99',
    'huaweicloudsdkiotda==3.1.99',
    'huaweicloudsdkiotedge==3.1.99',
    'huaweicloudsdkivs==3.1.99',
    'huaweicloudsdkkafka==3.1.99',
    'huaweicloudsdkkms==3.1.99',
    'huaweicloudsdkkoomessage==3.1.99',
    'huaweicloudsdkkps==3.1.99',
    'huaweicloudsdklakeformation==3.1.99',
    'huaweicloudsdklive==3.1.99',
    'huaweicloudsdklts==3.1.99',
    'huaweicloudsdkmapds==3.1.99',
    'huaweicloudsdkmas==3.1.99',
    'huaweicloudsdkmeeting==3.1.99',
    'huaweicloudsdkmetastudio==3.1.99',
    'huaweicloudsdkmoderation==3.1.99',
    'huaweicloudsdkmpc==3.1.99',
    'huaweicloudsdkmrs==3.1.99',
    'huaweicloudsdkmsgsms==3.1.99',
    'huaweicloudsdkmssi==3.1.99',
    'huaweicloudsdknat==3.1.99',
    'huaweicloudsdknlp==3.1.99',
    'huaweicloudsdkobs==3.1.99',
    'huaweicloudsdkocr==3.1.99',
    'huaweicloudsdkoctopus==3.1.99',
    'huaweicloudsdkoms==3.1.99',
    'huaweicloudsdkoptverse==3.1.99',
    'huaweicloudsdkorganizations==3.1.99',
    'huaweicloudsdkorgid==3.1.99',
    'huaweicloudsdkoroas==3.1.99',
    'huaweicloudsdkosm==3.1.99',
    'huaweicloudsdkpangulargemodels==3.1.99',
    'huaweicloudsdkprojectman==3.1.99',
    'huaweicloudsdkrabbitmq==3.1.99',
    'huaweicloudsdkram==3.1.99',
    'huaweicloudsdkrds==3.1.99',
    'huaweicloudsdkres==3.1.99',
    'huaweicloudsdkrgc==3.1.99',
    'huaweicloudsdkrms==3.1.99',
    'huaweicloudsdkrocketmq==3.1.99',
    'huaweicloudsdkroma==3.1.99',
    'huaweicloudsdksa==3.1.99',
    'huaweicloudsdkscm==3.1.99',
    'huaweicloudsdksdrs==3.1.99',
    'huaweicloudsdksecmaster==3.1.99',
    'huaweicloudsdkservicestage==3.1.99',
    'huaweicloudsdksfsturbo==3.1.99',
    'huaweicloudsdksis==3.1.99',
    'huaweicloudsdksmn==3.1.99',
    'huaweicloudsdksms==3.1.99',
    'huaweicloudsdksts==3.1.99',
    'huaweicloudsdkswr==3.1.99',
    'huaweicloudsdktics==3.1.99',
    'huaweicloudsdktms==3.1.99',
    'huaweicloudsdkugo==3.1.99',
    'huaweicloudsdkvas==3.1.99',
    'huaweicloudsdkvcm==3.1.99',
    'huaweicloudsdkvod==3.1.99',
    'huaweicloudsdkvpc==3.1.99',
    'huaweicloudsdkvpcep==3.1.99',
    'huaweicloudsdkvpn==3.1.99',
    'huaweicloudsdkwaf==3.1.99',
    'huaweicloudsdkworkspace==3.1.99',
    'huaweicloudsdkworkspaceapp==3.1.99',
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
