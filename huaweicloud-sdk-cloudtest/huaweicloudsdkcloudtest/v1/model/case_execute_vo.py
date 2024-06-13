# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseExecuteVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execute_rate': 'str',
        'executed_number': 'int',
        'not_executed_number': 'int'
    }

    attribute_map = {
        'execute_rate': 'execute_rate',
        'executed_number': 'executed_number',
        'not_executed_number': 'not_executed_number'
    }

    def __init__(self, execute_rate=None, executed_number=None, not_executed_number=None):
        """CaseExecuteVo

        The model defined in huaweicloud sdk

        :param execute_rate: 需求关联用例执行率
        :type execute_rate: str
        :param executed_number: 需求关联已执行用例总数
        :type executed_number: int
        :param not_executed_number: 需求关联未执行用例总数
        :type not_executed_number: int
        """
        
        

        self._execute_rate = None
        self._executed_number = None
        self._not_executed_number = None
        self.discriminator = None

        if execute_rate is not None:
            self.execute_rate = execute_rate
        if executed_number is not None:
            self.executed_number = executed_number
        if not_executed_number is not None:
            self.not_executed_number = not_executed_number

    @property
    def execute_rate(self):
        """Gets the execute_rate of this CaseExecuteVo.

        需求关联用例执行率

        :return: The execute_rate of this CaseExecuteVo.
        :rtype: str
        """
        return self._execute_rate

    @execute_rate.setter
    def execute_rate(self, execute_rate):
        """Sets the execute_rate of this CaseExecuteVo.

        需求关联用例执行率

        :param execute_rate: The execute_rate of this CaseExecuteVo.
        :type execute_rate: str
        """
        self._execute_rate = execute_rate

    @property
    def executed_number(self):
        """Gets the executed_number of this CaseExecuteVo.

        需求关联已执行用例总数

        :return: The executed_number of this CaseExecuteVo.
        :rtype: int
        """
        return self._executed_number

    @executed_number.setter
    def executed_number(self, executed_number):
        """Sets the executed_number of this CaseExecuteVo.

        需求关联已执行用例总数

        :param executed_number: The executed_number of this CaseExecuteVo.
        :type executed_number: int
        """
        self._executed_number = executed_number

    @property
    def not_executed_number(self):
        """Gets the not_executed_number of this CaseExecuteVo.

        需求关联未执行用例总数

        :return: The not_executed_number of this CaseExecuteVo.
        :rtype: int
        """
        return self._not_executed_number

    @not_executed_number.setter
    def not_executed_number(self, not_executed_number):
        """Sets the not_executed_number of this CaseExecuteVo.

        需求关联未执行用例总数

        :param not_executed_number: The not_executed_number of this CaseExecuteVo.
        :type not_executed_number: int
        """
        self._not_executed_number = not_executed_number

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
        if not isinstance(other, CaseExecuteVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
