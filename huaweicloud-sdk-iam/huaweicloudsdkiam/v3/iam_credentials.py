from huaweicloudsdkcore.signer.signer import Signer


class IamCredentials:

    _X_AUTH_TOKEN = "X-Auth-Token"

    def __init__(self, auth_token=None):
        self.auth_token = auth_token

    def with_x_auth_token(self, auth_token):
        self.auth_token = auth_token
        return self

    def get_update_path_params(self):
        return {}

    def process_auth_params(self, http_client, region_id):
        return self

    def process_auth_request(self, request, http_client):
        if self.auth_token and self._X_AUTH_TOKEN not in request.header_params:
            request.header_params[self._X_AUTH_TOKEN] = self.auth_token

        Signer.process_request_uri(request)
        return http_client.executor.submit(lambda: request)
