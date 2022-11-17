# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkcore.auth.credentials import Credentials
from huaweicloudsdkcore.exceptions.exceptions import ApiValueError, ServiceResponseException
from huaweicloudsdkcore.auth.cache import AuthCache

from huaweicloudsdkiotda.v5.region.iotda_region import IoTDARegion
from huaweicloudsdkcore.signer.signer import Signer, DerivationAKSKSigner
from huaweicloudsdkcore.auth.internal import Iam


class IoTDACredentials(Credentials):
    _DERIVED_AUTH_SERVICE_NAME = "iotdm"

    def __init__(self, ak, sk, project_id=None):
        if not ak:
            raise ApiValueError("AK can not be null.")
        if not sk:
            raise ApiValueError("SK can not be null.")
        super(IoTDACredentials, self).__init__(ak, sk)
        self.project_id = project_id
        self.region_id = None
        """
        是否为默认端点
        True: 默认端点，使用 {huaweicloudsdkcore.auth.credentials.BasicCredentials} 方式相同的
        False or None: 非默认端点
        """
        self.default_endpoint = None

    def with_default_iam_endpoint(self, is_default_endpoint):
        self.default_endpoint = is_default_endpoint
        return self

    def get_update_path_params(self):
        path_params = {}
        if self.project_id:
            path_params["project_id"] = self.project_id
        return path_params

    def process_auth_params(self, http_client, region_id):
        self.region_id = region_id

        if self.project_id:
            return self

        ak_with_name = self.ak + region_id
        project_id = AuthCache.get_auth(ak_with_name)
        if project_id:
            self.project_id = project_id
            return self

        if self.iam_endpoint is None:
            self.iam_endpoint = Iam.DEFAULT_ENDPOINT
        future_request = self.process_auth_request(
            Iam.get_keystone_list_projects_request(self.iam_endpoint, region_id=region_id), http_client)
        request = future_request.result()
        try:
            self.project_id = Iam.keystone_list_projects(http_client, request)
            AuthCache.put_auth(ak_with_name, self.project_id)
        except ServiceResponseException as e:
            err_msg = e.error_msg if hasattr(e, "error_msg") else "unknown exception."
            raise ApiValueError("Failed to get project id, " + err_msg)
        return self

    def process_auth_request(self, request, http_client):
        return super(IoTDACredentials, self).process_auth_request(request, http_client)

    def sign_request(self, request):
        if self.project_id:
            request.header_params["X-Project-Id"] = self.project_id
        if self.security_token is not None:
            request.header_params["X-Security-Token"] = self.security_token

        if "Content-Type" in request.header_params and not request.header_params["Content-Type"].startswith(
                "application/json"):
            request.header_params["X-Sdk-Content-Sha256"] = "UNSIGNED-PAYLOAD"

        if self.is_default_endpoint(request):
            return Signer(self).sign(request)
        else:
            return DerivationAKSKSigner(self).sign(request, self._DERIVED_AUTH_SERVICE_NAME, self.region_id)

    def is_default_endpoint(self, request):
        if self.default_endpoint is not None:
            return self.default_endpoint

        try:
            request_endpoint = request.schema + "://" + request.host
            return IoTDARegion.value_of(self.region_id).endpoint == request_endpoint
        except KeyError as e:
            return False
