# coding: utf-8

import pprint
import re

import six





class PrePaidServerSchedulerHints:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group': 'str',
        'tenancy': 'str',
        'dedicated_host_id': 'str'
    }

    attribute_map = {
        'group': 'group',
        'tenancy': 'tenancy',
        'dedicated_host_id': 'dedicated_host_id'
    }

    def __init__(self, group=None, tenancy=None, dedicated_host_id=None):
        """PrePaidServerSchedulerHints - a model defined in huaweicloud sdk"""
        
        

        self._group = None
        self._tenancy = None
        self._dedicated_host_id = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if tenancy is not None:
            self.tenancy = tenancy
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id

    @property
    def group(self):
        """Gets the group of this PrePaidServerSchedulerHints.

        云服务器组ID，UUID格式。

        :return: The group of this PrePaidServerSchedulerHints.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this PrePaidServerSchedulerHints.

        云服务器组ID，UUID格式。

        :param group: The group of this PrePaidServerSchedulerHints.
        :type: str
        """
        self._group = group

    @property
    def tenancy(self):
        """Gets the tenancy of this PrePaidServerSchedulerHints.

        在指定的专属主机或者共享主机上创建弹性云服务器。参数值为shared或者dedicated。

        :return: The tenancy of this PrePaidServerSchedulerHints.
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        """Sets the tenancy of this PrePaidServerSchedulerHints.

        在指定的专属主机或者共享主机上创建弹性云服务器。参数值为shared或者dedicated。

        :param tenancy: The tenancy of this PrePaidServerSchedulerHints.
        :type: str
        """
        self._tenancy = tenancy

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this PrePaidServerSchedulerHints.

        专属主机的ID。

        :return: The dedicated_host_id of this PrePaidServerSchedulerHints.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this PrePaidServerSchedulerHints.

        专属主机的ID。

        :param dedicated_host_id: The dedicated_host_id of this PrePaidServerSchedulerHints.
        :type: str
        """
        self._dedicated_host_id = dedicated_host_id

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
        if not isinstance(other, PrePaidServerSchedulerHints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
