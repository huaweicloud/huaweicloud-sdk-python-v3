import base64
import datetime
import functools
import json
from concurrent.futures.thread import ThreadPoolExecutor
from pprint import pprint

from huaweicloudsdkcore.auth.credentials import Credentials
from huaweicloudsdkcore.exceptions.exceptions import SdkException
from huaweicloudsdkcore.sdk_request import SdkRequest


class MeetingCredentials(Credentials):
    def __init__(self, username, password):
        self._token = None
        self._last_token_date = None

        if username is None or username == "":
            raise ApiValueError("username can not be null.")

        if password is None or password == "":
            raise ApiValueError("password can not be null.")

        self._username = username
        self._password = password

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
            authorization = "Basic " + str(base64.b64encode((self._username + ':' + self._password).encode('utf-8')),
                                           'utf-8')
                                           
            body = {'account': self._username, 'clientType': 0}
            sdk_request = SdkRequest('POST', 'https', request.host, [], '/v1/usg/acs/auth/account', [],
                                     {'Authorization': authorization, 'Content-Type': 'application/json'},
                                     json.dumps(body), [])

            response = http_client.do_request_sync(sdk_request)
            content = json.loads(response.content.decode())
            self._token = content['accessToken']
            self._last_token_date = datetime.datetime.now()
            request.header_params["X-Auth-Token"] = self._token
            request.uri = request.resource_path
            return request
        else:
            request.header_params["X-Auth-Token"] = self._token
            request.uri = request.resource_path
            return request


