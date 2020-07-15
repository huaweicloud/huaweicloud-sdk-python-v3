# coding: utf-8

import pprint
import re

import six





class PrePaidServerPublicip:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'eip': 'PrePaidServerEip'
    }

    attribute_map = {
        'id': 'id',
        'eip': 'eip'
    }

    def __init__(self, id=None, eip=None):
        """PrePaidServerPublicip - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._eip = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if eip is not None:
            self.eip = eip

    @property
    def id(self):
        """Gets the id of this PrePaidServerPublicip.

        为待创建云服务器分配已有弹性IP时，分配的弹性IP的ID，UUID格式。  约束：只能分配状态（status）为DOWN的弹性IP。

        :return: The id of this PrePaidServerPublicip.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrePaidServerPublicip.

        为待创建云服务器分配已有弹性IP时，分配的弹性IP的ID，UUID格式。  约束：只能分配状态（status）为DOWN的弹性IP。

        :param id: The id of this PrePaidServerPublicip.
        :type: str
        """
        self._id = id

    @property
    def eip(self):
        """Gets the eip of this PrePaidServerPublicip.


        :return: The eip of this PrePaidServerPublicip.
        :rtype: PrePaidServerEip
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this PrePaidServerPublicip.


        :param eip: The eip of this PrePaidServerPublicip.
        :type: PrePaidServerEip
        """
        self._eip = eip

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
        if not isinstance(other, PrePaidServerPublicip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
