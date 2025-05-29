# coding: utf-8
"""
 Copyright 2022 Huawei Technologies Co.,Ltd.

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
import six
from abc import abstractmethod
from huaweicloudsdkcore.utils import six_utils, filepath_utils
from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.exceptions.exceptions import ApiTypeError, ApiValueError, SdkException


class _CredentialType:
    BASIC = "basic"
    GLOBAL = "global"


class CredentialProvider(six_utils.get_abstract_meta_class()):
    def __init__(self, credential_type):
        if not credential_type:
            raise ApiValueError("credential type is empty")
        self._credential_type = credential_type.lower()

    @abstractmethod
    def get_credentials(self):
        pass


class EnvCredentialProvider(CredentialProvider):
    _AK_ENV_NAME = "HUAWEICLOUD_SDK_AK"
    _SK_ENV_NAME = "HUAWEICLOUD_SDK_SK"
    _PROJECT_ID_ENV_NAME = "HUAWEICLOUD_SDK_PROJECT_ID"
    _DOMAIN_ID_ENV_NAME = "HUAWEICLOUD_SDK_DOMAIN_ID"
    _SECURITY_TOKEN_ENV_NAME = "HUAWEICLOUD_SDK_SECURITY_TOKEN"
    _IDP_ID_ENV_NAME = "HUAWEICLOUD_SDK_IDP_ID"
    _ID_TOKEN_FILE_ENV_NAME = "HUAWEICLOUD_SDK_ID_TOKEN_FILE"

    @staticmethod
    def get_basic_credential_env_provider():
        return EnvCredentialProvider(_CredentialType.BASIC)

    @staticmethod
    def get_global_credential_env_provider():
        return EnvCredentialProvider(_CredentialType.GLOBAL)

    def get_credentials(self):
        if self._credential_type.startswith(_CredentialType.BASIC):
            credentials = BasicCredentials().with_project_id(os.getenv(self._PROJECT_ID_ENV_NAME))
        elif self._credential_type.startswith(_CredentialType.GLOBAL):
            credentials = GlobalCredentials().with_domain_id(os.getenv(self._DOMAIN_ID_ENV_NAME))
        else:
            raise ApiTypeError("unsupported credential type: " + self._credential_type)

        ak = os.getenv(self._AK_ENV_NAME)
        sk = os.getenv(self._SK_ENV_NAME)
        security_token = os.getenv(self._SECURITY_TOKEN_ENV_NAME)
        idp_id = os.getenv(self._IDP_ID_ENV_NAME)
        id_token_file = os.getenv(self._ID_TOKEN_FILE_ENV_NAME)

        if idp_id and id_token_file:
            credentials.with_idp_id(idp_id).with_id_token_file(id_token_file)
        elif ak and sk:
            credentials.with_ak(ak).with_sk(sk).with_security_token(security_token)
        else:
            raise ApiValueError("ak&sk or idpId&idTokenFile does not exist in environmental variables")

        return credentials


class ProfileCredentialProvider(CredentialProvider):
    _CREDENTIALS_FILE_ENV_NAME = "HUAWEICLOUD_SDK_CREDENTIALS_FILE"
    _DEFAULT_CREDENTIALS_FILE_DIR = ".huaweicloud"
    _DEFAULT_CREDENTIALS_FILE_NAME = "credentials"
    _ENCODING = "utf-8"

    _AK_NAME = "ak"
    _SK_NAME = "sk"
    _PROJECT_ID_NAME = "project_id"
    _DOMAIN_ID_NAME = "domain_id"
    _SECURITY_TOKEN_NAME = "security_token"
    _IAM_ENDPOINT_NAME = "iam_endpoint"
    _IDP_ID_NAME = "idp_id"
    _ID_TOKEN_FILE_NAME = "id_token_file"

    @staticmethod
    def get_basic_credential_profile_provider():
        return ProfileCredentialProvider(_CredentialType.BASIC)

    @staticmethod
    def get_global_credential_profile_provider():
        return ProfileCredentialProvider(_CredentialType.GLOBAL)

    def get_credentials(self):
        if six.PY3:
            import configparser
            parser = configparser.ConfigParser()
        else:
            from backports import configparser
            parser = configparser.SafeConfigParser()

        path = self._get_credentials_file_path()
        if not filepath_utils.is_path_exist(path) or not parser.read(path, encoding=self._ENCODING):
            raise ApiValueError("credentials file '%s' does not exist" % path)

        if not parser.has_section(self._credential_type):
            raise ApiValueError("credential type '%s' does not exist in credentials file '%s'" % (
                self._credential_type, path))

        profile_dict = {}
        for item in parser.items(self._credential_type):
            profile_dict[item[0]] = item[1]

        ak = profile_dict.get(self._AK_NAME)
        sk = profile_dict.get(self._SK_NAME)
        security_token = profile_dict.get(self._SECURITY_TOKEN_NAME)
        idp_id = profile_dict.get(self._IDP_ID_NAME)
        id_token_file = profile_dict.get(self._ID_TOKEN_FILE_NAME)
        iam_endpoint = profile_dict.get(self._IAM_ENDPOINT_NAME)

        if self._credential_type.startswith(_CredentialType.BASIC):
            credentials = BasicCredentials().with_project_id(profile_dict.get(self._PROJECT_ID_NAME))
        elif self._credential_type.startswith(_CredentialType.GLOBAL):
            credentials = GlobalCredentials().with_domain_id(profile_dict.get(self._DOMAIN_ID_NAME))
        else:
            raise ApiTypeError("unsupported credential type '%s'" % self._credential_type)

        if idp_id and id_token_file:
            credentials.with_idp_id(idp_id).with_id_token_file(id_token_file)
        elif ak and sk:
            credentials.with_ak(ak).with_sk(sk).with_security_token(security_token)
        else:
            raise ApiValueError("%s&%s or %s&%s does not exist in credentials file '%s'" % (
                self._AK_NAME, self._SK_NAME, self._AK_NAME, self._SK_NAME, path))
        if iam_endpoint:
            credentials.with_iam_endpoint(iam_endpoint)

        return credentials

    @classmethod
    def _get_credentials_file_path(cls):
        credentials_file = os.getenv(cls._CREDENTIALS_FILE_ENV_NAME)
        if credentials_file:
            return credentials_file

        home_path = filepath_utils.get_home_path()
        return os.path.join(home_path, cls._DEFAULT_CREDENTIALS_FILE_DIR, cls._DEFAULT_CREDENTIALS_FILE_NAME
                            ) if home_path else home_path


class MetadataCredentialProvider(CredentialProvider):
    @staticmethod
    def get_basic_credential_metadata_provider():
        return MetadataBasicCredentialProvider()

    @staticmethod
    def get_global_credential_metadata_provider():
        return MetadataGlobalCredentialProvider()

    def get_credentials(self):
        if self._credential_type.startswith(_CredentialType.BASIC):
            credentials = MetadataBasicCredentialProvider().get_credentials()
        elif self._credential_type.startswith(_CredentialType.GLOBAL):
            credentials = MetadataGlobalCredentialProvider().get_credentials()
        else:
            raise ApiTypeError("unsupported credential type: " + self._credential_type)

        return credentials


class MetadataBasicCredentialProvider(MetadataCredentialProvider):
    def __init__(self, credential_type=_CredentialType.BASIC):
        super(MetadataBasicCredentialProvider, self).__init__(credential_type)
        self._project_id = None

    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value

    def get_credentials(self):
        credentials = BasicCredentials(project_id=self._project_id)
        credentials.update_security_token_from_metadata()
        return credentials


class MetadataGlobalCredentialProvider(MetadataCredentialProvider):
    def __init__(self, credential_type=_CredentialType.GLOBAL):
        super(MetadataGlobalCredentialProvider, self).__init__(credential_type)
        self._domain_id = None

    @property
    def domain_id(self):
        return self._domain_id

    @domain_id.setter
    def domain_id(self, value):
        self._domain_id = value

    def get_credentials(self):
        credentials = GlobalCredentials(domain_id=self._domain_id)
        credentials.update_security_token_from_metadata()
        return credentials


class CredentialProviderChain(object):
    def __init__(self, providers):
        self._providers = providers

    @staticmethod
    def get_basic_credential_provider_chain():
        providers = (
            EnvCredentialProvider.get_basic_credential_env_provider(),
            ProfileCredentialProvider.get_basic_credential_profile_provider(),
            MetadataCredentialProvider.get_basic_credential_metadata_provider()
        )
        return CredentialProviderChain(providers)

    @staticmethod
    def get_global_credential_provider_chain():
        providers = (
            EnvCredentialProvider.get_global_credential_env_provider(),
            ProfileCredentialProvider.get_global_credential_profile_provider(),
            MetadataCredentialProvider.get_global_credential_metadata_provider()
        )
        return CredentialProviderChain(providers)

    @staticmethod
    def get_default_credential_provider_chain(credential_type):
        providers = (
            EnvCredentialProvider(credential_type),
            ProfileCredentialProvider(credential_type),
            MetadataCredentialProvider(credential_type)
        )
        return CredentialProviderChain(providers)

    def get_credentials(self):
        errors = []
        for provider in self._providers:
            try:
                credentials = provider.get_credentials()
                return credentials
            except (ApiTypeError, ApiValueError, SdkException) as e:
                errors.append(str(e))

        raise ApiValueError("Failed to get credentials from provider chain\n" + "\n".join(errors))
