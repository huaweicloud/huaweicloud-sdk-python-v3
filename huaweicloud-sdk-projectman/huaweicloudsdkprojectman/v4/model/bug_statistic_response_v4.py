# coding: utf-8

import pprint
import re

import six





class BugStatisticResponseV4:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'critical_num': 'int',
        'defect_index': 'float',
        'module': 'str',
        'normal_num': 'int',
        'serious_num': 'int',
        'tip_num': 'int',
        'total': 'int'
    }

    attribute_map = {
        'critical_num': 'critical_num',
        'defect_index': 'defect_index',
        'module': 'module',
        'normal_num': 'normal_num',
        'serious_num': 'serious_num',
        'tip_num': 'tip_num',
        'total': 'total'
    }

    def __init__(self, critical_num=None, defect_index=None, module=None, normal_num=None, serious_num=None, tip_num=None, total=None):
        """BugStatisticResponseV4 - a model defined in huaweicloud sdk"""
        
        

        self._critical_num = None
        self._defect_index = None
        self._module = None
        self._normal_num = None
        self._serious_num = None
        self._tip_num = None
        self._total = None
        self.discriminator = None

        if critical_num is not None:
            self.critical_num = critical_num
        if defect_index is not None:
            self.defect_index = defect_index
        if module is not None:
            self.module = module
        if normal_num is not None:
            self.normal_num = normal_num
        if serious_num is not None:
            self.serious_num = serious_num
        if tip_num is not None:
            self.tip_num = tip_num
        if total is not None:
            self.total = total

    @property
    def critical_num(self):
        """Gets the critical_num of this BugStatisticResponseV4.

        重要程度为关键的缺陷数

        :return: The critical_num of this BugStatisticResponseV4.
        :rtype: int
        """
        return self._critical_num

    @critical_num.setter
    def critical_num(self, critical_num):
        """Sets the critical_num of this BugStatisticResponseV4.

        重要程度为关键的缺陷数

        :param critical_num: The critical_num of this BugStatisticResponseV4.
        :type: int
        """
        self._critical_num = critical_num

    @property
    def defect_index(self):
        """Gets the defect_index of this BugStatisticResponseV4.

        DI

        :return: The defect_index of this BugStatisticResponseV4.
        :rtype: float
        """
        return self._defect_index

    @defect_index.setter
    def defect_index(self, defect_index):
        """Sets the defect_index of this BugStatisticResponseV4.

        DI

        :param defect_index: The defect_index of this BugStatisticResponseV4.
        :type: float
        """
        self._defect_index = defect_index

    @property
    def module(self):
        """Gets the module of this BugStatisticResponseV4.

        模块

        :return: The module of this BugStatisticResponseV4.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this BugStatisticResponseV4.

        模块

        :param module: The module of this BugStatisticResponseV4.
        :type: str
        """
        self._module = module

    @property
    def normal_num(self):
        """Gets the normal_num of this BugStatisticResponseV4.

        重要程度为一般的缺陷数

        :return: The normal_num of this BugStatisticResponseV4.
        :rtype: int
        """
        return self._normal_num

    @normal_num.setter
    def normal_num(self, normal_num):
        """Sets the normal_num of this BugStatisticResponseV4.

        重要程度为一般的缺陷数

        :param normal_num: The normal_num of this BugStatisticResponseV4.
        :type: int
        """
        self._normal_num = normal_num

    @property
    def serious_num(self):
        """Gets the serious_num of this BugStatisticResponseV4.

        重要程度为严重的缺陷数

        :return: The serious_num of this BugStatisticResponseV4.
        :rtype: int
        """
        return self._serious_num

    @serious_num.setter
    def serious_num(self, serious_num):
        """Sets the serious_num of this BugStatisticResponseV4.

        重要程度为严重的缺陷数

        :param serious_num: The serious_num of this BugStatisticResponseV4.
        :type: int
        """
        self._serious_num = serious_num

    @property
    def tip_num(self):
        """Gets the tip_num of this BugStatisticResponseV4.

        重要程度为提示的缺陷数

        :return: The tip_num of this BugStatisticResponseV4.
        :rtype: int
        """
        return self._tip_num

    @tip_num.setter
    def tip_num(self, tip_num):
        """Sets the tip_num of this BugStatisticResponseV4.

        重要程度为提示的缺陷数

        :param tip_num: The tip_num of this BugStatisticResponseV4.
        :type: int
        """
        self._tip_num = tip_num

    @property
    def total(self):
        """Gets the total of this BugStatisticResponseV4.

        总数

        :return: The total of this BugStatisticResponseV4.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BugStatisticResponseV4.

        总数

        :param total: The total of this BugStatisticResponseV4.
        :type: int
        """
        self._total = total

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
        if not isinstance(other, BugStatisticResponseV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
