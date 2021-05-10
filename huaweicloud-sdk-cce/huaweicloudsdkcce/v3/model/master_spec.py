# coding: utf-8

import pprint
import re

import six





class MasterSpec:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'flavor': 'str',
        'fault_domain': 'str'
    }

    attribute_map = {
        'availability_zone': 'availabilityZone',
        'flavor': 'flavor',
        'fault_domain': 'faultDomain'
    }

    def __init__(self, availability_zone=None, flavor=None, fault_domain=None):
        """MasterSpec - a model defined in huaweicloud sdk"""
        
        

        self._availability_zone = None
        self._flavor = None
        self._fault_domain = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if flavor is not None:
            self.flavor = flavor
        if fault_domain is not None:
            self.fault_domain = fault_domain

    @property
    def availability_zone(self):
        """Gets the availability_zone of this MasterSpec.

        可用区

        :return: The availability_zone of this MasterSpec.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this MasterSpec.

        可用区

        :param availability_zone: The availability_zone of this MasterSpec.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def flavor(self):
        """Gets the flavor of this MasterSpec.

        规格

        :return: The flavor of this MasterSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this MasterSpec.

        规格

        :param flavor: The flavor of this MasterSpec.
        :type: str
        """
        self._flavor = flavor

    @property
    def fault_domain(self):
        """Gets the fault_domain of this MasterSpec.

        故障域。 1. 指定该字段需要当前系统已开启故障域特性，否则校验失败。 2. 仅单az场景支持且必须显式指定az。

        :return: The fault_domain of this MasterSpec.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """Sets the fault_domain of this MasterSpec.

        故障域。 1. 指定该字段需要当前系统已开启故障域特性，否则校验失败。 2. 仅单az场景支持且必须显式指定az。

        :param fault_domain: The fault_domain of this MasterSpec.
        :type: str
        """
        self._fault_domain = fault_domain

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
        if not isinstance(other, MasterSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
