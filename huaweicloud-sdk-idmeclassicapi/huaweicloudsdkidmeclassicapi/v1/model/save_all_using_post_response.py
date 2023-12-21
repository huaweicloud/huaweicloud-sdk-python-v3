# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaveAllUsingPostResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'data': 'list[int]',
        'errors': 'list[str]'
    }

    attribute_map = {
        'result': 'result',
        'data': 'data',
        'errors': 'errors'
    }

    def __init__(self, result=None, data=None, errors=None):
        """SaveAllUsingPostResponse

        The model defined in huaweicloud sdk

        :param result: 请求结果。
        :type result: str
        :param data: 请求数据。
        :type data: list[int]
        :param errors: 异常信息。
        :type errors: list[str]
        """
        
        super(SaveAllUsingPostResponse, self).__init__()

        self._result = None
        self._data = None
        self._errors = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if data is not None:
            self.data = data
        if errors is not None:
            self.errors = errors

    @property
    def result(self):
        """Gets the result of this SaveAllUsingPostResponse.

        请求结果。

        :return: The result of this SaveAllUsingPostResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this SaveAllUsingPostResponse.

        请求结果。

        :param result: The result of this SaveAllUsingPostResponse.
        :type result: str
        """
        self._result = result

    @property
    def data(self):
        """Gets the data of this SaveAllUsingPostResponse.

        请求数据。

        :return: The data of this SaveAllUsingPostResponse.
        :rtype: list[int]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SaveAllUsingPostResponse.

        请求数据。

        :param data: The data of this SaveAllUsingPostResponse.
        :type data: list[int]
        """
        self._data = data

    @property
    def errors(self):
        """Gets the errors of this SaveAllUsingPostResponse.

        异常信息。

        :return: The errors of this SaveAllUsingPostResponse.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this SaveAllUsingPostResponse.

        异常信息。

        :param errors: The errors of this SaveAllUsingPostResponse.
        :type errors: list[str]
        """
        self._errors = errors

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
        if not isinstance(other, SaveAllUsingPostResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
