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
VERSION = "3.1.71"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.71',
    'huaweicloudsdkaad==3.1.71',
    'huaweicloudsdkantiddos==3.1.71',
    'huaweicloudsdkaom==3.1.71',
    'huaweicloudsdkaos==3.1.71',
    'huaweicloudsdkapig==3.1.71',
    'huaweicloudsdkapm==3.1.71',
    'huaweicloudsdkas==3.1.71',
    'huaweicloudsdkasm==3.1.71',
    'huaweicloudsdkbcs==3.1.71',
    'huaweicloudsdkbms==3.1.71',
    'huaweicloudsdkbss==3.1.71',
    'huaweicloudsdkbssintl==3.1.71',
    'huaweicloudsdkcae==3.1.71',
    'huaweicloudsdkcampusgo==3.1.71',
    'huaweicloudsdkcbh==3.1.71',
    'huaweicloudsdkcbr==3.1.71',
    'huaweicloudsdkcbs==3.1.71',
    'huaweicloudsdkcc==3.1.71',
    'huaweicloudsdkcce==3.1.71',
    'huaweicloudsdkccm==3.1.71',
    'huaweicloudsdkcdm==3.1.71',
    'huaweicloudsdkcdn==3.1.71',
    'huaweicloudsdkces==3.1.71',
    'huaweicloudsdkcfw==3.1.71',
    'huaweicloudsdkcgs==3.1.71',
    'huaweicloudsdkclassroom==3.1.71',
    'huaweicloudsdkcloudide==3.1.71',
    'huaweicloudsdkcloudpond==3.1.71',
    'huaweicloudsdkcloudrtc==3.1.71',
    'huaweicloudsdkcloudtable==3.1.71',
    'huaweicloudsdkcloudtest==3.1.71',
    'huaweicloudsdkcodeartsartifact==3.1.71',
    'huaweicloudsdkcodeartsbuild==3.1.71',
    'huaweicloudsdkcodeartscheck==3.1.71',
    'huaweicloudsdkcodeartsdeploy==3.1.71',
    'huaweicloudsdkcodeartsinspector==3.1.71',
    'huaweicloudsdkcodeartspipeline==3.1.71',
    'huaweicloudsdkcodecraft==3.1.71',
    'huaweicloudsdkcodehub==3.1.71',
    'huaweicloudsdkconfig==3.1.71',
    'huaweicloudsdkcph==3.1.71',
    'huaweicloudsdkcpts==3.1.71',
    'huaweicloudsdkcse==3.1.71',
    'huaweicloudsdkcsms==3.1.71',
    'huaweicloudsdkcss==3.1.71',
    'huaweicloudsdkcts==3.1.71',
    'huaweicloudsdkdas==3.1.71',
    'huaweicloudsdkdataartsstudio==3.1.71',
    'huaweicloudsdkdbss==3.1.71',
    'huaweicloudsdkdc==3.1.71',
    'huaweicloudsdkdcs==3.1.71',
    'huaweicloudsdkddm==3.1.71',
    'huaweicloudsdkdds==3.1.71',
    'huaweicloudsdkdeh==3.1.71',
    'huaweicloudsdkdevsecurity==3.1.71',
    'huaweicloudsdkdevstar==3.1.71',
    'huaweicloudsdkdgc==3.1.71',
    'huaweicloudsdkdis==3.1.71',
    'huaweicloudsdkdlf==3.1.71',
    'huaweicloudsdkdli==3.1.71',
    'huaweicloudsdkdns==3.1.71',
    'huaweicloudsdkdris==3.1.71',
    'huaweicloudsdkdrs==3.1.71',
    'huaweicloudsdkdsc==3.1.71',
    'huaweicloudsdkdwr==3.1.71',
    'huaweicloudsdkdws==3.1.71',
    'huaweicloudsdkec==3.1.71',
    'huaweicloudsdkecs==3.1.71',
    'huaweicloudsdkedgesec==3.1.71',
    'huaweicloudsdkeg==3.1.71',
    'huaweicloudsdkeihealth==3.1.71',
    'huaweicloudsdkeip==3.1.71',
    'huaweicloudsdkelb==3.1.71',
    'huaweicloudsdkeps==3.1.71',
    'huaweicloudsdker==3.1.71',
    'huaweicloudsdkevs==3.1.71',
    'huaweicloudsdkfrs==3.1.71',
    'huaweicloudsdkfunctiongraph==3.1.71',
    'huaweicloudsdkga==3.1.71',
    'huaweicloudsdkgaussdb==3.1.71',
    'huaweicloudsdkgaussdbfornosql==3.1.71',
    'huaweicloudsdkgaussdbforopengauss==3.1.71',
    'huaweicloudsdkges==3.1.71',
    'huaweicloudsdkgsl==3.1.71',
    'huaweicloudsdkhilens==3.1.71',
    'huaweicloudsdkhss==3.1.71',
    'huaweicloudsdkiam==3.1.71',
    'huaweicloudsdkidentitycenter==3.1.71',
    'huaweicloudsdkidentitycenterstore==3.1.71',
    'huaweicloudsdkidme==3.1.71',
    'huaweicloudsdkiec==3.1.71',
    'huaweicloudsdkief==3.1.71',
    'huaweicloudsdkimage==3.1.71',
    'huaweicloudsdkimagesearch==3.1.71',
    'huaweicloudsdkims==3.1.71',
    'huaweicloudsdkiotanalytics==3.1.71',
    'huaweicloudsdkiotda==3.1.71',
    'huaweicloudsdkiotedge==3.1.71',
    'huaweicloudsdkivs==3.1.71',
    'huaweicloudsdkkafka==3.1.71',
    'huaweicloudsdkkms==3.1.71',
    'huaweicloudsdkkoomessage==3.1.71',
    'huaweicloudsdkkps==3.1.71',
    'huaweicloudsdklakeformation==3.1.71',
    'huaweicloudsdklive==3.1.71',
    'huaweicloudsdklts==3.1.71',
    'huaweicloudsdkmapds==3.1.71',
    'huaweicloudsdkmas==3.1.71',
    'huaweicloudsdkmeeting==3.1.71',
    'huaweicloudsdkmetastudio==3.1.71',
    'huaweicloudsdkmoderation==3.1.71',
    'huaweicloudsdkmpc==3.1.71',
    'huaweicloudsdkmrs==3.1.71',
    'huaweicloudsdkmsgsms==3.1.71',
    'huaweicloudsdkmssi==3.1.71',
    'huaweicloudsdknat==3.1.71',
    'huaweicloudsdknlp==3.1.71',
    'huaweicloudsdkocr==3.1.71',
    'huaweicloudsdkoctopus==3.1.71',
    'huaweicloudsdkoms==3.1.71',
    'huaweicloudsdkoptverse==3.1.71',
    'huaweicloudsdkorganizations==3.1.71',
    'huaweicloudsdkoroas==3.1.71',
    'huaweicloudsdkosm==3.1.71',
    'huaweicloudsdkpangulargemodels==3.1.71',
    'huaweicloudsdkprojectman==3.1.71',
    'huaweicloudsdkrabbitmq==3.1.71',
    'huaweicloudsdkram==3.1.71',
    'huaweicloudsdkrds==3.1.71',
    'huaweicloudsdkres==3.1.71',
    'huaweicloudsdkrgc==3.1.71',
    'huaweicloudsdkrms==3.1.71',
    'huaweicloudsdkrocketmq==3.1.71',
    'huaweicloudsdkroma==3.1.71',
    'huaweicloudsdksa==3.1.71',
    'huaweicloudsdkscm==3.1.71',
    'huaweicloudsdksdrs==3.1.71',
    'huaweicloudsdksecmaster==3.1.71',
    'huaweicloudsdkservicestage==3.1.71',
    'huaweicloudsdksfsturbo==3.1.71',
    'huaweicloudsdksis==3.1.71',
    'huaweicloudsdksmn==3.1.71',
    'huaweicloudsdksms==3.1.71',
    'huaweicloudsdkswr==3.1.71',
    'huaweicloudsdktics==3.1.71',
    'huaweicloudsdktms==3.1.71',
    'huaweicloudsdkugo==3.1.71',
    'huaweicloudsdkvas==3.1.71',
    'huaweicloudsdkvcm==3.1.71',
    'huaweicloudsdkvod==3.1.71',
    'huaweicloudsdkvpc==3.1.71',
    'huaweicloudsdkvpcep==3.1.71',
    'huaweicloudsdkvpn==3.1.71',
    'huaweicloudsdkwaf==3.1.71',
    'huaweicloudsdkworkspace==3.1.71',
    'huaweicloudsdkworkspaceapp==3.1.71',
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
