# coding: utf-8

import pprint
import re

import six





class ApiConditionBase:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'req_param_name': 'str',
        'condition_type': 'str',
        'condition_origin': 'str',
        'condition_value': 'str'
    }

    attribute_map = {
        'req_param_name': 'req_param_name',
        'condition_type': 'condition_type',
        'condition_origin': 'condition_origin',
        'condition_value': 'condition_value'
    }

    def __init__(self, req_param_name=None, condition_type=None, condition_origin=None, condition_value=None):
        """ApiConditionBase - a model defined in huaweicloud sdk"""
        
        

        self._req_param_name = None
        self._condition_type = None
        self._condition_origin = None
        self._condition_value = None
        self.discriminator = None

        if req_param_name is not None:
            self.req_param_name = req_param_name
        if condition_type is not None:
            self.condition_type = condition_type
        self.condition_origin = condition_origin
        self.condition_value = condition_value

    @property
    def req_param_name(self):
        """Gets the req_param_name of this ApiConditionBase.

        关联的请求参数对象名称。策略类型为param时必选

        :return: The req_param_name of this ApiConditionBase.
        :rtype: str
        """
        return self._req_param_name

    @req_param_name.setter
    def req_param_name(self, req_param_name):
        """Sets the req_param_name of this ApiConditionBase.

        关联的请求参数对象名称。策略类型为param时必选

        :param req_param_name: The req_param_name of this ApiConditionBase.
        :type: str
        """
        self._req_param_name = req_param_name

    @property
    def condition_type(self):
        """Gets the condition_type of this ApiConditionBase.

        策略条件 - exact：绝对匹配 - enum：枚举 - pattern：正则  策略类型为param时必选 

        :return: The condition_type of this ApiConditionBase.
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """Sets the condition_type of this ApiConditionBase.

        策略条件 - exact：绝对匹配 - enum：枚举 - pattern：正则  策略类型为param时必选 

        :param condition_type: The condition_type of this ApiConditionBase.
        :type: str
        """
        self._condition_type = condition_type

    @property
    def condition_origin(self):
        """Gets the condition_origin of this ApiConditionBase.

        策略类型 - param：参数 - source：源IP

        :return: The condition_origin of this ApiConditionBase.
        :rtype: str
        """
        return self._condition_origin

    @condition_origin.setter
    def condition_origin(self, condition_origin):
        """Sets the condition_origin of this ApiConditionBase.

        策略类型 - param：参数 - source：源IP

        :param condition_origin: The condition_origin of this ApiConditionBase.
        :type: str
        """
        self._condition_origin = condition_origin

    @property
    def condition_value(self):
        """Gets the condition_value of this ApiConditionBase.

        策略值

        :return: The condition_value of this ApiConditionBase.
        :rtype: str
        """
        return self._condition_value

    @condition_value.setter
    def condition_value(self, condition_value):
        """Sets the condition_value of this ApiConditionBase.

        策略值

        :param condition_value: The condition_value of this ApiConditionBase.
        :type: str
        """
        self._condition_value = condition_value

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
        if not isinstance(other, ApiConditionBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
