# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class InvokeFunctionResponse(SdkResponse):


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
        'result': 'str',
        'log': 'str',
        'status': 'int'
    }

    attribute_map = {
        'request_id': 'request_id',
        'result': 'result',
        'log': 'log',
        'status': 'status'
    }

    def __init__(self, request_id=None, result=None, log=None, status=None):
        """InvokeFunctionResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._request_id = None
        self._result = None
        self._log = None
        self._status = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if result is not None:
            self.result = result
        if log is not None:
            self.log = log
        if status is not None:
            self.status = status

    @property
    def request_id(self):
        """Gets the request_id of this InvokeFunctionResponse.

        请求ID。

        :return: The request_id of this InvokeFunctionResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this InvokeFunctionResponse.

        请求ID。

        :param request_id: The request_id of this InvokeFunctionResponse.
        :type: str
        """
        self._request_id = request_id

    @property
    def result(self):
        """Gets the result of this InvokeFunctionResponse.

        函数执行结果

        :return: The result of this InvokeFunctionResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this InvokeFunctionResponse.

        函数执行结果

        :param result: The result of this InvokeFunctionResponse.
        :type: str
        """
        self._result = result

    @property
    def log(self):
        """Gets the log of this InvokeFunctionResponse.

        函数执行返回日志

        :return: The log of this InvokeFunctionResponse.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this InvokeFunctionResponse.

        函数执行返回日志

        :param log: The log of this InvokeFunctionResponse.
        :type: str
        """
        self._log = log

    @property
    def status(self):
        """Gets the status of this InvokeFunctionResponse.

        函数执行返回状态

        :return: The status of this InvokeFunctionResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InvokeFunctionResponse.

        函数执行返回状态

        :param status: The status of this InvokeFunctionResponse.
        :type: int
        """
        self._status = status

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InvokeFunctionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
