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
VERSION = "3.1.84"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.84',
    'huaweicloudsdkaad==3.1.84',
    'huaweicloudsdkantiddos==3.1.84',
    'huaweicloudsdkaom==3.1.84',
    'huaweicloudsdkaos==3.1.84',
    'huaweicloudsdkapig==3.1.84',
    'huaweicloudsdkapm==3.1.84',
    'huaweicloudsdkas==3.1.84',
    'huaweicloudsdkasm==3.1.84',
    'huaweicloudsdkbcs==3.1.84',
    'huaweicloudsdkbms==3.1.84',
    'huaweicloudsdkbss==3.1.84',
    'huaweicloudsdkbssintl==3.1.84',
    'huaweicloudsdkcae==3.1.84',
    'huaweicloudsdkcampusgo==3.1.84',
    'huaweicloudsdkcbh==3.1.84',
    'huaweicloudsdkcbr==3.1.84',
    'huaweicloudsdkcbs==3.1.84',
    'huaweicloudsdkcc==3.1.84',
    'huaweicloudsdkcce==3.1.84',
    'huaweicloudsdkccm==3.1.84',
    'huaweicloudsdkcdm==3.1.84',
    'huaweicloudsdkcdn==3.1.84',
    'huaweicloudsdkces==3.1.84',
    'huaweicloudsdkcfw==3.1.84',
    'huaweicloudsdkcgs==3.1.84',
    'huaweicloudsdkclassroom==3.1.84',
    'huaweicloudsdkcloudide==3.1.84',
    'huaweicloudsdkcloudpond==3.1.84',
    'huaweicloudsdkcloudrtc==3.1.84',
    'huaweicloudsdkcloudtable==3.1.84',
    'huaweicloudsdkcloudtest==3.1.84',
    'huaweicloudsdkcodeartsartifact==3.1.84',
    'huaweicloudsdkcodeartsbuild==3.1.84',
    'huaweicloudsdkcodeartscheck==3.1.84',
    'huaweicloudsdkcodeartsdeploy==3.1.84',
    'huaweicloudsdkcodeartsinspector==3.1.84',
    'huaweicloudsdkcodeartspipeline==3.1.84',
    'huaweicloudsdkcodecraft==3.1.84',
    'huaweicloudsdkcodehub==3.1.84',
    'huaweicloudsdkconfig==3.1.84',
    'huaweicloudsdkcph==3.1.84',
    'huaweicloudsdkcpts==3.1.84',
    'huaweicloudsdkcse==3.1.84',
    'huaweicloudsdkcsms==3.1.84',
    'huaweicloudsdkcss==3.1.84',
    'huaweicloudsdkcts==3.1.84',
    'huaweicloudsdkdas==3.1.84',
    'huaweicloudsdkdataartsstudio==3.1.84',
    'huaweicloudsdkdbss==3.1.84',
    'huaweicloudsdkdc==3.1.84',
    'huaweicloudsdkdcs==3.1.84',
    'huaweicloudsdkddm==3.1.84',
    'huaweicloudsdkdds==3.1.84',
    'huaweicloudsdkdeh==3.1.84',
    'huaweicloudsdkdevsecurity==3.1.84',
    'huaweicloudsdkdevstar==3.1.84',
    'huaweicloudsdkdgc==3.1.84',
    'huaweicloudsdkdis==3.1.84',
    'huaweicloudsdkdlf==3.1.84',
    'huaweicloudsdkdli==3.1.84',
    'huaweicloudsdkdns==3.1.84',
    'huaweicloudsdkdris==3.1.84',
    'huaweicloudsdkdrs==3.1.84',
    'huaweicloudsdkdsc==3.1.84',
    'huaweicloudsdkdwr==3.1.84',
    'huaweicloudsdkdws==3.1.84',
    'huaweicloudsdkec==3.1.84',
    'huaweicloudsdkecs==3.1.84',
    'huaweicloudsdkedgesec==3.1.84',
    'huaweicloudsdkeg==3.1.84',
    'huaweicloudsdkeihealth==3.1.84',
    'huaweicloudsdkeip==3.1.84',
    'huaweicloudsdkelb==3.1.84',
    'huaweicloudsdkeps==3.1.84',
    'huaweicloudsdker==3.1.84',
    'huaweicloudsdkevs==3.1.84',
    'huaweicloudsdkfrs==3.1.84',
    'huaweicloudsdkfunctiongraph==3.1.84',
    'huaweicloudsdkga==3.1.84',
    'huaweicloudsdkgaussdb==3.1.84',
    'huaweicloudsdkgaussdbfornosql==3.1.84',
    'huaweicloudsdkgaussdbforopengauss==3.1.84',
    'huaweicloudsdkgeip==3.1.84',
    'huaweicloudsdkges==3.1.84',
    'huaweicloudsdkgsl==3.1.84',
    'huaweicloudsdkhilens==3.1.84',
    'huaweicloudsdkhss==3.1.84',
    'huaweicloudsdkiam==3.1.84',
    'huaweicloudsdkiamaccessanalyzer==3.1.84',
    'huaweicloudsdkidentitycenter==3.1.84',
    'huaweicloudsdkidentitycenterstore==3.1.84',
    'huaweicloudsdkidme==3.1.84',
    'huaweicloudsdkidmeclassicapi==3.1.84',
    'huaweicloudsdkiec==3.1.84',
    'huaweicloudsdkief==3.1.84',
    'huaweicloudsdkimage==3.1.84',
    'huaweicloudsdkimagesearch==3.1.84',
    'huaweicloudsdkims==3.1.84',
    'huaweicloudsdkiotanalytics==3.1.84',
    'huaweicloudsdkiotda==3.1.84',
    'huaweicloudsdkiotedge==3.1.84',
    'huaweicloudsdkivs==3.1.84',
    'huaweicloudsdkkafka==3.1.84',
    'huaweicloudsdkkms==3.1.84',
    'huaweicloudsdkkoomessage==3.1.84',
    'huaweicloudsdkkps==3.1.84',
    'huaweicloudsdklakeformation==3.1.84',
    'huaweicloudsdklive==3.1.84',
    'huaweicloudsdklts==3.1.84',
    'huaweicloudsdkmapds==3.1.84',
    'huaweicloudsdkmas==3.1.84',
    'huaweicloudsdkmeeting==3.1.84',
    'huaweicloudsdkmetastudio==3.1.84',
    'huaweicloudsdkmoderation==3.1.84',
    'huaweicloudsdkmpc==3.1.84',
    'huaweicloudsdkmrs==3.1.84',
    'huaweicloudsdkmsgsms==3.1.84',
    'huaweicloudsdkmssi==3.1.84',
    'huaweicloudsdknat==3.1.84',
    'huaweicloudsdknlp==3.1.84',
    'huaweicloudsdkobs==3.1.84',
    'huaweicloudsdkocr==3.1.84',
    'huaweicloudsdkoctopus==3.1.84',
    'huaweicloudsdkoms==3.1.84',
    'huaweicloudsdkoptverse==3.1.84',
    'huaweicloudsdkorganizations==3.1.84',
    'huaweicloudsdkorgid==3.1.84',
    'huaweicloudsdkoroas==3.1.84',
    'huaweicloudsdkosm==3.1.84',
    'huaweicloudsdkpangulargemodels==3.1.84',
    'huaweicloudsdkprojectman==3.1.84',
    'huaweicloudsdkrabbitmq==3.1.84',
    'huaweicloudsdkram==3.1.84',
    'huaweicloudsdkrds==3.1.84',
    'huaweicloudsdkres==3.1.84',
    'huaweicloudsdkrgc==3.1.84',
    'huaweicloudsdkrms==3.1.84',
    'huaweicloudsdkrocketmq==3.1.84',
    'huaweicloudsdkroma==3.1.84',
    'huaweicloudsdksa==3.1.84',
    'huaweicloudsdkscm==3.1.84',
    'huaweicloudsdksdrs==3.1.84',
    'huaweicloudsdksecmaster==3.1.84',
    'huaweicloudsdkservicestage==3.1.84',
    'huaweicloudsdksfsturbo==3.1.84',
    'huaweicloudsdksis==3.1.84',
    'huaweicloudsdksmn==3.1.84',
    'huaweicloudsdksms==3.1.84',
    'huaweicloudsdkswr==3.1.84',
    'huaweicloudsdktics==3.1.84',
    'huaweicloudsdktms==3.1.84',
    'huaweicloudsdkugo==3.1.84',
    'huaweicloudsdkvas==3.1.84',
    'huaweicloudsdkvcm==3.1.84',
    'huaweicloudsdkvod==3.1.84',
    'huaweicloudsdkvpc==3.1.84',
    'huaweicloudsdkvpcep==3.1.84',
    'huaweicloudsdkvpn==3.1.84',
    'huaweicloudsdkwaf==3.1.84',
    'huaweicloudsdkworkspace==3.1.84',
    'huaweicloudsdkworkspaceapp==3.1.84',
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
