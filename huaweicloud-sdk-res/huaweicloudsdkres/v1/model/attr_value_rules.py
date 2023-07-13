# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttrValueRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attr_values_a': 'list[AttrValue]',
        'attr_values_b': 'list[AttrValue]'
    }

    attribute_map = {
        'attr_values_a': 'attr_values_a',
        'attr_values_b': 'attr_values_b'
    }

    def __init__(self, attr_values_a=None, attr_values_b=None):
        """AttrValueRules

        The model defined in huaweicloud sdk

        :param attr_values_a: 被推荐对象的属性-值配置。
        :type attr_values_a: list[:class:`huaweicloudsdkres.v1.AttrValue`]
        :param attr_values_b: 待推荐对象的属性-值配置。
        :type attr_values_b: list[:class:`huaweicloudsdkres.v1.AttrValue`]
        """
        
        

        self._attr_values_a = None
        self._attr_values_b = None
        self.discriminator = None

        if attr_values_a is not None:
            self.attr_values_a = attr_values_a
        self.attr_values_b = attr_values_b

    @property
    def attr_values_a(self):
        """Gets the attr_values_a of this AttrValueRules.

        被推荐对象的属性-值配置。

        :return: The attr_values_a of this AttrValueRules.
        :rtype: list[:class:`huaweicloudsdkres.v1.AttrValue`]
        """
        return self._attr_values_a

    @attr_values_a.setter
    def attr_values_a(self, attr_values_a):
        """Sets the attr_values_a of this AttrValueRules.

        被推荐对象的属性-值配置。

        :param attr_values_a: The attr_values_a of this AttrValueRules.
        :type attr_values_a: list[:class:`huaweicloudsdkres.v1.AttrValue`]
        """
        self._attr_values_a = attr_values_a

    @property
    def attr_values_b(self):
        """Gets the attr_values_b of this AttrValueRules.

        待推荐对象的属性-值配置。

        :return: The attr_values_b of this AttrValueRules.
        :rtype: list[:class:`huaweicloudsdkres.v1.AttrValue`]
        """
        return self._attr_values_b

    @attr_values_b.setter
    def attr_values_b(self, attr_values_b):
        """Sets the attr_values_b of this AttrValueRules.

        待推荐对象的属性-值配置。

        :param attr_values_b: The attr_values_b of this AttrValueRules.
        :type attr_values_b: list[:class:`huaweicloudsdkres.v1.AttrValue`]
        """
        self._attr_values_b = attr_values_b

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
        if not isinstance(other, AttrValueRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
