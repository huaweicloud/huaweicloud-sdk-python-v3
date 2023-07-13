# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomFeildRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, key=None, name=None, value=None):
        """CustomFeildRecord

        The model defined in huaweicloud sdk

        :param key: 自定义工作项属性
        :type key: str
        :param name: 自定义工作项名称
        :type name: str
        :param value: 自定义工作项值
        :type value: str
        """
        
        

        self._key = None
        self._name = None
        self._value = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def key(self):
        """Gets the key of this CustomFeildRecord.

        自定义工作项属性

        :return: The key of this CustomFeildRecord.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CustomFeildRecord.

        自定义工作项属性

        :param key: The key of this CustomFeildRecord.
        :type key: str
        """
        self._key = key

    @property
    def name(self):
        """Gets the name of this CustomFeildRecord.

        自定义工作项名称

        :return: The name of this CustomFeildRecord.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomFeildRecord.

        自定义工作项名称

        :param name: The name of this CustomFeildRecord.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this CustomFeildRecord.

        自定义工作项值

        :return: The value of this CustomFeildRecord.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomFeildRecord.

        自定义工作项值

        :param value: The value of this CustomFeildRecord.
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
        if not isinstance(other, CustomFeildRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
