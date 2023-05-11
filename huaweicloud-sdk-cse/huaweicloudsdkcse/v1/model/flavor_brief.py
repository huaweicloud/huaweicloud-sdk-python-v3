# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorBrief:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'description': 'str'
    }

    attribute_map = {
        'flavor': 'flavor',
        'description': 'description'
    }

    def __init__(self, flavor=None, description=None):
        """FlavorBrief

        The model defined in huaweicloud sdk

        :param flavor: 微服务引擎专享版规格
        :type flavor: str
        :param description: 微服务引擎专享版规格描述
        :type description: str
        """
        
        

        self._flavor = None
        self._description = None
        self.discriminator = None

        if flavor is not None:
            self.flavor = flavor
        if description is not None:
            self.description = description

    @property
    def flavor(self):
        """Gets the flavor of this FlavorBrief.

        微服务引擎专享版规格

        :return: The flavor of this FlavorBrief.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this FlavorBrief.

        微服务引擎专享版规格

        :param flavor: The flavor of this FlavorBrief.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def description(self):
        """Gets the description of this FlavorBrief.

        微服务引擎专享版规格描述

        :return: The description of this FlavorBrief.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FlavorBrief.

        微服务引擎专享版规格描述

        :param description: The description of this FlavorBrief.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, FlavorBrief):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
