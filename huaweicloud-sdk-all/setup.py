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
VERSION = "3.1.63"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.63',
    'huaweicloudsdkantiddos==3.1.63',
    'huaweicloudsdkaom==3.1.63',
    'huaweicloudsdkaos==3.1.63',
    'huaweicloudsdkapig==3.1.63',
    'huaweicloudsdkapm==3.1.63',
    'huaweicloudsdkas==3.1.63',
    'huaweicloudsdkasm==3.1.63',
    'huaweicloudsdkbcs==3.1.63',
    'huaweicloudsdkbms==3.1.63',
    'huaweicloudsdkbss==3.1.63',
    'huaweicloudsdkbssintl==3.1.63',
    'huaweicloudsdkcae==3.1.63',
    'huaweicloudsdkcampusgo==3.1.63',
    'huaweicloudsdkcbh==3.1.63',
    'huaweicloudsdkcbr==3.1.63',
    'huaweicloudsdkcbs==3.1.63',
    'huaweicloudsdkcc==3.1.63',
    'huaweicloudsdkcce==3.1.63',
    'huaweicloudsdkccm==3.1.63',
    'huaweicloudsdkcdm==3.1.63',
    'huaweicloudsdkcdn==3.1.63',
    'huaweicloudsdkces==3.1.63',
    'huaweicloudsdkcfw==3.1.63',
    'huaweicloudsdkcgs==3.1.63',
    'huaweicloudsdkclassroom==3.1.63',
    'huaweicloudsdkcloudide==3.1.63',
    'huaweicloudsdkcloudpond==3.1.63',
    'huaweicloudsdkcloudrtc==3.1.63',
    'huaweicloudsdkcloudtable==3.1.63',
    'huaweicloudsdkcloudtest==3.1.63',
    'huaweicloudsdkcodeartsartifact==3.1.63',
    'huaweicloudsdkcodeartsbuild==3.1.63',
    'huaweicloudsdkcodeartscheck==3.1.63',
    'huaweicloudsdkcodeartsdeploy==3.1.63',
    'huaweicloudsdkcodeartsinspector==3.1.63',
    'huaweicloudsdkcodeartspipeline==3.1.63',
    'huaweicloudsdkcodecraft==3.1.63',
    'huaweicloudsdkcodehub==3.1.63',
    'huaweicloudsdkconfig==3.1.63',
    'huaweicloudsdkcph==3.1.63',
    'huaweicloudsdkcpts==3.1.63',
    'huaweicloudsdkcse==3.1.63',
    'huaweicloudsdkcsms==3.1.63',
    'huaweicloudsdkcss==3.1.63',
    'huaweicloudsdkcts==3.1.63',
    'huaweicloudsdkdas==3.1.63',
    'huaweicloudsdkdataartsstudio==3.1.63',
    'huaweicloudsdkdbss==3.1.63',
    'huaweicloudsdkdc==3.1.63',
    'huaweicloudsdkdcs==3.1.63',
    'huaweicloudsdkddm==3.1.63',
    'huaweicloudsdkdds==3.1.63',
    'huaweicloudsdkdeh==3.1.63',
    'huaweicloudsdkdevsecurity==3.1.63',
    'huaweicloudsdkdevstar==3.1.63',
    'huaweicloudsdkdgc==3.1.63',
    'huaweicloudsdkdlf==3.1.63',
    'huaweicloudsdkdli==3.1.63',
    'huaweicloudsdkdns==3.1.63',
    'huaweicloudsdkdris==3.1.63',
    'huaweicloudsdkdrs==3.1.63',
    'huaweicloudsdkdsc==3.1.63',
    'huaweicloudsdkdwr==3.1.63',
    'huaweicloudsdkdws==3.1.63',
    'huaweicloudsdkec==3.1.63',
    'huaweicloudsdkecs==3.1.63',
    'huaweicloudsdkedgesec==3.1.63',
    'huaweicloudsdkeg==3.1.63',
    'huaweicloudsdkeihealth==3.1.63',
    'huaweicloudsdkeip==3.1.63',
    'huaweicloudsdkelb==3.1.63',
    'huaweicloudsdkeps==3.1.63',
    'huaweicloudsdker==3.1.63',
    'huaweicloudsdkevs==3.1.63',
    'huaweicloudsdkfrs==3.1.63',
    'huaweicloudsdkfunctiongraph==3.1.63',
    'huaweicloudsdkga==3.1.63',
    'huaweicloudsdkgaussdb==3.1.63',
    'huaweicloudsdkgaussdbfornosql==3.1.63',
    'huaweicloudsdkgaussdbforopengauss==3.1.63',
    'huaweicloudsdkges==3.1.63',
    'huaweicloudsdkgsl==3.1.63',
    'huaweicloudsdkhilens==3.1.63',
    'huaweicloudsdkhss==3.1.63',
    'huaweicloudsdkiam==3.1.63',
    'huaweicloudsdkidentitycenter==3.1.63',
    'huaweicloudsdkidentitycenterstore==3.1.63',
    'huaweicloudsdkidme==3.1.63',
    'huaweicloudsdkiec==3.1.63',
    'huaweicloudsdkief==3.1.63',
    'huaweicloudsdkimage==3.1.63',
    'huaweicloudsdkimagesearch==3.1.63',
    'huaweicloudsdkims==3.1.63',
    'huaweicloudsdkiotanalytics==3.1.63',
    'huaweicloudsdkiotda==3.1.63',
    'huaweicloudsdkiotedge==3.1.63',
    'huaweicloudsdkivs==3.1.63',
    'huaweicloudsdkkafka==3.1.63',
    'huaweicloudsdkkms==3.1.63',
    'huaweicloudsdkkoomessage==3.1.63',
    'huaweicloudsdkkps==3.1.63',
    'huaweicloudsdklakeformation==3.1.63',
    'huaweicloudsdklive==3.1.63',
    'huaweicloudsdklts==3.1.63',
    'huaweicloudsdkmapds==3.1.63',
    'huaweicloudsdkmas==3.1.63',
    'huaweicloudsdkmeeting==3.1.63',
    'huaweicloudsdkmetastudio==3.1.63',
    'huaweicloudsdkmoderation==3.1.63',
    'huaweicloudsdkmpc==3.1.63',
    'huaweicloudsdkmrs==3.1.63',
    'huaweicloudsdkmsgsms==3.1.63',
    'huaweicloudsdkmssi==3.1.63',
    'huaweicloudsdknat==3.1.63',
    'huaweicloudsdknlp==3.1.63',
    'huaweicloudsdkocr==3.1.63',
    'huaweicloudsdkoms==3.1.63',
    'huaweicloudsdkoptverse==3.1.63',
    'huaweicloudsdkorganizations==3.1.63',
    'huaweicloudsdkoroas==3.1.63',
    'huaweicloudsdkosm==3.1.63',
    'huaweicloudsdkpangulargemodels==3.1.63',
    'huaweicloudsdkprojectman==3.1.63',
    'huaweicloudsdkrabbitmq==3.1.63',
    'huaweicloudsdkram==3.1.63',
    'huaweicloudsdkrds==3.1.63',
    'huaweicloudsdkres==3.1.63',
    'huaweicloudsdkrms==3.1.63',
    'huaweicloudsdkrocketmq==3.1.63',
    'huaweicloudsdkroma==3.1.63',
    'huaweicloudsdksa==3.1.63',
    'huaweicloudsdkscm==3.1.63',
    'huaweicloudsdksdrs==3.1.63',
    'huaweicloudsdksecmaster==3.1.63',
    'huaweicloudsdkservicestage==3.1.63',
    'huaweicloudsdksfsturbo==3.1.63',
    'huaweicloudsdksis==3.1.63',
    'huaweicloudsdksmn==3.1.63',
    'huaweicloudsdksms==3.1.63',
    'huaweicloudsdkswr==3.1.63',
    'huaweicloudsdktms==3.1.63',
    'huaweicloudsdkugo==3.1.63',
    'huaweicloudsdkvas==3.1.63',
    'huaweicloudsdkvcm==3.1.63',
    'huaweicloudsdkvod==3.1.63',
    'huaweicloudsdkvpc==3.1.63',
    'huaweicloudsdkvpcep==3.1.63',
    'huaweicloudsdkwaf==3.1.63',
    'huaweicloudsdkworkspace==3.1.63',
    'huaweicloudsdkworkspaceapp==3.1.63',
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
