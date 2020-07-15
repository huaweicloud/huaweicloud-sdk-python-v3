# coding: utf-8

import pprint
import re

import six





class BatchOpsResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'instance': 'str'
    }

    attribute_map = {
        'result': 'result',
        'instance': 'instance'
    }

    def __init__(self, result=None, instance=None):
        """BatchOpsResult - a model defined in huaweicloud sdk"""
        
        

        self._result = None
        self._instance = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if instance is not None:
            self.instance = instance

    @property
    def result(self):
        """Gets the result of this BatchOpsResult.

        操作结果，取值有success或failed。

        :return: The result of this BatchOpsResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this BatchOpsResult.

        操作结果，取值有success或failed。

        :param result: The result of this BatchOpsResult.
        :type: str
        """
        self._result = result

    @property
    def instance(self):
        """Gets the instance of this BatchOpsResult.

        缓存实例ID。

        :return: The instance of this BatchOpsResult.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this BatchOpsResult.

        缓存实例ID。

        :param instance: The instance of this BatchOpsResult.
        :type: str
        """
        self._instance = instance

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
        if not isinstance(other, BatchOpsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
