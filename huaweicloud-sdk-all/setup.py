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
VERSION = "3.1.59"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.59',
    'huaweicloudsdkantiddos==3.1.59',
    'huaweicloudsdkaom==3.1.59',
    'huaweicloudsdkaos==3.1.59',
    'huaweicloudsdkapig==3.1.59',
    'huaweicloudsdkapm==3.1.59',
    'huaweicloudsdkas==3.1.59',
    'huaweicloudsdkbcs==3.1.59',
    'huaweicloudsdkbms==3.1.59',
    'huaweicloudsdkbss==3.1.59',
    'huaweicloudsdkbssintl==3.1.59',
    'huaweicloudsdkcae==3.1.59',
    'huaweicloudsdkcampusgo==3.1.59',
    'huaweicloudsdkcbh==3.1.59',
    'huaweicloudsdkcbr==3.1.59',
    'huaweicloudsdkcbs==3.1.59',
    'huaweicloudsdkcc==3.1.59',
    'huaweicloudsdkcce==3.1.59',
    'huaweicloudsdkccm==3.1.59',
    'huaweicloudsdkcdm==3.1.59',
    'huaweicloudsdkcdn==3.1.59',
    'huaweicloudsdkces==3.1.59',
    'huaweicloudsdkcfw==3.1.59',
    'huaweicloudsdkcgs==3.1.59',
    'huaweicloudsdkclassroom==3.1.59',
    'huaweicloudsdkcloudide==3.1.59',
    'huaweicloudsdkcloudpond==3.1.59',
    'huaweicloudsdkcloudrtc==3.1.59',
    'huaweicloudsdkcloudtable==3.1.59',
    'huaweicloudsdkcloudtest==3.1.59',
    'huaweicloudsdkcodeartsartifact==3.1.59',
    'huaweicloudsdkcodeartsbuild==3.1.59',
    'huaweicloudsdkcodeartscheck==3.1.59',
    'huaweicloudsdkcodeartsdeploy==3.1.59',
    'huaweicloudsdkcodeartsinspector==3.1.59',
    'huaweicloudsdkcodeartspipeline==3.1.59',
    'huaweicloudsdkcodecraft==3.1.59',
    'huaweicloudsdkcodehub==3.1.59',
    'huaweicloudsdkconfig==3.1.59',
    'huaweicloudsdkcph==3.1.59',
    'huaweicloudsdkcpts==3.1.59',
    'huaweicloudsdkcse==3.1.59',
    'huaweicloudsdkcsms==3.1.59',
    'huaweicloudsdkcss==3.1.59',
    'huaweicloudsdkcts==3.1.59',
    'huaweicloudsdkdas==3.1.59',
    'huaweicloudsdkdataartsstudio==3.1.59',
    'huaweicloudsdkdbss==3.1.59',
    'huaweicloudsdkdc==3.1.59',
    'huaweicloudsdkdcs==3.1.59',
    'huaweicloudsdkddm==3.1.59',
    'huaweicloudsdkdds==3.1.59',
    'huaweicloudsdkdeh==3.1.59',
    'huaweicloudsdkdevsecurity==3.1.59',
    'huaweicloudsdkdevstar==3.1.59',
    'huaweicloudsdkdgc==3.1.59',
    'huaweicloudsdkdlf==3.1.59',
    'huaweicloudsdkdli==3.1.59',
    'huaweicloudsdkdns==3.1.59',
    'huaweicloudsdkdris==3.1.59',
    'huaweicloudsdkdrs==3.1.59',
    'huaweicloudsdkdsc==3.1.59',
    'huaweicloudsdkdwr==3.1.59',
    'huaweicloudsdkdws==3.1.59',
    'huaweicloudsdkec==3.1.59',
    'huaweicloudsdkecs==3.1.59',
    'huaweicloudsdkedgesec==3.1.59',
    'huaweicloudsdkeg==3.1.59',
    'huaweicloudsdkeihealth==3.1.59',
    'huaweicloudsdkeip==3.1.59',
    'huaweicloudsdkelb==3.1.59',
    'huaweicloudsdkeps==3.1.59',
    'huaweicloudsdker==3.1.59',
    'huaweicloudsdkevs==3.1.59',
    'huaweicloudsdkfrs==3.1.59',
    'huaweicloudsdkfunctiongraph==3.1.59',
    'huaweicloudsdkga==3.1.59',
    'huaweicloudsdkgaussdb==3.1.59',
    'huaweicloudsdkgaussdbfornosql==3.1.59',
    'huaweicloudsdkgaussdbforopengauss==3.1.59',
    'huaweicloudsdkges==3.1.59',
    'huaweicloudsdkgsl==3.1.59',
    'huaweicloudsdkhilens==3.1.59',
    'huaweicloudsdkhss==3.1.59',
    'huaweicloudsdkiam==3.1.59',
    'huaweicloudsdkidentitycenter==3.1.59',
    'huaweicloudsdkidme==3.1.59',
    'huaweicloudsdkiec==3.1.59',
    'huaweicloudsdkief==3.1.59',
    'huaweicloudsdkimage==3.1.59',
    'huaweicloudsdkimagesearch==3.1.59',
    'huaweicloudsdkims==3.1.59',
    'huaweicloudsdkiotanalytics==3.1.59',
    'huaweicloudsdkiotda==3.1.59',
    'huaweicloudsdkiotedge==3.1.59',
    'huaweicloudsdkivs==3.1.59',
    'huaweicloudsdkkafka==3.1.59',
    'huaweicloudsdkkms==3.1.59',
    'huaweicloudsdkkoomessage==3.1.59',
    'huaweicloudsdkkps==3.1.59',
    'huaweicloudsdklakeformation==3.1.59',
    'huaweicloudsdklive==3.1.59',
    'huaweicloudsdklts==3.1.59',
    'huaweicloudsdkmapds==3.1.59',
    'huaweicloudsdkmas==3.1.59',
    'huaweicloudsdkmeeting==3.1.59',
    'huaweicloudsdkmetastudio==3.1.59',
    'huaweicloudsdkmoderation==3.1.59',
    'huaweicloudsdkmpc==3.1.59',
    'huaweicloudsdkmrs==3.1.59',
    'huaweicloudsdkmsgsms==3.1.59',
    'huaweicloudsdkmssi==3.1.59',
    'huaweicloudsdknat==3.1.59',
    'huaweicloudsdknlp==3.1.59',
    'huaweicloudsdkocr==3.1.59',
    'huaweicloudsdkoms==3.1.59',
    'huaweicloudsdkoptverse==3.1.59',
    'huaweicloudsdkorganizations==3.1.59',
    'huaweicloudsdkoroas==3.1.59',
    'huaweicloudsdkosm==3.1.59',
    'huaweicloudsdkpangulargemodels==3.1.59',
    'huaweicloudsdkprojectman==3.1.59',
    'huaweicloudsdkrabbitmq==3.1.59',
    'huaweicloudsdkram==3.1.59',
    'huaweicloudsdkrds==3.1.59',
    'huaweicloudsdkres==3.1.59',
    'huaweicloudsdkrms==3.1.59',
    'huaweicloudsdkrocketmq==3.1.59',
    'huaweicloudsdkroma==3.1.59',
    'huaweicloudsdksa==3.1.59',
    'huaweicloudsdkscm==3.1.59',
    'huaweicloudsdksdrs==3.1.59',
    'huaweicloudsdksecmaster==3.1.59',
    'huaweicloudsdkservicestage==3.1.59',
    'huaweicloudsdksfsturbo==3.1.59',
    'huaweicloudsdksis==3.1.59',
    'huaweicloudsdksmn==3.1.59',
    'huaweicloudsdksms==3.1.59',
    'huaweicloudsdkswr==3.1.59',
    'huaweicloudsdktms==3.1.59',
    'huaweicloudsdkugo==3.1.59',
    'huaweicloudsdkvas==3.1.59',
    'huaweicloudsdkvcm==3.1.59',
    'huaweicloudsdkvod==3.1.59',
    'huaweicloudsdkvpc==3.1.59',
    'huaweicloudsdkvpcep==3.1.59',
    'huaweicloudsdkwaf==3.1.59',
    'huaweicloudsdkworkspace==3.1.59',
    'huaweicloudsdkworkspaceapp==3.1.59',
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
