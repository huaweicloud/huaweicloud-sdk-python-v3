# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerJobInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'job_id': 'str',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'job_id': 'job_id',
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, server_id=None, job_id=None, error_code=None, error_message=None):
        r"""ServerJobInfo

        The model defined in huaweicloud sdk

        :param server_id: 服务器ID。
        :type server_id: str
        :param job_id: 任务ID。
        :type job_id: str
        :param error_code: 失败时的错误码。
        :type error_code: str
        :param error_message: 失败原因。
        :type error_message: str
        """
        
        

        self._server_id = None
        self._job_id = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if server_id is not None:
            self.server_id = server_id
        if job_id is not None:
            self.job_id = job_id
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def server_id(self):
        r"""Gets the server_id of this ServerJobInfo.

        服务器ID。

        :return: The server_id of this ServerJobInfo.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ServerJobInfo.

        服务器ID。

        :param server_id: The server_id of this ServerJobInfo.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ServerJobInfo.

        任务ID。

        :return: The job_id of this ServerJobInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ServerJobInfo.

        任务ID。

        :param job_id: The job_id of this ServerJobInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def error_code(self):
        r"""Gets the error_code of this ServerJobInfo.

        失败时的错误码。

        :return: The error_code of this ServerJobInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ServerJobInfo.

        失败时的错误码。

        :param error_code: The error_code of this ServerJobInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this ServerJobInfo.

        失败原因。

        :return: The error_message of this ServerJobInfo.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ServerJobInfo.

        失败原因。

        :param error_message: The error_message of this ServerJobInfo.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, ServerJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
