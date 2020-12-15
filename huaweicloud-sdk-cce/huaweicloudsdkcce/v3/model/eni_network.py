# coding: utf-8

import pprint
import re

import six





class ENINetwork:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'eni_subnet_cidr': 'str',
        'eni_subnet_id': 'str'
    }

    attribute_map = {
        'eni_subnet_cidr': 'eniSubnetCIDR',
        'eni_subnet_id': 'eniSubnetId'
    }

    def __init__(self, eni_subnet_cidr=None, eni_subnet_id=None):
        """ENINetwork - a model defined in huaweicloud sdk"""
        
        

        self._eni_subnet_cidr = None
        self._eni_subnet_id = None
        self.discriminator = None

        self.eni_subnet_cidr = eni_subnet_cidr
        self.eni_subnet_id = eni_subnet_id

    @property
    def eni_subnet_cidr(self):
        """Gets the eni_subnet_cidr of this ENINetwork.

        ENI子网CIDR

        :return: The eni_subnet_cidr of this ENINetwork.
        :rtype: str
        """
        return self._eni_subnet_cidr

    @eni_subnet_cidr.setter
    def eni_subnet_cidr(self, eni_subnet_cidr):
        """Sets the eni_subnet_cidr of this ENINetwork.

        ENI子网CIDR

        :param eni_subnet_cidr: The eni_subnet_cidr of this ENINetwork.
        :type: str
        """
        self._eni_subnet_cidr = eni_subnet_cidr

    @property
    def eni_subnet_id(self):
        """Gets the eni_subnet_id of this ENINetwork.

        eni子网ID

        :return: The eni_subnet_id of this ENINetwork.
        :rtype: str
        """
        return self._eni_subnet_id

    @eni_subnet_id.setter
    def eni_subnet_id(self, eni_subnet_id):
        """Sets the eni_subnet_id of this ENINetwork.

        eni子网ID

        :param eni_subnet_id: The eni_subnet_id of this ENINetwork.
        :type: str
        """
        self._eni_subnet_id = eni_subnet_id

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
        if not isinstance(other, ENINetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
