# coding: utf-8

import pprint
import re

import six





class BillbingCreateExtraInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'combined_order_id': 'str',
        'combined_order_ecs_num': 'int'
    }

    attribute_map = {
        'combined_order_id': 'combined_order_id',
        'combined_order_ecs_num': 'combined_order_ecs_num'
    }

    def __init__(self, combined_order_id=None, combined_order_ecs_num=None):
        """BillbingCreateExtraInfo - a model defined in huaweicloud sdk"""
        
        

        self._combined_order_id = None
        self._combined_order_ecs_num = None
        self.discriminator = None

        if combined_order_id is not None:
            self.combined_order_id = combined_order_id
        if combined_order_ecs_num is not None:
            self.combined_order_ecs_num = combined_order_ecs_num

    @property
    def combined_order_id(self):
        """Gets the combined_order_id of this BillbingCreateExtraInfo.

        组合创建ID，组合创建时必传。

        :return: The combined_order_id of this BillbingCreateExtraInfo.
        :rtype: str
        """
        return self._combined_order_id

    @combined_order_id.setter
    def combined_order_id(self, combined_order_id):
        """Sets the combined_order_id of this BillbingCreateExtraInfo.

        组合创建ID，组合创建时必传。

        :param combined_order_id: The combined_order_id of this BillbingCreateExtraInfo.
        :type: str
        """
        self._combined_order_id = combined_order_id

    @property
    def combined_order_ecs_num(self):
        """Gets the combined_order_ecs_num of this BillbingCreateExtraInfo.

        组合创建数量，组合创建时必填。

        :return: The combined_order_ecs_num of this BillbingCreateExtraInfo.
        :rtype: int
        """
        return self._combined_order_ecs_num

    @combined_order_ecs_num.setter
    def combined_order_ecs_num(self, combined_order_ecs_num):
        """Sets the combined_order_ecs_num of this BillbingCreateExtraInfo.

        组合创建数量，组合创建时必填。

        :param combined_order_ecs_num: The combined_order_ecs_num of this BillbingCreateExtraInfo.
        :type: int
        """
        self._combined_order_ecs_num = combined_order_ecs_num

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
        if not isinstance(other, BillbingCreateExtraInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
