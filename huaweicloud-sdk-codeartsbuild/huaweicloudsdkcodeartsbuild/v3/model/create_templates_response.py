# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'list[CreateTemplatesItems]',
        'error': 'str',
        'status': 'str'
    }

    attribute_map = {
        'result': 'result',
        'error': 'error',
        'status': 'status'
    }

    def __init__(self, result=None, error=None, status=None):
        """CreateTemplatesResponse

        The model defined in huaweicloud sdk

        :param result: 查询模板结果
        :type result: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateTemplatesItems`]
        :param error: 返回错误信息
        :type error: str
        :param status: 返回状态信息
        :type status: str
        """
        
        super(CreateTemplatesResponse, self).__init__()

        self._result = None
        self._error = None
        self._status = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if error is not None:
            self.error = error
        if status is not None:
            self.status = status

    @property
    def result(self):
        """Gets the result of this CreateTemplatesResponse.

        查询模板结果

        :return: The result of this CreateTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateTemplatesItems`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CreateTemplatesResponse.

        查询模板结果

        :param result: The result of this CreateTemplatesResponse.
        :type result: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateTemplatesItems`]
        """
        self._result = result

    @property
    def error(self):
        """Gets the error of this CreateTemplatesResponse.

        返回错误信息

        :return: The error of this CreateTemplatesResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this CreateTemplatesResponse.

        返回错误信息

        :param error: The error of this CreateTemplatesResponse.
        :type error: str
        """
        self._error = error

    @property
    def status(self):
        """Gets the status of this CreateTemplatesResponse.

        返回状态信息

        :return: The status of this CreateTemplatesResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateTemplatesResponse.

        返回状态信息

        :param status: The status of this CreateTemplatesResponse.
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
        if not isinstance(other, CreateTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
