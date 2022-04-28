# coding: utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""
import os

from huaweicloudsdkcore.auth.credentials import DerivedCredentials, BasicCredentials, GlobalCredentials, TempCredentials

BASIC_CREDENTIAL_TYPE = "BasicCredentials"
GLOBAL_CREDENTIAL_TYPE = "GlobalCredentials"


class EnvCredentialHelper(object):

    def __init__(self):
        pass

    AK_ENV_NAME = "HUAWEICLOUD_SDK_AK"
    SK_ENV_NAME = "HUAWEICLOUD_SDK_SK"
    PROJECT_ID_ENV_NAME = "HUAWEICLOUD_SDK_PROJECT_ID"
    DOMAIN_ID_ENV_NAME = "HUAWEICLOUD_SDK_DOMAIN_ID"
    IAM_ENDPOINT_ENV_NAME = "HUAWEICLOUD_SDK_IAM_ENDPOINT"
    REGION_ID_ENV_NAME = "HUAWEICLOUD_SDK_REGION_ID"
    DERIVED_AUTH_SERVICE_NAME_ENV_NAME = "HUAWEICLOUD_SDK_DERIVED_AUTH_SERVICE_NAME"
    DERIVED_PREDICATE_ENV_NAME = "HUAWEICLOUD_SDK_DERIVED_PREDICATE"
    DEFAULT_DERIVED_PREDICATE = "DEFAULT_DERIVED_PREDICATE"

    @classmethod
    def load_credential_from_env(cls, default_type):

        credential = None

        ak = os.environ.get(cls.AK_ENV_NAME)
        sk = os.environ.get(cls.SK_ENV_NAME)

        if not ak or not sk:
            return credential

        iam_endpoint = cls.get_iam_endpoint_env_name()

        region_id = os.environ.get(cls.REGION_ID_ENV_NAME)
        derived_auth_service_name = os.environ.get(cls.DERIVED_AUTH_SERVICE_NAME_ENV_NAME)
        derived_predicate = os.environ.get(cls.DERIVED_PREDICATE_ENV_NAME)
        if derived_predicate and derived_predicate == cls.DEFAULT_DERIVED_PREDICATE:
            derived_predicate = DerivedCredentials.get_default_derived_predicate()

        if default_type == BASIC_CREDENTIAL_TYPE:
            project_id = os.environ.get(cls.PROJECT_ID_ENV_NAME)
            credential = BasicCredentials(ak, sk, project_id).with_derived_predicate(derived_predicate)
            credential._process_derived_auth_params(derived_auth_service_name, region_id)
            credential.with_iam_endpoint(iam_endpoint)
        elif default_type == GLOBAL_CREDENTIAL_TYPE:
            domain_id = os.environ.get(cls.DOMAIN_ID_ENV_NAME)
            credential = GlobalCredentials(ak, sk, domain_id).with_derived_predicate(derived_predicate)
            credential._process_derived_auth_params(derived_auth_service_name, region_id)
            credential.with_iam_endpoint(iam_endpoint)

        return credential

    @classmethod
    def get_iam_endpoint_env_name(cls):
        return os.environ.get(cls.IAM_ENDPOINT_ENV_NAME)


class TempCredentialHelper(object):
    @classmethod
    def process_credential(cls, http_client, default_type, cred):
        if not cred:
            return cls._load_credential_from_metadata(http_client, default_type)

        if isinstance(cred, TempCredentials) and cred.need_update():
            cred.update_credential(http_client)

        return cred

    @classmethod
    def _load_credential_from_metadata(cls, http_client, default_type):
        cred = None
        if BASIC_CREDENTIAL_TYPE == default_type:
            cred = BasicCredentials()
            cred.update_credential(http_client)
        elif GLOBAL_CREDENTIAL_TYPE == default_type:
            cred = GlobalCredentials()
            cred.update_credential(http_client)

        return cred
