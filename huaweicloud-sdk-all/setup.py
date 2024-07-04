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
VERSION = "3.1.104"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.104',
    'huaweicloudsdkaad==3.1.104',
    'huaweicloudsdkantiddos==3.1.104',
    'huaweicloudsdkaom==3.1.104',
    'huaweicloudsdkaos==3.1.104',
    'huaweicloudsdkapig==3.1.104',
    'huaweicloudsdkapm==3.1.104',
    'huaweicloudsdkas==3.1.104',
    'huaweicloudsdkasm==3.1.104',
    'huaweicloudsdkbcs==3.1.104',
    'huaweicloudsdkbms==3.1.104',
    'huaweicloudsdkbss==3.1.104',
    'huaweicloudsdkbssintl==3.1.104',
    'huaweicloudsdkcae==3.1.104',
    'huaweicloudsdkcampusgo==3.1.104',
    'huaweicloudsdkcbh==3.1.104',
    'huaweicloudsdkcbr==3.1.104',
    'huaweicloudsdkcbs==3.1.104',
    'huaweicloudsdkcc==3.1.104',
    'huaweicloudsdkcce==3.1.104',
    'huaweicloudsdkccm==3.1.104',
    'huaweicloudsdkcdm==3.1.104',
    'huaweicloudsdkcdn==3.1.104',
    'huaweicloudsdkces==3.1.104',
    'huaweicloudsdkcfw==3.1.104',
    'huaweicloudsdkcgs==3.1.104',
    'huaweicloudsdkclassroom==3.1.104',
    'huaweicloudsdkcloudide==3.1.104',
    'huaweicloudsdkcloudpond==3.1.104',
    'huaweicloudsdkcloudrtc==3.1.104',
    'huaweicloudsdkcloudtable==3.1.104',
    'huaweicloudsdkcloudtest==3.1.104',
    'huaweicloudsdkcodeartsartifact==3.1.104',
    'huaweicloudsdkcodeartsbuild==3.1.104',
    'huaweicloudsdkcodeartscheck==3.1.104',
    'huaweicloudsdkcodeartsdeploy==3.1.104',
    'huaweicloudsdkcodeartsinspector==3.1.104',
    'huaweicloudsdkcodeartspipeline==3.1.104',
    'huaweicloudsdkcodecraft==3.1.104',
    'huaweicloudsdkcodehub==3.1.104',
    'huaweicloudsdkconfig==3.1.104',
    'huaweicloudsdkcph==3.1.104',
    'huaweicloudsdkcpts==3.1.104',
    'huaweicloudsdkcse==3.1.104',
    'huaweicloudsdkcsms==3.1.104',
    'huaweicloudsdkcss==3.1.104',
    'huaweicloudsdkcts==3.1.104',
    'huaweicloudsdkdas==3.1.104',
    'huaweicloudsdkdataartsstudio==3.1.104',
    'huaweicloudsdkdbss==3.1.104',
    'huaweicloudsdkdc==3.1.104',
    'huaweicloudsdkdcs==3.1.104',
    'huaweicloudsdkddm==3.1.104',
    'huaweicloudsdkdds==3.1.104',
    'huaweicloudsdkdeh==3.1.104',
    'huaweicloudsdkdevsecurity==3.1.104',
    'huaweicloudsdkdevstar==3.1.104',
    'huaweicloudsdkdgc==3.1.104',
    'huaweicloudsdkdis==3.1.104',
    'huaweicloudsdkdlf==3.1.104',
    'huaweicloudsdkdli==3.1.104',
    'huaweicloudsdkdns==3.1.104',
    'huaweicloudsdkdris==3.1.104',
    'huaweicloudsdkdrs==3.1.104',
    'huaweicloudsdkdsc==3.1.104',
    'huaweicloudsdkdwr==3.1.104',
    'huaweicloudsdkdws==3.1.104',
    'huaweicloudsdkec==3.1.104',
    'huaweicloudsdkecs==3.1.104',
    'huaweicloudsdkedgesec==3.1.104',
    'huaweicloudsdkeg==3.1.104',
    'huaweicloudsdkeihealth==3.1.104',
    'huaweicloudsdkeip==3.1.104',
    'huaweicloudsdkelb==3.1.104',
    'huaweicloudsdkeps==3.1.104',
    'huaweicloudsdker==3.1.104',
    'huaweicloudsdkevs==3.1.104',
    'huaweicloudsdkfrs==3.1.104',
    'huaweicloudsdkfunctiongraph==3.1.104',
    'huaweicloudsdkga==3.1.104',
    'huaweicloudsdkgaussdb==3.1.104',
    'huaweicloudsdkgaussdbfornosql==3.1.104',
    'huaweicloudsdkgaussdbforopengauss==3.1.104',
    'huaweicloudsdkgeip==3.1.104',
    'huaweicloudsdkges==3.1.104',
    'huaweicloudsdkgsl==3.1.104',
    'huaweicloudsdkhilens==3.1.104',
    'huaweicloudsdkhss==3.1.104',
    'huaweicloudsdkiam==3.1.104',
    'huaweicloudsdkiamaccessanalyzer==3.1.104',
    'huaweicloudsdkidentitycenter==3.1.104',
    'huaweicloudsdkidentitycenterstore==3.1.104',
    'huaweicloudsdkidme==3.1.104',
    'huaweicloudsdkidmeclassicapi==3.1.104',
    'huaweicloudsdkiec==3.1.104',
    'huaweicloudsdkief==3.1.104',
    'huaweicloudsdkimage==3.1.104',
    'huaweicloudsdkimagesearch==3.1.104',
    'huaweicloudsdkims==3.1.104',
    'huaweicloudsdkiotanalytics==3.1.104',
    'huaweicloudsdkiotda==3.1.104',
    'huaweicloudsdkiotedge==3.1.104',
    'huaweicloudsdkivs==3.1.104',
    'huaweicloudsdkkafka==3.1.104',
    'huaweicloudsdkkms==3.1.104',
    'huaweicloudsdkkoomessage==3.1.104',
    'huaweicloudsdkkps==3.1.104',
    'huaweicloudsdklakeformation==3.1.104',
    'huaweicloudsdklive==3.1.104',
    'huaweicloudsdklts==3.1.104',
    'huaweicloudsdkmapds==3.1.104',
    'huaweicloudsdkmas==3.1.104',
    'huaweicloudsdkmeeting==3.1.104',
    'huaweicloudsdkmetastudio==3.1.104',
    'huaweicloudsdkmoderation==3.1.104',
    'huaweicloudsdkmpc==3.1.104',
    'huaweicloudsdkmrs==3.1.104',
    'huaweicloudsdkmsgsms==3.1.104',
    'huaweicloudsdkmssi==3.1.104',
    'huaweicloudsdknat==3.1.104',
    'huaweicloudsdknlp==3.1.104',
    'huaweicloudsdkobs==3.1.104',
    'huaweicloudsdkocr==3.1.104',
    'huaweicloudsdkoctopus==3.1.104',
    'huaweicloudsdkoms==3.1.104',
    'huaweicloudsdkoptverse==3.1.104',
    'huaweicloudsdkorganizations==3.1.104',
    'huaweicloudsdkorgid==3.1.104',
    'huaweicloudsdkoroas==3.1.104',
    'huaweicloudsdkosm==3.1.104',
    'huaweicloudsdkpangulargemodels==3.1.104',
    'huaweicloudsdkprojectman==3.1.104',
    'huaweicloudsdkrabbitmq==3.1.104',
    'huaweicloudsdkram==3.1.104',
    'huaweicloudsdkrds==3.1.104',
    'huaweicloudsdkres==3.1.104',
    'huaweicloudsdkrgc==3.1.104',
    'huaweicloudsdkrms==3.1.104',
    'huaweicloudsdkrocketmq==3.1.104',
    'huaweicloudsdkroma==3.1.104',
    'huaweicloudsdksa==3.1.104',
    'huaweicloudsdkscm==3.1.104',
    'huaweicloudsdksdrs==3.1.104',
    'huaweicloudsdksecmaster==3.1.104',
    'huaweicloudsdkservicestage==3.1.104',
    'huaweicloudsdksfsturbo==3.1.104',
    'huaweicloudsdksis==3.1.104',
    'huaweicloudsdksmn==3.1.104',
    'huaweicloudsdksms==3.1.104',
    'huaweicloudsdksts==3.1.104',
    'huaweicloudsdkswr==3.1.104',
    'huaweicloudsdktics==3.1.104',
    'huaweicloudsdktms==3.1.104',
    'huaweicloudsdkugo==3.1.104',
    'huaweicloudsdkvas==3.1.104',
    'huaweicloudsdkvcm==3.1.104',
    'huaweicloudsdkvod==3.1.104',
    'huaweicloudsdkvpc==3.1.104',
    'huaweicloudsdkvpcep==3.1.104',
    'huaweicloudsdkvpn==3.1.104',
    'huaweicloudsdkwaf==3.1.104',
    'huaweicloudsdkworkspace==3.1.104',
    'huaweicloudsdkworkspaceapp==3.1.104',
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
