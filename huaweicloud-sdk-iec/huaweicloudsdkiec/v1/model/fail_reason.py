# coding: utf-8

import pprint
import re

import six





class FailReason:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'fail_code': 'str',
        'fail_message': 'str'
    }

    attribute_map = {
        'fail_code': 'fail_code',
        'fail_message': 'fail_message'
    }

    def __init__(self, fail_code=None, fail_message=None):
        """FailReason - a model defined in huaweicloud sdk"""
        
        

        self._fail_code = None
        self._fail_message = None
        self.discriminator = None

        if fail_code is not None:
            self.fail_code = fail_code
        if fail_message is not None:
            self.fail_message = fail_message

    @property
    def fail_code(self):
        """Gets the fail_code of this FailReason.

        错误码

        :return: The fail_code of this FailReason.
        :rtype: str
        """
        return self._fail_code

    @fail_code.setter
    def fail_code(self, fail_code):
        """Sets the fail_code of this FailReason.

        错误码

        :param fail_code: The fail_code of this FailReason.
        :type: str
        """
        self._fail_code = fail_code

    @property
    def fail_message(self):
        """Gets the fail_message of this FailReason.

        边缘云失败原因列表。包含所边缘云的失败原因。

        :return: The fail_message of this FailReason.
        :rtype: str
        """
        return self._fail_message

    @fail_message.setter
    def fail_message(self, fail_message):
        """Sets the fail_message of this FailReason.

        边缘云失败原因列表。包含所边缘云的失败原因。

        :param fail_message: The fail_message of this FailReason.
        :type: str
        """
        self._fail_message = fail_message

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
        if not isinstance(other, FailReason):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
