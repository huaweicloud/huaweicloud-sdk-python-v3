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
VERSION = "3.1.56"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.56',
    'huaweicloudsdkantiddos==3.1.56',
    'huaweicloudsdkaom==3.1.56',
    'huaweicloudsdkaos==3.1.56',
    'huaweicloudsdkapig==3.1.56',
    'huaweicloudsdkapm==3.1.56',
    'huaweicloudsdkas==3.1.56',
    'huaweicloudsdkbcs==3.1.56',
    'huaweicloudsdkbms==3.1.56',
    'huaweicloudsdkbss==3.1.56',
    'huaweicloudsdkbssintl==3.1.56',
    'huaweicloudsdkcae==3.1.56',
    'huaweicloudsdkcampusgo==3.1.56',
    'huaweicloudsdkcbh==3.1.56',
    'huaweicloudsdkcbr==3.1.56',
    'huaweicloudsdkcbs==3.1.56',
    'huaweicloudsdkcc==3.1.56',
    'huaweicloudsdkcce==3.1.56',
    'huaweicloudsdkccm==3.1.56',
    'huaweicloudsdkcdm==3.1.56',
    'huaweicloudsdkcdn==3.1.56',
    'huaweicloudsdkces==3.1.56',
    'huaweicloudsdkcfw==3.1.56',
    'huaweicloudsdkcgs==3.1.56',
    'huaweicloudsdkclassroom==3.1.56',
    'huaweicloudsdkcloudide==3.1.56',
    'huaweicloudsdkcloudpipeline==3.1.56',
    'huaweicloudsdkcloudrtc==3.1.56',
    'huaweicloudsdkcloudtable==3.1.56',
    'huaweicloudsdkcloudtest==3.1.56',
    'huaweicloudsdkcodeartsartifact==3.1.56',
    'huaweicloudsdkcodeartsbuild==3.1.56',
    'huaweicloudsdkcodeartscheck==3.1.56',
    'huaweicloudsdkcodeartsdeploy==3.1.56',
    'huaweicloudsdkcodecraft==3.1.56',
    'huaweicloudsdkcodehub==3.1.56',
    'huaweicloudsdkconfig==3.1.56',
    'huaweicloudsdkcph==3.1.56',
    'huaweicloudsdkcpts==3.1.56',
    'huaweicloudsdkcse==3.1.56',
    'huaweicloudsdkcsms==3.1.56',
    'huaweicloudsdkcss==3.1.56',
    'huaweicloudsdkcts==3.1.56',
    'huaweicloudsdkdas==3.1.56',
    'huaweicloudsdkdataartsstudio==3.1.56',
    'huaweicloudsdkdbss==3.1.56',
    'huaweicloudsdkdc==3.1.56',
    'huaweicloudsdkdcs==3.1.56',
    'huaweicloudsdkddm==3.1.56',
    'huaweicloudsdkdds==3.1.56',
    'huaweicloudsdkdeh==3.1.56',
    'huaweicloudsdkdevsecurity==3.1.56',
    'huaweicloudsdkdevstar==3.1.56',
    'huaweicloudsdkdgc==3.1.56',
    'huaweicloudsdkdlf==3.1.56',
    'huaweicloudsdkdli==3.1.56',
    'huaweicloudsdkdns==3.1.56',
    'huaweicloudsdkdris==3.1.56',
    'huaweicloudsdkdrs==3.1.56',
    'huaweicloudsdkdsc==3.1.56',
    'huaweicloudsdkdwr==3.1.56',
    'huaweicloudsdkdws==3.1.56',
    'huaweicloudsdkecs==3.1.56',
    'huaweicloudsdkedgesec==3.1.56',
    'huaweicloudsdkeg==3.1.56',
    'huaweicloudsdkeihealth==3.1.56',
    'huaweicloudsdkeip==3.1.56',
    'huaweicloudsdkelb==3.1.56',
    'huaweicloudsdkeps==3.1.56',
    'huaweicloudsdker==3.1.56',
    'huaweicloudsdkevs==3.1.56',
    'huaweicloudsdkfrs==3.1.56',
    'huaweicloudsdkfunctiongraph==3.1.56',
    'huaweicloudsdkga==3.1.56',
    'huaweicloudsdkgaussdb==3.1.56',
    'huaweicloudsdkgaussdbfornosql==3.1.56',
    'huaweicloudsdkgaussdbforopengauss==3.1.56',
    'huaweicloudsdkges==3.1.56',
    'huaweicloudsdkgsl==3.1.56',
    'huaweicloudsdkhilens==3.1.56',
    'huaweicloudsdkhss==3.1.56',
    'huaweicloudsdkiam==3.1.56',
    'huaweicloudsdkidentitycenter==3.1.56',
    'huaweicloudsdkidme==3.1.56',
    'huaweicloudsdkiec==3.1.56',
    'huaweicloudsdkief==3.1.56',
    'huaweicloudsdkies==3.1.56',
    'huaweicloudsdkimage==3.1.56',
    'huaweicloudsdkimagesearch==3.1.56',
    'huaweicloudsdkims==3.1.56',
    'huaweicloudsdkiotanalytics==3.1.56',
    'huaweicloudsdkiotda==3.1.56',
    'huaweicloudsdkiotedge==3.1.56',
    'huaweicloudsdkivs==3.1.56',
    'huaweicloudsdkkafka==3.1.56',
    'huaweicloudsdkkms==3.1.56',
    'huaweicloudsdkkoomessage==3.1.56',
    'huaweicloudsdkkps==3.1.56',
    'huaweicloudsdklakeformation==3.1.56',
    'huaweicloudsdklive==3.1.56',
    'huaweicloudsdklts==3.1.56',
    'huaweicloudsdkmapds==3.1.56',
    'huaweicloudsdkmas==3.1.56',
    'huaweicloudsdkmeeting==3.1.56',
    'huaweicloudsdkmetastudio==3.1.56',
    'huaweicloudsdkmoderation==3.1.56',
    'huaweicloudsdkmpc==3.1.56',
    'huaweicloudsdkmrs==3.1.56',
    'huaweicloudsdkmsgsms==3.1.56',
    'huaweicloudsdknat==3.1.56',
    'huaweicloudsdknlp==3.1.56',
    'huaweicloudsdkocr==3.1.56',
    'huaweicloudsdkoms==3.1.56',
    'huaweicloudsdkoptverse==3.1.56',
    'huaweicloudsdkorganizations==3.1.56',
    'huaweicloudsdkoroas==3.1.56',
    'huaweicloudsdkosm==3.1.56',
    'huaweicloudsdkpangulargemodels==3.1.56',
    'huaweicloudsdkprojectman==3.1.56',
    'huaweicloudsdkrabbitmq==3.1.56',
    'huaweicloudsdkram==3.1.56',
    'huaweicloudsdkrds==3.1.56',
    'huaweicloudsdkres==3.1.56',
    'huaweicloudsdkrms==3.1.56',
    'huaweicloudsdkrocketmq==3.1.56',
    'huaweicloudsdkroma==3.1.56',
    'huaweicloudsdksa==3.1.56',
    'huaweicloudsdkscm==3.1.56',
    'huaweicloudsdksdrs==3.1.56',
    'huaweicloudsdksecmaster==3.1.56',
    'huaweicloudsdkservicestage==3.1.56',
    'huaweicloudsdksfsturbo==3.1.56',
    'huaweicloudsdksis==3.1.56',
    'huaweicloudsdksmn==3.1.56',
    'huaweicloudsdksms==3.1.56',
    'huaweicloudsdkswr==3.1.56',
    'huaweicloudsdktms==3.1.56',
    'huaweicloudsdkugo==3.1.56',
    'huaweicloudsdkvas==3.1.56',
    'huaweicloudsdkvcm==3.1.56',
    'huaweicloudsdkvod==3.1.56',
    'huaweicloudsdkvpc==3.1.56',
    'huaweicloudsdkvpcep==3.1.56',
    'huaweicloudsdkvss==3.1.56',
    'huaweicloudsdkwaf==3.1.56',
    'huaweicloudsdkworkspace==3.1.56',
    'huaweicloudsdkworkspaceapp==3.1.56',
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
