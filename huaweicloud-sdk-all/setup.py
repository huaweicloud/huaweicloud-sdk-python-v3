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
VERSION = "3.1.97"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.97',
    'huaweicloudsdkaad==3.1.97',
    'huaweicloudsdkantiddos==3.1.97',
    'huaweicloudsdkaom==3.1.97',
    'huaweicloudsdkaos==3.1.97',
    'huaweicloudsdkapig==3.1.97',
    'huaweicloudsdkapm==3.1.97',
    'huaweicloudsdkas==3.1.97',
    'huaweicloudsdkasm==3.1.97',
    'huaweicloudsdkbcs==3.1.97',
    'huaweicloudsdkbms==3.1.97',
    'huaweicloudsdkbss==3.1.97',
    'huaweicloudsdkbssintl==3.1.97',
    'huaweicloudsdkcae==3.1.97',
    'huaweicloudsdkcampusgo==3.1.97',
    'huaweicloudsdkcbh==3.1.97',
    'huaweicloudsdkcbr==3.1.97',
    'huaweicloudsdkcbs==3.1.97',
    'huaweicloudsdkcc==3.1.97',
    'huaweicloudsdkcce==3.1.97',
    'huaweicloudsdkccm==3.1.97',
    'huaweicloudsdkcdm==3.1.97',
    'huaweicloudsdkcdn==3.1.97',
    'huaweicloudsdkces==3.1.97',
    'huaweicloudsdkcfw==3.1.97',
    'huaweicloudsdkcgs==3.1.97',
    'huaweicloudsdkclassroom==3.1.97',
    'huaweicloudsdkcloudide==3.1.97',
    'huaweicloudsdkcloudpond==3.1.97',
    'huaweicloudsdkcloudrtc==3.1.97',
    'huaweicloudsdkcloudtable==3.1.97',
    'huaweicloudsdkcloudtest==3.1.97',
    'huaweicloudsdkcodeartsartifact==3.1.97',
    'huaweicloudsdkcodeartsbuild==3.1.97',
    'huaweicloudsdkcodeartscheck==3.1.97',
    'huaweicloudsdkcodeartsdeploy==3.1.97',
    'huaweicloudsdkcodeartsinspector==3.1.97',
    'huaweicloudsdkcodeartspipeline==3.1.97',
    'huaweicloudsdkcodecraft==3.1.97',
    'huaweicloudsdkcodehub==3.1.97',
    'huaweicloudsdkconfig==3.1.97',
    'huaweicloudsdkcph==3.1.97',
    'huaweicloudsdkcpts==3.1.97',
    'huaweicloudsdkcse==3.1.97',
    'huaweicloudsdkcsms==3.1.97',
    'huaweicloudsdkcss==3.1.97',
    'huaweicloudsdkcts==3.1.97',
    'huaweicloudsdkdas==3.1.97',
    'huaweicloudsdkdataartsstudio==3.1.97',
    'huaweicloudsdkdbss==3.1.97',
    'huaweicloudsdkdc==3.1.97',
    'huaweicloudsdkdcs==3.1.97',
    'huaweicloudsdkddm==3.1.97',
    'huaweicloudsdkdds==3.1.97',
    'huaweicloudsdkdeh==3.1.97',
    'huaweicloudsdkdevsecurity==3.1.97',
    'huaweicloudsdkdevstar==3.1.97',
    'huaweicloudsdkdgc==3.1.97',
    'huaweicloudsdkdis==3.1.97',
    'huaweicloudsdkdlf==3.1.97',
    'huaweicloudsdkdli==3.1.97',
    'huaweicloudsdkdns==3.1.97',
    'huaweicloudsdkdris==3.1.97',
    'huaweicloudsdkdrs==3.1.97',
    'huaweicloudsdkdsc==3.1.97',
    'huaweicloudsdkdwr==3.1.97',
    'huaweicloudsdkdws==3.1.97',
    'huaweicloudsdkec==3.1.97',
    'huaweicloudsdkecs==3.1.97',
    'huaweicloudsdkedgesec==3.1.97',
    'huaweicloudsdkeg==3.1.97',
    'huaweicloudsdkeihealth==3.1.97',
    'huaweicloudsdkeip==3.1.97',
    'huaweicloudsdkelb==3.1.97',
    'huaweicloudsdkeps==3.1.97',
    'huaweicloudsdker==3.1.97',
    'huaweicloudsdkevs==3.1.97',
    'huaweicloudsdkfrs==3.1.97',
    'huaweicloudsdkfunctiongraph==3.1.97',
    'huaweicloudsdkga==3.1.97',
    'huaweicloudsdkgaussdb==3.1.97',
    'huaweicloudsdkgaussdbfornosql==3.1.97',
    'huaweicloudsdkgaussdbforopengauss==3.1.97',
    'huaweicloudsdkgeip==3.1.97',
    'huaweicloudsdkges==3.1.97',
    'huaweicloudsdkgsl==3.1.97',
    'huaweicloudsdkhilens==3.1.97',
    'huaweicloudsdkhss==3.1.97',
    'huaweicloudsdkiam==3.1.97',
    'huaweicloudsdkiamaccessanalyzer==3.1.97',
    'huaweicloudsdkidentitycenter==3.1.97',
    'huaweicloudsdkidentitycenterstore==3.1.97',
    'huaweicloudsdkidme==3.1.97',
    'huaweicloudsdkidmeclassicapi==3.1.97',
    'huaweicloudsdkiec==3.1.97',
    'huaweicloudsdkief==3.1.97',
    'huaweicloudsdkimage==3.1.97',
    'huaweicloudsdkimagesearch==3.1.97',
    'huaweicloudsdkims==3.1.97',
    'huaweicloudsdkiotanalytics==3.1.97',
    'huaweicloudsdkiotda==3.1.97',
    'huaweicloudsdkiotedge==3.1.97',
    'huaweicloudsdkivs==3.1.97',
    'huaweicloudsdkkafka==3.1.97',
    'huaweicloudsdkkms==3.1.97',
    'huaweicloudsdkkoomessage==3.1.97',
    'huaweicloudsdkkps==3.1.97',
    'huaweicloudsdklakeformation==3.1.97',
    'huaweicloudsdklive==3.1.97',
    'huaweicloudsdklts==3.1.97',
    'huaweicloudsdkmapds==3.1.97',
    'huaweicloudsdkmas==3.1.97',
    'huaweicloudsdkmeeting==3.1.97',
    'huaweicloudsdkmetastudio==3.1.97',
    'huaweicloudsdkmoderation==3.1.97',
    'huaweicloudsdkmpc==3.1.97',
    'huaweicloudsdkmrs==3.1.97',
    'huaweicloudsdkmsgsms==3.1.97',
    'huaweicloudsdkmssi==3.1.97',
    'huaweicloudsdknat==3.1.97',
    'huaweicloudsdknlp==3.1.97',
    'huaweicloudsdkobs==3.1.97',
    'huaweicloudsdkocr==3.1.97',
    'huaweicloudsdkoctopus==3.1.97',
    'huaweicloudsdkoms==3.1.97',
    'huaweicloudsdkoptverse==3.1.97',
    'huaweicloudsdkorganizations==3.1.97',
    'huaweicloudsdkorgid==3.1.97',
    'huaweicloudsdkoroas==3.1.97',
    'huaweicloudsdkosm==3.1.97',
    'huaweicloudsdkpangulargemodels==3.1.97',
    'huaweicloudsdkprojectman==3.1.97',
    'huaweicloudsdkrabbitmq==3.1.97',
    'huaweicloudsdkram==3.1.97',
    'huaweicloudsdkrds==3.1.97',
    'huaweicloudsdkres==3.1.97',
    'huaweicloudsdkrgc==3.1.97',
    'huaweicloudsdkrms==3.1.97',
    'huaweicloudsdkrocketmq==3.1.97',
    'huaweicloudsdkroma==3.1.97',
    'huaweicloudsdksa==3.1.97',
    'huaweicloudsdkscm==3.1.97',
    'huaweicloudsdksdrs==3.1.97',
    'huaweicloudsdksecmaster==3.1.97',
    'huaweicloudsdkservicestage==3.1.97',
    'huaweicloudsdksfsturbo==3.1.97',
    'huaweicloudsdksis==3.1.97',
    'huaweicloudsdksmn==3.1.97',
    'huaweicloudsdksms==3.1.97',
    'huaweicloudsdksts==3.1.97',
    'huaweicloudsdkswr==3.1.97',
    'huaweicloudsdktics==3.1.97',
    'huaweicloudsdktms==3.1.97',
    'huaweicloudsdkugo==3.1.97',
    'huaweicloudsdkvas==3.1.97',
    'huaweicloudsdkvcm==3.1.97',
    'huaweicloudsdkvod==3.1.97',
    'huaweicloudsdkvpc==3.1.97',
    'huaweicloudsdkvpcep==3.1.97',
    'huaweicloudsdkvpn==3.1.97',
    'huaweicloudsdkwaf==3.1.97',
    'huaweicloudsdkworkspace==3.1.97',
    'huaweicloudsdkworkspaceapp==3.1.97',
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
