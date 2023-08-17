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
VERSION = "3.1.54"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.54',
    'huaweicloudsdkantiddos==3.1.54',
    'huaweicloudsdkaom==3.1.54',
    'huaweicloudsdkaos==3.1.54',
    'huaweicloudsdkapig==3.1.54',
    'huaweicloudsdkapm==3.1.54',
    'huaweicloudsdkas==3.1.54',
    'huaweicloudsdkbcs==3.1.54',
    'huaweicloudsdkbms==3.1.54',
    'huaweicloudsdkbss==3.1.54',
    'huaweicloudsdkbssintl==3.1.54',
    'huaweicloudsdkcae==3.1.54',
    'huaweicloudsdkcampusgo==3.1.54',
    'huaweicloudsdkcbh==3.1.54',
    'huaweicloudsdkcbr==3.1.54',
    'huaweicloudsdkcbs==3.1.54',
    'huaweicloudsdkcc==3.1.54',
    'huaweicloudsdkcce==3.1.54',
    'huaweicloudsdkccm==3.1.54',
    'huaweicloudsdkcdm==3.1.54',
    'huaweicloudsdkcdn==3.1.54',
    'huaweicloudsdkces==3.1.54',
    'huaweicloudsdkcfw==3.1.54',
    'huaweicloudsdkcgs==3.1.54',
    'huaweicloudsdkclassroom==3.1.54',
    'huaweicloudsdkcloudide==3.1.54',
    'huaweicloudsdkcloudpipeline==3.1.54',
    'huaweicloudsdkcloudrtc==3.1.54',
    'huaweicloudsdkcloudtable==3.1.54',
    'huaweicloudsdkcloudtest==3.1.54',
    'huaweicloudsdkcodeartsartifact==3.1.54',
    'huaweicloudsdkcodeartsbuild==3.1.54',
    'huaweicloudsdkcodeartscheck==3.1.54',
    'huaweicloudsdkcodeartsdeploy==3.1.54',
    'huaweicloudsdkcodecraft==3.1.54',
    'huaweicloudsdkcodehub==3.1.54',
    'huaweicloudsdkconfig==3.1.54',
    'huaweicloudsdkcph==3.1.54',
    'huaweicloudsdkcpts==3.1.54',
    'huaweicloudsdkcse==3.1.54',
    'huaweicloudsdkcsms==3.1.54',
    'huaweicloudsdkcss==3.1.54',
    'huaweicloudsdkcts==3.1.54',
    'huaweicloudsdkdas==3.1.54',
    'huaweicloudsdkdataartsstudio==3.1.54',
    'huaweicloudsdkdbss==3.1.54',
    'huaweicloudsdkdc==3.1.54',
    'huaweicloudsdkdcs==3.1.54',
    'huaweicloudsdkddm==3.1.54',
    'huaweicloudsdkdds==3.1.54',
    'huaweicloudsdkdeh==3.1.54',
    'huaweicloudsdkdevsecurity==3.1.54',
    'huaweicloudsdkdevstar==3.1.54',
    'huaweicloudsdkdgc==3.1.54',
    'huaweicloudsdkdlf==3.1.54',
    'huaweicloudsdkdli==3.1.54',
    'huaweicloudsdkdns==3.1.54',
    'huaweicloudsdkdris==3.1.54',
    'huaweicloudsdkdrs==3.1.54',
    'huaweicloudsdkdsc==3.1.54',
    'huaweicloudsdkdwr==3.1.54',
    'huaweicloudsdkdws==3.1.54',
    'huaweicloudsdkecs==3.1.54',
    'huaweicloudsdkeg==3.1.54',
    'huaweicloudsdkeihealth==3.1.54',
    'huaweicloudsdkeip==3.1.54',
    'huaweicloudsdkelb==3.1.54',
    'huaweicloudsdkeps==3.1.54',
    'huaweicloudsdker==3.1.54',
    'huaweicloudsdkevs==3.1.54',
    'huaweicloudsdkfrs==3.1.54',
    'huaweicloudsdkfunctiongraph==3.1.54',
    'huaweicloudsdkga==3.1.54',
    'huaweicloudsdkgaussdb==3.1.54',
    'huaweicloudsdkgaussdbfornosql==3.1.54',
    'huaweicloudsdkgaussdbforopengauss==3.1.54',
    'huaweicloudsdkges==3.1.54',
    'huaweicloudsdkgsl==3.1.54',
    'huaweicloudsdkhilens==3.1.54',
    'huaweicloudsdkhss==3.1.54',
    'huaweicloudsdkiam==3.1.54',
    'huaweicloudsdkidentitycenter==3.1.54',
    'huaweicloudsdkidme==3.1.54',
    'huaweicloudsdkiec==3.1.54',
    'huaweicloudsdkief==3.1.54',
    'huaweicloudsdkies==3.1.54',
    'huaweicloudsdkimage==3.1.54',
    'huaweicloudsdkimagesearch==3.1.54',
    'huaweicloudsdkims==3.1.54',
    'huaweicloudsdkiotanalytics==3.1.54',
    'huaweicloudsdkiotda==3.1.54',
    'huaweicloudsdkiotedge==3.1.54',
    'huaweicloudsdkivs==3.1.54',
    'huaweicloudsdkkafka==3.1.54',
    'huaweicloudsdkkms==3.1.54',
    'huaweicloudsdkkoomessage==3.1.54',
    'huaweicloudsdkkps==3.1.54',
    'huaweicloudsdklakeformation==3.1.54',
    'huaweicloudsdklive==3.1.54',
    'huaweicloudsdklts==3.1.54',
    'huaweicloudsdkmapds==3.1.54',
    'huaweicloudsdkmas==3.1.54',
    'huaweicloudsdkmeeting==3.1.54',
    'huaweicloudsdkmetastudio==3.1.54',
    'huaweicloudsdkmoderation==3.1.54',
    'huaweicloudsdkmpc==3.1.54',
    'huaweicloudsdkmrs==3.1.54',
    'huaweicloudsdkmsgsms==3.1.54',
    'huaweicloudsdknat==3.1.54',
    'huaweicloudsdknlp==3.1.54',
    'huaweicloudsdkocr==3.1.54',
    'huaweicloudsdkoms==3.1.54',
    'huaweicloudsdkorganizations==3.1.54',
    'huaweicloudsdkoroas==3.1.54',
    'huaweicloudsdkosm==3.1.54',
    'huaweicloudsdkpangulargemodels==3.1.54',
    'huaweicloudsdkprojectman==3.1.54',
    'huaweicloudsdkrabbitmq==3.1.54',
    'huaweicloudsdkram==3.1.54',
    'huaweicloudsdkrds==3.1.54',
    'huaweicloudsdkres==3.1.54',
    'huaweicloudsdkrms==3.1.54',
    'huaweicloudsdkrocketmq==3.1.54',
    'huaweicloudsdkroma==3.1.54',
    'huaweicloudsdksa==3.1.54',
    'huaweicloudsdkscm==3.1.54',
    'huaweicloudsdksdrs==3.1.54',
    'huaweicloudsdksecmaster==3.1.54',
    'huaweicloudsdkservicestage==3.1.54',
    'huaweicloudsdksfsturbo==3.1.54',
    'huaweicloudsdksis==3.1.54',
    'huaweicloudsdksmn==3.1.54',
    'huaweicloudsdksms==3.1.54',
    'huaweicloudsdkswr==3.1.54',
    'huaweicloudsdktms==3.1.54',
    'huaweicloudsdkugo==3.1.54',
    'huaweicloudsdkvas==3.1.54',
    'huaweicloudsdkvcm==3.1.54',
    'huaweicloudsdkvod==3.1.54',
    'huaweicloudsdkvpc==3.1.54',
    'huaweicloudsdkvpcep==3.1.54',
    'huaweicloudsdkvss==3.1.54',
    'huaweicloudsdkwaf==3.1.54',
    'huaweicloudsdkworkspace==3.1.54',
    'huaweicloudsdkworkspaceapp==3.1.54',
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
