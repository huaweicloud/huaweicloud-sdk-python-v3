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
VERSION = "3.1.62"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.62',
    'huaweicloudsdkantiddos==3.1.62',
    'huaweicloudsdkaom==3.1.62',
    'huaweicloudsdkaos==3.1.62',
    'huaweicloudsdkapig==3.1.62',
    'huaweicloudsdkapm==3.1.62',
    'huaweicloudsdkas==3.1.62',
    'huaweicloudsdkasm==3.1.62',
    'huaweicloudsdkbcs==3.1.62',
    'huaweicloudsdkbms==3.1.62',
    'huaweicloudsdkbss==3.1.62',
    'huaweicloudsdkbssintl==3.1.62',
    'huaweicloudsdkcae==3.1.62',
    'huaweicloudsdkcampusgo==3.1.62',
    'huaweicloudsdkcbh==3.1.62',
    'huaweicloudsdkcbr==3.1.62',
    'huaweicloudsdkcbs==3.1.62',
    'huaweicloudsdkcc==3.1.62',
    'huaweicloudsdkcce==3.1.62',
    'huaweicloudsdkccm==3.1.62',
    'huaweicloudsdkcdm==3.1.62',
    'huaweicloudsdkcdn==3.1.62',
    'huaweicloudsdkces==3.1.62',
    'huaweicloudsdkcfw==3.1.62',
    'huaweicloudsdkcgs==3.1.62',
    'huaweicloudsdkclassroom==3.1.62',
    'huaweicloudsdkcloudide==3.1.62',
    'huaweicloudsdkcloudpond==3.1.62',
    'huaweicloudsdkcloudrtc==3.1.62',
    'huaweicloudsdkcloudtable==3.1.62',
    'huaweicloudsdkcloudtest==3.1.62',
    'huaweicloudsdkcodeartsartifact==3.1.62',
    'huaweicloudsdkcodeartsbuild==3.1.62',
    'huaweicloudsdkcodeartscheck==3.1.62',
    'huaweicloudsdkcodeartsdeploy==3.1.62',
    'huaweicloudsdkcodeartsinspector==3.1.62',
    'huaweicloudsdkcodeartspipeline==3.1.62',
    'huaweicloudsdkcodecraft==3.1.62',
    'huaweicloudsdkcodehub==3.1.62',
    'huaweicloudsdkconfig==3.1.62',
    'huaweicloudsdkcph==3.1.62',
    'huaweicloudsdkcpts==3.1.62',
    'huaweicloudsdkcse==3.1.62',
    'huaweicloudsdkcsms==3.1.62',
    'huaweicloudsdkcss==3.1.62',
    'huaweicloudsdkcts==3.1.62',
    'huaweicloudsdkdas==3.1.62',
    'huaweicloudsdkdataartsstudio==3.1.62',
    'huaweicloudsdkdbss==3.1.62',
    'huaweicloudsdkdc==3.1.62',
    'huaweicloudsdkdcs==3.1.62',
    'huaweicloudsdkddm==3.1.62',
    'huaweicloudsdkdds==3.1.62',
    'huaweicloudsdkdeh==3.1.62',
    'huaweicloudsdkdevsecurity==3.1.62',
    'huaweicloudsdkdevstar==3.1.62',
    'huaweicloudsdkdgc==3.1.62',
    'huaweicloudsdkdlf==3.1.62',
    'huaweicloudsdkdli==3.1.62',
    'huaweicloudsdkdns==3.1.62',
    'huaweicloudsdkdris==3.1.62',
    'huaweicloudsdkdrs==3.1.62',
    'huaweicloudsdkdsc==3.1.62',
    'huaweicloudsdkdwr==3.1.62',
    'huaweicloudsdkdws==3.1.62',
    'huaweicloudsdkec==3.1.62',
    'huaweicloudsdkecs==3.1.62',
    'huaweicloudsdkedgesec==3.1.62',
    'huaweicloudsdkeg==3.1.62',
    'huaweicloudsdkeihealth==3.1.62',
    'huaweicloudsdkeip==3.1.62',
    'huaweicloudsdkelb==3.1.62',
    'huaweicloudsdkeps==3.1.62',
    'huaweicloudsdker==3.1.62',
    'huaweicloudsdkevs==3.1.62',
    'huaweicloudsdkfrs==3.1.62',
    'huaweicloudsdkfunctiongraph==3.1.62',
    'huaweicloudsdkga==3.1.62',
    'huaweicloudsdkgaussdb==3.1.62',
    'huaweicloudsdkgaussdbfornosql==3.1.62',
    'huaweicloudsdkgaussdbforopengauss==3.1.62',
    'huaweicloudsdkges==3.1.62',
    'huaweicloudsdkgsl==3.1.62',
    'huaweicloudsdkhilens==3.1.62',
    'huaweicloudsdkhss==3.1.62',
    'huaweicloudsdkiam==3.1.62',
    'huaweicloudsdkidentitycenter==3.1.62',
    'huaweicloudsdkidentitycenterstore==3.1.62',
    'huaweicloudsdkidme==3.1.62',
    'huaweicloudsdkiec==3.1.62',
    'huaweicloudsdkief==3.1.62',
    'huaweicloudsdkimage==3.1.62',
    'huaweicloudsdkimagesearch==3.1.62',
    'huaweicloudsdkims==3.1.62',
    'huaweicloudsdkiotanalytics==3.1.62',
    'huaweicloudsdkiotda==3.1.62',
    'huaweicloudsdkiotedge==3.1.62',
    'huaweicloudsdkivs==3.1.62',
    'huaweicloudsdkkafka==3.1.62',
    'huaweicloudsdkkms==3.1.62',
    'huaweicloudsdkkoomessage==3.1.62',
    'huaweicloudsdkkps==3.1.62',
    'huaweicloudsdklakeformation==3.1.62',
    'huaweicloudsdklive==3.1.62',
    'huaweicloudsdklts==3.1.62',
    'huaweicloudsdkmapds==3.1.62',
    'huaweicloudsdkmas==3.1.62',
    'huaweicloudsdkmeeting==3.1.62',
    'huaweicloudsdkmetastudio==3.1.62',
    'huaweicloudsdkmoderation==3.1.62',
    'huaweicloudsdkmpc==3.1.62',
    'huaweicloudsdkmrs==3.1.62',
    'huaweicloudsdkmsgsms==3.1.62',
    'huaweicloudsdkmssi==3.1.62',
    'huaweicloudsdknat==3.1.62',
    'huaweicloudsdknlp==3.1.62',
    'huaweicloudsdkocr==3.1.62',
    'huaweicloudsdkoms==3.1.62',
    'huaweicloudsdkoptverse==3.1.62',
    'huaweicloudsdkorganizations==3.1.62',
    'huaweicloudsdkoroas==3.1.62',
    'huaweicloudsdkosm==3.1.62',
    'huaweicloudsdkpangulargemodels==3.1.62',
    'huaweicloudsdkprojectman==3.1.62',
    'huaweicloudsdkrabbitmq==3.1.62',
    'huaweicloudsdkram==3.1.62',
    'huaweicloudsdkrds==3.1.62',
    'huaweicloudsdkres==3.1.62',
    'huaweicloudsdkrms==3.1.62',
    'huaweicloudsdkrocketmq==3.1.62',
    'huaweicloudsdkroma==3.1.62',
    'huaweicloudsdksa==3.1.62',
    'huaweicloudsdkscm==3.1.62',
    'huaweicloudsdksdrs==3.1.62',
    'huaweicloudsdksecmaster==3.1.62',
    'huaweicloudsdkservicestage==3.1.62',
    'huaweicloudsdksfsturbo==3.1.62',
    'huaweicloudsdksis==3.1.62',
    'huaweicloudsdksmn==3.1.62',
    'huaweicloudsdksms==3.1.62',
    'huaweicloudsdkswr==3.1.62',
    'huaweicloudsdktms==3.1.62',
    'huaweicloudsdkugo==3.1.62',
    'huaweicloudsdkvas==3.1.62',
    'huaweicloudsdkvcm==3.1.62',
    'huaweicloudsdkvod==3.1.62',
    'huaweicloudsdkvpc==3.1.62',
    'huaweicloudsdkvpcep==3.1.62',
    'huaweicloudsdkwaf==3.1.62',
    'huaweicloudsdkworkspace==3.1.62',
    'huaweicloudsdkworkspaceapp==3.1.62',
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
