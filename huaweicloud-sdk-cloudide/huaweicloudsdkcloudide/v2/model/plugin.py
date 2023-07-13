# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Plugin:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attribute': 'str',
        'name': 'str'
    }

    attribute_map = {
        'attribute': 'attribute',
        'name': 'name'
    }

    def __init__(self, attribute=None, name=None):
        """Plugin

        The model defined in huaweicloud sdk

        :param attribute: 插件属性
        :type attribute: str
        :param name: 插件名
        :type name: str
        """
        
        

        self._attribute = None
        self._name = None
        self.discriminator = None

        if attribute is not None:
            self.attribute = attribute
        if name is not None:
            self.name = name

    @property
    def attribute(self):
        """Gets the attribute of this Plugin.

        插件属性

        :return: The attribute of this Plugin.
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this Plugin.

        插件属性

        :param attribute: The attribute of this Plugin.
        :type attribute: str
        """
        self._attribute = attribute

    @property
    def name(self):
        """Gets the name of this Plugin.

        插件名

        :return: The name of this Plugin.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Plugin.

        插件名

        :param name: The name of this Plugin.
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
        if not isinstance(other, Plugin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
