# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityProperty:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'rules': 'SecurityRule'
    }

    attribute_map = {
        'enable': 'enable',
        'rules': 'rules'
    }

    def __init__(self, enable=None, rules=None):
        """SecurityProperty

        The model defined in huaweicloud sdk

        :param enable: 是否启用
        :type enable: bool
        :param rules: 
        :type rules: :class:`huaweicloudsdkcodeartspipeline.v2.SecurityRule`
        """
        
        

        self._enable = None
        self._rules = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if rules is not None:
            self.rules = rules

    @property
    def enable(self):
        """Gets the enable of this SecurityProperty.

        是否启用

        :return: The enable of this SecurityProperty.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this SecurityProperty.

        是否启用

        :param enable: The enable of this SecurityProperty.
        :type enable: bool
        """
        self._enable = enable

    @property
    def rules(self):
        """Gets the rules of this SecurityProperty.

        :return: The rules of this SecurityProperty.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.SecurityRule`
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this SecurityProperty.

        :param rules: The rules of this SecurityProperty.
        :type rules: :class:`huaweicloudsdkcodeartspipeline.v2.SecurityRule`
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
        if not isinstance(other, SecurityProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
