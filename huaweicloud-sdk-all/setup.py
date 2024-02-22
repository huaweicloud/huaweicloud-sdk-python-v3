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
VERSION = "3.1.83"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.83',
    'huaweicloudsdkaad==3.1.83',
    'huaweicloudsdkantiddos==3.1.83',
    'huaweicloudsdkaom==3.1.83',
    'huaweicloudsdkaos==3.1.83',
    'huaweicloudsdkapig==3.1.83',
    'huaweicloudsdkapm==3.1.83',
    'huaweicloudsdkas==3.1.83',
    'huaweicloudsdkasm==3.1.83',
    'huaweicloudsdkbcs==3.1.83',
    'huaweicloudsdkbms==3.1.83',
    'huaweicloudsdkbss==3.1.83',
    'huaweicloudsdkbssintl==3.1.83',
    'huaweicloudsdkcae==3.1.83',
    'huaweicloudsdkcampusgo==3.1.83',
    'huaweicloudsdkcbh==3.1.83',
    'huaweicloudsdkcbr==3.1.83',
    'huaweicloudsdkcbs==3.1.83',
    'huaweicloudsdkcc==3.1.83',
    'huaweicloudsdkcce==3.1.83',
    'huaweicloudsdkccm==3.1.83',
    'huaweicloudsdkcdm==3.1.83',
    'huaweicloudsdkcdn==3.1.83',
    'huaweicloudsdkces==3.1.83',
    'huaweicloudsdkcfw==3.1.83',
    'huaweicloudsdkcgs==3.1.83',
    'huaweicloudsdkclassroom==3.1.83',
    'huaweicloudsdkcloudide==3.1.83',
    'huaweicloudsdkcloudpond==3.1.83',
    'huaweicloudsdkcloudrtc==3.1.83',
    'huaweicloudsdkcloudtable==3.1.83',
    'huaweicloudsdkcloudtest==3.1.83',
    'huaweicloudsdkcodeartsartifact==3.1.83',
    'huaweicloudsdkcodeartsbuild==3.1.83',
    'huaweicloudsdkcodeartscheck==3.1.83',
    'huaweicloudsdkcodeartsdeploy==3.1.83',
    'huaweicloudsdkcodeartsinspector==3.1.83',
    'huaweicloudsdkcodeartspipeline==3.1.83',
    'huaweicloudsdkcodecraft==3.1.83',
    'huaweicloudsdkcodehub==3.1.83',
    'huaweicloudsdkconfig==3.1.83',
    'huaweicloudsdkcph==3.1.83',
    'huaweicloudsdkcpts==3.1.83',
    'huaweicloudsdkcse==3.1.83',
    'huaweicloudsdkcsms==3.1.83',
    'huaweicloudsdkcss==3.1.83',
    'huaweicloudsdkcts==3.1.83',
    'huaweicloudsdkdas==3.1.83',
    'huaweicloudsdkdataartsstudio==3.1.83',
    'huaweicloudsdkdbss==3.1.83',
    'huaweicloudsdkdc==3.1.83',
    'huaweicloudsdkdcs==3.1.83',
    'huaweicloudsdkddm==3.1.83',
    'huaweicloudsdkdds==3.1.83',
    'huaweicloudsdkdeh==3.1.83',
    'huaweicloudsdkdevsecurity==3.1.83',
    'huaweicloudsdkdevstar==3.1.83',
    'huaweicloudsdkdgc==3.1.83',
    'huaweicloudsdkdis==3.1.83',
    'huaweicloudsdkdlf==3.1.83',
    'huaweicloudsdkdli==3.1.83',
    'huaweicloudsdkdns==3.1.83',
    'huaweicloudsdkdris==3.1.83',
    'huaweicloudsdkdrs==3.1.83',
    'huaweicloudsdkdsc==3.1.83',
    'huaweicloudsdkdwr==3.1.83',
    'huaweicloudsdkdws==3.1.83',
    'huaweicloudsdkec==3.1.83',
    'huaweicloudsdkecs==3.1.83',
    'huaweicloudsdkedgesec==3.1.83',
    'huaweicloudsdkeg==3.1.83',
    'huaweicloudsdkeihealth==3.1.83',
    'huaweicloudsdkeip==3.1.83',
    'huaweicloudsdkelb==3.1.83',
    'huaweicloudsdkeps==3.1.83',
    'huaweicloudsdker==3.1.83',
    'huaweicloudsdkevs==3.1.83',
    'huaweicloudsdkfrs==3.1.83',
    'huaweicloudsdkfunctiongraph==3.1.83',
    'huaweicloudsdkga==3.1.83',
    'huaweicloudsdkgaussdb==3.1.83',
    'huaweicloudsdkgaussdbfornosql==3.1.83',
    'huaweicloudsdkgaussdbforopengauss==3.1.83',
    'huaweicloudsdkgeip==3.1.83',
    'huaweicloudsdkges==3.1.83',
    'huaweicloudsdkgsl==3.1.83',
    'huaweicloudsdkhilens==3.1.83',
    'huaweicloudsdkhss==3.1.83',
    'huaweicloudsdkiam==3.1.83',
    'huaweicloudsdkiamaccessanalyzer==3.1.83',
    'huaweicloudsdkidentitycenter==3.1.83',
    'huaweicloudsdkidentitycenterstore==3.1.83',
    'huaweicloudsdkidme==3.1.83',
    'huaweicloudsdkidmeclassicapi==3.1.83',
    'huaweicloudsdkiec==3.1.83',
    'huaweicloudsdkief==3.1.83',
    'huaweicloudsdkimage==3.1.83',
    'huaweicloudsdkimagesearch==3.1.83',
    'huaweicloudsdkims==3.1.83',
    'huaweicloudsdkiotanalytics==3.1.83',
    'huaweicloudsdkiotda==3.1.83',
    'huaweicloudsdkiotedge==3.1.83',
    'huaweicloudsdkivs==3.1.83',
    'huaweicloudsdkkafka==3.1.83',
    'huaweicloudsdkkms==3.1.83',
    'huaweicloudsdkkoomessage==3.1.83',
    'huaweicloudsdkkps==3.1.83',
    'huaweicloudsdklakeformation==3.1.83',
    'huaweicloudsdklive==3.1.83',
    'huaweicloudsdklts==3.1.83',
    'huaweicloudsdkmapds==3.1.83',
    'huaweicloudsdkmas==3.1.83',
    'huaweicloudsdkmeeting==3.1.83',
    'huaweicloudsdkmetastudio==3.1.83',
    'huaweicloudsdkmoderation==3.1.83',
    'huaweicloudsdkmpc==3.1.83',
    'huaweicloudsdkmrs==3.1.83',
    'huaweicloudsdkmsgsms==3.1.83',
    'huaweicloudsdkmssi==3.1.83',
    'huaweicloudsdknat==3.1.83',
    'huaweicloudsdknlp==3.1.83',
    'huaweicloudsdkobs==3.1.83',
    'huaweicloudsdkocr==3.1.83',
    'huaweicloudsdkoctopus==3.1.83',
    'huaweicloudsdkoms==3.1.83',
    'huaweicloudsdkoptverse==3.1.83',
    'huaweicloudsdkorganizations==3.1.83',
    'huaweicloudsdkorgid==3.1.83',
    'huaweicloudsdkoroas==3.1.83',
    'huaweicloudsdkosm==3.1.83',
    'huaweicloudsdkpangulargemodels==3.1.83',
    'huaweicloudsdkprojectman==3.1.83',
    'huaweicloudsdkrabbitmq==3.1.83',
    'huaweicloudsdkram==3.1.83',
    'huaweicloudsdkrds==3.1.83',
    'huaweicloudsdkres==3.1.83',
    'huaweicloudsdkrgc==3.1.83',
    'huaweicloudsdkrms==3.1.83',
    'huaweicloudsdkrocketmq==3.1.83',
    'huaweicloudsdkroma==3.1.83',
    'huaweicloudsdksa==3.1.83',
    'huaweicloudsdkscm==3.1.83',
    'huaweicloudsdksdrs==3.1.83',
    'huaweicloudsdksecmaster==3.1.83',
    'huaweicloudsdkservicestage==3.1.83',
    'huaweicloudsdksfsturbo==3.1.83',
    'huaweicloudsdksis==3.1.83',
    'huaweicloudsdksmn==3.1.83',
    'huaweicloudsdksms==3.1.83',
    'huaweicloudsdkswr==3.1.83',
    'huaweicloudsdktics==3.1.83',
    'huaweicloudsdktms==3.1.83',
    'huaweicloudsdkugo==3.1.83',
    'huaweicloudsdkvas==3.1.83',
    'huaweicloudsdkvcm==3.1.83',
    'huaweicloudsdkvod==3.1.83',
    'huaweicloudsdkvpc==3.1.83',
    'huaweicloudsdkvpcep==3.1.83',
    'huaweicloudsdkvpn==3.1.83',
    'huaweicloudsdkwaf==3.1.83',
    'huaweicloudsdkworkspace==3.1.83',
    'huaweicloudsdkworkspaceapp==3.1.83',
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
