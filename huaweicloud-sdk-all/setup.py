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
VERSION = "3.1.95"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.95',
    'huaweicloudsdkaad==3.1.95',
    'huaweicloudsdkantiddos==3.1.95',
    'huaweicloudsdkaom==3.1.95',
    'huaweicloudsdkaos==3.1.95',
    'huaweicloudsdkapig==3.1.95',
    'huaweicloudsdkapm==3.1.95',
    'huaweicloudsdkas==3.1.95',
    'huaweicloudsdkasm==3.1.95',
    'huaweicloudsdkbcs==3.1.95',
    'huaweicloudsdkbms==3.1.95',
    'huaweicloudsdkbss==3.1.95',
    'huaweicloudsdkbssintl==3.1.95',
    'huaweicloudsdkcae==3.1.95',
    'huaweicloudsdkcampusgo==3.1.95',
    'huaweicloudsdkcbh==3.1.95',
    'huaweicloudsdkcbr==3.1.95',
    'huaweicloudsdkcbs==3.1.95',
    'huaweicloudsdkcc==3.1.95',
    'huaweicloudsdkcce==3.1.95',
    'huaweicloudsdkccm==3.1.95',
    'huaweicloudsdkcdm==3.1.95',
    'huaweicloudsdkcdn==3.1.95',
    'huaweicloudsdkces==3.1.95',
    'huaweicloudsdkcfw==3.1.95',
    'huaweicloudsdkcgs==3.1.95',
    'huaweicloudsdkclassroom==3.1.95',
    'huaweicloudsdkcloudide==3.1.95',
    'huaweicloudsdkcloudpond==3.1.95',
    'huaweicloudsdkcloudrtc==3.1.95',
    'huaweicloudsdkcloudtable==3.1.95',
    'huaweicloudsdkcloudtest==3.1.95',
    'huaweicloudsdkcodeartsartifact==3.1.95',
    'huaweicloudsdkcodeartsbuild==3.1.95',
    'huaweicloudsdkcodeartscheck==3.1.95',
    'huaweicloudsdkcodeartsdeploy==3.1.95',
    'huaweicloudsdkcodeartsinspector==3.1.95',
    'huaweicloudsdkcodeartspipeline==3.1.95',
    'huaweicloudsdkcodecraft==3.1.95',
    'huaweicloudsdkcodehub==3.1.95',
    'huaweicloudsdkconfig==3.1.95',
    'huaweicloudsdkcph==3.1.95',
    'huaweicloudsdkcpts==3.1.95',
    'huaweicloudsdkcse==3.1.95',
    'huaweicloudsdkcsms==3.1.95',
    'huaweicloudsdkcss==3.1.95',
    'huaweicloudsdkcts==3.1.95',
    'huaweicloudsdkdas==3.1.95',
    'huaweicloudsdkdataartsstudio==3.1.95',
    'huaweicloudsdkdbss==3.1.95',
    'huaweicloudsdkdc==3.1.95',
    'huaweicloudsdkdcs==3.1.95',
    'huaweicloudsdkddm==3.1.95',
    'huaweicloudsdkdds==3.1.95',
    'huaweicloudsdkdeh==3.1.95',
    'huaweicloudsdkdevsecurity==3.1.95',
    'huaweicloudsdkdevstar==3.1.95',
    'huaweicloudsdkdgc==3.1.95',
    'huaweicloudsdkdis==3.1.95',
    'huaweicloudsdkdlf==3.1.95',
    'huaweicloudsdkdli==3.1.95',
    'huaweicloudsdkdns==3.1.95',
    'huaweicloudsdkdris==3.1.95',
    'huaweicloudsdkdrs==3.1.95',
    'huaweicloudsdkdsc==3.1.95',
    'huaweicloudsdkdwr==3.1.95',
    'huaweicloudsdkdws==3.1.95',
    'huaweicloudsdkec==3.1.95',
    'huaweicloudsdkecs==3.1.95',
    'huaweicloudsdkedgesec==3.1.95',
    'huaweicloudsdkeg==3.1.95',
    'huaweicloudsdkeihealth==3.1.95',
    'huaweicloudsdkeip==3.1.95',
    'huaweicloudsdkelb==3.1.95',
    'huaweicloudsdkeps==3.1.95',
    'huaweicloudsdker==3.1.95',
    'huaweicloudsdkevs==3.1.95',
    'huaweicloudsdkfrs==3.1.95',
    'huaweicloudsdkfunctiongraph==3.1.95',
    'huaweicloudsdkga==3.1.95',
    'huaweicloudsdkgaussdb==3.1.95',
    'huaweicloudsdkgaussdbfornosql==3.1.95',
    'huaweicloudsdkgaussdbforopengauss==3.1.95',
    'huaweicloudsdkgeip==3.1.95',
    'huaweicloudsdkges==3.1.95',
    'huaweicloudsdkgsl==3.1.95',
    'huaweicloudsdkhilens==3.1.95',
    'huaweicloudsdkhss==3.1.95',
    'huaweicloudsdkiam==3.1.95',
    'huaweicloudsdkiamaccessanalyzer==3.1.95',
    'huaweicloudsdkidentitycenter==3.1.95',
    'huaweicloudsdkidentitycenterstore==3.1.95',
    'huaweicloudsdkidme==3.1.95',
    'huaweicloudsdkidmeclassicapi==3.1.95',
    'huaweicloudsdkiec==3.1.95',
    'huaweicloudsdkief==3.1.95',
    'huaweicloudsdkimage==3.1.95',
    'huaweicloudsdkimagesearch==3.1.95',
    'huaweicloudsdkims==3.1.95',
    'huaweicloudsdkiotanalytics==3.1.95',
    'huaweicloudsdkiotda==3.1.95',
    'huaweicloudsdkiotedge==3.1.95',
    'huaweicloudsdkivs==3.1.95',
    'huaweicloudsdkkafka==3.1.95',
    'huaweicloudsdkkms==3.1.95',
    'huaweicloudsdkkoomessage==3.1.95',
    'huaweicloudsdkkps==3.1.95',
    'huaweicloudsdklakeformation==3.1.95',
    'huaweicloudsdklive==3.1.95',
    'huaweicloudsdklts==3.1.95',
    'huaweicloudsdkmapds==3.1.95',
    'huaweicloudsdkmas==3.1.95',
    'huaweicloudsdkmeeting==3.1.95',
    'huaweicloudsdkmetastudio==3.1.95',
    'huaweicloudsdkmoderation==3.1.95',
    'huaweicloudsdkmpc==3.1.95',
    'huaweicloudsdkmrs==3.1.95',
    'huaweicloudsdkmsgsms==3.1.95',
    'huaweicloudsdkmssi==3.1.95',
    'huaweicloudsdknat==3.1.95',
    'huaweicloudsdknlp==3.1.95',
    'huaweicloudsdkobs==3.1.95',
    'huaweicloudsdkocr==3.1.95',
    'huaweicloudsdkoctopus==3.1.95',
    'huaweicloudsdkoms==3.1.95',
    'huaweicloudsdkoptverse==3.1.95',
    'huaweicloudsdkorganizations==3.1.95',
    'huaweicloudsdkorgid==3.1.95',
    'huaweicloudsdkoroas==3.1.95',
    'huaweicloudsdkosm==3.1.95',
    'huaweicloudsdkpangulargemodels==3.1.95',
    'huaweicloudsdkprojectman==3.1.95',
    'huaweicloudsdkrabbitmq==3.1.95',
    'huaweicloudsdkram==3.1.95',
    'huaweicloudsdkrds==3.1.95',
    'huaweicloudsdkres==3.1.95',
    'huaweicloudsdkrgc==3.1.95',
    'huaweicloudsdkrms==3.1.95',
    'huaweicloudsdkrocketmq==3.1.95',
    'huaweicloudsdkroma==3.1.95',
    'huaweicloudsdksa==3.1.95',
    'huaweicloudsdkscm==3.1.95',
    'huaweicloudsdksdrs==3.1.95',
    'huaweicloudsdksecmaster==3.1.95',
    'huaweicloudsdkservicestage==3.1.95',
    'huaweicloudsdksfsturbo==3.1.95',
    'huaweicloudsdksis==3.1.95',
    'huaweicloudsdksmn==3.1.95',
    'huaweicloudsdksms==3.1.95',
    'huaweicloudsdksts==3.1.95',
    'huaweicloudsdkswr==3.1.95',
    'huaweicloudsdktics==3.1.95',
    'huaweicloudsdktms==3.1.95',
    'huaweicloudsdkugo==3.1.95',
    'huaweicloudsdkvas==3.1.95',
    'huaweicloudsdkvcm==3.1.95',
    'huaweicloudsdkvod==3.1.95',
    'huaweicloudsdkvpc==3.1.95',
    'huaweicloudsdkvpcep==3.1.95',
    'huaweicloudsdkvpn==3.1.95',
    'huaweicloudsdkwaf==3.1.95',
    'huaweicloudsdkworkspace==3.1.95',
    'huaweicloudsdkworkspaceapp==3.1.95',
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
