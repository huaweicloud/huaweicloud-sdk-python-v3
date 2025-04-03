from huaweicloudsdkcore.signer.signer import Signer


class IdentityCenterOIDCCredentials:
    def __init__(self):
        pass

    def get_update_path_params(self):
        return {}

    def process_auth_params(self, http_client, region_id):
        return self

    def process_auth_request(self, request, http_client):
        Signer.process_request_uri(request)
        return http_client.executor.submit(lambda: request)
