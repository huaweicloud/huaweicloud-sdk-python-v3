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
VERSION = "3.1.52"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.52',
    'huaweicloudsdkantiddos==3.1.52',
    'huaweicloudsdkaom==3.1.52',
    'huaweicloudsdkaos==3.1.52',
    'huaweicloudsdkapig==3.1.52',
    'huaweicloudsdkapm==3.1.52',
    'huaweicloudsdkas==3.1.52',
    'huaweicloudsdkbcs==3.1.52',
    'huaweicloudsdkbms==3.1.52',
    'huaweicloudsdkbss==3.1.52',
    'huaweicloudsdkbssintl==3.1.52',
    'huaweicloudsdkcae==3.1.52',
    'huaweicloudsdkcampusgo==3.1.52',
    'huaweicloudsdkcbh==3.1.52',
    'huaweicloudsdkcbr==3.1.52',
    'huaweicloudsdkcbs==3.1.52',
    'huaweicloudsdkcc==3.1.52',
    'huaweicloudsdkcce==3.1.52',
    'huaweicloudsdkccm==3.1.52',
    'huaweicloudsdkcdm==3.1.52',
    'huaweicloudsdkcdn==3.1.52',
    'huaweicloudsdkces==3.1.52',
    'huaweicloudsdkcfw==3.1.52',
    'huaweicloudsdkcgs==3.1.52',
    'huaweicloudsdkclassroom==3.1.52',
    'huaweicloudsdkcloudide==3.1.52',
    'huaweicloudsdkcloudpipeline==3.1.52',
    'huaweicloudsdkcloudrtc==3.1.52',
    'huaweicloudsdkcloudtable==3.1.52',
    'huaweicloudsdkcloudtest==3.1.52',
    'huaweicloudsdkcodeartsartifact==3.1.52',
    'huaweicloudsdkcodeartsbuild==3.1.52',
    'huaweicloudsdkcodeartscheck==3.1.52',
    'huaweicloudsdkcodeartsdeploy==3.1.52',
    'huaweicloudsdkcodecraft==3.1.52',
    'huaweicloudsdkcodehub==3.1.52',
    'huaweicloudsdkconfig==3.1.52',
    'huaweicloudsdkcph==3.1.52',
    'huaweicloudsdkcpts==3.1.52',
    'huaweicloudsdkcse==3.1.52',
    'huaweicloudsdkcsms==3.1.52',
    'huaweicloudsdkcss==3.1.52',
    'huaweicloudsdkcts==3.1.52',
    'huaweicloudsdkdas==3.1.52',
    'huaweicloudsdkdataartsstudio==3.1.52',
    'huaweicloudsdkdbss==3.1.52',
    'huaweicloudsdkdc==3.1.52',
    'huaweicloudsdkdcs==3.1.52',
    'huaweicloudsdkddm==3.1.52',
    'huaweicloudsdkdds==3.1.52',
    'huaweicloudsdkdeh==3.1.52',
    'huaweicloudsdkdevsecurity==3.1.52',
    'huaweicloudsdkdevstar==3.1.52',
    'huaweicloudsdkdgc==3.1.52',
    'huaweicloudsdkdlf==3.1.52',
    'huaweicloudsdkdli==3.1.52',
    'huaweicloudsdkdns==3.1.52',
    'huaweicloudsdkdris==3.1.52',
    'huaweicloudsdkdrs==3.1.52',
    'huaweicloudsdkdsc==3.1.52',
    'huaweicloudsdkdwr==3.1.52',
    'huaweicloudsdkdws==3.1.52',
    'huaweicloudsdkecs==3.1.52',
    'huaweicloudsdkeg==3.1.52',
    'huaweicloudsdkeihealth==3.1.52',
    'huaweicloudsdkeip==3.1.52',
    'huaweicloudsdkelb==3.1.52',
    'huaweicloudsdkeps==3.1.52',
    'huaweicloudsdker==3.1.52',
    'huaweicloudsdkevs==3.1.52',
    'huaweicloudsdkfrs==3.1.52',
    'huaweicloudsdkfunctiongraph==3.1.52',
    'huaweicloudsdkga==3.1.52',
    'huaweicloudsdkgaussdb==3.1.52',
    'huaweicloudsdkgaussdbfornosql==3.1.52',
    'huaweicloudsdkgaussdbforopengauss==3.1.52',
    'huaweicloudsdkges==3.1.52',
    'huaweicloudsdkgsl==3.1.52',
    'huaweicloudsdkhilens==3.1.52',
    'huaweicloudsdkhss==3.1.52',
    'huaweicloudsdkiam==3.1.52',
    'huaweicloudsdkidentitycenter==3.1.52',
    'huaweicloudsdkidme==3.1.52',
    'huaweicloudsdkiec==3.1.52',
    'huaweicloudsdkief==3.1.52',
    'huaweicloudsdkies==3.1.52',
    'huaweicloudsdkimage==3.1.52',
    'huaweicloudsdkimagesearch==3.1.52',
    'huaweicloudsdkims==3.1.52',
    'huaweicloudsdkiotanalytics==3.1.52',
    'huaweicloudsdkiotda==3.1.52',
    'huaweicloudsdkiotedge==3.1.52',
    'huaweicloudsdkivs==3.1.52',
    'huaweicloudsdkkafka==3.1.52',
    'huaweicloudsdkkms==3.1.52',
    'huaweicloudsdkkoomessage==3.1.52',
    'huaweicloudsdkkps==3.1.52',
    'huaweicloudsdklakeformation==3.1.52',
    'huaweicloudsdklive==3.1.52',
    'huaweicloudsdklts==3.1.52',
    'huaweicloudsdkmapds==3.1.52',
    'huaweicloudsdkmas==3.1.52',
    'huaweicloudsdkmeeting==3.1.52',
    'huaweicloudsdkmetastudio==3.1.52',
    'huaweicloudsdkmoderation==3.1.52',
    'huaweicloudsdkmpc==3.1.52',
    'huaweicloudsdkmrs==3.1.52',
    'huaweicloudsdkmsgsms==3.1.52',
    'huaweicloudsdknat==3.1.52',
    'huaweicloudsdknlp==3.1.52',
    'huaweicloudsdkocr==3.1.52',
    'huaweicloudsdkoms==3.1.52',
    'huaweicloudsdkorganizations==3.1.52',
    'huaweicloudsdkoroas==3.1.52',
    'huaweicloudsdkosm==3.1.52',
    'huaweicloudsdkpangulargemodels==3.1.52',
    'huaweicloudsdkprojectman==3.1.52',
    'huaweicloudsdkrabbitmq==3.1.52',
    'huaweicloudsdkram==3.1.52',
    'huaweicloudsdkrds==3.1.52',
    'huaweicloudsdkres==3.1.52',
    'huaweicloudsdkrms==3.1.52',
    'huaweicloudsdkrocketmq==3.1.52',
    'huaweicloudsdkroma==3.1.52',
    'huaweicloudsdksa==3.1.52',
    'huaweicloudsdkscm==3.1.52',
    'huaweicloudsdksdrs==3.1.52',
    'huaweicloudsdksecmaster==3.1.52',
    'huaweicloudsdkservicestage==3.1.52',
    'huaweicloudsdksfsturbo==3.1.52',
    'huaweicloudsdksis==3.1.52',
    'huaweicloudsdksmn==3.1.52',
    'huaweicloudsdksms==3.1.52',
    'huaweicloudsdkswr==3.1.52',
    'huaweicloudsdktms==3.1.52',
    'huaweicloudsdkugo==3.1.52',
    'huaweicloudsdkvas==3.1.52',
    'huaweicloudsdkvcm==3.1.52',
    'huaweicloudsdkvod==3.1.52',
    'huaweicloudsdkvpc==3.1.52',
    'huaweicloudsdkvpcep==3.1.52',
    'huaweicloudsdkvss==3.1.52',
    'huaweicloudsdkwaf==3.1.52',
    'huaweicloudsdkworkspace==3.1.52',
    'huaweicloudsdkworkspaceapp==3.1.52',
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
