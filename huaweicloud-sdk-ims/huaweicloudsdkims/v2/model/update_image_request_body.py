# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateImageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'op': 'str',
        'path': 'str',
        'value': 'str'
    }

    attribute_map = {
        'op': 'op',
        'path': 'path',
        'value': 'value'
    }

    def __init__(self, op=None, path=None, value=None):
        """UpdateImageRequestBody

        The model defined in huaweicloud sdk

        :param op: 操作类型，目前取值为add，replace和remove。
        :type op: str
        :param path: 需要更新的属性名称，需要在属性名称前加“/”。
        :type path: str
        :param value: 需要更新属性的值。
        :type value: str
        """
        
        

        self._op = None
        self._path = None
        self._value = None
        self.discriminator = None

        self.op = op
        self.path = path
        self.value = value

    @property
    def op(self):
        """Gets the op of this UpdateImageRequestBody.

        操作类型，目前取值为add，replace和remove。

        :return: The op of this UpdateImageRequestBody.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this UpdateImageRequestBody.

        操作类型，目前取值为add，replace和remove。

        :param op: The op of this UpdateImageRequestBody.
        :type op: str
        """
        self._op = op

    @property
    def path(self):
        """Gets the path of this UpdateImageRequestBody.

        需要更新的属性名称，需要在属性名称前加“/”。

        :return: The path of this UpdateImageRequestBody.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this UpdateImageRequestBody.

        需要更新的属性名称，需要在属性名称前加“/”。

        :param path: The path of this UpdateImageRequestBody.
        :type path: str
        """
        self._path = path

    @property
    def value(self):
        """Gets the value of this UpdateImageRequestBody.

        需要更新属性的值。

        :return: The value of this UpdateImageRequestBody.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdateImageRequestBody.

        需要更新属性的值。

        :param value: The value of this UpdateImageRequestBody.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, UpdateImageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
