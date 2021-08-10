import base64
import datetime
import functools
import json
from concurrent.futures.thread import ThreadPoolExecutor
from pprint import pprint

import six

from huaweicloudsdkcore.auth.credentials import Credentials
from huaweicloudsdkcore.exceptions.exceptions import SdkException, ApiValueError
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.signer.signer import process_canonical_query_string


class MeetingCredentials(Credentials):
    def __init__(self, user_name, user_password):
        self._token = None
        self._last_token_date = None

        if user_name is None or user_name == "":
            raise ApiValueError("user_name can not be null.")

        if user_password is None or user_password == "":
            raise ApiValueError("user_password can not be null.")

        self._user_name = user_name
        self._user_password = user_password

    def get_update_path_params(self):
        pass

    def process_auth_request(self, request, http_client, executor=None):
        if executor is None:
            executor = ThreadPoolExecutor(max_workers=1)
        future = executor.submit(self.process_request, request, http_client)
        return future

    def process_request(self, request, http_client):
        now_time = datetime.datetime.now()

        if self._token is None or self._last_token_date is None or (
                now_time - self._last_token_date).days * 24 * 3600 + (
                now_time - self._last_token_date).seconds > 12 * 60 * 60:
            authorization = "Basic " + six.ensure_str(
                base64.b64encode((self._user_name + ':' + self._user_password).encode('utf-8')))
                                           
            body = {'account': self._user_name, 'clientType': 72}
            sdk_request = SdkRequest('POST', 'https', request.host, [], '/v1/usg/acs/auth/account', [],
                                     {'Authorization': authorization, 'Content-Type': 'application/json'},
                                     json.dumps(body), [])

            response = http_client.do_request_sync(sdk_request)
            content = json.loads(response.content.decode())
            self._token = content['accessToken']
            self._last_token_date = datetime.datetime.now()
            request.header_params["X-Access-Token"] = self._token
            canonical_query_string = process_canonical_query_string(request)
            request.uri = request.resource_path + "?" + canonical_query_string if canonical_query_string != "" else request.resource_path
            return request
        else:
            request.header_params["X-Access-Token"] = self._token
            canonical_query_string = process_canonical_query_string(request)
            request.uri = request.resource_path + "?" + canonical_query_string if canonical_query_string != "" else request.resource_path
            return request


