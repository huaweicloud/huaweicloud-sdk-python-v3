# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommandTimeTakenList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'total_usec_sum': 'float',
        'result': 'str',
        'command_list': 'list[CommandTimeTaken]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'total_usec_sum': 'total_usec_sum',
        'result': 'result',
        'command_list': 'command_list'
    }

    def __init__(self, total_num=None, total_usec_sum=None, result=None, command_list=None):
        r"""CommandTimeTakenList

        The model defined in huaweicloud sdk

        :param total_num: 执行命令的总次数
        :type total_num: int
        :param total_usec_sum: 执行命令的总耗时
        :type total_usec_sum: float
        :param result: 命令耗时统计结果
        :type result: str
        :param command_list: 命令耗时统计
        :type command_list: list[:class:`huaweicloudsdkdcs.v2.CommandTimeTaken`]
        """
        
        

        self._total_num = None
        self._total_usec_sum = None
        self._result = None
        self._command_list = None
        self.discriminator = None

        self.total_num = total_num
        self.total_usec_sum = total_usec_sum
        self.result = result
        self.command_list = command_list

    @property
    def total_num(self):
        r"""Gets the total_num of this CommandTimeTakenList.

        执行命令的总次数

        :return: The total_num of this CommandTimeTakenList.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this CommandTimeTakenList.

        执行命令的总次数

        :param total_num: The total_num of this CommandTimeTakenList.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def total_usec_sum(self):
        r"""Gets the total_usec_sum of this CommandTimeTakenList.

        执行命令的总耗时

        :return: The total_usec_sum of this CommandTimeTakenList.
        :rtype: float
        """
        return self._total_usec_sum

    @total_usec_sum.setter
    def total_usec_sum(self, total_usec_sum):
        r"""Sets the total_usec_sum of this CommandTimeTakenList.

        执行命令的总耗时

        :param total_usec_sum: The total_usec_sum of this CommandTimeTakenList.
        :type total_usec_sum: float
        """
        self._total_usec_sum = total_usec_sum

    @property
    def result(self):
        r"""Gets the result of this CommandTimeTakenList.

        命令耗时统计结果

        :return: The result of this CommandTimeTakenList.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this CommandTimeTakenList.

        命令耗时统计结果

        :param result: The result of this CommandTimeTakenList.
        :type result: str
        """
        self._result = result

    @property
    def command_list(self):
        r"""Gets the command_list of this CommandTimeTakenList.

        命令耗时统计

        :return: The command_list of this CommandTimeTakenList.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.CommandTimeTaken`]
        """
        return self._command_list

    @command_list.setter
    def command_list(self, command_list):
        r"""Sets the command_list of this CommandTimeTakenList.

        命令耗时统计

        :param command_list: The command_list of this CommandTimeTakenList.
        :type command_list: list[:class:`huaweicloudsdkdcs.v2.CommandTimeTaken`]
        """
        self._command_list = command_list

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
        if not isinstance(other, CommandTimeTakenList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
