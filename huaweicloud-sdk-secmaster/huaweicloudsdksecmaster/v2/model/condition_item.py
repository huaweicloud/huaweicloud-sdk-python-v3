# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConditionItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'detail': 'str',
        'data': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'detail': 'detail',
        'data': 'data'
    }

    def __init__(self, name=None, detail=None, data=None):
        """ConditionItem

        The model defined in huaweicloud sdk

        :param name: Name of the condition.
        :type name: str
        :param detail: Detail of the condition.
        :type detail: str
        :param data: Detail of the condition.
        :type data: list[str]
        """
        
        

        self._name = None
        self._detail = None
        self._data = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if detail is not None:
            self.detail = detail
        if data is not None:
            self.data = data

    @property
    def name(self):
        """Gets the name of this ConditionItem.

        Name of the condition.

        :return: The name of this ConditionItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConditionItem.

        Name of the condition.

        :param name: The name of this ConditionItem.
        :type name: str
        """
        self._name = name

    @property
    def detail(self):
        """Gets the detail of this ConditionItem.

        Detail of the condition.

        :return: The detail of this ConditionItem.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ConditionItem.

        Detail of the condition.

        :param detail: The detail of this ConditionItem.
        :type detail: str
        """
        self._detail = detail

    @property
    def data(self):
        """Gets the data of this ConditionItem.

        Detail of the condition.

        :return: The data of this ConditionItem.
        :rtype: list[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ConditionItem.

        Detail of the condition.

        :param data: The data of this ConditionItem.
        :type data: list[str]
        """
        self._data = data

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
        if not isinstance(other, ConditionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
