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

import os
import stat

import pytest

from huaweicloudsdkcore.auth import provider
from huaweicloudsdkcore.utils import filepath_utils
from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.exceptions.exceptions import ApiValueError

AK = "ak"
SK = "sk"
SECURITY_TOKEN = "security_token"
PROJECT_ID = "project_id"
DOMAIN_ID = "domain_id"
IDP_ID = "idp_id"
ID_TOKEN_FILE = "id_token_file"
IAM_ENDPOINT = "https://iam.endpoint.com"

CONTENT = r"""[basic]
idp_id = idp_id
id_token_file = id_token_file
project_id = project_id
iam_endpoint = https://iam.endpoint.com

[global]                          
ak = ak
sk = sk
domain_id = domain_id
security_token = security_token
iam_endpoint = https://iam.endpoint.com
"""


def _clear_envs():
    keys = (key for key in os.environ.keys() if key.startswith("HUAWEICLOUD_SDK"))
    for key in keys:
        os.environ.pop(key)


def _get_credentials_file_dir():
    home_path = filepath_utils.get_home_path()
    if home_path:
        return home_path
    return os.path.abspath(os.curdir)


class TestEnvCredentialProvider:
    def teardown(self):
        _clear_envs()

    def test_without_env_with_basic_type(self):
        p = provider.EnvCredentialProvider.get_basic_credential_env_provider()
        try:
            p.get_credentials()
        except ApiValueError as e:
            assert "ak&sk or idpId&idTokenFile does not exist in environmental variables" == str(e)

    def test_ak_auth_with_basic_type(self):
        p = provider.EnvCredentialProvider.get_basic_credential_env_provider()
        os.environ["HUAWEICLOUD_SDK_AK"] = AK
        os.environ["HUAWEICLOUD_SDK_SK"] = SK
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        os.environ["HUAWEICLOUD_SDK_SECURITY_TOKEN"] = SECURITY_TOKEN
        actual = p.get_credentials()
        expected = BasicCredentials(AK, SK, PROJECT_ID).with_security_token(SECURITY_TOKEN)
        assert expected.ak == actual.ak \
               and expected.sk == actual.sk \
               and expected.project_id == actual.project_id \
               and expected.security_token == actual.security_token

    def test_id_token_auth_with_basic_type(self):
        p = provider.EnvCredentialProvider.get_basic_credential_env_provider()
        os.environ["HUAWEICLOUD_SDK_IDP_ID"] = IDP_ID
        os.environ["HUAWEICLOUD_SDK_ID_TOKEN_FILE"] = ID_TOKEN_FILE
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        actual = p.get_credentials()
        expected = BasicCredentials().with_idp_id(IDP_ID).with_id_token_file(ID_TOKEN_FILE).with_project_id(PROJECT_ID)
        assert expected.idp_id == actual.idp_id \
               and expected.id_token_file == actual.id_token_file \
               and expected.project_id == actual.project_id \
               and actual.ak is None \
               and actual.sk is None

    def test_without_env_with_global_type(self):
        p = provider.EnvCredentialProvider.get_global_credential_env_provider()
        try:
            p.get_credentials()
        except ApiValueError as e:
            assert "ak&sk or idpId&idTokenFile does not exist in environmental variables" == str(e)

    def test_ak_auth_with_global_type(self):
        p = provider.EnvCredentialProvider.get_global_credential_env_provider()
        os.environ["HUAWEICLOUD_SDK_AK"] = AK
        os.environ["HUAWEICLOUD_SDK_SK"] = SK
        os.environ["HUAWEICLOUD_SDK_DOMAIN_ID"] = DOMAIN_ID
        os.environ["HUAWEICLOUD_SDK_SECURITY_TOKEN"] = SECURITY_TOKEN
        actual = p.get_credentials()
        expected = GlobalCredentials(AK, SK, DOMAIN_ID).with_security_token(SECURITY_TOKEN)
        assert expected.ak == actual.ak \
               and expected.sk == actual.sk \
               and expected.domain_id == actual.domain_id \
               and expected.security_token == actual.security_token

    def test_id_token_auth_with_global_type(self):
        p = provider.EnvCredentialProvider.get_global_credential_env_provider()
        os.environ["HUAWEICLOUD_SDK_IDP_ID"] = IDP_ID
        os.environ["HUAWEICLOUD_SDK_ID_TOKEN_FILE"] = ID_TOKEN_FILE
        os.environ["HUAWEICLOUD_SDK_DOMAIN_ID"] = DOMAIN_ID
        actual = p.get_credentials()
        expected = GlobalCredentials().with_idp_id(IDP_ID).with_id_token_file(ID_TOKEN_FILE).with_domain_id(DOMAIN_ID)
        assert expected.idp_id == actual.idp_id \
               and expected.id_token_file == actual.id_token_file \
               and expected.domain_id == actual.domain_id \
               and actual.ak is None \
               and actual.sk is None


class TestProfileCredentialProvider:
    CREDENTIALS_FILE_ENV_NAME = "HUAWEICLOUD_SDK_CREDENTIALS_FILE"
    CREDENTIALS_FILE_DIR = _get_credentials_file_dir()
    TEST_CREDENTIALS_FILE = os.path.join(CREDENTIALS_FILE_DIR, "test_credentials")

    @classmethod
    def setup_class(cls):
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        modes = stat.S_IWUSR | stat.S_IRUSR
        with os.fdopen(os.open(cls.TEST_CREDENTIALS_FILE, flags, modes), 'w') as f:
            f.write(CONTENT)

    @classmethod
    def teardown_class(cls):
        if os.path.exists(cls.TEST_CREDENTIALS_FILE):
            os.remove(cls.TEST_CREDENTIALS_FILE)

    def setup(self):
        os.environ[self.CREDENTIALS_FILE_ENV_NAME] = self.TEST_CREDENTIALS_FILE

    def teardown(self):
        if self.CREDENTIALS_FILE_ENV_NAME in os.environ:
            os.environ.pop(self.CREDENTIALS_FILE_ENV_NAME)

    def test_file_not_exist(self):
        # test not found
        path = os.path.join(self.CREDENTIALS_FILE_DIR, "not_exist")
        os.environ[self.CREDENTIALS_FILE_ENV_NAME] = path
        p = provider.ProfileCredentialProvider.get_basic_credential_profile_provider()
        try:
            p.get_credentials()
        except ApiValueError as e:
            assert "credentials file '{}' does not exist".format(path) == str(e)
            os.environ["HUAWEICLOUD_SDK_CREDENTIALS_FILE"] = self.TEST_CREDENTIALS_FILE

    def test_basic_type(self):
        p = provider.ProfileCredentialProvider.get_basic_credential_profile_provider()
        actual = p.get_credentials()
        expected = BasicCredentials() \
            .with_idp_id(IDP_ID) \
            .with_id_token_file(ID_TOKEN_FILE) \
            .with_project_id(PROJECT_ID) \
            .with_iam_endpoint(IAM_ENDPOINT)
        assert expected.idp_id == actual.idp_id \
               and expected.id_token_file == actual.id_token_file \
               and expected.project_id == actual.project_id \
               and expected.iam_endpoint == actual.iam_endpoint

    def test_global_type(self):
        p = provider.ProfileCredentialProvider.get_global_credential_profile_provider()
        actual = p.get_credentials()
        expected = GlobalCredentials(AK, SK, DOMAIN_ID) \
            .with_security_token(SECURITY_TOKEN) \
            .with_iam_endpoint(IAM_ENDPOINT)
        assert expected.ak == actual.ak \
               and expected.sk == actual.sk \
               and expected.domain_id == actual.domain_id \
               and expected.security_token == actual.security_token \
               and expected.iam_endpoint == actual.iam_endpoint


class TestCredentialProviderChain:

    @classmethod
    def teardown_class(cls):
        _clear_envs()

    def test_custom_providers(self):
        providers = [
            provider.ProfileCredentialProvider.get_basic_credential_profile_provider(),
            provider.EnvCredentialProvider.get_basic_credential_env_provider()
        ]
        path = os.path.join(_get_credentials_file_dir(), "not_exist")
        os.environ["HUAWEICLOUD_SDK_CREDENTIALS_FILE"] = path
        chain = provider.CredentialProviderChain(providers)
        try:
            chain.get_credentials()
        except ApiValueError as e:
            assert "failed to get credentials from provider chain\n" \
                   "credentials file '{}' does not exist\n" \
                   "ak&sk or idpId&idTokenFile does not exist in environmental variables".format(path) == str(e)

        os.environ["HUAWEICLOUD_SDK_AK"] = AK
        os.environ["HUAWEICLOUD_SDK_SK"] = SK
        actual = chain.get_credentials()
        expected = BasicCredentials(AK, SK)
        assert expected.ak == actual.ak and expected.sk == actual.sk


if __name__ == '__main__':
    pytest.main()
