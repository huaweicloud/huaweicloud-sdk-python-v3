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
VERSION = "3.1.77"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.77',
    'huaweicloudsdkaad==3.1.77',
    'huaweicloudsdkantiddos==3.1.77',
    'huaweicloudsdkaom==3.1.77',
    'huaweicloudsdkaos==3.1.77',
    'huaweicloudsdkapig==3.1.77',
    'huaweicloudsdkapm==3.1.77',
    'huaweicloudsdkas==3.1.77',
    'huaweicloudsdkasm==3.1.77',
    'huaweicloudsdkbcs==3.1.77',
    'huaweicloudsdkbms==3.1.77',
    'huaweicloudsdkbss==3.1.77',
    'huaweicloudsdkbssintl==3.1.77',
    'huaweicloudsdkcae==3.1.77',
    'huaweicloudsdkcampusgo==3.1.77',
    'huaweicloudsdkcbh==3.1.77',
    'huaweicloudsdkcbr==3.1.77',
    'huaweicloudsdkcbs==3.1.77',
    'huaweicloudsdkcc==3.1.77',
    'huaweicloudsdkcce==3.1.77',
    'huaweicloudsdkccm==3.1.77',
    'huaweicloudsdkcdm==3.1.77',
    'huaweicloudsdkcdn==3.1.77',
    'huaweicloudsdkces==3.1.77',
    'huaweicloudsdkcfw==3.1.77',
    'huaweicloudsdkcgs==3.1.77',
    'huaweicloudsdkclassroom==3.1.77',
    'huaweicloudsdkcloudide==3.1.77',
    'huaweicloudsdkcloudpond==3.1.77',
    'huaweicloudsdkcloudrtc==3.1.77',
    'huaweicloudsdkcloudtable==3.1.77',
    'huaweicloudsdkcloudtest==3.1.77',
    'huaweicloudsdkcodeartsartifact==3.1.77',
    'huaweicloudsdkcodeartsbuild==3.1.77',
    'huaweicloudsdkcodeartscheck==3.1.77',
    'huaweicloudsdkcodeartsdeploy==3.1.77',
    'huaweicloudsdkcodeartsinspector==3.1.77',
    'huaweicloudsdkcodeartspipeline==3.1.77',
    'huaweicloudsdkcodecraft==3.1.77',
    'huaweicloudsdkcodehub==3.1.77',
    'huaweicloudsdkconfig==3.1.77',
    'huaweicloudsdkcph==3.1.77',
    'huaweicloudsdkcpts==3.1.77',
    'huaweicloudsdkcse==3.1.77',
    'huaweicloudsdkcsms==3.1.77',
    'huaweicloudsdkcss==3.1.77',
    'huaweicloudsdkcts==3.1.77',
    'huaweicloudsdkdas==3.1.77',
    'huaweicloudsdkdataartsstudio==3.1.77',
    'huaweicloudsdkdbss==3.1.77',
    'huaweicloudsdkdc==3.1.77',
    'huaweicloudsdkdcs==3.1.77',
    'huaweicloudsdkddm==3.1.77',
    'huaweicloudsdkdds==3.1.77',
    'huaweicloudsdkdeh==3.1.77',
    'huaweicloudsdkdevsecurity==3.1.77',
    'huaweicloudsdkdevstar==3.1.77',
    'huaweicloudsdkdgc==3.1.77',
    'huaweicloudsdkdis==3.1.77',
    'huaweicloudsdkdlf==3.1.77',
    'huaweicloudsdkdli==3.1.77',
    'huaweicloudsdkdns==3.1.77',
    'huaweicloudsdkdris==3.1.77',
    'huaweicloudsdkdrs==3.1.77',
    'huaweicloudsdkdsc==3.1.77',
    'huaweicloudsdkdwr==3.1.77',
    'huaweicloudsdkdws==3.1.77',
    'huaweicloudsdkec==3.1.77',
    'huaweicloudsdkecs==3.1.77',
    'huaweicloudsdkedgesec==3.1.77',
    'huaweicloudsdkeg==3.1.77',
    'huaweicloudsdkeihealth==3.1.77',
    'huaweicloudsdkeip==3.1.77',
    'huaweicloudsdkelb==3.1.77',
    'huaweicloudsdkeps==3.1.77',
    'huaweicloudsdker==3.1.77',
    'huaweicloudsdkevs==3.1.77',
    'huaweicloudsdkfrs==3.1.77',
    'huaweicloudsdkfunctiongraph==3.1.77',
    'huaweicloudsdkga==3.1.77',
    'huaweicloudsdkgaussdb==3.1.77',
    'huaweicloudsdkgaussdbfornosql==3.1.77',
    'huaweicloudsdkgaussdbforopengauss==3.1.77',
    'huaweicloudsdkges==3.1.77',
    'huaweicloudsdkgsl==3.1.77',
    'huaweicloudsdkhilens==3.1.77',
    'huaweicloudsdkhss==3.1.77',
    'huaweicloudsdkiam==3.1.77',
    'huaweicloudsdkidentitycenter==3.1.77',
    'huaweicloudsdkidentitycenterstore==3.1.77',
    'huaweicloudsdkidme==3.1.77',
    'huaweicloudsdkidmeclassicapi==3.1.77',
    'huaweicloudsdkiec==3.1.77',
    'huaweicloudsdkief==3.1.77',
    'huaweicloudsdkimage==3.1.77',
    'huaweicloudsdkimagesearch==3.1.77',
    'huaweicloudsdkims==3.1.77',
    'huaweicloudsdkiotanalytics==3.1.77',
    'huaweicloudsdkiotda==3.1.77',
    'huaweicloudsdkiotedge==3.1.77',
    'huaweicloudsdkivs==3.1.77',
    'huaweicloudsdkkafka==3.1.77',
    'huaweicloudsdkkms==3.1.77',
    'huaweicloudsdkkoomessage==3.1.77',
    'huaweicloudsdkkps==3.1.77',
    'huaweicloudsdklakeformation==3.1.77',
    'huaweicloudsdklive==3.1.77',
    'huaweicloudsdklts==3.1.77',
    'huaweicloudsdkmapds==3.1.77',
    'huaweicloudsdkmas==3.1.77',
    'huaweicloudsdkmeeting==3.1.77',
    'huaweicloudsdkmetastudio==3.1.77',
    'huaweicloudsdkmoderation==3.1.77',
    'huaweicloudsdkmpc==3.1.77',
    'huaweicloudsdkmrs==3.1.77',
    'huaweicloudsdkmsgsms==3.1.77',
    'huaweicloudsdkmssi==3.1.77',
    'huaweicloudsdknat==3.1.77',
    'huaweicloudsdknlp==3.1.77',
    'huaweicloudsdkobs==3.1.77',
    'huaweicloudsdkocr==3.1.77',
    'huaweicloudsdkoctopus==3.1.77',
    'huaweicloudsdkoms==3.1.77',
    'huaweicloudsdkoptverse==3.1.77',
    'huaweicloudsdkorganizations==3.1.77',
    'huaweicloudsdkoroas==3.1.77',
    'huaweicloudsdkosm==3.1.77',
    'huaweicloudsdkpangulargemodels==3.1.77',
    'huaweicloudsdkprojectman==3.1.77',
    'huaweicloudsdkrabbitmq==3.1.77',
    'huaweicloudsdkram==3.1.77',
    'huaweicloudsdkrds==3.1.77',
    'huaweicloudsdkres==3.1.77',
    'huaweicloudsdkrgc==3.1.77',
    'huaweicloudsdkrms==3.1.77',
    'huaweicloudsdkrocketmq==3.1.77',
    'huaweicloudsdkroma==3.1.77',
    'huaweicloudsdksa==3.1.77',
    'huaweicloudsdkscm==3.1.77',
    'huaweicloudsdksdrs==3.1.77',
    'huaweicloudsdksecmaster==3.1.77',
    'huaweicloudsdkservicestage==3.1.77',
    'huaweicloudsdksfsturbo==3.1.77',
    'huaweicloudsdksis==3.1.77',
    'huaweicloudsdksmn==3.1.77',
    'huaweicloudsdksms==3.1.77',
    'huaweicloudsdkswr==3.1.77',
    'huaweicloudsdktics==3.1.77',
    'huaweicloudsdktms==3.1.77',
    'huaweicloudsdkugo==3.1.77',
    'huaweicloudsdkvas==3.1.77',
    'huaweicloudsdkvcm==3.1.77',
    'huaweicloudsdkvod==3.1.77',
    'huaweicloudsdkvpc==3.1.77',
    'huaweicloudsdkvpcep==3.1.77',
    'huaweicloudsdkvpn==3.1.77',
    'huaweicloudsdkwaf==3.1.77',
    'huaweicloudsdkworkspace==3.1.77',
    'huaweicloudsdkworkspaceapp==3.1.77',
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
