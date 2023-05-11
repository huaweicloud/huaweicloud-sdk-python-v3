# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'object',
        'type': 'str'
    }

    attribute_map = {
        'data': 'data',
        'type': 'type'
    }

    def __init__(self, data=None, type=None):
        """TaskInput

        The model defined in huaweicloud sdk

        :param data: 输入数据
        :type data: object
        :param type: 输入类型
        :type type: str
        """
        
        

        self._data = None
        self._type = None
        self.discriminator = None

        self.data = data
        self.type = type

    @property
    def data(self):
        """Gets the data of this TaskInput.

        输入数据

        :return: The data of this TaskInput.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TaskInput.

        输入数据

        :param data: The data of this TaskInput.
        :type data: object
        """
        self._data = data

    @property
    def type(self):
        """Gets the type of this TaskInput.

        输入类型

        :return: The type of this TaskInput.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskInput.

        输入类型

        :param type: The type of this TaskInput.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, TaskInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
