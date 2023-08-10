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
VERSION = "3.1.53"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.53',
    'huaweicloudsdkantiddos==3.1.53',
    'huaweicloudsdkaom==3.1.53',
    'huaweicloudsdkaos==3.1.53',
    'huaweicloudsdkapig==3.1.53',
    'huaweicloudsdkapm==3.1.53',
    'huaweicloudsdkas==3.1.53',
    'huaweicloudsdkbcs==3.1.53',
    'huaweicloudsdkbms==3.1.53',
    'huaweicloudsdkbss==3.1.53',
    'huaweicloudsdkbssintl==3.1.53',
    'huaweicloudsdkcae==3.1.53',
    'huaweicloudsdkcampusgo==3.1.53',
    'huaweicloudsdkcbh==3.1.53',
    'huaweicloudsdkcbr==3.1.53',
    'huaweicloudsdkcbs==3.1.53',
    'huaweicloudsdkcc==3.1.53',
    'huaweicloudsdkcce==3.1.53',
    'huaweicloudsdkccm==3.1.53',
    'huaweicloudsdkcdm==3.1.53',
    'huaweicloudsdkcdn==3.1.53',
    'huaweicloudsdkces==3.1.53',
    'huaweicloudsdkcfw==3.1.53',
    'huaweicloudsdkcgs==3.1.53',
    'huaweicloudsdkclassroom==3.1.53',
    'huaweicloudsdkcloudide==3.1.53',
    'huaweicloudsdkcloudpipeline==3.1.53',
    'huaweicloudsdkcloudrtc==3.1.53',
    'huaweicloudsdkcloudtable==3.1.53',
    'huaweicloudsdkcloudtest==3.1.53',
    'huaweicloudsdkcodeartsartifact==3.1.53',
    'huaweicloudsdkcodeartsbuild==3.1.53',
    'huaweicloudsdkcodeartscheck==3.1.53',
    'huaweicloudsdkcodeartsdeploy==3.1.53',
    'huaweicloudsdkcodecraft==3.1.53',
    'huaweicloudsdkcodehub==3.1.53',
    'huaweicloudsdkconfig==3.1.53',
    'huaweicloudsdkcph==3.1.53',
    'huaweicloudsdkcpts==3.1.53',
    'huaweicloudsdkcse==3.1.53',
    'huaweicloudsdkcsms==3.1.53',
    'huaweicloudsdkcss==3.1.53',
    'huaweicloudsdkcts==3.1.53',
    'huaweicloudsdkdas==3.1.53',
    'huaweicloudsdkdataartsstudio==3.1.53',
    'huaweicloudsdkdbss==3.1.53',
    'huaweicloudsdkdc==3.1.53',
    'huaweicloudsdkdcs==3.1.53',
    'huaweicloudsdkddm==3.1.53',
    'huaweicloudsdkdds==3.1.53',
    'huaweicloudsdkdeh==3.1.53',
    'huaweicloudsdkdevsecurity==3.1.53',
    'huaweicloudsdkdevstar==3.1.53',
    'huaweicloudsdkdgc==3.1.53',
    'huaweicloudsdkdlf==3.1.53',
    'huaweicloudsdkdli==3.1.53',
    'huaweicloudsdkdns==3.1.53',
    'huaweicloudsdkdris==3.1.53',
    'huaweicloudsdkdrs==3.1.53',
    'huaweicloudsdkdsc==3.1.53',
    'huaweicloudsdkdwr==3.1.53',
    'huaweicloudsdkdws==3.1.53',
    'huaweicloudsdkecs==3.1.53',
    'huaweicloudsdkeg==3.1.53',
    'huaweicloudsdkeihealth==3.1.53',
    'huaweicloudsdkeip==3.1.53',
    'huaweicloudsdkelb==3.1.53',
    'huaweicloudsdkeps==3.1.53',
    'huaweicloudsdker==3.1.53',
    'huaweicloudsdkevs==3.1.53',
    'huaweicloudsdkfrs==3.1.53',
    'huaweicloudsdkfunctiongraph==3.1.53',
    'huaweicloudsdkga==3.1.53',
    'huaweicloudsdkgaussdb==3.1.53',
    'huaweicloudsdkgaussdbfornosql==3.1.53',
    'huaweicloudsdkgaussdbforopengauss==3.1.53',
    'huaweicloudsdkges==3.1.53',
    'huaweicloudsdkgsl==3.1.53',
    'huaweicloudsdkhilens==3.1.53',
    'huaweicloudsdkhss==3.1.53',
    'huaweicloudsdkiam==3.1.53',
    'huaweicloudsdkidentitycenter==3.1.53',
    'huaweicloudsdkidme==3.1.53',
    'huaweicloudsdkiec==3.1.53',
    'huaweicloudsdkief==3.1.53',
    'huaweicloudsdkies==3.1.53',
    'huaweicloudsdkimage==3.1.53',
    'huaweicloudsdkimagesearch==3.1.53',
    'huaweicloudsdkims==3.1.53',
    'huaweicloudsdkiotanalytics==3.1.53',
    'huaweicloudsdkiotda==3.1.53',
    'huaweicloudsdkiotedge==3.1.53',
    'huaweicloudsdkivs==3.1.53',
    'huaweicloudsdkkafka==3.1.53',
    'huaweicloudsdkkms==3.1.53',
    'huaweicloudsdkkoomessage==3.1.53',
    'huaweicloudsdkkps==3.1.53',
    'huaweicloudsdklakeformation==3.1.53',
    'huaweicloudsdklive==3.1.53',
    'huaweicloudsdklts==3.1.53',
    'huaweicloudsdkmapds==3.1.53',
    'huaweicloudsdkmas==3.1.53',
    'huaweicloudsdkmeeting==3.1.53',
    'huaweicloudsdkmetastudio==3.1.53',
    'huaweicloudsdkmoderation==3.1.53',
    'huaweicloudsdkmpc==3.1.53',
    'huaweicloudsdkmrs==3.1.53',
    'huaweicloudsdkmsgsms==3.1.53',
    'huaweicloudsdknat==3.1.53',
    'huaweicloudsdknlp==3.1.53',
    'huaweicloudsdkocr==3.1.53',
    'huaweicloudsdkoms==3.1.53',
    'huaweicloudsdkorganizations==3.1.53',
    'huaweicloudsdkoroas==3.1.53',
    'huaweicloudsdkosm==3.1.53',
    'huaweicloudsdkpangulargemodels==3.1.53',
    'huaweicloudsdkprojectman==3.1.53',
    'huaweicloudsdkrabbitmq==3.1.53',
    'huaweicloudsdkram==3.1.53',
    'huaweicloudsdkrds==3.1.53',
    'huaweicloudsdkres==3.1.53',
    'huaweicloudsdkrms==3.1.53',
    'huaweicloudsdkrocketmq==3.1.53',
    'huaweicloudsdkroma==3.1.53',
    'huaweicloudsdksa==3.1.53',
    'huaweicloudsdkscm==3.1.53',
    'huaweicloudsdksdrs==3.1.53',
    'huaweicloudsdksecmaster==3.1.53',
    'huaweicloudsdkservicestage==3.1.53',
    'huaweicloudsdksfsturbo==3.1.53',
    'huaweicloudsdksis==3.1.53',
    'huaweicloudsdksmn==3.1.53',
    'huaweicloudsdksms==3.1.53',
    'huaweicloudsdkswr==3.1.53',
    'huaweicloudsdktms==3.1.53',
    'huaweicloudsdkugo==3.1.53',
    'huaweicloudsdkvas==3.1.53',
    'huaweicloudsdkvcm==3.1.53',
    'huaweicloudsdkvod==3.1.53',
    'huaweicloudsdkvpc==3.1.53',
    'huaweicloudsdkvpcep==3.1.53',
    'huaweicloudsdkvss==3.1.53',
    'huaweicloudsdkwaf==3.1.53',
    'huaweicloudsdkworkspace==3.1.53',
    'huaweicloudsdkworkspaceapp==3.1.53',
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
