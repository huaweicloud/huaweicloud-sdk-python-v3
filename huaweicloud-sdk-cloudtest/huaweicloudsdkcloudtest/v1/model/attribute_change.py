# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttributeChange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_value': 'str',
        'old_value': 'str',
        'attribute_type': 'str'
    }

    attribute_map = {
        'new_value': 'new_value',
        'old_value': 'old_value',
        'attribute_type': 'attribute_type'
    }

    def __init__(self, new_value=None, old_value=None, attribute_type=None):
        """AttributeChange

        The model defined in huaweicloud sdk

        :param new_value: 变更后的取值
        :type new_value: str
        :param old_value: 变更前的取值
        :type old_value: str
        :param attribute_type: 发生变更的测试计划属性
        :type attribute_type: str
        """
        
        

        self._new_value = None
        self._old_value = None
        self._attribute_type = None
        self.discriminator = None

        if new_value is not None:
            self.new_value = new_value
        if old_value is not None:
            self.old_value = old_value
        if attribute_type is not None:
            self.attribute_type = attribute_type

    @property
    def new_value(self):
        """Gets the new_value of this AttributeChange.

        变更后的取值

        :return: The new_value of this AttributeChange.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this AttributeChange.

        变更后的取值

        :param new_value: The new_value of this AttributeChange.
        :type new_value: str
        """
        self._new_value = new_value

    @property
    def old_value(self):
        """Gets the old_value of this AttributeChange.

        变更前的取值

        :return: The old_value of this AttributeChange.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this AttributeChange.

        变更前的取值

        :param old_value: The old_value of this AttributeChange.
        :type old_value: str
        """
        self._old_value = old_value

    @property
    def attribute_type(self):
        """Gets the attribute_type of this AttributeChange.

        发生变更的测试计划属性

        :return: The attribute_type of this AttributeChange.
        :rtype: str
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """Sets the attribute_type of this AttributeChange.

        发生变更的测试计划属性

        :param attribute_type: The attribute_type of this AttributeChange.
        :type attribute_type: str
        """
        self._attribute_type = attribute_type

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
        if not isinstance(other, AttributeChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
