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
VERSION = "3.1.61"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.61',
    'huaweicloudsdkantiddos==3.1.61',
    'huaweicloudsdkaom==3.1.61',
    'huaweicloudsdkaos==3.1.61',
    'huaweicloudsdkapig==3.1.61',
    'huaweicloudsdkapm==3.1.61',
    'huaweicloudsdkas==3.1.61',
    'huaweicloudsdkasm==3.1.61',
    'huaweicloudsdkbcs==3.1.61',
    'huaweicloudsdkbms==3.1.61',
    'huaweicloudsdkbss==3.1.61',
    'huaweicloudsdkbssintl==3.1.61',
    'huaweicloudsdkcae==3.1.61',
    'huaweicloudsdkcampusgo==3.1.61',
    'huaweicloudsdkcbh==3.1.61',
    'huaweicloudsdkcbr==3.1.61',
    'huaweicloudsdkcbs==3.1.61',
    'huaweicloudsdkcc==3.1.61',
    'huaweicloudsdkcce==3.1.61',
    'huaweicloudsdkccm==3.1.61',
    'huaweicloudsdkcdm==3.1.61',
    'huaweicloudsdkcdn==3.1.61',
    'huaweicloudsdkces==3.1.61',
    'huaweicloudsdkcfw==3.1.61',
    'huaweicloudsdkcgs==3.1.61',
    'huaweicloudsdkclassroom==3.1.61',
    'huaweicloudsdkcloudide==3.1.61',
    'huaweicloudsdkcloudpond==3.1.61',
    'huaweicloudsdkcloudrtc==3.1.61',
    'huaweicloudsdkcloudtable==3.1.61',
    'huaweicloudsdkcloudtest==3.1.61',
    'huaweicloudsdkcodeartsartifact==3.1.61',
    'huaweicloudsdkcodeartsbuild==3.1.61',
    'huaweicloudsdkcodeartscheck==3.1.61',
    'huaweicloudsdkcodeartsdeploy==3.1.61',
    'huaweicloudsdkcodeartsinspector==3.1.61',
    'huaweicloudsdkcodeartspipeline==3.1.61',
    'huaweicloudsdkcodecraft==3.1.61',
    'huaweicloudsdkcodehub==3.1.61',
    'huaweicloudsdkconfig==3.1.61',
    'huaweicloudsdkcph==3.1.61',
    'huaweicloudsdkcpts==3.1.61',
    'huaweicloudsdkcse==3.1.61',
    'huaweicloudsdkcsms==3.1.61',
    'huaweicloudsdkcss==3.1.61',
    'huaweicloudsdkcts==3.1.61',
    'huaweicloudsdkdas==3.1.61',
    'huaweicloudsdkdataartsstudio==3.1.61',
    'huaweicloudsdkdbss==3.1.61',
    'huaweicloudsdkdc==3.1.61',
    'huaweicloudsdkdcs==3.1.61',
    'huaweicloudsdkddm==3.1.61',
    'huaweicloudsdkdds==3.1.61',
    'huaweicloudsdkdeh==3.1.61',
    'huaweicloudsdkdevsecurity==3.1.61',
    'huaweicloudsdkdevstar==3.1.61',
    'huaweicloudsdkdgc==3.1.61',
    'huaweicloudsdkdlf==3.1.61',
    'huaweicloudsdkdli==3.1.61',
    'huaweicloudsdkdns==3.1.61',
    'huaweicloudsdkdris==3.1.61',
    'huaweicloudsdkdrs==3.1.61',
    'huaweicloudsdkdsc==3.1.61',
    'huaweicloudsdkdwr==3.1.61',
    'huaweicloudsdkdws==3.1.61',
    'huaweicloudsdkec==3.1.61',
    'huaweicloudsdkecs==3.1.61',
    'huaweicloudsdkedgesec==3.1.61',
    'huaweicloudsdkeg==3.1.61',
    'huaweicloudsdkeihealth==3.1.61',
    'huaweicloudsdkeip==3.1.61',
    'huaweicloudsdkelb==3.1.61',
    'huaweicloudsdkeps==3.1.61',
    'huaweicloudsdker==3.1.61',
    'huaweicloudsdkevs==3.1.61',
    'huaweicloudsdkfrs==3.1.61',
    'huaweicloudsdkfunctiongraph==3.1.61',
    'huaweicloudsdkga==3.1.61',
    'huaweicloudsdkgaussdb==3.1.61',
    'huaweicloudsdkgaussdbfornosql==3.1.61',
    'huaweicloudsdkgaussdbforopengauss==3.1.61',
    'huaweicloudsdkges==3.1.61',
    'huaweicloudsdkgsl==3.1.61',
    'huaweicloudsdkhilens==3.1.61',
    'huaweicloudsdkhss==3.1.61',
    'huaweicloudsdkiam==3.1.61',
    'huaweicloudsdkidentitycenter==3.1.61',
    'huaweicloudsdkidentitycenterstore==3.1.61',
    'huaweicloudsdkidme==3.1.61',
    'huaweicloudsdkiec==3.1.61',
    'huaweicloudsdkief==3.1.61',
    'huaweicloudsdkimage==3.1.61',
    'huaweicloudsdkimagesearch==3.1.61',
    'huaweicloudsdkims==3.1.61',
    'huaweicloudsdkiotanalytics==3.1.61',
    'huaweicloudsdkiotda==3.1.61',
    'huaweicloudsdkiotedge==3.1.61',
    'huaweicloudsdkivs==3.1.61',
    'huaweicloudsdkkafka==3.1.61',
    'huaweicloudsdkkms==3.1.61',
    'huaweicloudsdkkoomessage==3.1.61',
    'huaweicloudsdkkps==3.1.61',
    'huaweicloudsdklakeformation==3.1.61',
    'huaweicloudsdklive==3.1.61',
    'huaweicloudsdklts==3.1.61',
    'huaweicloudsdkmapds==3.1.61',
    'huaweicloudsdkmas==3.1.61',
    'huaweicloudsdkmeeting==3.1.61',
    'huaweicloudsdkmetastudio==3.1.61',
    'huaweicloudsdkmoderation==3.1.61',
    'huaweicloudsdkmpc==3.1.61',
    'huaweicloudsdkmrs==3.1.61',
    'huaweicloudsdkmsgsms==3.1.61',
    'huaweicloudsdkmssi==3.1.61',
    'huaweicloudsdknat==3.1.61',
    'huaweicloudsdknlp==3.1.61',
    'huaweicloudsdkocr==3.1.61',
    'huaweicloudsdkoms==3.1.61',
    'huaweicloudsdkoptverse==3.1.61',
    'huaweicloudsdkorganizations==3.1.61',
    'huaweicloudsdkoroas==3.1.61',
    'huaweicloudsdkosm==3.1.61',
    'huaweicloudsdkpangulargemodels==3.1.61',
    'huaweicloudsdkprojectman==3.1.61',
    'huaweicloudsdkrabbitmq==3.1.61',
    'huaweicloudsdkram==3.1.61',
    'huaweicloudsdkrds==3.1.61',
    'huaweicloudsdkres==3.1.61',
    'huaweicloudsdkrms==3.1.61',
    'huaweicloudsdkrocketmq==3.1.61',
    'huaweicloudsdkroma==3.1.61',
    'huaweicloudsdksa==3.1.61',
    'huaweicloudsdkscm==3.1.61',
    'huaweicloudsdksdrs==3.1.61',
    'huaweicloudsdksecmaster==3.1.61',
    'huaweicloudsdkservicestage==3.1.61',
    'huaweicloudsdksfsturbo==3.1.61',
    'huaweicloudsdksis==3.1.61',
    'huaweicloudsdksmn==3.1.61',
    'huaweicloudsdksms==3.1.61',
    'huaweicloudsdkswr==3.1.61',
    'huaweicloudsdktms==3.1.61',
    'huaweicloudsdkugo==3.1.61',
    'huaweicloudsdkvas==3.1.61',
    'huaweicloudsdkvcm==3.1.61',
    'huaweicloudsdkvod==3.1.61',
    'huaweicloudsdkvpc==3.1.61',
    'huaweicloudsdkvpcep==3.1.61',
    'huaweicloudsdkwaf==3.1.61',
    'huaweicloudsdkworkspace==3.1.61',
    'huaweicloudsdkworkspaceapp==3.1.61',
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
