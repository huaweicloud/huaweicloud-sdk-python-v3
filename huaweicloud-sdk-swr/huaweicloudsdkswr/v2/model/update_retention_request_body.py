# coding: utf-8

import pprint
import re

import six





class UpdateRetentionRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'algorithm': 'str',
        'rules': 'list[Rule]'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'rules': 'rules'
    }

    def __init__(self, algorithm=None, rules=None):
        """UpdateRetentionRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._algorithm = None
        self._rules = None
        self.discriminator = None

        self.algorithm = algorithm
        self.rules = rules

    @property
    def algorithm(self):
        """Gets the algorithm of this UpdateRetentionRequestBody.

        算法

        :return: The algorithm of this UpdateRetentionRequestBody.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this UpdateRetentionRequestBody.

        算法

        :param algorithm: The algorithm of this UpdateRetentionRequestBody.
        :type: str
        """
        self._algorithm = algorithm

    @property
    def rules(self):
        """Gets the rules of this UpdateRetentionRequestBody.

        镜像老化规则

        :return: The rules of this UpdateRetentionRequestBody.
        :rtype: list[Rule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this UpdateRetentionRequestBody.

        镜像老化规则

        :param rules: The rules of this UpdateRetentionRequestBody.
        :type: list[Rule]
        """
        self._rules = rules

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
        if not isinstance(other, UpdateRetentionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
