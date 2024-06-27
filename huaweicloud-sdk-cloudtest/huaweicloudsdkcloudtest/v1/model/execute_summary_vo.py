# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteSummaryVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execute_case_num': 'int',
        'defect_num': 'int',
        'completed_defect_num': 'int',
        'case_success_rate': 'str',
        'case_execution_rate': 'str'
    }

    attribute_map = {
        'execute_case_num': 'execute_case_num',
        'defect_num': 'defect_num',
        'completed_defect_num': 'completed_defect_num',
        'case_success_rate': 'case_success_rate',
        'case_execution_rate': 'case_execution_rate'
    }

    def __init__(self, execute_case_num=None, defect_num=None, completed_defect_num=None, case_success_rate=None, case_execution_rate=None):
        """ExecuteSummaryVo

        The model defined in huaweicloud sdk

        :param execute_case_num: 已执行用例数
        :type execute_case_num: int
        :param defect_num: 缺陷总数
        :type defect_num: int
        :param completed_defect_num: 已完成缺陷数
        :type completed_defect_num: int
        :param case_success_rate: 测试用例通过率
        :type case_success_rate: str
        :param case_execution_rate: 用例执行率
        :type case_execution_rate: str
        """
        
        

        self._execute_case_num = None
        self._defect_num = None
        self._completed_defect_num = None
        self._case_success_rate = None
        self._case_execution_rate = None
        self.discriminator = None

        if execute_case_num is not None:
            self.execute_case_num = execute_case_num
        if defect_num is not None:
            self.defect_num = defect_num
        if completed_defect_num is not None:
            self.completed_defect_num = completed_defect_num
        if case_success_rate is not None:
            self.case_success_rate = case_success_rate
        if case_execution_rate is not None:
            self.case_execution_rate = case_execution_rate

    @property
    def execute_case_num(self):
        """Gets the execute_case_num of this ExecuteSummaryVo.

        已执行用例数

        :return: The execute_case_num of this ExecuteSummaryVo.
        :rtype: int
        """
        return self._execute_case_num

    @execute_case_num.setter
    def execute_case_num(self, execute_case_num):
        """Sets the execute_case_num of this ExecuteSummaryVo.

        已执行用例数

        :param execute_case_num: The execute_case_num of this ExecuteSummaryVo.
        :type execute_case_num: int
        """
        self._execute_case_num = execute_case_num

    @property
    def defect_num(self):
        """Gets the defect_num of this ExecuteSummaryVo.

        缺陷总数

        :return: The defect_num of this ExecuteSummaryVo.
        :rtype: int
        """
        return self._defect_num

    @defect_num.setter
    def defect_num(self, defect_num):
        """Sets the defect_num of this ExecuteSummaryVo.

        缺陷总数

        :param defect_num: The defect_num of this ExecuteSummaryVo.
        :type defect_num: int
        """
        self._defect_num = defect_num

    @property
    def completed_defect_num(self):
        """Gets the completed_defect_num of this ExecuteSummaryVo.

        已完成缺陷数

        :return: The completed_defect_num of this ExecuteSummaryVo.
        :rtype: int
        """
        return self._completed_defect_num

    @completed_defect_num.setter
    def completed_defect_num(self, completed_defect_num):
        """Sets the completed_defect_num of this ExecuteSummaryVo.

        已完成缺陷数

        :param completed_defect_num: The completed_defect_num of this ExecuteSummaryVo.
        :type completed_defect_num: int
        """
        self._completed_defect_num = completed_defect_num

    @property
    def case_success_rate(self):
        """Gets the case_success_rate of this ExecuteSummaryVo.

        测试用例通过率

        :return: The case_success_rate of this ExecuteSummaryVo.
        :rtype: str
        """
        return self._case_success_rate

    @case_success_rate.setter
    def case_success_rate(self, case_success_rate):
        """Sets the case_success_rate of this ExecuteSummaryVo.

        测试用例通过率

        :param case_success_rate: The case_success_rate of this ExecuteSummaryVo.
        :type case_success_rate: str
        """
        self._case_success_rate = case_success_rate

    @property
    def case_execution_rate(self):
        """Gets the case_execution_rate of this ExecuteSummaryVo.

        用例执行率

        :return: The case_execution_rate of this ExecuteSummaryVo.
        :rtype: str
        """
        return self._case_execution_rate

    @case_execution_rate.setter
    def case_execution_rate(self, case_execution_rate):
        """Sets the case_execution_rate of this ExecuteSummaryVo.

        用例执行率

        :param case_execution_rate: The case_execution_rate of this ExecuteSummaryVo.
        :type case_execution_rate: str
        """
        self._case_execution_rate = case_execution_rate

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
        if not isinstance(other, ExecuteSummaryVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
