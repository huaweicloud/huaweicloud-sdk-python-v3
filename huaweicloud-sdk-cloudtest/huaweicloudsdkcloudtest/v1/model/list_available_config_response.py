# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'error': 'CommonResponseErrorAvailableConfig',
        'reason': 'str',
        'result': 'AvailableConfig',
        'status': 'str'
    }

    attribute_map = {
        'code': 'code',
        'error': 'error',
        'reason': 'reason',
        'result': 'result',
        'status': 'status'
    }

    def __init__(self, code=None, error=None, reason=None, result=None, status=None):
        """ListAvailableConfigResponse

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: str
        :param error: 
        :type error: :class:`huaweicloudsdkcloudtest.v1.CommonResponseErrorAvailableConfig`
        :param reason: 失败原因
        :type reason: str
        :param result: 
        :type result: :class:`huaweicloudsdkcloudtest.v1.AvailableConfig`
        :param status: 状态
        :type status: str
        """
        
        super(ListAvailableConfigResponse, self).__init__()

        self._code = None
        self._error = None
        self._reason = None
        self._result = None
        self._status = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if error is not None:
            self.error = error
        if reason is not None:
            self.reason = reason
        if result is not None:
            self.result = result
        if status is not None:
            self.status = status

    @property
    def code(self):
        """Gets the code of this ListAvailableConfigResponse.

        错误码

        :return: The code of this ListAvailableConfigResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListAvailableConfigResponse.

        错误码

        :param code: The code of this ListAvailableConfigResponse.
        :type code: str
        """
        self._code = code

    @property
    def error(self):
        """Gets the error of this ListAvailableConfigResponse.

        :return: The error of this ListAvailableConfigResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CommonResponseErrorAvailableConfig`
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ListAvailableConfigResponse.

        :param error: The error of this ListAvailableConfigResponse.
        :type error: :class:`huaweicloudsdkcloudtest.v1.CommonResponseErrorAvailableConfig`
        """
        self._error = error

    @property
    def reason(self):
        """Gets the reason of this ListAvailableConfigResponse.

        失败原因

        :return: The reason of this ListAvailableConfigResponse.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ListAvailableConfigResponse.

        失败原因

        :param reason: The reason of this ListAvailableConfigResponse.
        :type reason: str
        """
        self._reason = reason

    @property
    def result(self):
        """Gets the result of this ListAvailableConfigResponse.

        :return: The result of this ListAvailableConfigResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AvailableConfig`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ListAvailableConfigResponse.

        :param result: The result of this ListAvailableConfigResponse.
        :type result: :class:`huaweicloudsdkcloudtest.v1.AvailableConfig`
        """
        self._result = result

    @property
    def status(self):
        """Gets the status of this ListAvailableConfigResponse.

        状态

        :return: The status of this ListAvailableConfigResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAvailableConfigResponse.

        状态

        :param status: The status of this ListAvailableConfigResponse.
        :type status: str
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
        if not isinstance(other, ListAvailableConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
