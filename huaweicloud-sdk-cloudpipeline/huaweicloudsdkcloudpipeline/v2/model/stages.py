# coding: utf-8

import pprint
import re

import six





class Stages:


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
        'status': 'str',
        'name': 'str',
        'parameters': 'object',
        'order': 'int',
        'dsl_method': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'result': 'result',
        'status': 'status',
        'name': 'name',
        'parameters': 'parameters',
        'order': 'order',
        'dsl_method': 'dsl_method',
        'display_name': 'display_name'
    }

    def __init__(self, result=None, status=None, name=None, parameters=None, order=None, dsl_method=None, display_name=None):
        """Stages - a model defined in huaweicloud sdk"""
        
        

        self._result = None
        self._status = None
        self._name = None
        self._parameters = None
        self._order = None
        self._dsl_method = None
        self._display_name = None
        self.discriminator = None

        self.result = result
        self.status = status
        self.name = name
        self.parameters = parameters
        self.order = order
        self.dsl_method = dsl_method
        self.display_name = display_name

    @property
    def result(self):
        """Gets the result of this Stages.

        阶段执行结果

        :return: The result of this Stages.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Stages.

        阶段执行结果

        :param result: The result of this Stages.
        :type: str
        """
        self._result = result

    @property
    def status(self):
        """Gets the status of this Stages.

        阶段执行状态

        :return: The status of this Stages.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Stages.

        阶段执行状态

        :param status: The status of this Stages.
        :type: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this Stages.

        阶段名字

        :return: The name of this Stages.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Stages.

        阶段名字

        :param name: The name of this Stages.
        :type: str
        """
        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this Stages.

        任务参数

        :return: The parameters of this Stages.
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Stages.

        任务参数

        :param parameters: The parameters of this Stages.
        :type: object
        """
        self._parameters = parameters

    @property
    def order(self):
        """Gets the order of this Stages.

        阶段顺序

        :return: The order of this Stages.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Stages.

        阶段顺序

        :param order: The order of this Stages.
        :type: int
        """
        self._order = order

    @property
    def dsl_method(self):
        """Gets the dsl_method of this Stages.

        阶段类型

        :return: The dsl_method of this Stages.
        :rtype: str
        """
        return self._dsl_method

    @dsl_method.setter
    def dsl_method(self, dsl_method):
        """Sets the dsl_method of this Stages.

        阶段类型

        :param dsl_method: The dsl_method of this Stages.
        :type: str
        """
        self._dsl_method = dsl_method

    @property
    def display_name(self):
        """Gets the display_name of this Stages.

        阶段显示名称

        :return: The display_name of this Stages.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Stages.

        阶段显示名称

        :param display_name: The display_name of this Stages.
        :type: str
        """
        self._display_name = display_name

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
        if not isinstance(other, Stages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
