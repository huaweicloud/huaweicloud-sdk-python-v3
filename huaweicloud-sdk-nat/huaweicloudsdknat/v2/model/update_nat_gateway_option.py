# coding: utf-8

import pprint
import re

import six





class UpdateNatGatewayOption:


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
        'description': 'str',
        'spec': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'spec': 'spec'
    }

    def __init__(self, name=None, description=None, spec=None):
        """UpdateNatGatewayOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._spec = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if spec is not None:
            self.spec = spec

    @property
    def name(self):
        """Gets the name of this UpdateNatGatewayOption.

        公网NAT网关实例的名字，长度限制为64。 公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。

        :return: The name of this UpdateNatGatewayOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateNatGatewayOption.

        公网NAT网关实例的名字，长度限制为64。 公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。

        :param name: The name of this UpdateNatGatewayOption.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateNatGatewayOption.

        公网NAT网关的描述，长度限制为255。

        :return: The description of this UpdateNatGatewayOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateNatGatewayOption.

        公网NAT网关的描述，长度限制为255。

        :param description: The description of this UpdateNatGatewayOption.
        :type: str
        """
        self._description = description

    @property
    def spec(self):
        """Gets the spec of this UpdateNatGatewayOption.

        公网NAT网关的规格。 取值为： \"1\"：小型，SNAT最大连接数10000 \"2\"：中型，SNAT最大连接数50000 \"3\"：大型，SNAT最大连接数200000 \"4\"：超大型，SNAT最大连接数1000000 

        :return: The spec of this UpdateNatGatewayOption.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this UpdateNatGatewayOption.

        公网NAT网关的规格。 取值为： \"1\"：小型，SNAT最大连接数10000 \"2\"：中型，SNAT最大连接数50000 \"3\"：大型，SNAT最大连接数200000 \"4\"：超大型，SNAT最大连接数1000000 

        :param spec: The spec of this UpdateNatGatewayOption.
        :type: str
        """
        self._spec = spec

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateNatGatewayOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
