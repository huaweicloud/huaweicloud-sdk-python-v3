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
VERSION = "3.1.58"
AUTHOR = "HuaweiCloud SDK"
AUTHOR_EMAIL = "hwcloudsdk@huawei.com"
URL = "https://github.com/huaweicloud/huaweicloud-sdk-python-v3"

DESCRIPTION = "HuaweiCloud SDK Python All"
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_PYPI.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    'huaweicloudsdkcore==3.1.58',
    'huaweicloudsdkantiddos==3.1.58',
    'huaweicloudsdkaom==3.1.58',
    'huaweicloudsdkaos==3.1.58',
    'huaweicloudsdkapig==3.1.58',
    'huaweicloudsdkapm==3.1.58',
    'huaweicloudsdkas==3.1.58',
    'huaweicloudsdkbcs==3.1.58',
    'huaweicloudsdkbms==3.1.58',
    'huaweicloudsdkbss==3.1.58',
    'huaweicloudsdkbssintl==3.1.58',
    'huaweicloudsdkcae==3.1.58',
    'huaweicloudsdkcampusgo==3.1.58',
    'huaweicloudsdkcbh==3.1.58',
    'huaweicloudsdkcbr==3.1.58',
    'huaweicloudsdkcbs==3.1.58',
    'huaweicloudsdkcc==3.1.58',
    'huaweicloudsdkcce==3.1.58',
    'huaweicloudsdkccm==3.1.58',
    'huaweicloudsdkcdm==3.1.58',
    'huaweicloudsdkcdn==3.1.58',
    'huaweicloudsdkces==3.1.58',
    'huaweicloudsdkcfw==3.1.58',
    'huaweicloudsdkcgs==3.1.58',
    'huaweicloudsdkclassroom==3.1.58',
    'huaweicloudsdkcloudide==3.1.58',
    'huaweicloudsdkcloudpipeline==3.1.58',
    'huaweicloudsdkcloudrtc==3.1.58',
    'huaweicloudsdkcloudtable==3.1.58',
    'huaweicloudsdkcloudtest==3.1.58',
    'huaweicloudsdkcodeartsartifact==3.1.58',
    'huaweicloudsdkcodeartsbuild==3.1.58',
    'huaweicloudsdkcodeartscheck==3.1.58',
    'huaweicloudsdkcodeartsdeploy==3.1.58',
    'huaweicloudsdkcodecraft==3.1.58',
    'huaweicloudsdkcodehub==3.1.58',
    'huaweicloudsdkconfig==3.1.58',
    'huaweicloudsdkcph==3.1.58',
    'huaweicloudsdkcpts==3.1.58',
    'huaweicloudsdkcse==3.1.58',
    'huaweicloudsdkcsms==3.1.58',
    'huaweicloudsdkcss==3.1.58',
    'huaweicloudsdkcts==3.1.58',
    'huaweicloudsdkdas==3.1.58',
    'huaweicloudsdkdataartsstudio==3.1.58',
    'huaweicloudsdkdbss==3.1.58',
    'huaweicloudsdkdc==3.1.58',
    'huaweicloudsdkdcs==3.1.58',
    'huaweicloudsdkddm==3.1.58',
    'huaweicloudsdkdds==3.1.58',
    'huaweicloudsdkdeh==3.1.58',
    'huaweicloudsdkdevsecurity==3.1.58',
    'huaweicloudsdkdevstar==3.1.58',
    'huaweicloudsdkdgc==3.1.58',
    'huaweicloudsdkdlf==3.1.58',
    'huaweicloudsdkdli==3.1.58',
    'huaweicloudsdkdns==3.1.58',
    'huaweicloudsdkdris==3.1.58',
    'huaweicloudsdkdrs==3.1.58',
    'huaweicloudsdkdsc==3.1.58',
    'huaweicloudsdkdwr==3.1.58',
    'huaweicloudsdkdws==3.1.58',
    'huaweicloudsdkec==3.1.58',
    'huaweicloudsdkecs==3.1.58',
    'huaweicloudsdkedgesec==3.1.58',
    'huaweicloudsdkeg==3.1.58',
    'huaweicloudsdkeihealth==3.1.58',
    'huaweicloudsdkeip==3.1.58',
    'huaweicloudsdkelb==3.1.58',
    'huaweicloudsdkeps==3.1.58',
    'huaweicloudsdker==3.1.58',
    'huaweicloudsdkevs==3.1.58',
    'huaweicloudsdkfrs==3.1.58',
    'huaweicloudsdkfunctiongraph==3.1.58',
    'huaweicloudsdkga==3.1.58',
    'huaweicloudsdkgaussdb==3.1.58',
    'huaweicloudsdkgaussdbfornosql==3.1.58',
    'huaweicloudsdkgaussdbforopengauss==3.1.58',
    'huaweicloudsdkges==3.1.58',
    'huaweicloudsdkgsl==3.1.58',
    'huaweicloudsdkhilens==3.1.58',
    'huaweicloudsdkhss==3.1.58',
    'huaweicloudsdkiam==3.1.58',
    'huaweicloudsdkidentitycenter==3.1.58',
    'huaweicloudsdkidme==3.1.58',
    'huaweicloudsdkiec==3.1.58',
    'huaweicloudsdkief==3.1.58',
    'huaweicloudsdkies==3.1.58',
    'huaweicloudsdkimage==3.1.58',
    'huaweicloudsdkimagesearch==3.1.58',
    'huaweicloudsdkims==3.1.58',
    'huaweicloudsdkiotanalytics==3.1.58',
    'huaweicloudsdkiotda==3.1.58',
    'huaweicloudsdkiotedge==3.1.58',
    'huaweicloudsdkivs==3.1.58',
    'huaweicloudsdkkafka==3.1.58',
    'huaweicloudsdkkms==3.1.58',
    'huaweicloudsdkkoomessage==3.1.58',
    'huaweicloudsdkkps==3.1.58',
    'huaweicloudsdklakeformation==3.1.58',
    'huaweicloudsdklive==3.1.58',
    'huaweicloudsdklts==3.1.58',
    'huaweicloudsdkmapds==3.1.58',
    'huaweicloudsdkmas==3.1.58',
    'huaweicloudsdkmeeting==3.1.58',
    'huaweicloudsdkmetastudio==3.1.58',
    'huaweicloudsdkmoderation==3.1.58',
    'huaweicloudsdkmpc==3.1.58',
    'huaweicloudsdkmrs==3.1.58',
    'huaweicloudsdkmsgsms==3.1.58',
    'huaweicloudsdkmssi==3.1.58',
    'huaweicloudsdknat==3.1.58',
    'huaweicloudsdknlp==3.1.58',
    'huaweicloudsdkocr==3.1.58',
    'huaweicloudsdkoms==3.1.58',
    'huaweicloudsdkoptverse==3.1.58',
    'huaweicloudsdkorganizations==3.1.58',
    'huaweicloudsdkoroas==3.1.58',
    'huaweicloudsdkosm==3.1.58',
    'huaweicloudsdkpangulargemodels==3.1.58',
    'huaweicloudsdkprojectman==3.1.58',
    'huaweicloudsdkrabbitmq==3.1.58',
    'huaweicloudsdkram==3.1.58',
    'huaweicloudsdkrds==3.1.58',
    'huaweicloudsdkres==3.1.58',
    'huaweicloudsdkrms==3.1.58',
    'huaweicloudsdkrocketmq==3.1.58',
    'huaweicloudsdkroma==3.1.58',
    'huaweicloudsdksa==3.1.58',
    'huaweicloudsdkscm==3.1.58',
    'huaweicloudsdksdrs==3.1.58',
    'huaweicloudsdksecmaster==3.1.58',
    'huaweicloudsdkservicestage==3.1.58',
    'huaweicloudsdksfsturbo==3.1.58',
    'huaweicloudsdksis==3.1.58',
    'huaweicloudsdksmn==3.1.58',
    'huaweicloudsdksms==3.1.58',
    'huaweicloudsdkswr==3.1.58',
    'huaweicloudsdktms==3.1.58',
    'huaweicloudsdkugo==3.1.58',
    'huaweicloudsdkvas==3.1.58',
    'huaweicloudsdkvcm==3.1.58',
    'huaweicloudsdkvod==3.1.58',
    'huaweicloudsdkvpc==3.1.58',
    'huaweicloudsdkvpcep==3.1.58',
    'huaweicloudsdkvss==3.1.58',
    'huaweicloudsdkwaf==3.1.58',
    'huaweicloudsdkworkspace==3.1.58',
    'huaweicloudsdkworkspaceapp==3.1.58',
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
