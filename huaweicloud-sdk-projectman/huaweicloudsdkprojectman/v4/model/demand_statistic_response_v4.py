# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DemandStatisticResponseV4:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'closed_num': 'int',
        'module': 'str',
        'new_num': 'int',
        'process_num': 'int',
        'rejected_num': 'int',
        'solved_num': 'int',
        'test_num': 'int',
        'total': 'int'
    }

    attribute_map = {
        'closed_num': 'closed_num',
        'module': 'module',
        'new_num': 'new_num',
        'process_num': 'process_num',
        'rejected_num': 'rejected_num',
        'solved_num': 'solved_num',
        'test_num': 'test_num',
        'total': 'total'
    }

    def __init__(self, closed_num=None, module=None, new_num=None, process_num=None, rejected_num=None, solved_num=None, test_num=None, total=None):
        r"""DemandStatisticResponseV4

        The model defined in huaweicloud sdk

        :param closed_num: 已关闭数量
        :type closed_num: int
        :param module: 模块
        :type module: str
        :param new_num: 新建的数量
        :type new_num: int
        :param process_num: 开发中的数量
        :type process_num: int
        :param rejected_num: 已拒绝数量
        :type rejected_num: int
        :param solved_num: 已解决数量
        :type solved_num: int
        :param test_num: 测试中的数量
        :type test_num: int
        :param total: 总数
        :type total: int
        """
        
        

        self._closed_num = None
        self._module = None
        self._new_num = None
        self._process_num = None
        self._rejected_num = None
        self._solved_num = None
        self._test_num = None
        self._total = None
        self.discriminator = None

        if closed_num is not None:
            self.closed_num = closed_num
        if module is not None:
            self.module = module
        if new_num is not None:
            self.new_num = new_num
        if process_num is not None:
            self.process_num = process_num
        if rejected_num is not None:
            self.rejected_num = rejected_num
        if solved_num is not None:
            self.solved_num = solved_num
        if test_num is not None:
            self.test_num = test_num
        if total is not None:
            self.total = total

    @property
    def closed_num(self):
        r"""Gets the closed_num of this DemandStatisticResponseV4.

        已关闭数量

        :return: The closed_num of this DemandStatisticResponseV4.
        :rtype: int
        """
        return self._closed_num

    @closed_num.setter
    def closed_num(self, closed_num):
        r"""Sets the closed_num of this DemandStatisticResponseV4.

        已关闭数量

        :param closed_num: The closed_num of this DemandStatisticResponseV4.
        :type closed_num: int
        """
        self._closed_num = closed_num

    @property
    def module(self):
        r"""Gets the module of this DemandStatisticResponseV4.

        模块

        :return: The module of this DemandStatisticResponseV4.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this DemandStatisticResponseV4.

        模块

        :param module: The module of this DemandStatisticResponseV4.
        :type module: str
        """
        self._module = module

    @property
    def new_num(self):
        r"""Gets the new_num of this DemandStatisticResponseV4.

        新建的数量

        :return: The new_num of this DemandStatisticResponseV4.
        :rtype: int
        """
        return self._new_num

    @new_num.setter
    def new_num(self, new_num):
        r"""Sets the new_num of this DemandStatisticResponseV4.

        新建的数量

        :param new_num: The new_num of this DemandStatisticResponseV4.
        :type new_num: int
        """
        self._new_num = new_num

    @property
    def process_num(self):
        r"""Gets the process_num of this DemandStatisticResponseV4.

        开发中的数量

        :return: The process_num of this DemandStatisticResponseV4.
        :rtype: int
        """
        return self._process_num

    @process_num.setter
    def process_num(self, process_num):
        r"""Sets the process_num of this DemandStatisticResponseV4.

        开发中的数量

        :param process_num: The process_num of this DemandStatisticResponseV4.
        :type process_num: int
        """
        self._process_num = process_num

    @property
    def rejected_num(self):
        r"""Gets the rejected_num of this DemandStatisticResponseV4.

        已拒绝数量

        :return: The rejected_num of this DemandStatisticResponseV4.
        :rtype: int
        """
        return self._rejected_num

    @rejected_num.setter
    def rejected_num(self, rejected_num):
        r"""Sets the rejected_num of this DemandStatisticResponseV4.

        已拒绝数量

        :param rejected_num: The rejected_num of this DemandStatisticResponseV4.
        :type rejected_num: int
        """
        self._rejected_num = rejected_num

    @property
    def solved_num(self):
        r"""Gets the solved_num of this DemandStatisticResponseV4.

        已解决数量

        :return: The solved_num of this DemandStatisticResponseV4.
        :rtype: int
        """
        return self._solved_num

    @solved_num.setter
    def solved_num(self, solved_num):
        r"""Sets the solved_num of this DemandStatisticResponseV4.

        已解决数量

        :param solved_num: The solved_num of this DemandStatisticResponseV4.
        :type solved_num: int
        """
        self._solved_num = solved_num

    @property
    def test_num(self):
        r"""Gets the test_num of this DemandStatisticResponseV4.

        测试中的数量

        :return: The test_num of this DemandStatisticResponseV4.
        :rtype: int
        """
        return self._test_num

    @test_num.setter
    def test_num(self, test_num):
        r"""Sets the test_num of this DemandStatisticResponseV4.

        测试中的数量

        :param test_num: The test_num of this DemandStatisticResponseV4.
        :type test_num: int
        """
        self._test_num = test_num

    @property
    def total(self):
        r"""Gets the total of this DemandStatisticResponseV4.

        总数

        :return: The total of this DemandStatisticResponseV4.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this DemandStatisticResponseV4.

        总数

        :param total: The total of this DemandStatisticResponseV4.
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
        if not isinstance(other, DemandStatisticResponseV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
