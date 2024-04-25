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
VERSION = "3.1.93"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.93',
    'huaweicloudsdkaad==3.1.93',
    'huaweicloudsdkantiddos==3.1.93',
    'huaweicloudsdkaom==3.1.93',
    'huaweicloudsdkaos==3.1.93',
    'huaweicloudsdkapig==3.1.93',
    'huaweicloudsdkapm==3.1.93',
    'huaweicloudsdkas==3.1.93',
    'huaweicloudsdkasm==3.1.93',
    'huaweicloudsdkbcs==3.1.93',
    'huaweicloudsdkbms==3.1.93',
    'huaweicloudsdkbss==3.1.93',
    'huaweicloudsdkbssintl==3.1.93',
    'huaweicloudsdkcae==3.1.93',
    'huaweicloudsdkcampusgo==3.1.93',
    'huaweicloudsdkcbh==3.1.93',
    'huaweicloudsdkcbr==3.1.93',
    'huaweicloudsdkcbs==3.1.93',
    'huaweicloudsdkcc==3.1.93',
    'huaweicloudsdkcce==3.1.93',
    'huaweicloudsdkccm==3.1.93',
    'huaweicloudsdkcdm==3.1.93',
    'huaweicloudsdkcdn==3.1.93',
    'huaweicloudsdkces==3.1.93',
    'huaweicloudsdkcfw==3.1.93',
    'huaweicloudsdkcgs==3.1.93',
    'huaweicloudsdkclassroom==3.1.93',
    'huaweicloudsdkcloudide==3.1.93',
    'huaweicloudsdkcloudpond==3.1.93',
    'huaweicloudsdkcloudrtc==3.1.93',
    'huaweicloudsdkcloudtable==3.1.93',
    'huaweicloudsdkcloudtest==3.1.93',
    'huaweicloudsdkcodeartsartifact==3.1.93',
    'huaweicloudsdkcodeartsbuild==3.1.93',
    'huaweicloudsdkcodeartscheck==3.1.93',
    'huaweicloudsdkcodeartsdeploy==3.1.93',
    'huaweicloudsdkcodeartsinspector==3.1.93',
    'huaweicloudsdkcodeartspipeline==3.1.93',
    'huaweicloudsdkcodecraft==3.1.93',
    'huaweicloudsdkcodehub==3.1.93',
    'huaweicloudsdkconfig==3.1.93',
    'huaweicloudsdkcph==3.1.93',
    'huaweicloudsdkcpts==3.1.93',
    'huaweicloudsdkcse==3.1.93',
    'huaweicloudsdkcsms==3.1.93',
    'huaweicloudsdkcss==3.1.93',
    'huaweicloudsdkcts==3.1.93',
    'huaweicloudsdkdas==3.1.93',
    'huaweicloudsdkdataartsstudio==3.1.93',
    'huaweicloudsdkdbss==3.1.93',
    'huaweicloudsdkdc==3.1.93',
    'huaweicloudsdkdcs==3.1.93',
    'huaweicloudsdkddm==3.1.93',
    'huaweicloudsdkdds==3.1.93',
    'huaweicloudsdkdeh==3.1.93',
    'huaweicloudsdkdevsecurity==3.1.93',
    'huaweicloudsdkdevstar==3.1.93',
    'huaweicloudsdkdgc==3.1.93',
    'huaweicloudsdkdis==3.1.93',
    'huaweicloudsdkdlf==3.1.93',
    'huaweicloudsdkdli==3.1.93',
    'huaweicloudsdkdns==3.1.93',
    'huaweicloudsdkdris==3.1.93',
    'huaweicloudsdkdrs==3.1.93',
    'huaweicloudsdkdsc==3.1.93',
    'huaweicloudsdkdwr==3.1.93',
    'huaweicloudsdkdws==3.1.93',
    'huaweicloudsdkec==3.1.93',
    'huaweicloudsdkecs==3.1.93',
    'huaweicloudsdkedgesec==3.1.93',
    'huaweicloudsdkeg==3.1.93',
    'huaweicloudsdkeihealth==3.1.93',
    'huaweicloudsdkeip==3.1.93',
    'huaweicloudsdkelb==3.1.93',
    'huaweicloudsdkeps==3.1.93',
    'huaweicloudsdker==3.1.93',
    'huaweicloudsdkevs==3.1.93',
    'huaweicloudsdkfrs==3.1.93',
    'huaweicloudsdkfunctiongraph==3.1.93',
    'huaweicloudsdkga==3.1.93',
    'huaweicloudsdkgaussdb==3.1.93',
    'huaweicloudsdkgaussdbfornosql==3.1.93',
    'huaweicloudsdkgaussdbforopengauss==3.1.93',
    'huaweicloudsdkgeip==3.1.93',
    'huaweicloudsdkges==3.1.93',
    'huaweicloudsdkgsl==3.1.93',
    'huaweicloudsdkhilens==3.1.93',
    'huaweicloudsdkhss==3.1.93',
    'huaweicloudsdkiam==3.1.93',
    'huaweicloudsdkiamaccessanalyzer==3.1.93',
    'huaweicloudsdkidentitycenter==3.1.93',
    'huaweicloudsdkidentitycenterstore==3.1.93',
    'huaweicloudsdkidme==3.1.93',
    'huaweicloudsdkidmeclassicapi==3.1.93',
    'huaweicloudsdkiec==3.1.93',
    'huaweicloudsdkief==3.1.93',
    'huaweicloudsdkimage==3.1.93',
    'huaweicloudsdkimagesearch==3.1.93',
    'huaweicloudsdkims==3.1.93',
    'huaweicloudsdkiotanalytics==3.1.93',
    'huaweicloudsdkiotda==3.1.93',
    'huaweicloudsdkiotedge==3.1.93',
    'huaweicloudsdkivs==3.1.93',
    'huaweicloudsdkkafka==3.1.93',
    'huaweicloudsdkkms==3.1.93',
    'huaweicloudsdkkoomessage==3.1.93',
    'huaweicloudsdkkps==3.1.93',
    'huaweicloudsdklakeformation==3.1.93',
    'huaweicloudsdklive==3.1.93',
    'huaweicloudsdklts==3.1.93',
    'huaweicloudsdkmapds==3.1.93',
    'huaweicloudsdkmas==3.1.93',
    'huaweicloudsdkmeeting==3.1.93',
    'huaweicloudsdkmetastudio==3.1.93',
    'huaweicloudsdkmoderation==3.1.93',
    'huaweicloudsdkmpc==3.1.93',
    'huaweicloudsdkmrs==3.1.93',
    'huaweicloudsdkmsgsms==3.1.93',
    'huaweicloudsdkmssi==3.1.93',
    'huaweicloudsdknat==3.1.93',
    'huaweicloudsdknlp==3.1.93',
    'huaweicloudsdkobs==3.1.93',
    'huaweicloudsdkocr==3.1.93',
    'huaweicloudsdkoctopus==3.1.93',
    'huaweicloudsdkoms==3.1.93',
    'huaweicloudsdkoptverse==3.1.93',
    'huaweicloudsdkorganizations==3.1.93',
    'huaweicloudsdkorgid==3.1.93',
    'huaweicloudsdkoroas==3.1.93',
    'huaweicloudsdkosm==3.1.93',
    'huaweicloudsdkpangulargemodels==3.1.93',
    'huaweicloudsdkprojectman==3.1.93',
    'huaweicloudsdkrabbitmq==3.1.93',
    'huaweicloudsdkram==3.1.93',
    'huaweicloudsdkrds==3.1.93',
    'huaweicloudsdkres==3.1.93',
    'huaweicloudsdkrgc==3.1.93',
    'huaweicloudsdkrms==3.1.93',
    'huaweicloudsdkrocketmq==3.1.93',
    'huaweicloudsdkroma==3.1.93',
    'huaweicloudsdksa==3.1.93',
    'huaweicloudsdkscm==3.1.93',
    'huaweicloudsdksdrs==3.1.93',
    'huaweicloudsdksecmaster==3.1.93',
    'huaweicloudsdkservicestage==3.1.93',
    'huaweicloudsdksfsturbo==3.1.93',
    'huaweicloudsdksis==3.1.93',
    'huaweicloudsdksmn==3.1.93',
    'huaweicloudsdksms==3.1.93',
    'huaweicloudsdksts==3.1.93',
    'huaweicloudsdkswr==3.1.93',
    'huaweicloudsdktics==3.1.93',
    'huaweicloudsdktms==3.1.93',
    'huaweicloudsdkugo==3.1.93',
    'huaweicloudsdkvas==3.1.93',
    'huaweicloudsdkvcm==3.1.93',
    'huaweicloudsdkvod==3.1.93',
    'huaweicloudsdkvpc==3.1.93',
    'huaweicloudsdkvpcep==3.1.93',
    'huaweicloudsdkvpn==3.1.93',
    'huaweicloudsdkwaf==3.1.93',
    'huaweicloudsdkworkspace==3.1.93',
    'huaweicloudsdkworkspaceapp==3.1.93',
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
