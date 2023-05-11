# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserAttrs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'data_type': 'data_type',
        'name': 'name'
    }

    def __init__(self, data_type=None, name=None):
        """UserAttrs

        The model defined in huaweicloud sdk

        :param data_type: 数据类型。
        :type data_type: str
        :param name: 用户名称。
        :type name: str
        """
        
        

        self._data_type = None
        self._name = None
        self.discriminator = None

        if data_type is not None:
            self.data_type = data_type
        if name is not None:
            self.name = name

    @property
    def data_type(self):
        """Gets the data_type of this UserAttrs.

        数据类型。

        :return: The data_type of this UserAttrs.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this UserAttrs.

        数据类型。

        :param data_type: The data_type of this UserAttrs.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def name(self):
        """Gets the name of this UserAttrs.

        用户名称。

        :return: The name of this UserAttrs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserAttrs.

        用户名称。

        :param name: The name of this UserAttrs.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, UserAttrs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
