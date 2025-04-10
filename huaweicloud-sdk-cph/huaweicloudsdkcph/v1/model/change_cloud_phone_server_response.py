# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeCloudPhoneServerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'server_id': 'str',
        'job_id': 'str',
        'error_msg': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'server_id': 'server_id',
        'job_id': 'job_id',
        'error_msg': 'error_msg',
        'error_code': 'error_code'
    }

    def __init__(self, request_id=None, server_id=None, job_id=None, error_msg=None, error_code=None):
        r"""ChangeCloudPhoneServerResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param server_id: 服务器id。
        :type server_id: str
        :param job_id: 任务id。
        :type job_id: str
        :param error_msg: 任务错误码说明。
        :type error_msg: str
        :param error_code: 任务错误码。
        :type error_code: str
        """
        
        super(ChangeCloudPhoneServerResponse, self).__init__()

        self._request_id = None
        self._server_id = None
        self._job_id = None
        self._error_msg = None
        self._error_code = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if server_id is not None:
            self.server_id = server_id
        if job_id is not None:
            self.job_id = job_id
        if error_msg is not None:
            self.error_msg = error_msg
        if error_code is not None:
            self.error_code = error_code

    @property
    def request_id(self):
        r"""Gets the request_id of this ChangeCloudPhoneServerResponse.

        请求的唯一标识ID。

        :return: The request_id of this ChangeCloudPhoneServerResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ChangeCloudPhoneServerResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ChangeCloudPhoneServerResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def server_id(self):
        r"""Gets the server_id of this ChangeCloudPhoneServerResponse.

        服务器id。

        :return: The server_id of this ChangeCloudPhoneServerResponse.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ChangeCloudPhoneServerResponse.

        服务器id。

        :param server_id: The server_id of this ChangeCloudPhoneServerResponse.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ChangeCloudPhoneServerResponse.

        任务id。

        :return: The job_id of this ChangeCloudPhoneServerResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ChangeCloudPhoneServerResponse.

        任务id。

        :param job_id: The job_id of this ChangeCloudPhoneServerResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ChangeCloudPhoneServerResponse.

        任务错误码说明。

        :return: The error_msg of this ChangeCloudPhoneServerResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ChangeCloudPhoneServerResponse.

        任务错误码说明。

        :param error_msg: The error_msg of this ChangeCloudPhoneServerResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def error_code(self):
        r"""Gets the error_code of this ChangeCloudPhoneServerResponse.

        任务错误码。

        :return: The error_code of this ChangeCloudPhoneServerResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ChangeCloudPhoneServerResponse.

        任务错误码。

        :param error_code: The error_code of this ChangeCloudPhoneServerResponse.
        :type error_code: str
        """
        self._error_code = error_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChangeCloudPhoneServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
