# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomAttributes:

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
        'rules': 'list[CustomAttributesRule]'
    }

    attribute_map = {
        'attribute': 'attribute',
        'rules': 'rules'
    }

    def __init__(self, attribute=None, rules=None):
        """CustomAttributes

        The model defined in huaweicloud sdk

        :param attribute: 配置项属性，severity：为问题级别
        :type attribute: str
        :param rules: 规则详细
        :type rules: list[:class:`huaweicloudsdkcodecheck.v2.CustomAttributesRule`]
        """
        
        

        self._attribute = None
        self._rules = None
        self.discriminator = None

        if attribute is not None:
            self.attribute = attribute
        if rules is not None:
            self.rules = rules

    @property
    def attribute(self):
        """Gets the attribute of this CustomAttributes.

        配置项属性，severity：为问题级别

        :return: The attribute of this CustomAttributes.
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this CustomAttributes.

        配置项属性，severity：为问题级别

        :param attribute: The attribute of this CustomAttributes.
        :type attribute: str
        """
        self._attribute = attribute

    @property
    def rules(self):
        """Gets the rules of this CustomAttributes.

        规则详细

        :return: The rules of this CustomAttributes.
        :rtype: list[:class:`huaweicloudsdkcodecheck.v2.CustomAttributesRule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this CustomAttributes.

        规则详细

        :param rules: The rules of this CustomAttributes.
        :type rules: list[:class:`huaweicloudsdkcodecheck.v2.CustomAttributesRule`]
        """
        self._rules = rules

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
        if not isinstance(other, CustomAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
