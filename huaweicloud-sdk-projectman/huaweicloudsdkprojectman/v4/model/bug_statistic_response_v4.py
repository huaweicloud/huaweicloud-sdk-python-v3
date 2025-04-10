# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""BugStatisticResponseV4

        The model defined in huaweicloud sdk

        :param critical_num: 重要程度为关键的缺陷数
        :type critical_num: int
        :param defect_index: DI
        :type defect_index: float
        :param module: 模块
        :type module: str
        :param normal_num: 重要程度为一般的缺陷数
        :type normal_num: int
        :param serious_num: 重要程度为严重的缺陷数
        :type serious_num: int
        :param tip_num: 重要程度为提示的缺陷数
        :type tip_num: int
        :param total: 总数
        :type total: int
        """
        
        

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
        r"""Gets the critical_num of this BugStatisticResponseV4.

        重要程度为关键的缺陷数

        :return: The critical_num of this BugStatisticResponseV4.
        :rtype: int
        """
        return self._critical_num

    @critical_num.setter
    def critical_num(self, critical_num):
        r"""Sets the critical_num of this BugStatisticResponseV4.

        重要程度为关键的缺陷数

        :param critical_num: The critical_num of this BugStatisticResponseV4.
        :type critical_num: int
        """
        self._critical_num = critical_num

    @property
    def defect_index(self):
        r"""Gets the defect_index of this BugStatisticResponseV4.

        DI

        :return: The defect_index of this BugStatisticResponseV4.
        :rtype: float
        """
        return self._defect_index

    @defect_index.setter
    def defect_index(self, defect_index):
        r"""Sets the defect_index of this BugStatisticResponseV4.

        DI

        :param defect_index: The defect_index of this BugStatisticResponseV4.
        :type defect_index: float
        """
        self._defect_index = defect_index

    @property
    def module(self):
        r"""Gets the module of this BugStatisticResponseV4.

        模块

        :return: The module of this BugStatisticResponseV4.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this BugStatisticResponseV4.

        模块

        :param module: The module of this BugStatisticResponseV4.
        :type module: str
        """
        self._module = module

    @property
    def normal_num(self):
        r"""Gets the normal_num of this BugStatisticResponseV4.

        重要程度为一般的缺陷数

        :return: The normal_num of this BugStatisticResponseV4.
        :rtype: int
        """
        return self._normal_num

    @normal_num.setter
    def normal_num(self, normal_num):
        r"""Sets the normal_num of this BugStatisticResponseV4.

        重要程度为一般的缺陷数

        :param normal_num: The normal_num of this BugStatisticResponseV4.
        :type normal_num: int
        """
        self._normal_num = normal_num

    @property
    def serious_num(self):
        r"""Gets the serious_num of this BugStatisticResponseV4.

        重要程度为严重的缺陷数

        :return: The serious_num of this BugStatisticResponseV4.
        :rtype: int
        """
        return self._serious_num

    @serious_num.setter
    def serious_num(self, serious_num):
        r"""Sets the serious_num of this BugStatisticResponseV4.

        重要程度为严重的缺陷数

        :param serious_num: The serious_num of this BugStatisticResponseV4.
        :type serious_num: int
        """
        self._serious_num = serious_num

    @property
    def tip_num(self):
        r"""Gets the tip_num of this BugStatisticResponseV4.

        重要程度为提示的缺陷数

        :return: The tip_num of this BugStatisticResponseV4.
        :rtype: int
        """
        return self._tip_num

    @tip_num.setter
    def tip_num(self, tip_num):
        r"""Sets the tip_num of this BugStatisticResponseV4.

        重要程度为提示的缺陷数

        :param tip_num: The tip_num of this BugStatisticResponseV4.
        :type tip_num: int
        """
        self._tip_num = tip_num

    @property
    def total(self):
        r"""Gets the total of this BugStatisticResponseV4.

        总数

        :return: The total of this BugStatisticResponseV4.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this BugStatisticResponseV4.

        总数

        :param total: The total of this BugStatisticResponseV4.
        :type total: int
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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BugStatisticResponseV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
