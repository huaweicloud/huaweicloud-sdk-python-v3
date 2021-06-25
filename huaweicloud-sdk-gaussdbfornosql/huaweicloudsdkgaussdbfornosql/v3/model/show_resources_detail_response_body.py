# coding: utf-8

import pprint
import re

import six





class ShowResourcesDetailResponseBody:


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
        'quota': 'int',
        'used': 'int'
    }

    attribute_map = {
        'type': 'type',
        'quota': 'quota',
        'used': 'used'
    }

    def __init__(self, type=None, quota=None, used=None):
        """ShowResourcesDetailResponseBody - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._quota = None
        self._used = None
        self.discriminator = None

        self.type = type
        self.quota = quota
        self.used = used

    @property
    def type(self):
        """Gets the type of this ShowResourcesDetailResponseBody.

        配额资源类型，当前配额类型仅支持实例类型（instance）。

        :return: The type of this ShowResourcesDetailResponseBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowResourcesDetailResponseBody.

        配额资源类型，当前配额类型仅支持实例类型（instance）。

        :param type: The type of this ShowResourcesDetailResponseBody.
        :type: str
        """
        self._type = type

    @property
    def quota(self):
        """Gets the quota of this ShowResourcesDetailResponseBody.

        当前配额值。

        :return: The quota of this ShowResourcesDetailResponseBody.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this ShowResourcesDetailResponseBody.

        当前配额值。

        :param quota: The quota of this ShowResourcesDetailResponseBody.
        :type: int
        """
        self._quota = quota

    @property
    def used(self):
        """Gets the used of this ShowResourcesDetailResponseBody.

        已使用的资源数。

        :return: The used of this ShowResourcesDetailResponseBody.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ShowResourcesDetailResponseBody.

        已使用的资源数。

        :param used: The used of this ShowResourcesDetailResponseBody.
        :type: int
        """
        self._used = used

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
        if not isinstance(other, ShowResourcesDetailResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other