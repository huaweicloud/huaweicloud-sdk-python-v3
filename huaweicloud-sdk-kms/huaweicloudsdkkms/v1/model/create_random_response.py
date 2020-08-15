# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateRandomResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'random_data': 'str'
    }

    attribute_map = {
        'random_data': 'random_data'
    }

    def __init__(self, random_data=None):
        """CreateRandomResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._random_data = None
        self.discriminator = None

        if random_data is not None:
            self.random_data = random_data

    @property
    def random_data(self):
        """Gets the random_data of this CreateRandomResponse.

        随机数16进制表示，两位表示1byte。随机数的长度与用户传入的参数 “random_data_length”的长度保持一致。

        :return: The random_data of this CreateRandomResponse.
        :rtype: str
        """
        return self._random_data

    @random_data.setter
    def random_data(self, random_data):
        """Sets the random_data of this CreateRandomResponse.

        随机数16进制表示，两位表示1byte。随机数的长度与用户传入的参数 “random_data_length”的长度保持一致。

        :param random_data: The random_data of this CreateRandomResponse.
        :type: str
        """
        self._random_data = random_data

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
        if not isinstance(other, CreateRandomResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
