# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommandTimeTaken:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'calls_sum': 'int',
        'usec_sum': 'float',
        'command_name': 'str',
        'per_usec': 'str',
        'average_usec': 'float'
    }

    attribute_map = {
        'calls_sum': 'calls_sum',
        'usec_sum': 'usec_sum',
        'command_name': 'command_name',
        'per_usec': 'per_usec',
        'average_usec': 'average_usec'
    }

    def __init__(self, calls_sum=None, usec_sum=None, command_name=None, per_usec=None, average_usec=None):
        """CommandTimeTaken

        The model defined in huaweicloud sdk

        :param calls_sum: 调用次数
        :type calls_sum: int
        :param usec_sum: 耗时总数
        :type usec_sum: float
        :param command_name: 命令名称
        :type command_name: str
        :param per_usec: 耗时占比
        :type per_usec: str
        :param average_usec: 每次调用平均耗时
        :type average_usec: float
        """
        
        

        self._calls_sum = None
        self._usec_sum = None
        self._command_name = None
        self._per_usec = None
        self._average_usec = None
        self.discriminator = None

        self.calls_sum = calls_sum
        self.usec_sum = usec_sum
        self.command_name = command_name
        self.per_usec = per_usec
        self.average_usec = average_usec

    @property
    def calls_sum(self):
        """Gets the calls_sum of this CommandTimeTaken.

        调用次数

        :return: The calls_sum of this CommandTimeTaken.
        :rtype: int
        """
        return self._calls_sum

    @calls_sum.setter
    def calls_sum(self, calls_sum):
        """Sets the calls_sum of this CommandTimeTaken.

        调用次数

        :param calls_sum: The calls_sum of this CommandTimeTaken.
        :type calls_sum: int
        """
        self._calls_sum = calls_sum

    @property
    def usec_sum(self):
        """Gets the usec_sum of this CommandTimeTaken.

        耗时总数

        :return: The usec_sum of this CommandTimeTaken.
        :rtype: float
        """
        return self._usec_sum

    @usec_sum.setter
    def usec_sum(self, usec_sum):
        """Sets the usec_sum of this CommandTimeTaken.

        耗时总数

        :param usec_sum: The usec_sum of this CommandTimeTaken.
        :type usec_sum: float
        """
        self._usec_sum = usec_sum

    @property
    def command_name(self):
        """Gets the command_name of this CommandTimeTaken.

        命令名称

        :return: The command_name of this CommandTimeTaken.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """Sets the command_name of this CommandTimeTaken.

        命令名称

        :param command_name: The command_name of this CommandTimeTaken.
        :type command_name: str
        """
        self._command_name = command_name

    @property
    def per_usec(self):
        """Gets the per_usec of this CommandTimeTaken.

        耗时占比

        :return: The per_usec of this CommandTimeTaken.
        :rtype: str
        """
        return self._per_usec

    @per_usec.setter
    def per_usec(self, per_usec):
        """Sets the per_usec of this CommandTimeTaken.

        耗时占比

        :param per_usec: The per_usec of this CommandTimeTaken.
        :type per_usec: str
        """
        self._per_usec = per_usec

    @property
    def average_usec(self):
        """Gets the average_usec of this CommandTimeTaken.

        每次调用平均耗时

        :return: The average_usec of this CommandTimeTaken.
        :rtype: float
        """
        return self._average_usec

    @average_usec.setter
    def average_usec(self, average_usec):
        """Sets the average_usec of this CommandTimeTaken.

        每次调用平均耗时

        :param average_usec: The average_usec of this CommandTimeTaken.
        :type average_usec: float
        """
        self._average_usec = average_usec

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
        if not isinstance(other, CommandTimeTaken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
