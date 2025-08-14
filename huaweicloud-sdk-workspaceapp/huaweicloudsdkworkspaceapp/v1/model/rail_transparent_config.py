# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RailTransparentConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'select_policy': 'int',
        'transparent_list_custom': 'str'
    }

    attribute_map = {
        'select_policy': 'select_policy',
        'transparent_list_custom': 'transparent_list_custom'
    }

    def __init__(self, select_policy=None, transparent_list_custom=None):
        r"""RailTransparentConfig

        The model defined in huaweicloud sdk

        :param select_policy: 策略选值原则。
        :type select_policy: int
        :param transparent_list_custom: 配置项内容。
        :type transparent_list_custom: str
        """
        
        

        self._select_policy = None
        self._transparent_list_custom = None
        self.discriminator = None

        if select_policy is not None:
            self.select_policy = select_policy
        if transparent_list_custom is not None:
            self.transparent_list_custom = transparent_list_custom

    @property
    def select_policy(self):
        r"""Gets the select_policy of this RailTransparentConfig.

        策略选值原则。

        :return: The select_policy of this RailTransparentConfig.
        :rtype: int
        """
        return self._select_policy

    @select_policy.setter
    def select_policy(self, select_policy):
        r"""Sets the select_policy of this RailTransparentConfig.

        策略选值原则。

        :param select_policy: The select_policy of this RailTransparentConfig.
        :type select_policy: int
        """
        self._select_policy = select_policy

    @property
    def transparent_list_custom(self):
        r"""Gets the transparent_list_custom of this RailTransparentConfig.

        配置项内容。

        :return: The transparent_list_custom of this RailTransparentConfig.
        :rtype: str
        """
        return self._transparent_list_custom

    @transparent_list_custom.setter
    def transparent_list_custom(self, transparent_list_custom):
        r"""Sets the transparent_list_custom of this RailTransparentConfig.

        配置项内容。

        :param transparent_list_custom: The transparent_list_custom of this RailTransparentConfig.
        :type transparent_list_custom: str
        """
        self._transparent_list_custom = transparent_list_custom

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
        if not isinstance(other, RailTransparentConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
