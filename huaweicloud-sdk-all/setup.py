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
VERSION = "3.1.60"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.60',
    'huaweicloudsdkantiddos==3.1.60',
    'huaweicloudsdkaom==3.1.60',
    'huaweicloudsdkaos==3.1.60',
    'huaweicloudsdkapig==3.1.60',
    'huaweicloudsdkapm==3.1.60',
    'huaweicloudsdkas==3.1.60',
    'huaweicloudsdkbcs==3.1.60',
    'huaweicloudsdkbms==3.1.60',
    'huaweicloudsdkbss==3.1.60',
    'huaweicloudsdkbssintl==3.1.60',
    'huaweicloudsdkcae==3.1.60',
    'huaweicloudsdkcampusgo==3.1.60',
    'huaweicloudsdkcbh==3.1.60',
    'huaweicloudsdkcbr==3.1.60',
    'huaweicloudsdkcbs==3.1.60',
    'huaweicloudsdkcc==3.1.60',
    'huaweicloudsdkcce==3.1.60',
    'huaweicloudsdkccm==3.1.60',
    'huaweicloudsdkcdm==3.1.60',
    'huaweicloudsdkcdn==3.1.60',
    'huaweicloudsdkces==3.1.60',
    'huaweicloudsdkcfw==3.1.60',
    'huaweicloudsdkcgs==3.1.60',
    'huaweicloudsdkclassroom==3.1.60',
    'huaweicloudsdkcloudide==3.1.60',
    'huaweicloudsdkcloudpond==3.1.60',
    'huaweicloudsdkcloudrtc==3.1.60',
    'huaweicloudsdkcloudtable==3.1.60',
    'huaweicloudsdkcloudtest==3.1.60',
    'huaweicloudsdkcodeartsartifact==3.1.60',
    'huaweicloudsdkcodeartsbuild==3.1.60',
    'huaweicloudsdkcodeartscheck==3.1.60',
    'huaweicloudsdkcodeartsdeploy==3.1.60',
    'huaweicloudsdkcodeartsinspector==3.1.60',
    'huaweicloudsdkcodeartspipeline==3.1.60',
    'huaweicloudsdkcodecraft==3.1.60',
    'huaweicloudsdkcodehub==3.1.60',
    'huaweicloudsdkconfig==3.1.60',
    'huaweicloudsdkcph==3.1.60',
    'huaweicloudsdkcpts==3.1.60',
    'huaweicloudsdkcse==3.1.60',
    'huaweicloudsdkcsms==3.1.60',
    'huaweicloudsdkcss==3.1.60',
    'huaweicloudsdkcts==3.1.60',
    'huaweicloudsdkdas==3.1.60',
    'huaweicloudsdkdataartsstudio==3.1.60',
    'huaweicloudsdkdbss==3.1.60',
    'huaweicloudsdkdc==3.1.60',
    'huaweicloudsdkdcs==3.1.60',
    'huaweicloudsdkddm==3.1.60',
    'huaweicloudsdkdds==3.1.60',
    'huaweicloudsdkdeh==3.1.60',
    'huaweicloudsdkdevsecurity==3.1.60',
    'huaweicloudsdkdevstar==3.1.60',
    'huaweicloudsdkdgc==3.1.60',
    'huaweicloudsdkdlf==3.1.60',
    'huaweicloudsdkdli==3.1.60',
    'huaweicloudsdkdns==3.1.60',
    'huaweicloudsdkdris==3.1.60',
    'huaweicloudsdkdrs==3.1.60',
    'huaweicloudsdkdsc==3.1.60',
    'huaweicloudsdkdwr==3.1.60',
    'huaweicloudsdkdws==3.1.60',
    'huaweicloudsdkec==3.1.60',
    'huaweicloudsdkecs==3.1.60',
    'huaweicloudsdkedgesec==3.1.60',
    'huaweicloudsdkeg==3.1.60',
    'huaweicloudsdkeihealth==3.1.60',
    'huaweicloudsdkeip==3.1.60',
    'huaweicloudsdkelb==3.1.60',
    'huaweicloudsdkeps==3.1.60',
    'huaweicloudsdker==3.1.60',
    'huaweicloudsdkevs==3.1.60',
    'huaweicloudsdkfrs==3.1.60',
    'huaweicloudsdkfunctiongraph==3.1.60',
    'huaweicloudsdkga==3.1.60',
    'huaweicloudsdkgaussdb==3.1.60',
    'huaweicloudsdkgaussdbfornosql==3.1.60',
    'huaweicloudsdkgaussdbforopengauss==3.1.60',
    'huaweicloudsdkges==3.1.60',
    'huaweicloudsdkgsl==3.1.60',
    'huaweicloudsdkhilens==3.1.60',
    'huaweicloudsdkhss==3.1.60',
    'huaweicloudsdkiam==3.1.60',
    'huaweicloudsdkidentitycenter==3.1.60',
    'huaweicloudsdkidentitycenterstore==3.1.60',
    'huaweicloudsdkidme==3.1.60',
    'huaweicloudsdkiec==3.1.60',
    'huaweicloudsdkief==3.1.60',
    'huaweicloudsdkimage==3.1.60',
    'huaweicloudsdkimagesearch==3.1.60',
    'huaweicloudsdkims==3.1.60',
    'huaweicloudsdkiotanalytics==3.1.60',
    'huaweicloudsdkiotda==3.1.60',
    'huaweicloudsdkiotedge==3.1.60',
    'huaweicloudsdkivs==3.1.60',
    'huaweicloudsdkkafka==3.1.60',
    'huaweicloudsdkkms==3.1.60',
    'huaweicloudsdkkoomessage==3.1.60',
    'huaweicloudsdkkps==3.1.60',
    'huaweicloudsdklakeformation==3.1.60',
    'huaweicloudsdklive==3.1.60',
    'huaweicloudsdklts==3.1.60',
    'huaweicloudsdkmapds==3.1.60',
    'huaweicloudsdkmas==3.1.60',
    'huaweicloudsdkmeeting==3.1.60',
    'huaweicloudsdkmetastudio==3.1.60',
    'huaweicloudsdkmoderation==3.1.60',
    'huaweicloudsdkmpc==3.1.60',
    'huaweicloudsdkmrs==3.1.60',
    'huaweicloudsdkmsgsms==3.1.60',
    'huaweicloudsdkmssi==3.1.60',
    'huaweicloudsdknat==3.1.60',
    'huaweicloudsdknlp==3.1.60',
    'huaweicloudsdkocr==3.1.60',
    'huaweicloudsdkoms==3.1.60',
    'huaweicloudsdkoptverse==3.1.60',
    'huaweicloudsdkorganizations==3.1.60',
    'huaweicloudsdkoroas==3.1.60',
    'huaweicloudsdkosm==3.1.60',
    'huaweicloudsdkpangulargemodels==3.1.60',
    'huaweicloudsdkprojectman==3.1.60',
    'huaweicloudsdkrabbitmq==3.1.60',
    'huaweicloudsdkram==3.1.60',
    'huaweicloudsdkrds==3.1.60',
    'huaweicloudsdkres==3.1.60',
    'huaweicloudsdkrms==3.1.60',
    'huaweicloudsdkrocketmq==3.1.60',
    'huaweicloudsdkroma==3.1.60',
    'huaweicloudsdksa==3.1.60',
    'huaweicloudsdkscm==3.1.60',
    'huaweicloudsdksdrs==3.1.60',
    'huaweicloudsdksecmaster==3.1.60',
    'huaweicloudsdkservicestage==3.1.60',
    'huaweicloudsdksfsturbo==3.1.60',
    'huaweicloudsdksis==3.1.60',
    'huaweicloudsdksmn==3.1.60',
    'huaweicloudsdksms==3.1.60',
    'huaweicloudsdkswr==3.1.60',
    'huaweicloudsdktms==3.1.60',
    'huaweicloudsdkugo==3.1.60',
    'huaweicloudsdkvas==3.1.60',
    'huaweicloudsdkvcm==3.1.60',
    'huaweicloudsdkvod==3.1.60',
    'huaweicloudsdkvpc==3.1.60',
    'huaweicloudsdkvpcep==3.1.60',
    'huaweicloudsdkwaf==3.1.60',
    'huaweicloudsdkworkspace==3.1.60',
    'huaweicloudsdkworkspaceapp==3.1.60',
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
