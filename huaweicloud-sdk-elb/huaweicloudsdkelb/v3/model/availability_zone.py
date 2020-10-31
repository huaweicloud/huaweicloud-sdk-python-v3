# coding: utf-8

import pprint
import re

import six





class AvailabilityZone:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'state': 'str'
    }

    attribute_map = {
        'code': 'code',
        'state': 'state'
    }

    def __init__(self, code=None, state=None):
        """AvailabilityZone - a model defined in huaweicloud sdk"""
        
        

        self._code = None
        self._state = None
        self.discriminator = None

        self.code = code
        self.state = state

    @property
    def code(self):
        """Gets the code of this AvailabilityZone.

        可用区code。

        :return: The code of this AvailabilityZone.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AvailabilityZone.

        可用区code。

        :param code: The code of this AvailabilityZone.
        :type: str
        """
        self._code = code

    @property
    def state(self):
        """Gets the state of this AvailabilityZone.

        az状态。  取值：ACTIVE

        :return: The state of this AvailabilityZone.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AvailabilityZone.

        az状态。  取值：ACTIVE

        :param state: The state of this AvailabilityZone.
        :type: str
        """
        self._state = state

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
        if not isinstance(other, AvailabilityZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
