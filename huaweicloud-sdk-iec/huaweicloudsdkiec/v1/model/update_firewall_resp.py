# coding: utf-8

import pprint
import re

import six





class UpdateFirewallResp:


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
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status'
    }

    def __init__(self, id=None, status=None):
        """UpdateFirewallResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.status = status

    @property
    def id(self):
        """Gets the id of this UpdateFirewallResp.

        网络ACL ID

        :return: The id of this UpdateFirewallResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateFirewallResp.

        网络ACL ID

        :param id: The id of this UpdateFirewallResp.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this UpdateFirewallResp.

        网络ACL状态。

        :return: The status of this UpdateFirewallResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateFirewallResp.

        网络ACL状态。

        :param status: The status of this UpdateFirewallResp.
        :type: str
        """
        self._status = status

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
        if not isinstance(other, UpdateFirewallResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other