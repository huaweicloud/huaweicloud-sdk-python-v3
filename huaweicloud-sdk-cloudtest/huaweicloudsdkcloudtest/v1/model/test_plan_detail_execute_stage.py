# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestPlanDetailExecuteStage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'defect_count': 'int',
        'completed_defect_count': 'int',
        'case_pass_rate': 'str',
        'executed_case_count': 'int'
    }

    attribute_map = {
        'defect_count': 'defect_count',
        'completed_defect_count': 'completed_defect_count',
        'case_pass_rate': 'case_pass_rate',
        'executed_case_count': 'executed_case_count'
    }

    def __init__(self, defect_count=None, completed_defect_count=None, case_pass_rate=None, executed_case_count=None):
        """TestPlanDetailExecuteStage

        The model defined in huaweicloud sdk

        :param defect_count: 缺陷个数
        :type defect_count: int
        :param completed_defect_count: 已完成缺陷个数
        :type completed_defect_count: int
        :param case_pass_rate: 用例通过率,按用例结果计算
        :type case_pass_rate: str
        :param executed_case_count: 已执行用例数, 按用例状态统计
        :type executed_case_count: int
        """
        
        

        self._defect_count = None
        self._completed_defect_count = None
        self._case_pass_rate = None
        self._executed_case_count = None
        self.discriminator = None

        if defect_count is not None:
            self.defect_count = defect_count
        if completed_defect_count is not None:
            self.completed_defect_count = completed_defect_count
        if case_pass_rate is not None:
            self.case_pass_rate = case_pass_rate
        if executed_case_count is not None:
            self.executed_case_count = executed_case_count

    @property
    def defect_count(self):
        """Gets the defect_count of this TestPlanDetailExecuteStage.

        缺陷个数

        :return: The defect_count of this TestPlanDetailExecuteStage.
        :rtype: int
        """
        return self._defect_count

    @defect_count.setter
    def defect_count(self, defect_count):
        """Sets the defect_count of this TestPlanDetailExecuteStage.

        缺陷个数

        :param defect_count: The defect_count of this TestPlanDetailExecuteStage.
        :type defect_count: int
        """
        self._defect_count = defect_count

    @property
    def completed_defect_count(self):
        """Gets the completed_defect_count of this TestPlanDetailExecuteStage.

        已完成缺陷个数

        :return: The completed_defect_count of this TestPlanDetailExecuteStage.
        :rtype: int
        """
        return self._completed_defect_count

    @completed_defect_count.setter
    def completed_defect_count(self, completed_defect_count):
        """Sets the completed_defect_count of this TestPlanDetailExecuteStage.

        已完成缺陷个数

        :param completed_defect_count: The completed_defect_count of this TestPlanDetailExecuteStage.
        :type completed_defect_count: int
        """
        self._completed_defect_count = completed_defect_count

    @property
    def case_pass_rate(self):
        """Gets the case_pass_rate of this TestPlanDetailExecuteStage.

        用例通过率,按用例结果计算

        :return: The case_pass_rate of this TestPlanDetailExecuteStage.
        :rtype: str
        """
        return self._case_pass_rate

    @case_pass_rate.setter
    def case_pass_rate(self, case_pass_rate):
        """Sets the case_pass_rate of this TestPlanDetailExecuteStage.

        用例通过率,按用例结果计算

        :param case_pass_rate: The case_pass_rate of this TestPlanDetailExecuteStage.
        :type case_pass_rate: str
        """
        self._case_pass_rate = case_pass_rate

    @property
    def executed_case_count(self):
        """Gets the executed_case_count of this TestPlanDetailExecuteStage.

        已执行用例数, 按用例状态统计

        :return: The executed_case_count of this TestPlanDetailExecuteStage.
        :rtype: int
        """
        return self._executed_case_count

    @executed_case_count.setter
    def executed_case_count(self, executed_case_count):
        """Sets the executed_case_count of this TestPlanDetailExecuteStage.

        已执行用例数, 按用例状态统计

        :param executed_case_count: The executed_case_count of this TestPlanDetailExecuteStage.
        :type executed_case_count: int
        """
        self._executed_case_count = executed_case_count

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
        if not isinstance(other, TestPlanDetailExecuteStage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
