# coding: utf-8

import pprint
import re

import six





class ThrottleBindingBatchDelete:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'throttle_bindings': 'list[str]'
    }

    attribute_map = {
        'throttle_bindings': 'throttle_bindings'
    }

    def __init__(self, throttle_bindings=None):
        """ThrottleBindingBatchDelete - a model defined in huaweicloud sdk"""
        
        

        self._throttle_bindings = None
        self.discriminator = None

        if throttle_bindings is not None:
            self.throttle_bindings = throttle_bindings

    @property
    def throttle_bindings(self):
        """Gets the throttle_bindings of this ThrottleBindingBatchDelete.

        需要解除绑定的API和流控策略绑定关系ID列表

        :return: The throttle_bindings of this ThrottleBindingBatchDelete.
        :rtype: list[str]
        """
        return self._throttle_bindings

    @throttle_bindings.setter
    def throttle_bindings(self, throttle_bindings):
        """Sets the throttle_bindings of this ThrottleBindingBatchDelete.

        需要解除绑定的API和流控策略绑定关系ID列表

        :param throttle_bindings: The throttle_bindings of this ThrottleBindingBatchDelete.
        :type: list[str]
        """
        self._throttle_bindings = throttle_bindings

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
        if not isinstance(other, ThrottleBindingBatchDelete):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
