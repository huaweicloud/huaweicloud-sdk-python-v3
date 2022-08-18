# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionTargetInfoTransform:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'value': 'str',
        'template': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'template': 'template'
    }

    def __init__(self, type=None, value=None, template=None):
        """SubscriptionTargetInfoTransform

        The model defined in huaweicloud sdk

        :param type: 转换规则类型
        :type type: str
        :param value: 转换规则内容
        :type value: str
        :param template: 转换规则模板
        :type template: str
        """
        
        

        self._type = None
        self._value = None
        self._template = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if template is not None:
            self.template = template

    @property
    def type(self):
        """Gets the type of this SubscriptionTargetInfoTransform.

        转换规则类型

        :return: The type of this SubscriptionTargetInfoTransform.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubscriptionTargetInfoTransform.

        转换规则类型

        :param type: The type of this SubscriptionTargetInfoTransform.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this SubscriptionTargetInfoTransform.

        转换规则内容

        :return: The value of this SubscriptionTargetInfoTransform.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SubscriptionTargetInfoTransform.

        转换规则内容

        :param value: The value of this SubscriptionTargetInfoTransform.
        :type value: str
        """
        self._value = value

    @property
    def template(self):
        """Gets the template of this SubscriptionTargetInfoTransform.

        转换规则模板

        :return: The template of this SubscriptionTargetInfoTransform.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this SubscriptionTargetInfoTransform.

        转换规则模板

        :param template: The template of this SubscriptionTargetInfoTransform.
        :type template: str
        """
        self._template = template

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
        if not isinstance(other, SubscriptionTargetInfoTransform):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
