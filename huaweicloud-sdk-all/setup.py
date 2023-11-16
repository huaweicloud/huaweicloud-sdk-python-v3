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
VERSION = "3.1.67"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.67',
    'huaweicloudsdkaad==3.1.67',
    'huaweicloudsdkantiddos==3.1.67',
    'huaweicloudsdkaom==3.1.67',
    'huaweicloudsdkaos==3.1.67',
    'huaweicloudsdkapig==3.1.67',
    'huaweicloudsdkapm==3.1.67',
    'huaweicloudsdkas==3.1.67',
    'huaweicloudsdkasm==3.1.67',
    'huaweicloudsdkbcs==3.1.67',
    'huaweicloudsdkbms==3.1.67',
    'huaweicloudsdkbss==3.1.67',
    'huaweicloudsdkbssintl==3.1.67',
    'huaweicloudsdkcae==3.1.67',
    'huaweicloudsdkcampusgo==3.1.67',
    'huaweicloudsdkcbh==3.1.67',
    'huaweicloudsdkcbr==3.1.67',
    'huaweicloudsdkcbs==3.1.67',
    'huaweicloudsdkcc==3.1.67',
    'huaweicloudsdkcce==3.1.67',
    'huaweicloudsdkccm==3.1.67',
    'huaweicloudsdkcdm==3.1.67',
    'huaweicloudsdkcdn==3.1.67',
    'huaweicloudsdkces==3.1.67',
    'huaweicloudsdkcfw==3.1.67',
    'huaweicloudsdkcgs==3.1.67',
    'huaweicloudsdkclassroom==3.1.67',
    'huaweicloudsdkcloudide==3.1.67',
    'huaweicloudsdkcloudpond==3.1.67',
    'huaweicloudsdkcloudrtc==3.1.67',
    'huaweicloudsdkcloudtable==3.1.67',
    'huaweicloudsdkcloudtest==3.1.67',
    'huaweicloudsdkcodeartsartifact==3.1.67',
    'huaweicloudsdkcodeartsbuild==3.1.67',
    'huaweicloudsdkcodeartscheck==3.1.67',
    'huaweicloudsdkcodeartsdeploy==3.1.67',
    'huaweicloudsdkcodeartsinspector==3.1.67',
    'huaweicloudsdkcodeartspipeline==3.1.67',
    'huaweicloudsdkcodecraft==3.1.67',
    'huaweicloudsdkcodehub==3.1.67',
    'huaweicloudsdkconfig==3.1.67',
    'huaweicloudsdkcph==3.1.67',
    'huaweicloudsdkcpts==3.1.67',
    'huaweicloudsdkcse==3.1.67',
    'huaweicloudsdkcsms==3.1.67',
    'huaweicloudsdkcss==3.1.67',
    'huaweicloudsdkcts==3.1.67',
    'huaweicloudsdkdas==3.1.67',
    'huaweicloudsdkdataartsstudio==3.1.67',
    'huaweicloudsdkdbss==3.1.67',
    'huaweicloudsdkdc==3.1.67',
    'huaweicloudsdkdcs==3.1.67',
    'huaweicloudsdkddm==3.1.67',
    'huaweicloudsdkdds==3.1.67',
    'huaweicloudsdkdeh==3.1.67',
    'huaweicloudsdkdevsecurity==3.1.67',
    'huaweicloudsdkdevstar==3.1.67',
    'huaweicloudsdkdgc==3.1.67',
    'huaweicloudsdkdlf==3.1.67',
    'huaweicloudsdkdli==3.1.67',
    'huaweicloudsdkdns==3.1.67',
    'huaweicloudsdkdris==3.1.67',
    'huaweicloudsdkdrs==3.1.67',
    'huaweicloudsdkdsc==3.1.67',
    'huaweicloudsdkdwr==3.1.67',
    'huaweicloudsdkdws==3.1.67',
    'huaweicloudsdkec==3.1.67',
    'huaweicloudsdkecs==3.1.67',
    'huaweicloudsdkedgesec==3.1.67',
    'huaweicloudsdkeg==3.1.67',
    'huaweicloudsdkeihealth==3.1.67',
    'huaweicloudsdkeip==3.1.67',
    'huaweicloudsdkelb==3.1.67',
    'huaweicloudsdkeps==3.1.67',
    'huaweicloudsdker==3.1.67',
    'huaweicloudsdkevs==3.1.67',
    'huaweicloudsdkfrs==3.1.67',
    'huaweicloudsdkfunctiongraph==3.1.67',
    'huaweicloudsdkga==3.1.67',
    'huaweicloudsdkgaussdb==3.1.67',
    'huaweicloudsdkgaussdbfornosql==3.1.67',
    'huaweicloudsdkgaussdbforopengauss==3.1.67',
    'huaweicloudsdkges==3.1.67',
    'huaweicloudsdkgsl==3.1.67',
    'huaweicloudsdkhilens==3.1.67',
    'huaweicloudsdkhss==3.1.67',
    'huaweicloudsdkiam==3.1.67',
    'huaweicloudsdkidentitycenter==3.1.67',
    'huaweicloudsdkidentitycenterstore==3.1.67',
    'huaweicloudsdkidme==3.1.67',
    'huaweicloudsdkiec==3.1.67',
    'huaweicloudsdkief==3.1.67',
    'huaweicloudsdkimage==3.1.67',
    'huaweicloudsdkimagesearch==3.1.67',
    'huaweicloudsdkims==3.1.67',
    'huaweicloudsdkiotanalytics==3.1.67',
    'huaweicloudsdkiotda==3.1.67',
    'huaweicloudsdkiotedge==3.1.67',
    'huaweicloudsdkivs==3.1.67',
    'huaweicloudsdkkafka==3.1.67',
    'huaweicloudsdkkms==3.1.67',
    'huaweicloudsdkkoomessage==3.1.67',
    'huaweicloudsdkkps==3.1.67',
    'huaweicloudsdklakeformation==3.1.67',
    'huaweicloudsdklive==3.1.67',
    'huaweicloudsdklts==3.1.67',
    'huaweicloudsdkmapds==3.1.67',
    'huaweicloudsdkmas==3.1.67',
    'huaweicloudsdkmeeting==3.1.67',
    'huaweicloudsdkmetastudio==3.1.67',
    'huaweicloudsdkmoderation==3.1.67',
    'huaweicloudsdkmpc==3.1.67',
    'huaweicloudsdkmrs==3.1.67',
    'huaweicloudsdkmsgsms==3.1.67',
    'huaweicloudsdkmssi==3.1.67',
    'huaweicloudsdknat==3.1.67',
    'huaweicloudsdknlp==3.1.67',
    'huaweicloudsdkocr==3.1.67',
    'huaweicloudsdkoms==3.1.67',
    'huaweicloudsdkoptverse==3.1.67',
    'huaweicloudsdkorganizations==3.1.67',
    'huaweicloudsdkoroas==3.1.67',
    'huaweicloudsdkosm==3.1.67',
    'huaweicloudsdkpangulargemodels==3.1.67',
    'huaweicloudsdkprojectman==3.1.67',
    'huaweicloudsdkrabbitmq==3.1.67',
    'huaweicloudsdkram==3.1.67',
    'huaweicloudsdkrds==3.1.67',
    'huaweicloudsdkres==3.1.67',
    'huaweicloudsdkrms==3.1.67',
    'huaweicloudsdkrocketmq==3.1.67',
    'huaweicloudsdkroma==3.1.67',
    'huaweicloudsdksa==3.1.67',
    'huaweicloudsdkscm==3.1.67',
    'huaweicloudsdksdrs==3.1.67',
    'huaweicloudsdksecmaster==3.1.67',
    'huaweicloudsdkservicestage==3.1.67',
    'huaweicloudsdksfsturbo==3.1.67',
    'huaweicloudsdksis==3.1.67',
    'huaweicloudsdksmn==3.1.67',
    'huaweicloudsdksms==3.1.67',
    'huaweicloudsdkswr==3.1.67',
    'huaweicloudsdktics==3.1.67',
    'huaweicloudsdktms==3.1.67',
    'huaweicloudsdkugo==3.1.67',
    'huaweicloudsdkvas==3.1.67',
    'huaweicloudsdkvcm==3.1.67',
    'huaweicloudsdkvod==3.1.67',
    'huaweicloudsdkvpc==3.1.67',
    'huaweicloudsdkvpcep==3.1.67',
    'huaweicloudsdkvpn==3.1.67',
    'huaweicloudsdkwaf==3.1.67',
    'huaweicloudsdkworkspace==3.1.67',
    'huaweicloudsdkworkspaceapp==3.1.67',
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
